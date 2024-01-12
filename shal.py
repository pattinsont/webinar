import argparse
from iosxr.xrcli.xrcli_helper import XrcliHelper
from cisco.script_mgmt import xrlog

def run_custom_show_command(alias):
    helper = XrcliHelper(debug=True)
    cmd = f"show run | include {alias}"
    result = helper.xrcli_exec(cmd)
    
    if result['status'] == 'success':
        print(result['output'].replace(';', '\n'))
        xrlog.getSysLogger('custom_show_command').info('SCRIPT : Custom show command successful')
    else:
        xrlog.getSysLogger('custom_show_command').error('SCRIPT : Custom show command failed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("alias", type=str, help="alias to include in the show command")
    args = parser.parse_args()
    run_custom_show_command(args.alias)
