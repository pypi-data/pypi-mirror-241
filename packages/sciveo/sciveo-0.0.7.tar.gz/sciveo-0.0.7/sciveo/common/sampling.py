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

import numpy as np
import pandas as pd

from sciveo.common.configuration import Configuration


class BaseSampler:
  def __init__(self, configuration):
    self.configuration = configuration
    self.samples = []
    self.idx = 0

  def sample(self):
    self.samples = []

  def pd_samples(self):
    return pd.DataFrame(self.samples)

  def __len__(self):
    return len(self.samples)

  def __call__(self):
    result = self[self.idx]
    self.idx += 1
    if self.idx >= len(self):
      self.idx = 0
    return result

  def __getitem__(self, idx):
    idx = max(min(idx, len(self)), 0)
    return Configuration(self.samples[idx])


class RandomSampler(BaseSampler):
  def __init__(self, configuration, n_samples):
    super().__init__(configuration)
    self.n_samples = n_samples
    self.sample()

  def sample_field(self, idx, field):
    if isinstance(field, dict):
      if "values" in field:
        return np.random.choice(field["values"])
      elif "min" in field and "max" in field:
        val = np.random.uniform(field["min"], field["max"])
        if isinstance(field["min"], int) and isinstance(field["max"], int):
          val = int(val)
        return val
      elif "value" in field:
        return field["value"]
      elif "seq" in field:
        return field["seq"] * idx
      else:
        return None
    else:
      return field

  def sample(self):
    super().sample()
    for i in range(self.n_samples):
      current_sample = {}
      for k, v in self.configuration.items():
        current_sample[k] = self.sample_field(i, v)
      self.samples.append(current_sample)



class GridSampler(BaseSampler):
  def __init__(self, configuration):
    super().__init__(configuration)

  def sample(self):
    super().sample()
