# -*- coding: utf-8 -*-
"""

@author: ulysses
"""

import argparse
import toml
import re
import json
import datetime
import requests

# Create the parser
my_parser = argparse.ArgumentParser(description='Show device of a TROPOS site at a specific timestamp')

# Add the arguments
my_parser.add_argument('--md_file', dest='md_file_input', metavar='markdown_file',
                       default='tropos_device_tracking_overview.md',
                       type=str,
                       help='the markdown file containing the device tracking informations')

my_parser.add_argument('--config_file',
                       default='config.json',
                       help='config file including base dirs etc.')

my_parser.add_argument('--site', dest='site', metavar='location',
                       default='all',
                       type=str,
                       help='the location to check; if set to \'all\' every location will be listed')

my_parser.add_argument('--timestamp', dest='timestamp', metavar='timestamp',
                       default='all',
                       type=str,
                       help='the date to look for; if set to \'all\' every timestamp will be listed')

my_parser.add_argument('--device_type', dest='device_type', metavar='type of device',
                       default='all',
                       type=str,
                       help='Here you can specify the type of the device - i.e. \'hatpro\' or \'polly\'. If left empty or set to \'all\' every device-type will be listet.')

my_parser.add_argument('--device_name', dest='device_name', metavar='name of device',
                       default='all',
                       type=str,
                       help='Here you can specify the device name you are looking for - i.e. \'Hatpro_LACROS\' or \'PollyXT_cpv\'. If left empty or set to \'all\' every device will be listet.')

my_parser.add_argument('--show_files', action='store_true',
                       help='switch: look for folder and files, where the measurement is stored.')

valid_levels = ['level', 'level0', 'level1', 'level1a', 'level1b', 'level2']
my_parser.add_argument('--datalevel', choices=valid_levels,
                       default='level',
                       help='choice of data level to scan for.')

my_parser.add_argument('--output_results_file', dest='outputfile', metavar='outputfile of results',
                       default='no',
                       type=str,
                       help='outputfile with full path to store the results to, when using the -s (--show_files)-option.')


# Execute the parse_args() method
args = my_parser.parse_args()

def main():
    with open(args.config_file,"r") as con_file:
            config_dict = json.load(con_file)

    meta_dict_ls = get_device_info(config_dict=config_dict, timestamp=args.timestamp, site=args.site, dev_type=args.device_type)
    for entry in meta_dict_ls:
        print(entry['DEVICE'])

    if args.show_files:
        data = get_data_base_dir_from_pylarda(config_dict=config_dict,meta_dict_ls=meta_dict_ls,datalevel=args.datalevel)
        for dev in data:
            print(dev)
            print(data[dev])



def get_device_info(config_dict:dict,timestamp:str,site:str,dev_type:str,dev_name='all') -> list:
    ## try using dev-tracker api
    deviceinfo = {}
    meta_dict_ls = []
    try:
        url = f'{config_dict["basic_url"]}?date={timestamp}&site={site}&dev_type={dev_type}&dev_name={dev_name}'
        metadata = requests.get(url).json()
        for c in metadata:
#            dev = metadata[f'{c}']['DEVICE']
#            camp = metadata[f'{c}']['HISTORY']['0']['pylarda_camp']
            meta_dict = metadata[f'{c}']
            meta_dict['TIMESTAMP'] = timestamp
            meta_dict_ls.append(meta_dict)
        return meta_dict_ls #deviceinfo 
    except Exception as e:
        print(f'Error: {e}')

def get_data_base_dir_from_pylarda(config_dict:dict,meta_dict_ls:list,filetype_ls=[]) -> dict:
    pylarda_basedir = config_dict['pylarda_basedir']
    all_campaigns_file = f'{pylarda_basedir}/larda-cfg/{config_dict["all_campaigns_file"]}'
    tomlcamp = toml.load(all_campaigns_file)

    data = {}
    for entry in meta_dict_ls:

        dev  = entry['DEVICE']
        dev_type  =entry['TYPE']
        pid  = entry['PID']
        camp = entry['HISTORY']['0']['pylarda_camp']
        timestamp = entry['TIMESTAMP']
        if len(camp) > 0:
            pass
        else:
            continue

        data[dev] = {}
        if dev in config_dict["device_dict"]:
            dev_translator = config_dict["device_dict"][dev]
        else:
            dev_translator = dev
        param_file = tomlcamp[camp]['param_config_file']
        param_file = f'{pylarda_basedir}/larda-cfg/{param_file}'
        tomldat = toml.load(param_file)
        correct_system = ''
        ft_ls = []
        for system in tomldat.keys():
            for file_type in tomldat[system]['path'].keys():
                base_dir = tomldat[system]['path'][file_type]['base_dir']
                if re.search(dev_translator, base_dir, re.IGNORECASE):
                    correct_system = system
                    break
            if len(correct_system) > 0:
                break
        ft_ls = [i for i in tomldat[correct_system]['path'].keys()]
        connector_file = f'{pylarda_basedir}/larda-connectordump/{camp}/connector_{correct_system}.json'
        try:
            connector_file_json = open(connector_file)
            connector_dict = json.load(connector_file_json)
        except Exception:
            connector_dict = ""
            pass

        data[dev][correct_system] = {}
        if len (filetype_ls) == 0:
            filetype_ls = ft_ls
        for ft in filetype_ls:
           data[dev][correct_system][ft] = []

           if connector_dict:
               filenames_ls = []
               for entry in connector_dict[ft]:
                   entry_date = re.split(r'-',str(entry[0][0]))[0]

                   if timestamp == entry_date:
                       filename = entry[1]
                       filename = re.split(r'^\.\/',filename)[1]
                       full_filename = f"{base_dir}{filename}"
                       data[dev][correct_system][ft].append(full_filename)

    return data



if __name__ == '__main__':
    main()

#
#                ## write files_list to json-$outputfile
#                outputfile_json = args.outputfile
##                outputfile_json = re.split(r'\.',args.outputfile)[0]
##                outputfile_json = f'{outputfile_json}.json'
#                if outputfile_json != 'no':
#                    files_list_file = open(outputfile_json, "w")
#                    files_list_file.write('{\n')
#                    files_list_file.write(f'"device": "{str(dev)}",\n')
#                    files_list_file.write(f'"device_type": "{str(args.device_type)}",\n')
#                    files_list_file.write(f'"site": "{str(location)}",\n')
#                    files_list_file.write(f'"instrumentPid": "{str(PID)}",\n')
#                    #files_list_file.write(f'"files": "{files_list}"\n')
#                    files_list_file.write(f'"files": "')
#                    if len(files_list)>0:
# #                       print("\nfiles found:")
#                        for f in files_list:
#                            if f == files_list[-1]:
#                                files_list_file.write(f'{f}')
#                            else:
#                                files_list_file.write(f'{f} ')
##                            print(f)
#                    files_list_file.write('"\n')
#                    files_list_file.write('}')
#                    files_list_file.close()
#
            
