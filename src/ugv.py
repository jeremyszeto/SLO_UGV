"""Autonomous UGV"""
import json
from coms import Coms

class UGV:
    def __init__(self):
        #TODO
        return None
    
    def setup_vehcicle(self):
        #TODO
        return None

    def coms_callback(self, message, _):
        '''callback for radio messages'''
        data = json.loads(message.data)
        print(data['type'])

    def setup_coms(self):
        '''sets up communication radios'''
        print('Initializing Coms')
        self.coms = Coms(self.configs, self.coms_callback)