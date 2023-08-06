
[![image][0]][1]
[![image][2]][3]
[![image][4]][5]
[![image][6]][7]

  [0]: https://github.com/oarepo/oarepo-search/workflows/CI/badge.svg
  [1]: https://github.com/oarepo/oarepo-search/actions?query=workflow%3ACI
  [2]: https://img.shields.io/github/tag/oarepo/oarepo-search.svg
  [3]: https://github.com/oarepo/oarepo-search/releases
  [4]: https://img.shields.io/pypi/dm/oarepo-search.svg
  [5]: https://pypi.python.org/pypi/oarepo-search
  [6]: https://img.shields.io/github/license/oarepo/oarepo-search.svg
  [7]: https://github.com/oarepo/oarepo-search/blob/master/LICENSE

# OARepo-Search

OArepo module that added auxiliary search features.

## Installation

OARepo-Search is on PyPI so all you need is:

``` console
$ pip install oarepo-search
```

## Configuration
### Supported languages
If you use multilingual fields ([oarepo-multilingual](https://github.com/oarepo/oarepo-multilingual)) and want use 
simple query for searching in the fields, you have to specify supported languages.

```python
OAREPO_SEARCH_SUPPORTED_LANGUAGES = ["cs", "en"]
```

### Search fields
Field settings for simple search (https://host.com/path/?q=<query>). Configuration is a dictionary, where key is the 
name of the 
endpoint and value is a list of supported fields. If you want to use a multilingual field, you can use an asterisk instead of the language, which is automatically replaced by OAREPO_SEARCH_SUPPORTED_FIELDS.

:warning: **Simple query does not support nested fields**: If you want search in nested fields you must use Lucene 
query with field specification (e.g.: "creator.role.title.cs:Karel Čapek")

```python
OAREPO_SEARCH_FIELDS = {
  "entrypoint_name": ["title.*", "creator"]
}
```

## Usage
### Query parser
The library provides an extension to the default parser provided by Invenio. The use of the query parser is 
described in the module [invenio-records-rest](https://invenio-records-rest.readthedocs.io/en/latest/usage.
html#query-parser).

The library can use a simple query as in invenio when you enter a search query in the form: q = <word>, but this simple expression cannot search in nested fields. Therefore, the library supports queries in Lucene syntax with support for nested field search (eg "title: robot AND creator.name:Capek")

Provide query parser from this library into your search_factory.

```python
from invenio_records_rest.query import default_search_factory
from oarepo_search.query_parsers import query_parser



def my_search_factory(*args, **kwargs):
    return default_search_factory(*args,
                                  query_parser=query_parser, **kwargs)

RECORDS_REST_ENDPOINTS = {
    'recid': {
        # ...
        'search_factory_imp': my_search_factory,
     }
}
```

Copyright (C) 2021 CESNET.

OARepo-Search is free software; you can redistribute it and/or
modify it under the terms of the MIT License; see LICENSE file for more
details.
