import subprocess, re, os, random
from .printer import printd

def run_nvidia_smi():

    try:
        o = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        o = o.stdout.decode('utf-8').split('\n')
    except:
        o = []

    return o

def find_all():
    """
    Method to find all available NVIDIA GPU(s) and associated usage status

    """
    lines = run_nvidia_smi()
    gpus = {}

    for n, line in enumerate(lines):
        
        # --- Look for _ MiB / _ MiB
        usage = re.findall('[0-9]*MiB', line)
        if len(usage) == 2 and n > 0:
            device = re.findall(' +[0-9]+', lines[n - 1])
            if len(device) > 0:

                gpus[int(device[0])] = {
                    'alloc': int(usage[0][:-3]),
                    'total': int(usage[1][:-3]),
                    'percentage': int(usage[0][:-3]) / int(usage[1][:-3])}

    return gpus

def find_available(percentage=0.5, alloc=5000, total=11000):
    """
    Method to find available NVIDIA GPU(s) based on criteria

    """
    return {k: v for k, v in find_all().items() if \
        (v['percentage'] < percentage) & \
        (v['alloc'] < alloc) & \
        (v['total'] > total)}

def autoselect(count=1, percentage=0.5, alloc=5000, total=11000, randomize=True, verbose=True):
    """
    Method to autoselect available NVIDIA GPU(s)

      (1) Use currently set os.environ['CUDA_VISIBLE_DEVICES'] if present, otherwise
      (2) Use availabe GPU(s) based on count

    :params

      (int)   count      : total # of GPU(s) to allocate
      (float) percentage : threshold for max current percentage usage
      (int)   alloc      : threshold for max current alloc GPU memory (MiB)
      (int)   total      : threshold for min current total GPU memory (MiB)
      (bool)  randomize  : if True, select random GPU meeting critiera; otherwise in PCI_BUS_ID order

    By default, this method will select 1 GPU with:

      * percent usage < 50%
      * alloc GPU memory < 5000 MiB
      * total GPU memory > 11000 MiB

    """
    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    DEVICES = os.environ.get('CUDA_VISIBLE_DEVICES', '')

    if len(DEVICES) > 0:
        printd('CUDA_VISIBLE_DEVICES already manually set to: {}'.format(DEVICES), verbose=verbose)
        return

    gpus = find_available(percentage=percentage, alloc=alloc, total=total)
    keys = list(gpus.keys())

    if len(keys) < count:
        printd('WARNING {} GPU device(s) requested but only {} available'.format(count, len(keys)), verbose=verbose)
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1' 
        return

    if count <= 0: 
        printd('CPU mode requested', verbose=verbose)
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1' 
        return

    if randomize:
        random.shuffle(keys)

    keys = sorted(keys[:count])
    DEVICES = ','.join([str(k) for k in keys])
    os.environ['CUDA_VISIBLE_DEVICES'] = DEVICES

    printd('CUDA_VISIBLE_DEVICES automatically set to: {}'.format(DEVICES), verbose=verbose)
