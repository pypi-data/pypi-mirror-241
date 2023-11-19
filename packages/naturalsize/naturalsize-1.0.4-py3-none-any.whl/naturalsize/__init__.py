"""
NATURALSIZE
"""
def nsize(value: int, comma: int = 0):
    """
    returns human-readable size of a file
    args:
    value -- integer size of file in bytes
    comma -- integer value of maximum ndigits
    """
    values = [1, 1024]
    for i in range(6):
        values.append(values[-1]*1024)
    names = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]
    idx = 0
    while value > values[idx+1]:
        idx += 1
    return str(round(value/values[idx], ndigits=comma if comma != 0 else None))+names[idx]
def about():
    """
    Returns information about yout release
    """
    return {"Version":(1, 0, 4)}
