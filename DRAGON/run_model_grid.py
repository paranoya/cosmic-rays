#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a new DRAGON model, changing some of the parameters.

Created on July 28, 2023
@author: Yago Ascasibar
"""

from __future__ import print_function, division

import os
import xml.dom.minidom as dom
#import subprocess  # TODO: use subprsubprocess.run() it instead of os.system()
import numpy as np


def generate_model(base_model_name, suffix, change_params):
    '''
    Read `base_model_name`.xml,
    change the parameters in the dictionary `change_params` to the specified values,
    and save as `base_model_name`_`suffix`.xml
    '''
    
    # read original XML file
    base_model_path = os.path.join('input', base_model_name)
    with open(f'{base_model_path}.xml', 'r') as file:
        lines = file.readlines()
    base_model_str = ''.join([lines[0], '<DRAGONmodel>\n'] + lines[1:] + ['</DRAGONmodel>'])  # proper XML can only contain one root node
    model = dom.parseString(base_model_str)

    # change parameters
    for param in change_params:
        model.getElementsByTagName(param)[0].setAttribute('value', f'{change_params[param]}')

    # write modified XML file
    model_str = '\n'.join([lines[0]] + model.toxml().split('\n')[1:-1])
    with open(f'{base_model_path}_{suffix}.xml', 'w') as file:
        file.write(model_str)


base_model_name = 'run_2D_DM'
#model_grid = {'D0_1e28': np.linspace(.5, 5, 3)}
model_grid = {'Delta': [0.4, 0.8]}
#models_run = 0
for param in model_grid:
    print(f'Changing {param}:')
    for value in model_grid[param]:
        suffix = f'{param}={value}'
        generate_model(base_model_name, suffix, {param: value})
        print(f'- {param} = {value}: {base_model_name}_{suffix}')
        #os.system(f'./run_DRAGON.sh {base_model_name}_{models_run}')
        os.system(f'./run_DRAGON.sh {base_model_name}_{suffix}')
        #models_run += 1
print('                                        ... Paranoy@ Rulz!')
