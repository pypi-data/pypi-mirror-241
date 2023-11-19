import gspread
from gspread.exceptions import WorksheetNotFound
import os

from ..converters.json_to_kv import JsonToKv


class KvToGspread:

    def __init__(self, sa_file: str) -> None:
        self.sa_file = sa_file

    def update_spreadsheet(self, kv: list, file_url: str, start_cell: str = 'A1', 
                           sheet: str = 'Sheet1', create_sheet: bool = False, overwrite: bool = False):
        gc = gspread.service_account(filename=self.sa_file)
        spreadsheet = gc.open_by_url(file_url)

        try:
            sh = spreadsheet.worksheet(sheet)
        except WorksheetNotFound as e:
            if create_sheet:
                sh = spreadsheet.add_worksheet(sheet, rows=len(kv), cols=2)
            else:
                raise Exception(f'Unable to use Worksheet {sheet}')

        if overwrite:
            sh.clear()

        sh.update(start_cell, kv)