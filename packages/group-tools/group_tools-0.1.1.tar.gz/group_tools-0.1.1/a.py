import group_tools
from time import time


def generate_large_dict_with_str_keys():
    d = {}
    for i in range(100000):
        d[str(i)] = i

    for i in range(100000):
        d[f"o___{str(i)}"] = i

    return d


def auto_group_dict(dict_structure: dict, merge_with_dict: dict = None) -> dict:
    """
    It can group dict keys with same prefix under one dict key. Group keys are identified by group separator "___"
    Example: {
                "a": 1, "b": 2, "c___a": 3, "c___b___bb": 4, "c___b___cc": 5,
            }
            ===>
            {
                "a": 1, "b": 2, "c": {
                    "a": 3, "b": {
                        "bb": 4, "cc": 5
                    }
                }
            }
    :param dict_structure: Dict wit one level of depth. It ususaly goes from databese row select.
    :param merge_with_dict: Result will be added into this dict
    :return: Dict with posible N level structure
    """

    def set_value(_key_path, _value):
        _result = result
        key_path_len = len(_key_path)
        for index, _key in enumerate(_key_path):
            is_last = index == key_path_len - 1
            if _key not in _result:
                _result[_key] = {}
            if is_last:
                _result[_key] = _value
            _result = _result[_key]

    result = merge_with_dict if merge_with_dict else {}
    for key, value in dict_structure.items():
        key_path = key.split("___")
        if len(key_path) > 1:
            set_value(key_path, value)
        else:
            result[key] = value
    return result


d = generate_large_dict_with_str_keys()


t1 = time()
group_tools.group_dict2(d)
t2 = time()
print("rs", t2 - t1)

t1 = time()
auto_group_dict(d)
t2 = time()
print("py", t2 - t1)
