"""decorators.py: decorator class and functions for junoplatform"""
__author__ = "Bruce.Lu"
__email__ = "lzbgt@icloud.com"
__time__ = "2023/07/20"


import logging
from collections import deque
from urllib.parse import parse_qs
import traceback
import json
import os
import time
import datetime
from functools import wraps
from junoplatform.log import logger
from junoplatform.io.utils import JunoConfig
from junoplatform.io import InputConfig, Storage, DataSet
from threading import Thread, Lock
import numpy as np
from junoplatform.io.misc import dict_value_diff
import yaml
import sys
import requests


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s %(lineno)d - %(message)s')

class EntryPoint:
    def __init__(self, cfg_in: str | InputConfig, detached: bool = False):
        super(EntryPoint, self).__init__()
        self.cfg_in: InputConfig
        self.detached = detached
        self.storage = Storage()
        # self.dataset = DataSet()
        self.ready = False
        self.que = deque(maxlen=2000)
        self.stop_flag = False
        self.tick = "-1"
        self.tick_key = "deadbeaf"
        self.reconfig = False
        self.last_meta = {}
        
        # handle mapped files
        if not os.path.exists('_boot'):
            if os.path.exists('_project.yml'):
                r = None
                with open('_project.yml', 'r', encoding='utf-8') as f:
                    r = yaml.safe_load(f)
                with open('project.yml', 'w', encoding='utf-8') as f:
                    yaml.safe_dump(r, f)
                logging.info("copied _project.yml")
                
            if os.path.exists('_config.json'):
                r = None
                with open('_config.json', 'r') as f:
                    r = json.load(f)
                with open('config.json', 'w', encoding='utf-8') as f:
                    json.dump(r, f, ensure_ascii=False)
                logging.info("copied _config.json")
            
        if not os.path.exists('_boot'):
            r = None
            with open('_boot', 'w', encoding='utf-8') as f:
                f.write(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                f.flush
            
        # load config
        self.config_lock = Lock()
        self.junoconfig = JunoConfig()
        self.enable_key = f"system.{self.junoconfig['plant']}.{self.junoconfig['module']}.enable"
        self._cfg_in = cfg_in
                
    def load_input(self):
        if isinstance(self._cfg_in, str):
            logging.debug(f"loading input spec from file: {self._cfg_in}")
            try:
                with open(self._cfg_in, "r", encoding="utf-8") as f:
                    self.cfg_in = InputConfig(**json.load(f))
            except Exception as e:
                msg = f"error in input.json: {e}"
                logger.error(msg)
                exit(1)
        elif isinstance(self._cfg_in, InputConfig):
            logging.info(f"loading input spec from class: {self.cfg_in}")
            self.cfg_in = self._cfg_in
        else:
            raise Exception(
                f"cfg_in must be type of InputConfig or string, but provides: {type(self._cfg_in)}")
            
    def update_meta(self, meta:dict):
        try:
            update_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            create_time = update_time
            if "create_time" in self.last_meta:
                create_time = self.last_meta["create_time"]
            meta["create_time"] = create_time
            vdiff = dict_value_diff(self.last_meta, meta)
            if vdiff:
                logging.info(f"meta changed: {vdiff}")
                meta["update_time"] = update_time
                self.storage.local.io.hset('system.ai.modules', f'{self.junoconfig["plant"]}.{self.junoconfig["module"]}', json.dumps(meta, ensure_ascii=False).encode())
                meta.pop("update_time")
                self.last_meta = meta.copy()
        except Exception as e:
            pass

    def _thread(self, func):
        once = True
        lasterr = False
        cnterr = 0
        while True:
            try:
                self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":1"
                try:
                    self.dataset = DataSet()
                except Exception as e:
                    logging.error(
                        "fault: failed to create DataSet to clickhouse, will retry in 7 seconds")
                    time.sleep(7)
                    continue
                # self.load_input()
                
                self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":3"
                self.config_lock.acquire()
                self.junoconfig = JunoConfig()
                self.cfg_in = self.junoconfig['input_cfg']
                logging.info(f'cfg_in: {self.cfg_in}')
                self.config_lock.release()
                algo_cfg = self.junoconfig["algo_cfg"]
                logging.info(f'algo_cfg: {algo_cfg}')
                logging.info(f"running algo with {algo_cfg}")
                
                self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":2"
                self.ready = True
                delay = self.cfg_in['sched_interval']
                enable = 1
                try:
                    enable = self.storage.local.read(self.enable_key, cast=int)
                    if enable is not None:
                        pass
                    else:
                        enable = 1  
                    self.stop_flag = not bool(enable)
                except Exception as e:
                    logging.error(f"failed to read local: {e}")
                    time.sleep(7)
                    continue
                
                if once:
                    # update config
                    meta = {
                        "package_id": self.junoconfig["package_id"],
                        "username": self.junoconfig["author"],
                        "plant": self.junoconfig["plant"],
                        "module": self.junoconfig["module"],
                        "config": self.junoconfig["algo_cfg"],
                        "status": 1,
                        "enable": enable,
                    }
                    
                    self.update_meta(meta)
                    r = self.storage.local.io.set(f"system.{self.junoconfig['plant']}.{self.junoconfig['module']}.reconfig", json.dumps(self.junoconfig["algo_cfg"], ensure_ascii=False))
                    once = False
                
                if not self.stop_flag:
                    data = None
                    timestamps = None
                    names = None
                    ts = datetime.datetime.now().timestamp()
                    if self.cfg_in['items']:
                        data, timestamps, names = self.dataset.fetch(
                            tags=self.cfg_in['tags'], num=self.cfg_in['items'])
                    elif self.cfg_in['minutes']:
                        time_from = datetime.datetime.now() - datetime.timedelta(minutes=self.cfg_in['minutes'])
                        data, timestamps, names = self.dataset.fetch(
                            tags=self.cfg_in['tags'], time_from=time_from)
                    else:
                        logging.error("invalid InputConfig")
                        time.sleep(11)
                        continue
                    
                    if isinstance(data, Exception):
                        logging.error(f"exceptin fetch data: {str(data)}, skip schedule")
                        self.sleep(7)
                        continue
                    
                    if data is None:
                        logging.error("failed to fetch data: None")
                        self.sleep(7)
                        continue
                    
                    self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":4"
                    
                    self.tick_key = f"system.ai.tick.{self.junoconfig['plant']}.{self.junoconfig['module']}"
                    td = datetime.datetime.now().timestamp()
                    logging.info(f"time used fetching dataset: {td-ts}s")

                    try:
                        func(self.storage, algo_cfg, data, timestamps, names, self)
                    except Exception as e:
                        msg = traceback.format_exc()
                        logger.error(f"exception {e}: {msg}")
                        
                        message = {
                            "name": "junoplatform",
                            "message": f"算法模块调度执行异常: ({self.junoconfig['plant']}, {self.junoconfig['module']}, {self.junoconfig['package_id']})" + "\n  " + msg
                        }
                        
                        try:
                            self.storage.cloud.write(
                                'juno-svc-notification', message, raw_table=True)
                            # smartcall
                            scr = self.storage.local.read(f'system.ai.smartcall.{self.junoconfig["plant"]}.{self.junoconfig["module"]}', cast=dict)
                            if scr and datetime.datetime.now().timestamp() - scr["params"]["ts"] < 60 * 30:
                                logging.info("skip smart voice call, since this module called in 30 minutes already")
                            elif "smartcall" in self.junoconfig and "token" in self.junoconfig["smartcall"] and "api" in self.junoconfig["smartcall"] and "numbers" in self.junoconfig["smartcall"]:
                                for number in self.junoconfig["smartcall"]["numbers"]:
                                    calldata = {
                                        "number": number,
                                        "params": {
                                            "plant": f'{self.junoconfig["plant"]}水厂 ',
                                            "module": f' {self.junoconfig["module"]}算法模块 ',
                                            "fault": f"算法代码执行错误为 {str(e)} ",
                                            "ts": datetime.datetime.now().timestamp()
                                         }
                                    }
                                    r = requests.post(self.junoconfig["smartcall"]["api"], json=calldata, headers={
                                        "Authorization": f'Bearer {self.junoconfig["smartcall"]["token"]}'
                                    })
                                    logging.info(r.text)
                                    self.storage.local.write(f'system.ai.smartcall.{self.junoconfig["plant"]}.{self.junoconfig["module"]}', calldata)
                            else:
                                logging.info("smartcall not configured, skip voice call")
                        except Exception as e:
                            errmsg = traceback.format_exc()
                            logging.error(f"failed send pulsar, {e}: {errmsg}")
                            
                    self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":5"

                    te = datetime.datetime.now().timestamp()
                    logging.info(f"time used running algo: {te-td}s")

                    delay = self.cfg_in['sched_interval'] - (te - ts) - 1
                    logging.debug(
                        f"delay in seconds to make up a full sched_interval: {delay}")
                    if delay < 0:
                        delay = 0
                else:
                    logging.info("module disabled, skip run algo func")
                    delay = 60
                    
                    
                logging.info(f"delay remain: {delay}s")
                    
                self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":6"
                del self.dataset
                self.sleep(delay)
                self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":7"
                lasterr = False
            except Exception as e:
                errmsg = traceback.format_exc()
                logging.error(errmsg)
                if cnterr == 5:
                    sys.exit(1)
                else:
                    if not lasterr:
                        lasterr = True
                        cnt = 1
                    else:
                        cnt += 1
                        
                self.sleep(20+1)
                  
    def sleep(self, secs:float):
      while secs >0:
        time.sleep(1)
        self.tick = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + f":-{secs}"
        secs -= 1
        try:
            r = self.storage.local.io.get(f"system.{self.junoconfig['plant']}.{self.junoconfig['module']}.enable")
            if r:
                r = bool(int(r.decode()))
                r = not r
                if r != self.stop_flag:
                    logging.info(f'stop flag: {r}, {self.stop_flag}')
                    self.stop_flag = r
                    self.reconfig = True
            r = self.storage.local.io.get(f"system.{self.junoconfig['plant']}.{self.junoconfig['module']}.reconfig")
            if r:
                r = json.loads(r.decode())
                diff = dict_value_diff(self.junoconfig['algo_cfg'], r)
                if diff:
                    logging.info(f'algo config diff: {diff}\ntnew: {r}')
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(r, f, ensure_ascii=False)
                        f.flush()
                    self.reconfig = True
        except Exception as e:
            logging.error(f"exception running algo: {str(e)}")
        
        if self.reconfig:
            logging.info("reconfig occurred")
            self.reconfig = False
            time.sleep(0)
            break

    def s_get_bool(self, v: str):
        try:
            x = int(v)
            return x != 0
        except:
            if v.lower() in ["t", "true", "y", "yes", "ok", "on", "enable", "active"]:
                return True
            else:
                return False

    def _pulsar(self):
        itopic = f"jprt-down-{self.junoconfig['plant']}-{self.junoconfig['module']}"
        while True:
            msg = None
            try:
                msg = self.storage.cloud.read(itopic, shared=False)
            except Exception as e:
                logging.error(f"failed to write cloud: {e}")
                time.sleep(7)
                continue
            data = {}
            logger.info(f"command received: {msg.data()}")
            try:
                data = json.loads(msg.data())
                if "package_id" not in data or self.junoconfig['package_id'] != data["package_id"]:
                    logger.error(
                        f"invalid msg received {data}, self package_id: {self.junoconfig['package_id']}")
                    self.storage.cloud.consumers[itopic].acknowledge(msg)
                    continue
            except Exception as e:
                logger.error(f"invalid msg received, {e}: {msg.data()}")
                if msg:
                    self.storage.cloud.consumers[itopic].acknowledge(msg)
                time.sleep(7)
                continue

            if "cmd" in data:
                if data["cmd"] == "enable":
                    cmd = parse_qs(data['qs'])
                    v = cmd.get('enable', [''])[0]
                    if v:
                        enable = self.s_get_bool(v)
                        if not enable:
                            self.stop_flag = True
                            logging.info("enable=false cmd received")
                        else:
                            self.stop_flag = False
                            logging.info("enable=true cmd received")

                        data = {"enable": enable,
                                "et": datetime.datetime.now().timestamp()*1000, "kind": "1", "package_id": data["package_id"]}
                        try:
                            self.storage.cloud.write("module_state_new", data)
                            self.storage.local.write(
                                self.enable_key, int(enable))

                        except Exception as e:
                            logging.error(
                                f"failed to write cloud and local: {e}")
                        self.reconfig = True
                elif data["cmd"] == "reconfig":
                    config = data["data"]["config"]
                    self.config_lock.acquire()
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(config, f, ensure_ascii=False)
                    self.config_lock.release()
                    self.reconfig = True

            else:
                logging.error(f"unkown msg: {data}")

            self.storage.cloud.consumers[itopic].acknowledge(msg)

    def _heart_beat(self):
        last_tick = "."
        count = 0
        while True:
            data = {"enable": not self.stop_flag,
                    "et": datetime.datetime.now().timestamp()*1000, "kind": "0", "package_id": self.junoconfig["package_id"]}
            try:
                self.storage.cloud.write("module_state_new", data)
            except Exception as e:
                logging.error(f"failed to write cloud: {e}")
                
            if count % 5 == 0:
                if last_tick == self.tick:
                    try:
                        if not self.storage.local.io.get(self.tick_key):
                            message = {
                                "name": "junoplatform",
                                "message": f"算法模块可能挂死: ({self.junoconfig['plant']}, {self.junoconfig['module']}, {self.junoconfig['package_id']})" + ":" + self.tick
                            }
                            self.storage.cloud.write('juno-svc-notification', message)
                            self.storage.local.io.set(self.tick_key, self.tick)
                    except Exception as e:
                        errmsg = traceback.format_exc()
                        logging.error(f"exception when check tick and send hang notification: {errmsg}")
                        sys.exit(1)
                        
            if last_tick != self.tick:
                try:
                    if self.storage.local.io.get(self.tick_key):
                        self.storage.local.io.delete(self.tick_key)
                        message = {
                        "name": "junoplatform",
                        "message": f"算法模块挂死恢复: ({self.junoconfig['plant']}, {self.junoconfig['module']}, {self.junoconfig['package_id']})" + ":" + self.tick
                        }
                        self.storage.cloud.write('juno-svc-notification', message)
                except Exception as e:
                    errmsg = traceback.format_exc()
                    logging.error(f"exception when check tick and send recovery notification: {errmsg}")
                    sys.exit(1)
                        
            # heartbeat interval is 1 minutes
            last_tick = self.tick
            count +=1
            time.sleep(60)

    def __call__(self, func):
        th = Thread(target=self._thread, args=(func,))
        th.start()

        while not self.ready:
            time.sleep(0)

        pt = Thread(target=self._pulsar)
        pt.start()

        hb = Thread(target=self._heart_beat)
        hb.start()


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.exists(args[0].juno_dir) or not os.path.exists(args[0].juno_file):
            logger.error(f"user not authenticationd.\n\
                          please run `junocli login [api_url]` to use your shuhan account")
            os.makedirs(args[0].juno_dir, exist_ok=True)
            return -1
        return func(*args, **kwargs)

    return wrapper
