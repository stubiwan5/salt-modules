from datetime import datetime
import sys
import subprocess
import os

__virtual_name__ = 'dns_serial'

def __virtual__():
    return __virtual_name__

def current(domain):
    dig_command = "dig any " + domain + " | grep SOA | awk '{print $7}'"
    current_serial = subprocess.check_output([dig_command], shell=True)
    return current_serial

def new(domain):
    dig_command = "dig any " + domain + " | grep SOA | awk '{print $7}'"
    current_serial = subprocess.check_output([dig_command], shell=True)
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds
    date = now.strftime("%Y%m%d")
    calculated_serial = str(date) + '01'
    if int(calculated_serial) > int(current_serial):
        new_serial = calculated_serial
    else:
        new_serial = int(current_serial) + 1
    return new_serial
