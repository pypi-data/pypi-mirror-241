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
import json
from urllib import request, parse
from urllib.error import HTTPError
import requests

from sciveo.common.tools.logger import *


class APIClientBase:
  def __init__(self):
    debug(type(self).__name__, "init")
    self.data = {}

  def save_content(self, content):
    pass


class APIRemoteClient(APIClientBase):
  def __init__(self, base_url, ver=1):
    self.base_url = f"{base_url}/api/v{ver}/"
    self.headers = { "Auth-Token": os.environ['SCIVEO_SECRET_ACCESS_KEY'] }
    debug(type(self).__name__, f"base url: {self.base_url}")

  def POST(self, content_type, data, timeout=30):
    url = f"{self.base_url}sci/{content_type}/"
    result = False
    try:
      data = parse.urlencode(data).encode("utf-8")
      # debug("POST", url, data)
      resp = request.urlopen(request.Request(url, data=data, headers=self.headers), timeout=timeout)
      result = json.loads(resp.read())
      # debug("POST result", result)
    except HTTPError as e:
      error(e, url, data)
    except Exception as e:
      error(e, url, data)
    return result
