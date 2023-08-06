from typing import Dict, Any, List, Tuple

import ckan.plugins as plugins

from ckan.lib.search.query import solr_literal

from .base import ICompositeSearch, SearchParam


class DefaultSearchPlugin(plugins.SingletonPlugin):
    plugins.implements(ICompositeSearch)

    # ICompositeSearch

    def before_composite_search(
        self, search_params: Dict[str, Any], params: List[SearchParam]
    ) -> Tuple[Dict[str, Any], List[SearchParam]]:
        query = ''
        for param in reversed(params):
            value = ' '.join([solr_literal(word) for word in param.value.split()])
            fragment = f"{param.type}:({value})"
            if param.junction == 'NOT':
                fragment = 'NOT ' + fragment + ' AND '
            elif query:
                fragment += ' ' + param.junction + ' '
                query = f'{fragment} ({query})'
            else:
                query = fragment
        q = search_params.get('q', '')
        q += ' ' + query
        search_params['q'] = q
        return search_params, params
