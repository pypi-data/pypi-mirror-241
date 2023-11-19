import gspread
from gspread import WorksheetNotFound


def create_spreadsheet(sa_file: str, name: str, owner: str):
    gc = gspread.service_account(filename=sa_file)
    sh = gc.create(name)
    sh.share(owner, perm_type='user', role='writer')

    return sh


def compare_json_gdoc(sa_file: str, json_file: str, link_file: str, column: int, sheet: str = 'Sheet1'):
    class Diff():
        pass

    from i18nconverter.converters.json_to_kv import JsonToKv

    diff = Diff()
    gc = gspread.service_account(filename=sa_file)
    spreadsheet = gc.open_by_url(link_file)

    try:
        sh = spreadsheet.worksheet(sheet)
    except WorksheetNotFound as e:
        raise Exception(f'Unable to find sheet {sheet}')

    gdoc_keys = sh.col_values(int(column))

    jkv = JsonToKv(from_file=json_file)
    json_keys = jkv.get_keys()

    diff.differences = len(set(gdoc_keys) - set(json_keys)) + len(set(json_keys) - set(gdoc_keys))
    diff.in_gdoc_not_json = ','.join(set(gdoc_keys).difference(set(json_keys)))
    diff.in_json_not_gdoc = ','.join(set(json_keys).difference(set(gdoc_keys)))

    diff.has_difference = diff.differences > 0

    return diff
