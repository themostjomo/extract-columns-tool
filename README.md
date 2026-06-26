```
                                          
      _|    _|_|    _|      _|    _|_|    
      _|  _|    _|  _|_|  _|_|  _|    _|  
      _|  _|    _|  _|  _|  _|  _|    _|  
_|    _|  _|    _|  _|      _|  _|    _|  
  _|_|      _|_|    _|      _|    _|_|    
                                          
```

<h1 align="center">extract-columns</h1>

<p align="center">
  A simple Python script that splits each column of a spreadsheet into its own .txt file.
</p>

<p align="center">
  Made by <a href="https://github.com/themostjomo">@themostjomo</a>
</p>

---

## What it does

Give it a `.xlsx` file, and it will create one `.txt` file per column — using the column header as the filename, and each row's value as a line in that file.

**Example:**

A spreadsheet with these columns:

| Name  | Score Total | Notes/Comments |
|-------|-------------|-----------------|
| Alice | 90          | Good            |
| Bob   | 85          | OK              |
| Carol | 77          | Great           |

produces:

```
output/
├── Name.txt
├── Score_Total.txt
└── Notes_Comments.txt
```

## Requirements

- Python 3
- pandas
- openpyxl

## Installation

```bash
pip install pandas openpyxl
```

> **Note:** On macOS with Homebrew-managed Python, you may need to use a virtual environment:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install pandas openpyxl
> ```

## Usage

```bash
python extract_columns.py input.xlsx [output_dir] [--sheet SHEET_NAME]
```

### Arguments

| Argument     | Required | Description                                                  |
|--------------|----------|----------------------------------------------------------------|
| `input.xlsx` | Yes      | Path to the spreadsheet file                                  |
| `output_dir` | No       | Folder to save `.txt` files into (default: `output`)         |
| `--sheet`    | No       | Sheet name or index to read (default: first sheet)            |

### Examples

```bash
# Basic usage
python extract_columns.py mysheet.xlsx

# Custom output folder
python extract_columns.py mysheet.xlsx results

# Specify a sheet
python extract_columns.py mysheet.xlsx --sheet "Sheet2"
```

## Notes

- Column names with characters invalid in filenames (like `/` or `:`) are automatically sanitized.
- Duplicate column names are handled by appending `_1`, `_2`, etc.
- Empty cells are written as blank lines.

## License

MIT

---

<p align="center">Built with 🐍 by <strong>JOMO</strong></p>
