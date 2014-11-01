__author__ = 'GuidoE'
#!/usr/bin/env python

import RFM69
import RFM69registers as regs
from RFM69registers import *

test = RFM69.RFM69(RF69_915MHZ, 0x01, 0x0A, True)
#test.promiscuousMode=True
print "setting encryption"
test.encrypt("guidoespinosa")

print "class initialized"
print "reading all registers"
results = test.readAllRegs()
for result in results:
    print result
print "Performing rcCalibration"
test.rcCalibration()
print "setting high power"
test.setHighPower(True)
print "Checking temperature"
print test.readTemperature(0)
print "reading"
test.receiveBegin()
while not test.receiveDone():
    pass
print test.DATA
print "shutting down"
test.shutdown()
