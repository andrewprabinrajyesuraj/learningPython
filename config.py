# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:26:31 2024

@author: araj2
"""

import os

def get_config():
    env = os.getenv('ENVIRONMENT', 'QA')
    print(env)# Default to DEV if not set

    configs = {
        'DEV': {'db': 'dev_db', 'debug': True},
        'QA': {'db': 'qa_db', 'debug': False},
        'PROD': {'db': 'prod_db', 'debug': False}
    }
    print(configs.get('PROD')['db'])
    return configs.get(env, configs['DEV'])
   

config = get_config()
print(config)
print(f"Database: {config['db']}")
print(f"Debug: {config['debug']}")
