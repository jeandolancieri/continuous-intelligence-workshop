import unittest
import json

class TestAccuracy(unittest.TestCase):
    METRICS_FILE = "results/metrics.json"

    def test_80percent_error_score(self):
        with open(self.METRICS_FILE, 'r') as file:
            metrics = json.load(file)
            self.assertGreater(metrics['nwrmsle'], 0.80)
            self.assertLessEqual(metrics['r2_score'], 0.0)


if __name__ == "__main__":
    unittest.main()
