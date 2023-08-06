import json
from functools import lru_cache
from typing import List, Union

from flask import current_app
from invenio_search import current_search


@lru_cache(maxsize=20)
def get_mapping(index_name) -> Union[dict, None]:
    mapping_path = current_search.mappings.get(index_name)
    if not mapping_path:
        index_name = current_app.config.get("OAREPO_SEARCH_DEFAULT_INDEX")
        mapping_path = current_search.mappings.get(index_name)
    if not mapping_path:
        return None
    with open(mapping_path, "r") as f:
        return json.load(f)


def replace_language_placeholder(field: str, languages: List[str]) -> List[str]:
    if "*" not in field:
        return [field]
    res = []
    for lang in languages:
        res.append(field.replace('*', lang))
    return res
