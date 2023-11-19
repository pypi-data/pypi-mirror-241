"""
NATURALSIZE
"""
def nsize(value: int, comma: int = 0):
    """
    returns human-readable size of a file
    args:
    value -- integer size of file in bytes
    comma -- integer value of ndigits
    """
    values = [0, 1024]
    for i in range(6):
        values.append(values[-1]**2)
    names = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]
    idx = 0
    while value > values[idx]:
        idx += 1
    return str(round(value/values[idx], ndigits=comma))+names[idx]
