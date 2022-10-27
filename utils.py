import random
from datetime import datetime
import json
START_TIME = datetime.now()

def get_printers(a=3,b=5):
    count = random.randint(a,b)
    names = ['winton', 'pabu', 'appa', 'naga', 'jackycha6', 'wantom123']
    return random.sample(names,count)

def init_printer(printer_name):
    printer = {'name': printer_name}
    printer['e_temp'] = 20.5
    printer['b_temp'] = 20.5
    printer['b_target'] = 0
    printer['e_target'] = 0
    printer['job'] = False
    printer['progress'] = 0
    printer['job_price'] = 0
    printer['job_progress'] = 0
    printer['time_update'] = datetime.now()
    return update_printer(printer)

def update_printer(printer):
    last_update = printer['time_update']
    seconds = int((datetime.now()-last_update).total_seconds())
    for second in range(10*seconds):

        if printer['job'] == False:
            if random.uniform(0,1)>0.999:
                printer['job'] = True
                printer['job_price'] = random.randint(1000,5000)
            printer['b_target'] = 20.5
            printer['e_target'] = 20.5
        
        if printer['job'] == True:
            if printer['progress'] >= 100:
                printer['job'] = False
            else:
                printer['progress'] = printer['job_progress']/printer['job_price']
                printer['job_progress'] += 1

        if (printer['e_target']-1) < printer['e_temp'] < (printer['e_target']+1):
            printer['e_temp'] = random.uniform(printer['e_temp']-1,printer['e_temp']+1)
        elif printer['e_temp'] > (printer['e_target']+1):
            printer['e_temp'] -= 0.2
        elif printer['e_temp'] < (printer['e_target']-1):
            printer['e_temp'] += 0.2

        if (printer['b_target']-1) < printer['b_temp'] < (printer['b_target']+1):
            printer['b_temp'] = random.uniform(printer['b_temp']-1,printer['b_temp']+1)
        elif printer['b_temp'] > (printer['b_target']+1):
            printer['b_temp'] -= 0.2
        elif printer['b_temp'] < (printer['b_target']-1):
            printer['b_temp'] += 0.2
    
    printer['time_update'] =datetime.now()
    return printer

def get_stats(printer):
    res = json.dumps(printer)
    return res

def get_all_stats(printers):
    result = []
    for printer in printers:
        result.append(update_printer(printer))
    return result





