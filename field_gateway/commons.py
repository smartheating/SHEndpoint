from pathlib import Path
from module import Module

def read_yaml(path):
    import yaml
    with open(path, 'r') as f:
        result = yaml.safe_load(f)
    return result


def read_device_ids():
    import json
    device_ids = None
    try:
        with open(str(get_project_root() / 'device_ids.json'), 'r') as f:
            device_ids = json.load(f)
    except:
        pass
    if not isinstance(device_ids, dict):
        device_ids = {}
    return device_ids


def store_device_ids(device_ids):
    import json
    with open(str(get_project_root() / 'device_ids.json'), 'w') as f:
        json.dump(device_ids, f)


def get_project_root() -> Path:
    import inspect, os
    return Path(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) / '..'


def print_modules(l_modules: [Module]):
    from tabulate import tabulate
    tab_data = [[m.module_name, m.module_type, m.module_id, m.module_ip, m.module_port, m.cloud_gateway_ip, m.cloud_gateway_port, m.reads_per_minute, m.send_interval, m.script_path] for m in l_modules]
    print(tabulate(tab_data, headers=['name', 'type', 'module_id', 'module_ip', 'module_port', 'cloud_gateway_ip', 'cloud_gateway_port', 'reads_per_minute', 'send_interval', 'script_path']))
