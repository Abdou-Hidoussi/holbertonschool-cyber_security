import importlib
import json
import os

def check_all(config_file=None,json_file=None,file_path=None):
    """ use config json to generat a json file with the status of the checks """
    if (config_file == None):
        return ("please provide a config file for this checker")
    if (json_file == None):
        return ("please provide an output file for this checker")
    config = open(config_file)
    check_list = json.load(config)
    output = []
    requirment = True
    for mod in check_list:
        for check in check_list[mod]:
            for conf in check_list[mod][check]:
                module = importlib.import_module(mod)
                response = {
                    "check": check,
                    "status": "",
                    "error": "",
                    "desc": getattr(module, check).__doc__,
                    "arg": "",
                    "file": "",
                }
                if requirment:
                    file = conf[0]
                    arg = conf[1]
                    result = getattr(module, check)(file_path+"/"+file, arg)
                    if not result:
                        response["status"] = "Failed"
                        response["error"] = ""
                        response["arg"] = arg
                        response["file"] = file
                        if (len(conf) >= 3) and (not result):
                            requirment = False
                        output.append(response)
                    else:
                        response["status"] = "Success"
                        response["error"] = ""
                        response["arg"] = arg
                        response["file"] = file
                        output.append(response)
                else:
                    response["status"] = "Failed"
                    response["arg"] = None
                    response["file"] = None
                    response["error"] = "Requirment Fail"
                    output.append(response)
    config.close()
    return output

def check_file(json_tasks=None, file_content=None):
    output = []
    requirment = True
    for mod in json_tasks:
        for check in json_tasks[mod]:
            for conf in json_tasks[mod][check]:
                module = importlib.import_module(mod)
                response = {
                    "check": check,
                    "status": "",
                    "error": "",
                    "desc": getattr(module, check).__doc__,
                    "arg": "",
                    "file": "",
                }
                if requirment:
                    file = conf[0]
                    arg = conf[1]
                    result = getattr(module, check)(file_content, arg)
                    if not result:
                        response["status"] = "Failed"
                        response["error"] = ""
                        response["arg"] = arg
                        response["file"] = file
                        if (len(conf) >= 3) and (not result):
                            requirment = False
                        output.append(response)
                    else:
                        response["status"] = "Success"
                        response["error"] = ""
                        response["arg"] = arg
                        response["file"] = file
                        output.append(response)
                else:
                    response["status"] = "Failed"
                    response["arg"] = None
                    response["file"] = None
                    response["error"] = "Requirment Fail"
                    output.append(response)
    return output