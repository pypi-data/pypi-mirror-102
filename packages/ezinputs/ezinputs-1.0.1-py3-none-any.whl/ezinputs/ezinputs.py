def core_input(prompt: str, error: str, astype: callable):
    """core input wrapper. USE FLOAT/INT/STR/BOOL/DICT/LIST/SET/TUPLE WRAPPER INSTEAD

    Args:
        prompt (str): the prompt to enter an input
        error (str): the error message displayed
        astype (callable): the primitive type to be entered (int, float, bool, str).

    Returns:
        primitive: typecast input from the user (dependent on astype)
    """
    if astype == int:
        def astype(x): return int(float(x))
    while True:
        entered = input(prompt)
        try:
            return astype(entered)
        except ValueError:
            print(error)


def float_input(prompt: str = "Enter a float: ", error: str = "Invalid float, try again") -> float:
    """gets a floating point input from the user

    Args:
        prompt (str, optional): the prompt to enter an input. Defaults to "Enter a float: ".
        error (str, optional): the error message displayed. Defaults to "Invalid float, try again".

    Returns:
        float: the user input as a float
    """
    return core_input(prompt=prompt, error=error, astype=float)


def int_input(prompt: str = "Enter an integer: ", error: str = "Invalid integer, try again") -> int:
    """gets an integer input from the user

    Args:
        prompt (str, optional): the prompt to enter an input. Defaults to "Enter an integer: ".
        error (str, optional): the error message displayed. Defaults to "Invalid integer, try again".

    Returns:
        int: the user input as an int
    """
    return core_input(prompt=prompt, error=error, astype=int)


def bool_input(prompt: str = "Enter boolean: ", error: str = "invalid boolean, try again") -> bool:
    """gets a boolean input from the user

    Args:
        prompt (str, optional): the prompt to enter an input. Defaults to "Enter boolean: ".
        error (str, optional): the error message displayed. Defaults to "invalid boolean, try again".

    Returns:
        bool: the user input as a bool
    """
    return bool(core_input(prompt=prompt, error=error, astype=bool))


def str_input(prompt: str = "Enter a string: ", error: str = "Invalid string, try again") -> str:
    """this is very rendundant, why are you not just using input() ?

    Args:
        prompt (str, optional): the prompt to enter an input. Defaults to "Enter a string: ".
        error (str, optional): the error message displayed. Defaults to "Invalid string, try again".

    Returns:
        str: the user input as a str
    """
    return core_input(prompt=prompt, error=error, astype=str)


def dict_input(prompt: str = "Enter {1} {0}: ", error: str = "invalid {0}", astype: callable = str, count: int = 1) -> dict:
    """gets user inputs and constructs a dictionary from them

    Args:
        prompt (str, optional): the prompt to enter an input; formattable place {0} will count key/value pairs when entering keys or show the current key when entering values, formattable place {1} will say "key" when entering a key or "<type> value for" when entering a value. Defaults to "Enter {1} {0}: ".
        error (str, optional): the error message displayed. Defaults to "invalid {0}".
        astype (callable, optional): theprimitive type to be entered for the value (int, float, bool, str). Defaults to str.
        count (int, optional): the number of items to be entered. Defaults to 1.

    Returns:
        dict: a dict containing key/value pairings of user inputs
    """
    this = {}
    for x in range(count):
        thiskey = core_input(
            prompt=prompt.format(x + 1, "key"), error=error.format(str(astype).split("'")[1]), astype=str
        )
        thisval = core_input(
            prompt=prompt.format(thiskey, f"""{str(astype).split("'")[1]} value for"""), error=error.format(str(astype).split("'")[1]), astype=astype
        )
        this[thiskey] = thisval
    return this


def collection_input(prompt: str, error: str, astype: callable, count: int) -> list:
    """base collection input wrapper. USE LIST/SET/TUPLE WRAPPER INSTEAD

    Args:
        prompt (str): the prompt to enter an input; add a formattable place to automatically count the inputs.
        error (str): the error message displayed; add a formattable place to automatically display the type required.
        astype (callable): the primitive type to be entered (int, float, bool, str).
        count (int): the number of items to be entered.

    Returns:
        list: a list containing the user inputs
    """
    return [core_input(prompt=prompt.format(x+1), error=error.format(str(astype).split("'")[1]), astype=astype) for x in range(count)]


def list_input(prompt: str = "Enter item {0}: ", error: str = "invalid {0}", astype: callable = str, count: int = 1) -> list:
    """gets user inputs and constructs a list from them

    Args:
        prompt (str, optional): the prompt to enter an input; add a formattable place to automatically count the inputs. Defaults to "Enter item {0}: ".
        error (str, optional): the error message displayed; add a formattable place to automatically display the type required. Defaults to "invalid {0}".
        astype (callable, optional): the primitive type to be entered (int, float, bool, str). Defaults to str.
        count (int, optional): the number of items to be entered. Defaults to 1.

    Returns:
        list: a list containing the user inputs
    """
    return collection_input(prompt=prompt, error=error, astype=astype, count=count)


def tuple_input(prompt: str = "Enter item {0}: ", error: str = "invalid {0}", astype: callable = str, count: int = 1) -> tuple:
    """gets user inputs and constructs a tuple from them

    Args:
        prompt (str, optional): the prompt to enter an input; add a formattable place to automatically count the inputs. Defaults to "Enter item {0}: ".
        error (str, optional): the error message displayed; add a formattable place to automatically display the type required. Defaults to "invalid {0}".
        astype (callable, optional): the primitive type to be entered (int, float, bool, str). Defaults to str.
        count (int, optional): the number of items to be entered. Defaults to 1.

    Returns:
        tuple: a tuple containing the user inputs
    """
    return tuple(collection_input(prompt=prompt, error=error, astype=astype, count=count))


def set_input(prompt: str = "Enter item {0}: ", error: str = "invalid {0}", astype: callable = str, count: int = 1) -> set:
    """gets user inputs and constructs a set from them

    Args:
        prompt (str, optional): the prompt to enter an input; add a formattable place to automatically count the inputs. Defaults to "Enter item {0}: ".
        error (str, optional): the error message displayed; add a formattable place to automatically display the type required. Defaults to "invalid {0}".
        astype (callable, optional): the primitive type to be entered (int, float, bool, str). Defaults to str.
        count (int, optional): the number of items to be entered. Defaults to 1.

    Returns:
        set: a set containing the user inputs
    """
    return set(collection_input(prompt=prompt, error=error, astype=astype, count=count))


def demo():
    print("Integer input int_input()")
    int_in = int_input()
    print(int_in, end="\n\n")

    print("Float input float_input()")
    float_in = float_input()
    print(float_in, end="\n\n")

    print("Boolean input bool_input()")
    bool_in = bool_input()
    print(bool_in, end="\n\n")

    print("String input str_input() - very redundant")
    str_in = str_input()
    print(str_in, end="\n\n")

    print("List input list_input(count=2, astype=int)")
    list_in = list_input(count=2, astype=int)
    print(list_in, end="\n\n")

    print("Set input set_input(count=3, astype=float)")
    set_in = set_input(count=3, astype=float)
    print(set_in, end="\n\n")

    print("Tuple input tuple_input(count=3, astype=bool)")
    tuple_in = tuple_input(count=3, astype=bool)
    print(tuple_in, end="\n\n")

    print("Dictionary input dict_input(count=3)")
    dict_in = dict_input(count=3)
    print(dict_in, end="\n\n")


if __name__ == "__main__":
    print("Hey! You just rand this file directly. Did you really mean to?")
    print("Doing so has called the test/demo function.\n")
    demo()
