"""
  Elastool -- Elastic toolkit for zero and finite-temperature elastic constants and mechanical properties calculations

  Copyright (C) 2019-2024 by Zhong-Li Liu and Chinedu Ekuma

  This program is free software; you can redistribute it and/or modify it under the
  terms of the GNU General Public License as published by the Free Software Foundation
  version 3 of the License.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY
  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
  PARTICULAR PURPOSE.  See the GNU General Public License for more details.

  E-mail: zl.liu@163.com, cekuma1@gmail.com

"""

from os import getcwd
import os
from write_default_input import write_default_input,write_default_elastool_in,print_default_input_message_0,print_default_input_message_1,display_help
import sys
from elastool_elate_browser import ElateAutomation

def process_parameters(input_string):
    parameters = input_string.strip().split(',')
    parameters = [param.strip() for param in parameters]
    return parameters

def read_input():
    cwd = getcwd()
    main_infile = open('%s/elastool.in' % cwd, 'r')
    line = main_infile.readline()
    global indict
    indict = {}
    while line:
        line = main_infile.readline()
        llist = line.split('=')
        
        if llist != ['\n'] and llist != ['']:
            if llist[0][0] != '#':
                inputlist = [i.strip().split() for i in llist]
                
                # Handle elateparameters differently
                if inputlist[0][0] == 'elateparameters':
                    indict['elateparameters'] = process_parameters(llist[1])
                    #parameters = llist[1].strip().split(',')
                    #parameters = [param.strip() for param in parameters]
                    #indict['elateparameters'] = parameters
                elif inputlist[0][0] == 'plotparameters':
                    indict['plotparameters'] = process_parameters(llist[1])
                else:
                    if inputlist[1] == []:
                        with open('../log.elastool', 'a') as logfile:
                            print >>logfile, "Please give the value(s) for: %s" % inputlist[0][0]
                    else:
                        indict[inputlist[0][0]] = inputlist[1]
                        
    run_mode_flag = (len(sys.argv) > 1 and sys.argv[1] == "-0") or ('run_mode' in indict and int(indict['run_mode'][0]) == 0)

    if 'method_stress_statistics' in indict and run_mode_flag:
        write_default_input(indict['method_stress_statistics'][0], cwd)
        print_default_input_message_1()
        sys.exit(0)
    return indict


if len(sys.argv) > 1:
    activate_flag = sys.argv[1] in ["-elate", "-Elate", "-ELATE"] #and int(indict['run_mode'][0]) == 4
else:
    activate_flag = False

if activate_flag:
    browser = input("Choose a browser; when done press Ctrl+C: (chrome, firefox, edge, safari): ").lower()
    elate_instance = ElateAutomation(browser_name=browser)
    elate_instance.run()
    sys.exit(0)


# Check if any argument is a help command
help_commands = (len(sys.argv) > 1 and (sys.argv[1] == "-help" or sys.argv[1] == "--help" or sys.argv[1] == "--h" or sys.argv[1] == "-h"))
if help_commands:
    display_help()
    sys.exit(0)



cwd = os.getcwd()
elastool_in_exists = os.path.exists(os.path.join(cwd, "elastool.in"))
run_mode_flag_elastoolin = (len(sys.argv) > 1 and sys.argv[1] == "-0")
if run_mode_flag_elastoolin and not elastool_in_exists:
  write_default_elastool_in(cwd)
  print_default_input_message_0()
  sys.exit(0)


indict = read_input()

