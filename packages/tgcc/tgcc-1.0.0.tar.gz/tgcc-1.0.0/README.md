![Logo](assets/favicon.png)<br>
# TGCC
[![PyPI Release Create](https://github.com/TechGeeks-Dev/tgcc/actions/workflows/Release-Create.yaml/badge.svg)](https://github.com/TechGeeks-Dev/tgcc/actions/workflows/Release-Create.yaml)<br>

## Installation

```shell
pip install tgcc
```

## Usage

First create a `tgcc.json` file with a **`compiler`** key:
```json
{
    "compiler": "compiler.json"
}
```
You can replace `compiler.json` with anything else and create that file with the value of:

```json
{
    "file": "file.md",
    "Content-Type": "text/markdown",
    "to": "html"
}
```

Then run:
```shell
tgcc start
```