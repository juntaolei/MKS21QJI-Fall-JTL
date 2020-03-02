# functions to query data
find_by_name = lambda database, name: list(
  database['license'].find({
    'name': name
  })
)
find_by_identifier = lambda database, identifier: list(
  database['license'].find({
    'identifiers': {
      '$elemMatch': {
        "identifier": identifier
      }
    }
  })
)
find_by_keyword = lambda database, keyword: list(
  database['license'].find({
    'keywords': {
      '$elemMatch': { keyword }
    }
  })
)
