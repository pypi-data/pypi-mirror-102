import logging
import operator
from typing import Dict, Any, List, Tuple

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)

CONFIG_PREFIX = "ckanext.composite_search.prefix"
DEFAULT_PREFIX = "ext_composite_"


def get_prefix() -> str:
    return toolkit.config.get(CONFIG_PREFIX, DEFAULT_PREFIX)


class SearchParam:
    keys = ("value", "type", "junction")
    value: str
    type: str
    junction: str

    def __init__(self, *values):
        for k, v in zip(self.keys, values):
            setattr(self, k, v)


class ICompositeSearch(plugins.Interface):
    def before_composite_search(
        self, search_params: Dict[str, Any], params: List[SearchParam]
    ) -> Tuple[Dict[str, Any], List[SearchParam]]:

        return search_params, params


class CompositeSearchPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IPackageController, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_resource("../assets", "composite_search")

    # ITemplateHelpers
    def get_helpers(self):
        return {"composite_search_get_prefix": get_prefix}

    # IPackageController

    def before_search(self, search_params: Dict[str, Any]) -> Dict[str, Any]:
        prefix = get_prefix()

        try:
            extras = operator.itemgetter(*(prefix + k for k in SearchParam.keys))(search_params["extras"])
        except KeyError as e:
            log.debug('Missing key: %s', e)
            return search_params

        params = [
            SearchParam(*record)
            for record in zip(*[ex if isinstance(ex, list) else [ex] for ex in extras])
        ]
        for plugin in plugins.PluginImplementations(ICompositeSearch):
            search_params, params = plugin.before_composite_search(
                search_params, params
            )
        return search_params
