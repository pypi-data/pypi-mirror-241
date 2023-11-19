import sys

import click
import os
import json

from i18nconverter.utils_google import compare_json_gdoc

CONFIG_FILE_NAME = '.i18nconverter.json'


@click.group()
@click.option('--auth', 'auth', default=None, help='Service Account JSON file path')
@click.option('--silent', 'silent', is_flag=True, show_default=True, default=False,
              help='Silent mode: questions to user will be skipped (ignored for setup)')
@click.pass_context
def cli(ctx, auth, silent):
    config = {}
    if os.path.exists(CONFIG_FILE_NAME):
        f = open(CONFIG_FILE_NAME, 'r')
        config = json.loads(f.read())

    ctx.obj = {'auth': auth or config.get('sa_file'), 'silent': silent}
    if config:
        ctx.obj.update(config)


@cli.command()
def init():
    click.echo('📝 Creating local configuration...')
    if os.path.exists(CONFIG_FILE_NAME):
        click.echo(f' ↳ ⚠️ local configuration file present in {CONFIG_FILE_NAME}')
        exit(1)

    config = dict()
    config['sa_file'] = click.prompt('↳ GCP Service Account JSON file location? ',
                                     type=click.Path(exists=True, readable=True, writable=False, dir_okay=False))

    config['wsh_url'] = click.prompt('↳ Google Spreadsheet link? ', type=str)
    config['locales_1st'] = click.prompt('↳ How do you manage locale codes? \n ' \
                                         '  ↳ [1] in different files \n ' \
                                         '  ↳ [2] on the first level of JSON \n', default=1, type=int)

    json_object = json.dumps(config, indent=2)

    with open(CONFIG_FILE_NAME, "w") as outfile:
        outfile.write(json_object)

    click.echo(f'\n \n🎉  Configuration file created {CONFIG_FILE_NAME}')


@cli.command()
@click.pass_context
@click.option('--name', 'name', required=True, help='The name for the new spreadsheet')
@click.option('--owner', 'owner', required=True, help='Your e-mail address in order to access the file')
@click.option('--save/--no-save', 'save', default=False, is_flag=True, show_default=True,
              help='Update local configuration, if present, with the new file url')
def create(ctx, name: str, owner: str, save: bool):
    """
    Creating new files require you to enable Google Drive API for Service Account.
    You may encounter an error during create but with the link to enable directly
    the Google Drive API.
    """
    click.echo(f'📝 Creating new spreadsheet "{name}"...')
    from i18nconverter.utils_google import create_spreadsheet

    sh = create_spreadsheet(ctx.obj.get('auth'), name, owner)
    click.echo(sh.url)

    if os.path.exists(CONFIG_FILE_NAME) and save is True:
        f = open(CONFIG_FILE_NAME, 'r')
        config = json.loads(f.read())
        config['wsh_url'] = sh.url
        json_object = json.dumps(config, indent=2)

        with open(CONFIG_FILE_NAME, "w") as outfile:
            outfile.write(json_object)

        click.echo('✅ Config file updated.')


@cli.command()
@click.pass_context
@click.option('-i', '--infile', 'infile', help='JSON input file')
@click.option('-ol', '--outlink', 'outlink', default=None, help='Destination link for Google Spreadsheet')
@click.option('-s', '--sheet', 'sheet', default='Sheet1', help='Destination sheet in Google Spreadsheet')
@click.option('-o', '--overwrite', 'overwrite', is_flag=True, show_default=True, default=False,
              help='Clear worksheet before writing values')
@click.option('--create-sheet/--no-create-sheet', 'create_sheet', default=False,
              help='Create new sheet with given name if it not exists')
def togdoc(ctx, infile, outlink, overwrite, sheet, create_sheet):
    from .converters.json_to_kv import JsonToKv
    from .converters.kv_to_gspreadsheet import KvToGspread

    if not outlink and ctx.obj['wsh_url']:
        outlink = ctx.obj['wsh_url']

    if overwrite and not ctx.obj.get('silent'):
        if not click.confirm(
                f'Are you sure to overwrite contents in sheet {sheet} of Google Spreadsheet at {outlink}? '):
            click.echo('Aborted.')
            exit(0)

    jkv = JsonToKv(from_file=infile)
    kvgs = KvToGspread(sa_file=ctx.obj.get('auth'))

    kvgs.update_spreadsheet(jkv.as_kvlist(), outlink, sheet=sheet, create_sheet=create_sheet, overwrite=overwrite)

    click.echo(f'✅ Update completed. \n💻 Check at {outlink}')


@cli.command()
@click.pass_context
@click.option('-o', '--outfile', 'outfile', help='JSON output file')
@click.option('-il', '--inlink', 'inlink', default=None, help='Source link for Google Spreadsheet')
@click.option('--start-cell', 'startcell', default='A1', help='Start reading from this cell coordinates')
@click.option('-s', '--sheet', 'sheet', default='Sheet1', help='Source sheet in Google Spreadsheet')
def tojson(ctx, inlink, outfile, sheet, startcell):
    from .converters.gspreadsheet_to_json import GspreadToJson

    if not inlink and ctx.obj['wsh_url']:
        inlink = ctx.obj['wsh_url']

    try:
        gs = GspreadToJson(ctx.obj.get('auth'), inlink, sheet, start_cell=startcell)
        gs.to_file(outfile)
    except Exception as e:
        click.echo(f'⚠️  Error creating Json file: {e}', err=True, color=True)


@cli.command()
@click.pass_context
@click.option('-f', '--file', 'json_file', required=True, help='JSON file for comparison')
@click.option('-l', '--link', 'link_file', help='Link to Google Spreadsheet')
@click.option('-s', '--sheet', 'sheet', default='Sheet1', help='Source sheet in Google Spreadsheet')
@click.option('-c', '--column', 'column', default=1, type=int, help='Colum to read in Google Spreadsheet')
def compare(ctx, json_file: str, link_file: str, column: int, sheet: str):
    if not link_file and ctx.obj['wsh_url']:
        link_file = ctx.obj['wsh_url']

    try:
        diff = compare_json_gdoc(ctx.obj.get('auth'), json_file, link_file, column, sheet)
    except Exception as e:
        click.echo(f'⚠️ Error during comparison: {e}', err=True, color=True)
        exit(1)

    click.echo(f'Keys present in Google Spreadsheet and not present in JSON: \n{diff.in_gdoc_not_json}')
    click.echo(f'Keys present in JSON and not present in Google Spreadsheet: \n{diff.in_json_not_gdoc}')


def main():
    cli(prog_name="cli")


if __name__ == '__main__':
    main()
