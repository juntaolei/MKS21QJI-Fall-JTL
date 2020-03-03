# functions to query data
find_by_name = lambda database, name: list(
  database['license'].find({'name': name})
)
find_by_identifier = lambda database, identifier: list(
  database['license'].find({
    'identifiers': { '$elemMatch': { "identifier": identifier } }
  })
)
find_by_keywords = lambda database, keywords: list(
  chain.from_iterable(filter(None, list(map(
          lambda keyword: list(
            database['license'].find({
              'keywords': { '$elemMatch': { '$eq': keyword } }
            })
          ), keywords
        )))))
find_by_filter = lambda database, _filter: list(
  database['license'].find({
    'keywords:': { '$nin': [_filter] }
  })
)