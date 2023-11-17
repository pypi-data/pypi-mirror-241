from functools import wraps
from ._aura_pybind import version_matches_filter


def prompt_user_yes_no(msg, default_yes=True):
    if default_yes:
        msg += ' [y]/n '
    else:
        msg += ' y/[n] '
    user_input = input(msg)
    if not user_input:
        return default_yes
    else:
        return user_input == 'y'


def requires_aura_version(aura_version_filter):
    """
    a decorator for AuraClient methods that require a certain AuraClient version
    :param aura_version_filter: required aura version for that feature to work
    :param prompt_update: whether to prompt user for updating
        if aura actuator version is less than required
    :return:
    """

    def f(func):
        @wraps(func)
        def wrapped(aura_client, *args, **kwargs):
            if not aura_client.is_connected():
                raise Exception("Not connected - please connect to Aura first")
            aura_version = aura_client.get_connected_version()
            client_version = aura_version.split('-')[1]
            if version_matches_filter(client_version, aura_version_filter):
                return func(aura_client, *args, **kwargs)
            else:
                raise Exception(f'this features requires aura version {aura_version_filter}.')

        extra_doc = f'*** requires aura version {aura_version_filter} ***'
        if wrapped.__doc__ is None:
            wrapped.__doc__ = extra_doc
        else:
            wrapped.__doc__ += '\n' + extra_doc

        return wrapped

    return f
