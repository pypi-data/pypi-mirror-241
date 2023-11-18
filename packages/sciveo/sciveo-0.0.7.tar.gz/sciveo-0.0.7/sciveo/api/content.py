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

import uuid
import datetime

from sciveo.common.tools.logger import *


class Content:
  def __init__(self, content_type, name):
    debug(type(self).__name__, "init", content_type, name)
    self.content_type = content_type
    self.name = name
    self.guid = f"{content_type}-{self.new_guid()}"

  def new_guid(self):
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-" + str(uuid.uuid4()).replace("-", "")

  def __str__(self):
    return f"<{self.content_type}> [{self.name}] [{self.guid}]"

  def __dict__(self):
    return {"content_type": self.content_type, "name": self.name, "guid": self.guid}


class Project(Content):
  def __init__(self, name):
    self.content_type = "project"
    self.name = name
    self.guid = f"prj-{self.new_guid()}"


class Experiment(Content):
  def __init__(self, parent, name):
    self.content_type = "experiment"
    self.parent = parent
    self.name = name
    self.guid = f"exp-{self.new_guid()}"