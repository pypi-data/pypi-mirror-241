import os
import gspread
from gspread.exceptions import WorksheetNotFound

from collections import defaultdict

def deep_dict():
    return defaultdict(deep_dict)

import json


class GspreadToJson:

    def __init__(self, sa_file: str, inlink: str, sheet: str, start_cell: str = 'A1') -> None:
        self.sa_file = sa_file
        self.inlink = inlink
        self.sheet = sheet
        self.start_cell = start_cell

        gc = gspread.service_account(filename=self.sa_file)
        spreadsheet = gc.open_by_url(inlink)

        try:
            sh = spreadsheet.worksheet(sheet)
        except WorksheetNotFound as e:
            raise Exception(f'Unable to find sheet {sheet}')
        
        self.sh = sh

    def read(self):
        result = deep_dict()

        def deep_insert(key, value):
            d = result
            keys = key.split(".")
            for subkey in keys[:-1]:
                d = d[subkey]
            d[keys[-1]] = value

        values = self.sh.get_all_values()

        dd = dict()

        for row in values:
            k = ''
            v = ''
            
            if len(row) < 1:
                k = row[0]
            if len(row) <= 2:
                k = row[0]
                v = row[1]

            deep_insert(k, v.encode('utf-8').decode())

        return result

    def to_file(self, outfile: str):
        
        json_object = json.dumps(self.read(), indent=2)
                
        with open(outfile, "w") as outfile:
            outfile.write(json_object)