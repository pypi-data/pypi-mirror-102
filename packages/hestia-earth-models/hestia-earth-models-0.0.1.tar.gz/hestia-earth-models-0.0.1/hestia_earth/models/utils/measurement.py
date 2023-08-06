from hestia_earth.schema import SchemaType
from hestia_earth.utils.api import download_hestia, find_node_exact

from hestia_earth.models.utils import _average, _linked_node, _term_id


def _new_measurement(term, biblio_title=None):
    measurement = {'@type': SchemaType.MEASUREMENT.value}
    measurement['term'] = _linked_node(term if isinstance(term, dict) else download_hestia(_term_id(term)))
    if biblio_title:
        source = find_node_exact(SchemaType.SOURCE, {'bibliography.title': biblio_title})
        if source:
            measurement['source'] = _linked_node({'@type': SchemaType.SOURCE.value, **source})
    return measurement


def measurement_value_average(measurement: dict): return _average(measurement.get('value', [0]))
