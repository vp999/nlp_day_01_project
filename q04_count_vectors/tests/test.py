import unittest
from inspect import getfullargspec
import warnings
# warnings.filterwarnings("ignore")
from ..build import q04_count_vectors
from greyatomlib.nlp_day_01_project.q04_count_vectors.build import q04_count_vectors as act_sol

import numpy as np

path = 'data/20news-bydate-train/'
student_return = q02_tokenize(path)
original_return = act_sol(path)


class Testing(unittest.TestCase):

    #  Check the arguements of the function

    def test_args(self):
        # Input parameters tests
        args = getfullargspec(q02_tokenize)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_defaults(self):
        args = getfullargspec(q02_tokenize)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_return_4(self):
        self.assertEqual(np.array(student_return[0]).shape, np.array(original_return[0]).shape,
                         "The return values do not match expected values")

    def test_return_4_2(self):
        self.assertEqual(np.array(student_return[1]).shape, np.array(original_return[1]).shape,
                         "The return values do not match expected values")
