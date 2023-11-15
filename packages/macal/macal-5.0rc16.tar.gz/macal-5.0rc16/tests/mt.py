# This is a test for creating an agent style appliaction that uses the Macal interpreter/runtime.

import os
import argparse
import sys
from macal.macal_vm import MacalVm

AGENTVERSIONMSG = "Meraki Agent v10.0.rc1"

gl_orgname = "orgname"
gl_orgid = "orgid"
gl_apikey = "api"
gl_hostname = "host"
gl_script = "script"
gl_configuration = {
    "bandwidth_timespan": "86400",
    "enable_bandwidth": "True",
    "enable_demo": "False",
    "enable_logging": "True",
    "enable_public_ip": "True",
    "show_address": "True",
    "show_errors": "True",
    "show_firmware": "True",
    "show_soft_errors": "True",
    "show_execution_time": "True",
    "save_unknown_events": "True",
    "security_event_timespan": "86400",
    "syslog_address": "",
    "device_serial": "",
    "customers" : [
        {"name": "Stage Entertainment", "orgid": "549236", "apikey": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"},
        {"name": "Medialane", "orgid": "549236", "apikey": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"},	
    ]
}

def ParseArgs():
    """Parse and return the command line arguments."""
    parser = argparse.ArgumentParser(description='Run Meraki Agent script .mcl file.')
    
    parser.add_argument('-c',  '--configure',      help='Change the configuration',                           action='store_true')
    parser.add_argument('-d',  '--del_customer',   help='Deletes a customer from the configuration',          action='store_true')
    parser.add_argument('-e',  '--execute',        help='Load and execute the *.pyql configuration file.',    action='store_true')
    parser.add_argument('-io', '--ignore_org',     help='Ignore the org parameter value, can be used for special scripts only.',    action='store_true')
    parser.add_argument('-l',  '--list_customers', help='Shows a list of all customers in the configuration', action='store_true')
    parser.add_argument('-m',  '--check_customer', help='Checks if a customer exists in the configuration',   action='store_true')
    parser.add_argument('-n',  '--new_customer',   help='Creates a new customer in the configuration',        action='store_true')
    parser.add_argument('-so', '--safetyoverride', help='Overrides exeption handling.',         					 action="store_true")
    parser.add_argument('-sc', '--show_config',    help='Shows the current agent configuration',              action="store_true")
    parser.add_argument('-v',  '--version',        help="Shows agent version information.",                   action='version', version=AGENTVERSIONMSG)
    parser.add_argument('-vv', '--versionverbose', help='Shows verbose agent version information.',           action="store_true")
    
    reqd = parser.add_argument_group('required named arguments')

    op_delcust    = '-d'  in sys.argv or '--del_customer'   in sys.argv
    op_exec       = '-e'  in sys.argv or '--execute'        in sys.argv
    op_newcust    = '-n'  in sys.argv or '--new_customer'   in sys.argv
    op_checkcust  = '-m'  in sys.argv or '--check_customer' in sys.argv
    op_vversion   = '-vv' in sys.argv or '--versionverbose' in sys.argv
    op_orgname    = '-o'  in sys.argv or '--orgname'        in sys.argv

    req_hostname  = op_exec
    req_apikey    = op_exec or op_vversion
    req_orgname   = op_delcust or op_exec or op_newcust or op_checkcust
    req_orgid     = (op_delcust or op_exec or op_newcust or op_checkcust) and not op_orgname

    reqd.add_argument('-H', '--hostname', help='Hostname variable. Used by API', required = req_hostname)
    reqd.add_argument('-k', '--apikey',   help='API Key to access the API', required = req_apikey)
    reqd.add_argument('-o', '--orgname',  help='Orginasation/Customer name variable. Used by API and configuration.', required = req_orgname)
    reqd.add_argument('-i', '--orgid',    help='Orginasation/Customer ID variable. Used by API and configuration.', required = req_orgid)
    reqd.add_argument('-s', '--script',   help='The PyQL script to execute.', required = op_exec)

    #For configuration -c // --config, all optional.
    reqd.add_argument('-bc', '--backup_config',           help='Make a backup of the current configuration to this file.', required = False)
    reqd.add_argument('-bt', '--bandwidth_timespan',      help='Set network bandwidth timespan for a customer.', required = False)
    reqd.add_argument('-eb', '--enable_bandwidth',        help='Enable/disable showing bandwidth history and trafficshaping max bandwidth for a customer.', required = False)
    reqd.add_argument('-ed', '--enable_demo',             help='Enable/disable demo mode for a customer.', required = False)
    reqd.add_argument('-el', '--enable_logging',          help='Enable/disable logging.', required = False)
    reqd.add_argument('-ep', '--enable_public_ip',        help='Enable/disable showing public ip for a customer.', required = False)
    reqd.add_argument('-rb', '--restore_config',          help='Restore configuration from this file.', required = False)
    reqd.add_argument('-sa', '--show_address',            help='Enable/disable show address for a customer.', required = False)
    reqd.add_argument('-se', '--show_errors',             help='Enable/disable show errors.', required = False)
    reqd.add_argument('-sf', '--show_firmware',           help='Enable/disable show firmware for a customer.', required = False)
    reqd.add_argument('-sse', '--show_soft_errors',       help='Enable/disable show soft errors (script execution).', required = False)
    reqd.add_argument('-st', '--show_execution_time',     help='Enable/disable show execution time.', required = False)
    reqd.add_argument('-su', '--save_unknown_events',     help='Enable/disable Save unknown network events.', required = False)
    reqd.add_argument('-sv', '--security_event_timespan', help='Set security event timespan for a customer.', required = False)
    reqd.add_argument('-sy', '--syslog_address',          help='Hostname syslog server.', required = False)
    reqd.add_argument('-sn', '--device_serial',           help='Device serial number for scripts.', required = False)
    return parser.parse_args()


def main():
    args = ParseArgs()
    global gl_hostname, gl_apikey, gl_orgname, gl_orgid, gl_script
    vm = MacalVm("usereserved.mbc")
    vm.SetReservedVariable("orgname", args.orgname)
    vm.SetReservedVariable("orgid", args.orgid)
    vm.SetReservedVariable("apikey", args.apikey)
    vm.SetReservedVariable("hostname", args.hostname)
    vm.SetReservedVariable("script", args.script)
    vm.SetReservedVariable("configuration", gl_configuration)
    result = vm.Execute()
    if result != -2:
        print(f"Runtime Error: expected -2 from execute, got: {result}.")
    exitcode = vm.stack[0][1]
    print("Process exitcode: ", exitcode)
    return exitcode


if __name__ == "__main__":
    main()