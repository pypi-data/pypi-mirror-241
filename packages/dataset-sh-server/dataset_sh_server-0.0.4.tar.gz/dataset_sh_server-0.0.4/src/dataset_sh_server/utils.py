def generate_download_code_py(hostname, dataset_name):
    template = f'''
import dataset_sh
dataset_sh.import_remote("{dataset_name}", host="{hostname}")
    '''.strip()
    return template


def generate_download_code_bash(hostname, dataset_name):
    template = f'''
dataset.sh import {dataset_name} -h {hostname}
    '''.strip()
    return template
