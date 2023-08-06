
import unittest
import numpy as np

import mmct.mc as mc

class TestGetMultinomObs(unittest.TestCase):

  def test_2d(self):
    prob = np.array([0.3,1.0])
    r = np.array([0.90,0.15,0.30,0.22,0.10])
    m = mc.get_multinom(prob,r)
    self.assertEqual(2,m.size)
    self.assertEqual(3,m[0])
    self.assertEqual(2,m[1])

  def test_3d(self):
    prob = np.array([0.5,0.9,1.0])
    r = np.array([0.50,0.90,0.15,0.45,0.81,0.46,0.38,0.38])
    m = mc.get_multinom(prob,r)
    self.assertEqual(3,m.size)
    self.assertEqual(5,m[0])
    self.assertEqual(2,m[1])
    self.assertEqual(1,m[2])
