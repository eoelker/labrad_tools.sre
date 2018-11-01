import json
import time

from twisted.internet.defer import inlineCallbacks

from conductor.parameter import ConductorParameter

class Plot(ConductorParameter):
    data_dir = '/media/j/data/{}/scans/{}#{}/'
    priority = 1

    
    def initialize(self):
        self.connect_to_labrad()
    
    def update(self):
        if self.value:
            settings = json.loads(self.value)
            date_str = time.strftime('%Y%m%d')
            exp_name = self.conductor.experiment_name
            exp_num = self.conductor.experiment_number
            exp_pt = self.conductor.point_number
            run_dir = self.data_dir.format(date_str, exp_name, exp_num)
            settings['data_path'] = run_dir

            self.cxn.plotter.plot(json.dumps(settings))
