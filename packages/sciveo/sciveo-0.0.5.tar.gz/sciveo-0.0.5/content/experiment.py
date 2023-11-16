#
# Pavlin Georgiev, Softel Labs
#
# This is a proprietary file and may not be copied,
# distributed, or modified without express permission
# from the owner. For licensing inquiries, please
# contact pavlin@softel.bg.
#
# 2023
#

import os
import time
import datetime

import numpy as np
import pandas as pd

from sciveo.common.tools.logger import *
from sciveo.api.base import APIRemoteClient
from sciveo.api.content import Content
from sciveo.common.tools.formating import format_elapsed_time
from sciveo.common.configuration import Configuration


class Experiment:
  def __init__(self, project_name, project_guid, config):
    self.project_name = project_name
    self.project_guid = project_guid
    self.config = config
    self.guid = None

    self.start_at = time.time()

    self.data = {
      "experiment": {
        "log": [],
        "config": config.data,
        "eval": {
          "score": -1.0,
        },
        "start_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }
    }

    self.name = f"Experiment {self.config.data['experiment_id']}"

    self.api = APIRemoteClient(base_url=os.environ.get("SCIVEO_API_BASE_URL", "https://sciveo.com"))

    remote_data = {
      "name": self.name,
      "data": self.data
    }
    if self.project_guid is not None:
      remote_data["project_guid"] = self.project_guid
    else:
      remote_data["project_name"] = self.project_name
    result = self.api.POST("experiment", remote_data)
    debug(type(self).__name__, "api", result)
    if result and "error" not in result:
      if result["name"] == self.name:
        self.guid = result["guid"]
      else:
        error(type(self).__name__, "Project name mismatch", result, self.name)
    else:
      error(type(self).__name__, "api", result)

  def close(self):
    self.end_at = time.time()
    self.elapsed = self.end_at - self.start_at

    self.data["experiment"]["end_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.data["experiment"]["elapsed"] = format_elapsed_time(self.elapsed)

    remote_data = {
      "guid": self.guid,
      "project_guid": self.project_guid,
      "data": self.data
    }
    result = self.api.POST("experiment", remote_data)
    debug(type(self).__name__, "close", self.name, "api", result)

  def append(self, d):
    self.data["experiment"]["log"].append(d)

  def eval(self, key, value):
    self.data["experiment"]["eval"][key] = value
  # Score value (no matter of its true meaning) which is used for experiments sorting
  def score(self, value):
    self.eval("score", value)

  def log(self, data, val=None, *args, **kwargs):
    if isinstance(data, Content):
      self.log_content(data)
    elif isinstance(data, dict):
      self.log_dict(data)
    else:
      self.log_any(data, val, *args, **kwargs)
  def log_content(self, content):
    debug(type(self).__name__, self.project_name, "LOG content", content)
  def log_dict(self, data):
    debug(type(self).__name__, self.project_name, "LOG data", data)
    self.append(data)
  def log_any(self, data, val=None, *args, **kwargs):
    debug(type(self).__name__, self.project_name, "LOG", (data, val), args, kwargs)
    if val is None:
      self.append(data)
    else:
      self.append({data: val})
    for a in args:
      self.append(a)
    for k, v in kwargs.items():
      self.append({k: v})
