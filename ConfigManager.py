import json 

def getConfig(configPath):
    '''
    Gets the config file for editing
    :param configPath:
    :return: jsonDecoded
    '''
    with open(configPath, "r") as f:
        jsonObject = f.read()
        jsonDecoded = json.loads(jsonObject)
        return jsonDecoded

def modifyConfig(configPath, jsonObject, modifyValue, modifier):
    '''
    modifies the config file
    :param configPath:
    :param jsonObject: json loaded string
    :param modifyValue: json object to be modified
    :param modifier: new value of json object
    '''
    with open(configPath, "w", encoding='utf-8') as f:
        jsonObject["config"][modifyValue] = modifier
        json.dump(jsonObject, f, ensure_ascii=False, indent=4)
