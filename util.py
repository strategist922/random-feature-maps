

def argparse(argv):

    args = []
    kwargs = {}

    for arg in argv:
        if '=' in arg:
            kwargs[arg.split('=')[0]] = arg.split('=')[1]
        else:
            args += '='

    return args, kwargs
