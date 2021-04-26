
def recurisive_get_value(d, k):

    if not isinstance(d, dict):
        return None
    
    if isinstance(k, str):
        k = k.split('/')

    elem = d.get(k[0], None)

    if len(k) == 1:
        return elem

    return recurisive_get_value(elem, k[1:])