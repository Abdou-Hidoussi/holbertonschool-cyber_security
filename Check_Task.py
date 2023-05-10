import importlib
import json

def check_all(config_file=None,json_file=None):
    if (config_file == None):
        return ("please provide a config file for this checker")
    if (json_file == None):
        return ("please provide an output file for this checker")
    config = open(config_file)
    check_list = json.load(config)
    output_file = open(json_file, 'w+')
    output = []
    for mod in check_list:
        for check in check_list[mod]:
            for conf in check_list[mod][check]:
                file = conf[0]
                arg = conf[1]
                module = importlib.import_module(mod)
                result = getattr(module, check)(file, arg)
                response = {
                    "check": "",
                    "status": "",
                    "error": "",
                    "desc": "",
                }
                response["check"] = check
                response["desc"] = getattr(module, check).__doc__
                if not result:
                    response["status"] = "Failed"
                    output.append(response)
                else:
                    response["status"] = "Success"
                    response["error"] = ""
                    output.append(response)
    json.dump(output, output_file)
    output_file.close()
    config.close()
