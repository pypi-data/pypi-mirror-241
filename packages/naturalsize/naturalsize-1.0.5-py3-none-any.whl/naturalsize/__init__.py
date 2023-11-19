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
    Returns information about your release
    """
    return {"Version":(1, 0, 5)}
def randprinter(numb: int = 1000, signs: list = list("abcdefghijklmnopqrstuvwxyzäöüß01234567890#'+*-_.:,;!§$%&/()=?`<>^°"), utf8: bool = False):
    """
    Prints numb random signs
    args:
    numb -- integer numb of signs
    signs -- list of possible signs
    utf8 -- utf8RandomMode
    """
    import random
    for i in range(numb):
        print(random.choice(signs), end="")
def special_starter(numb: int = 200000000):
    """
    Func for special startup:
    Function passes numb times. When the user presses ctrl+c,
    the special startup is unlocked
    """
    try:
        for i in range(numb):
            pass
        return False
    except KeyboardInterrupt:
        return True
