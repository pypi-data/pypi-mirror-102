from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.lookup import get_table_value, download_lookup
from hestia_earth.utils.tools import safe_parse_float

from hestia_earth.models.log import logger
from hestia_earth.models.utils.cycle import _is_term_type_incomplete
from hestia_earth.models.utils.product import _new_product
from hestia_earth.models.utils.property import _get_property_value

TERM_ID = 'belowGroundCropResidue'
PROPERTY_KEY = 'dryMatter'


def _get_value(term_name: str, primary_product_yield: int, dm_percent: float):
    lookup = download_lookup('crop.csv', True)

    logger.debug('lookup data for Term: %s', term_name)
    if term_name in list(lookup.termid):
        # Multiply yield by dryMatter proportion
        yield_dm = primary_product_yield * (dm_percent / 100)
        # TODO with the spreadsheet there are a number of ways this value is calculated.
        # Currently, the result of this model when applied to Sah et al does not match
        # the example due to hardcoded calc in the spreadsheet

        # estimate the BG DM calculation
        bg_slope = safe_parse_float(
            get_table_value(lookup, 'termid', term_name, 'crop_residue_slope')
        )
        bg_intercept = safe_parse_float(
            get_table_value(lookup, 'termid', term_name, 'crop_residue_intercept')
        )
        ab_bg_ratio = safe_parse_float(
            get_table_value(lookup, 'termid', term_name, 'ratio_abv_to_below_grou_crop_residue')
        )

        above_ground_residue = yield_dm * bg_slope + bg_intercept * 1000

        # TODO: Update to include fraction renewed addition of
        #  https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch11_Soils_N2O_CO2.pdf
        #  only if site.type = pasture
        # multiply by the ratio of above to below matter
        return None if bg_slope is None or bg_intercept is None or ab_bg_ratio is None \
            else (above_ground_residue + yield_dm) * ab_bg_ratio
    return None


def _product(value: float):
    logger.info('term=%s, value=%s', TERM_ID, value)
    product = _new_product(TERM_ID)
    product['value'] = [value]
    return product


def _run(primary_product: dict, dm_property: dict):
    term = primary_product.get('term', {})
    dm_percent = safe_parse_float(dm_property.get('value'))
    value = _get_value(term.get('@id', ''), primary_product.get('value', [0])[0], dm_percent)
    return _product(value) if value is not None else None


def _should_run(cycle: dict):
    product = find_primary_product(cycle)
    dm_property = _get_property_value(product, PROPERTY_KEY) if product is not None else None
    should_run = dm_property is not None and _is_term_type_incomplete(cycle, TERM_ID)
    logger.info('term=%s, should_run=%s', TERM_ID, should_run)
    return should_run, product, dm_property


def run(cycle: dict):
    should_run, primary_product, dm_property = _should_run(cycle)
    return _run(primary_product, dm_property) if should_run else []
