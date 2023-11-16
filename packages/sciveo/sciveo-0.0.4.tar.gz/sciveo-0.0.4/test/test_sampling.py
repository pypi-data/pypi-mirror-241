import unittest

from sciveo.sampling import RandomSampler


class TestSampling(unittest.TestCase):
  def test_random_1(self):
    config = {
        "booster": {
            "values": ["gbtree", "gblinear"]
        },
        "learning_rate": {
          "min": 0.001,
          "max": 1.0
        },
        "gamma": {
          "min": 0.001,
          "max": 1.0
        },
        "max_depth": {
            "values": [3, 5, 7]
        },
        "min_child_weight": {
          "min": 1,
          "max": 150
        },
        "early_stopping_rounds": {
          "values" : [10, 20, 30, 40]
        },
    }

    sampler = RandomSampler(config, n_samples=10)

    print(sampler.samples)

    self.assertTrue(len(sampler.samples) == 10)


if __name__ == '__main__':
    unittest.main()
    # T = TestSampling()
    # T.test_random_1()