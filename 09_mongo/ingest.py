from bson.json_util import loads

def ingest(f):
    with open(f) as _f:
        return loads(f'[{",".join(map(lambda s: s[:len(s) - 1], _f))}]')
