'''This module update.py provides functions to  make the data files dynamic.
'''

import pkg_resources
import requests

prefix = 'd9fb98d88f620d0320bf305ada414299/raw/616fadf34d3a46ae6e02b63580e0d318d0a4a0cf'

URL = f'https://gist.githubusercontent.com/aahnik/{prefix}/'

remote_varVer = f'{URL}wapp-driver-var-ver'
remote_var = f'{URL}wapp-driver-var.yml'

P = 'wappdriver'

var = pkg_resources.resource_filename(P, 'data/var.yml')

chrome_driver_path_file = pkg_resources.resource_filename(
    P, 'data/chrome_driver_path.txt')


varVer = pkg_resources.resource_filename(P, 'data/varVer.txt')

local_varVer_val = float(open(varVer).readline())


def set_chrome_driver_path(path):
    '''Method to set the chrome driver path, applies to your current virtual environment only
    Agumemts: path ( the value of path should be the absolute path to the 
    installation of Chrome Driver executable)
    '''
    with open(chrome_driver_path_file, 'w') as f:
        f.write(path)


def update_cdp():
    # cdp stands for chrome_driver_path
    path = input('Paste the absoulte path of Chrome Driver: \n')
    set_chrome_driver_path(path)


def fetch_vars():
    latest_varVer = float(requests.get(url=remote_varVer).text)
    if latest_varVer > local_varVer_val:
        open(var, 'w').write(requests.get(url=remote_var).text)
        open(varVer, 'w').write(str(latest_varVer))
        return('updated sucessfully')
    else:
        return('already the latest version')
