import unittest
from main import parse_object_rows, human_size

class BlobBudgetTests(unittest.TestCase):
    def test_filters_and_sorts_blobs(self):
        rows = ["a blob 100", "b tree 900", "c blob 500"]
        result = parse_object_rows(rows, {"a":"small.txt","c":"large.bin"}, 200, 5)
        self.assertEqual([item["oid"] for item in result], ["c"])
    def test_human_size(self):
        self.assertEqual(human_size(1024), "1.0 KB")

if __name__ == "__main__":
    unittest.main()
