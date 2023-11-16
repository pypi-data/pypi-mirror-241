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


if __name__ == '__main__':
    sa_file = os.getenv('SA_FILE')
    spreadsheet_url = os.getenv('SPREADSHEET_URL')
    
    in_file = 'res/sample.json'
    jkv = JsonToKv(from_file=in_file)        
    sample_data = jkv.as_kvlist()

    gc = gspread.service_account(filename=sa_file)

    spreadsheet = gc.open_by_url(spreadsheet_url)
    sh = spreadsheet.worksheet("sheet1")

    sh.update('A1', sample_data)