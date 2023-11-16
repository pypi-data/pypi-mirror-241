# i18n-json-spreadsheet

Lazy i18n json to spreadsheet and back tool. 

The aim of this utility is to help the management of JSON translations 
file used for example in JS frontends to handle locales.

Usually we can have key/value items nested in some way like the following:

```json
{
  "hello": "ciao",
  "how_are_you": "come stai",
  "component_a": {
    "my_name_is": "il mio nome é"
  }
}
```

To avoid editors to edit JSON files directly, ofted in git repos, the idea is 
to create/update online spreadsheet on Google Docs and maybe Microsoft Office 365.

## How to

This tool is intended to be used as CLI tool. Since the actual distribution of the 
tool is only as Docker image the following examples show usage using directly the 
cloned repo. We will update the examples as soon as we release in a different way.

To simplify the command syntax we can set main variable into the environment:

```bash
❯ export SA_JSON_FILE=./somepath/mysa.json
❯ export SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/000009999900000999/
```

### Get Help

```bash
❯ python main.py --help
Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --auth TEXT  Service Account JSON file path
  --help       Show this message and exit.

Commands:
  togdoc
```

### Json To Google Spreadsheet

```bash
❯ python main.py togdoc --help
Usage: cli togdoc [OPTIONS]

Options:
  -i, --infile TEXT    JSON input file
  -ol, --outlink TEXT  Destination link for Google Spreadsheet
  -oi, --outid TEXT    Destination ID for Google Spreadsheet
  -s, --sheet TEXT     Destination sheet in Google Spreadsheet
  --help               Show this message and exit.
```

**Use case: update**. We have a JSON file and we need to update an existing Google Spreadsheet file.

```bash
❯ python main.py --auth $SA_JSON_FILE togdoc \ -i /some/path/somefile-it.json -ol $SPREADSHEET_URL
```

