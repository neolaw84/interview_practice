import unittest
import tempfile

from tests.utils import remove_file_silently
from interview_practice.arrays.count_triplets import count_triplets

class CountTripletsTests(unittest.TestCase):
    def SetUp(self):
        pass

    def TearDown(self):
        pass

    def test_case_1(self):
        test_data = """2
            4
            1 5 3 2
            3
            3 2 7""".replace("  ", "")
        tf = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
        tfname = tf.name
        try:
            with open (tfname, "wt") as f:
                f.write(test_data)
            results = [2, -1]
            outputs = [output for output in count_triplets(tfname)]
            self.assertListEqual(results, outputs)
        finally:
            remove_file_silently(tfname)
        