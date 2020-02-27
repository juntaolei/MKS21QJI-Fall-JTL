from bson.json_util import loads

def ingest(f):
    fmt = ''
    with open(f) as _f:
        for line in _f:
            fmt += f'{line[:len(line) - 1]},'
        fmt = f'[{fmt[:len(fmt) - 1]}]'
        return loads(fmt)
