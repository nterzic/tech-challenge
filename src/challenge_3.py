
def recurisive_get_value(d, k):

    if not isinstance(d, dict):
        return None
    
    if isinstance(k, str):
        k = k.split('/')

    elem = d.get(k[0], None)

    if len(k) == 1:
        return elem

    return recurisive_get_value(elem, k[1:])


if __name__ == '__main__':
    input_1_obj = {"a":{"b":{"c":"d"}}}
    input_1_key = 'a'
    print(recurisive_get_value(input_1_obj, 'a'))