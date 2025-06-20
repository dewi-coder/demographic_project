import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicAnalyzer(unittest.TestCase):
    def test_keys_exist(self):
        data = calculate_demographic_data(print_data=False)
        expected_keys = [
            "race_count", "average_age_men", "percent_bachelors", "higher_ed_rich",
            "lower_ed_rich", "min_work_hours", "rich_percentage_min_workers",
            "highest_earning_country", "highest_earning_country_perc", "top_IN_occupation"
        ]
        for key in expected_keys:
            self.assertIn(key, data)

if __name__ == "__main__":
    unittest.main()
