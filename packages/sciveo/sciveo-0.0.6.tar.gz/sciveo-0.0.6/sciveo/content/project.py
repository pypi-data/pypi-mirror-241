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

import numpy as np
import pandas as pd

from sciveo.common.tools.logger import *
from sciveo.api.base import *
from sciveo.api.content import Content
from sciveo.common.configuration import Configuration
from sciveo.content.experiment import Experiment


class ProjectBase:
  def __init__(self, project_name):
    self.project_name = project_name
    self.guid = None
    self.config = Configuration()

    self.project_data = {
      "name": project_name,
      "project": {
        "experiments": [],
        "sort": {
          "experiment": "score"
        },
      }
    }

    debug(type(self).__name__, "init", self.project_name)

  def open(self):
    debug(type(self).__name__, "open", self.project_name)
    self.current_experiment = Experiment(self.project_name, self.guid, self.config)
    return self.current_experiment

  def close(self):
    debug(type(self).__name__, "close", self.project_name)
    self.project_data["project"]["experiments"].append(self.current_experiment.data)
    self.current_experiment.close()

  def __enter__(self):
    return self.open()

  def __exit__(self, exc_type, exc_value, traceback):
    self.close()


class RemoteProject(ProjectBase):
  def __init__(self, project_name, parent_id=None):
    super().__init__(project_name)

    self.api = APIRemoteClient(base_url=os.environ.get("SCIVEO_API_BASE_URL", "http://127.0.0.1:8081"))

    remote_data = {
      "name": project_name,
      "data": self.project_data
    }
    if parent_id is not None:
      remote_data["parent_id"] = parent_id
    result = self.api.POST("project", remote_data)
    debug(type(self).__name__, "api", result)
    if result and "error" not in result:
      if result["name"] == project_name:
        self.guid = result["guid"]
      else:
        error(type(self).__name__, "Project name mismatch", result, project_name)
    else:
      error(type(self).__name__, "api", remote_data, result)

  def open(self):
    self.auth()
    return super().open()

  def auth(self):
    debug(type(self).__name__, "API AUTH")


class LocalProject(ProjectBase):
  def __init__(self, project_name):
    super().__init__(project_name)
