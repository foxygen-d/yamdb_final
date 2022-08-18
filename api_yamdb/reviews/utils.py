import csv
import os
from typing import AnyStr, Dict, List

from django.conf import settings


def get_csv_data(source) -> List[Dict]:
    """Load test data from csv as python dict."""
    base_dir = settings.BASE_DIR
    with open(
        os.path.join(base_dir, f'static/data/{source}.csv'), 'r'
    ) as file:
        csv_dict = csv.DictReader(file)
    return [
            {attr: row.get(attr) for attr in row} for row in csv_dict
        ]


def set_by_id(payload: Dict, field: AnyStr) -> None:
    """Rename incoming dict key to the foreign key name."""
    payload[f'{field}_id'] = payload.pop(field)
