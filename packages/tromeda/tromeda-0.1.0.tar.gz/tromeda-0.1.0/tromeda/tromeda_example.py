import tromeda.get_tropos_datafiles as tromeda
import json

config_file = ''
with open(config_file,"r") as con_file:
            config_dict = json.load(con_file)

meta_dict_ls = tromeda.get_device_info(config_dict=config_dict, timestamp='20230111', site='mindelo', dev_type='halo')
for entry in meta_dict_ls:
    print(entry)
    print(entry['DEVICE'])
    print(entry['HISTORY']['0']['CAMPAIGN'])
    print(entry['HISTORY']['0']['pylarda_camp'])

data = tromeda.get_data_base_dir_from_pylarda(config_dict=config_dict,meta_dict_ls=meta_dict_ls,filetype_ls=['scans','hpl'])
print(data)

