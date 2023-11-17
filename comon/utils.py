def remove_none_values(json_dict):
    if isinstance(json_dict, dict):
        new_dict = {}
        for key, value in json_dict.items():
            if value is not None:
                new_dict[key] = (
                    remove_none_values(value)
                    if isinstance(value, (dict, list))
                    else value
                )
        return new_dict
    elif isinstance(json_dict, list):
        return [remove_none_values(item) for item in json_dict]
    else:
        return json_dict


def snake_to_camel(json_dict):
    if isinstance(json_dict, dict):
        new_dict = {}
        for key, value in json_dict.items():
            words = key.split("_")
            new_key = words[0] + "".join(word.capitalize() for word in words[1:])
            new_dict[new_key] = (
                snake_to_camel(value) if isinstance(value, (dict, list)) else value
            )
        return new_dict
    elif isinstance(json_dict, list):
        return [snake_to_camel(item) for item in json_dict]
    else:
        return json_dict
