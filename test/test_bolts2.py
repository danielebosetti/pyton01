import unittest
from eurocode import bolts

class TestBolt(unittest.TestCase):
  
  def testBoltAlpha(self):
    boltType=bolts.getBoltByLabel('4.6')
    alpha=bolts.getAlphaFor(boltType)
    assert alpha==0.6
