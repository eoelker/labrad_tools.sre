from twisted.internet.defer import inlineCallbacks
from labrad.wrappers import connectAsync
import json
from conductor.parameter import ConductorParameter

class HrDemodFrequencyCleanup(ConductorParameter):
    priority = 1
    dark_frequency = 2.0*135.374e6

    def initialize(self):
        self.connect_to_labrad()
        request =  {'cu_pulse': {'frequency': self.dark_frequency} }
        self.cxn.rf.frequency(json.dumps(request))

        print 'hr_demod_frequency_cleanup init\'d with freq: {}'.format(self.dark_frequency)
    
    def update(self):
        if self.value is not None:
            request =  {'cu_pulse': {'frequency': self.value} }
            self.cxn.rf.frequency(json.dumps(request))
