import unittest
from eurocode.bolts import *

class TestBolt(unittest.TestCase):
  
  def testBoltAlpha(self):
    boltType=getBoltByLabel('4.6')
    alpha=getAlphaFor(boltType)
    assert alpha==0.6
