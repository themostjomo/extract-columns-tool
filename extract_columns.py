#!/usr/bin/env python3
"""
Extract each column of a spreadsheet into its own .txt file.
The column header becomes the filename (sanitized), and each row's
value in that column becomes one line in the file.

Usage:
    python extract_columns.py input.xlsx [output_dir] [--sheet SHEET_NAME]
"""
import sys
import re
import argparse
from pathlib import Path
import pandas as pd


def sanitize_filename(name: str) -> str:
    name = str(name).strip()
    name = re.sub(r'[\\/*?:"<>|]', "_", name)  # remove illegal filename chars
    name = re.sub(r'\s+', "_", name)
    return name or "unnamed_column"


def main():
    parser = argparse.ArgumentParser(description="Extract each spreadsheet column into a .txt file.")
    parser.add_argument("input", help="Path to the .xlsx file")
    parser.add_argument("output_dir", nargs="?", default="output", help="Directory to write .txt files (default: ./output)")
    parser.add_argument("--sheet", default=0, help="Sheet name or index to read (default: first sheet)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    sheet = args.sheet
    if isinstance(sheet, str) and sheet.isdigit():
        sheet = int(sheet)

    df = pd.read_excel(in_path, sheet_name=sheet, dtype=str)

    used_names = {}
    for col in df.columns:
        base_name = sanitize_filename(col)
        count = used_names.get(base_name, 0)
        used_names[base_name] = count + 1
        filename = base_name if count == 0 else f"{base_name}_{count}"

        values = df[col].fillna("").tolist()
        file_path = out_dir / f"{filename}.txt"
        file_path.write_text("\n".join(values), encoding="utf-8")
        print(f"Wrote {file_path} ({len(values)} rows)")

    print(f"\nDone. {len(df.columns)} column(s) written to '{out_dir}/'")


if __name__ == "__main__":
    main()
