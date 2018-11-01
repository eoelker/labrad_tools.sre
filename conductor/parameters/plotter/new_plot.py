import json
from copy import deepcopy

from labrad.wrappers import connectAsync
from twisted.internet.defer import inlineCallbacks

from matplotlib import pyplot as plt

from conductor.parameter import ConductorParameter

class NewPlot(ConductorParameter):
    priority = 1

    def initialize(self):
        self.connect_to_labrad()
    
    def update(self):
        data_copy = deepcopy(self.conductor.data)
        if self.value:
            self.cxn.new_plotter.plot(json.dumps(self.value), 
                    json.dumps(data_copy, default=lambda x: None))
