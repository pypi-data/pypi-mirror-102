import logging

from submission_broker.validation.base import BaseValidator
from .load import ExcelLoader


class ValidatingExcel(ExcelLoader):
    def __init__(self, excel_path: str, service_map: dict, service_names: list, sheet_index=0):
        super().__init__(excel_path, service_map, service_names, sheet_index)

    def validate(self, validator: BaseValidator):
        validator.validate_data(self.data)
        logging.debug(f'{validator.__class__} Validation Complete.')
