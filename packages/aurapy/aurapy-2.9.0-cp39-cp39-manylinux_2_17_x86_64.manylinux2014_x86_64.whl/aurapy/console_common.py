import time


class InvalidCommand(Exception):
    pass


class SelectClientException(Exception):

    def __init__(self, port_hint=None, device_hint=None):
        super().__init__()
        self.port_hint = port_hint
        self.device_hint = device_hint


def validate_num_args(command, expected_num_args, *args):
    if len(args) != expected_num_args:
        raise InvalidCommand(f"{command} expects {expected_num_args} arg(s) but got {len(args)}: {' '.join(args)}")


def print_answer(*args):
    print('\t\t', ' '.join([str(arg) for arg in args]).replace('\n', '\n\t\t'))


def parse_float_value(val_str, val_type):
    """
    construct a float-like value from a string.
    :param val_str: a string representing a float.
    :param val_type: type of the float-like value (e.g. units types like ampere, volt, celsius)
    :return: a val_type instance
    """
    return val_type(float(val_str))


def range_gen(start, end, increment):
    """
    a range generator that works with floats too:
    returns values from start to end (exclusive) every increment.

    :param start: start value
    :param end: end value (exclusive)
    :param increment: step between
    :return: a value in [start, end[ of the same type as start.
    """
    val = start
    if start < end:
        while start < end:
            yield val
            val += abs(increment)
    elif start > end:
        while start > end:
            yield val
            val -= abs(increment)
    else:
        # start == end
        yield val


is_verbose = False


def parse_apply(func, val_str, val_type):
    """
    Parses an input to a function and calls the function on that input.
    Note that val_str can specify a range of values in which case
    func will be called repeatedly on those values.

    :param func: function to call
    :param val_str: function input in string format.
    :param val_type: type of the input expected by func
    :return:
    """
    if ':' in val_str:
        vals = val_str.split(':')
        start_str, end_str, increment_str, wait_time_str = vals
        start = parse_float_value(start_str, val_type)
        end = parse_float_value(end_str, val_type)

        increment_tokens = increment_str.split(',')

        increment = parse_float_value(increment_tokens[-1], val_type)
        if len(increment_tokens) > 1:
            pass

        wait_time = float(wait_time_str)

        for val in range_gen(start, end, increment):
            if is_verbose:
                print(func.__name__, val, f'wait {wait_time:.3f}s')

            func(val)
            time.sleep(wait_time)

    else:
        if is_verbose:
            print(func.__name__, val_str)

        func(parse_float_value(val_str, val_type))
