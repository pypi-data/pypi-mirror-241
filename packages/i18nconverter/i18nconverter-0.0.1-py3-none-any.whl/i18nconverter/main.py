import click

@click.group()
@click.option('--auth', 'auth', default=None, help='Service Account JSON file path')
@click.pass_context
def cli(ctx, auth):
    ctx.obj = {}
    ctx.obj['auth'] = auth

@cli.command()
@click.option('-i', '--infile', 'infile', help='JSON input file')
def tokv(infile):
    from converters.json_to_kv import JsonToKv

    jkv = JsonToKv(from_file=infile)
    print(jkv.as_kvlist())

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

    if overwrite:
        if not click.confirm(f'Are you sure to overwrite contents in sheet {sheet} of Google Spreadsheet at {outlink}? '):
            click.echo('Aborted.')
            exit(0)
    
    jkv = JsonToKv(from_file=infile)
    kvgs = KvToGspread(sa_file=ctx.obj.get('auth'))

    kvgs.update_spreadsheet(jkv.as_kvlist(), outlink, sheet=sheet, create_sheet=create_sheet, overwrite=overwrite)


@cli.command()
@click.pass_context
@click.option('-o', '--outfile', 'outfile', help='JSON output file')
@click.option('-il', '--inlink', 'inlink', default=None, help='Source link for Google Spreadsheet')
@click.option('--start-cell', 'startcell', default='A1', help='Start reading from this cell coordinates')
@click.option('-s', '--sheet', 'sheet', default='Sheet1', help='Source sheet in Google Spreadsheet')
def tojson(ctx, inlink, outfile, sheet, startcell):
    from .converters.gspreadsheet_to_json import GspreadToJson
    
    gs = GspreadToJson(ctx.obj.get('auth'), inlink, sheet, start_cell=startcell)
    gs.to_file(outfile)

def main():
   cli(prog_name="cli")
 
if __name__ == '__main__':
   main()