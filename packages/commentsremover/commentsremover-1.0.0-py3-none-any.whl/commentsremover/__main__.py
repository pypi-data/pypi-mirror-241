"""
commentsremover

Remove comments and docstrings from Python code.
"""

from re import sub, DOTALL
from os.path import isfile
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Remove comments and docstrings from Python files."
    )
    parser.add_argument(
        "files", metavar="file", type=str, nargs="+", help="File(s) to process."
    )
    parser.add_argument("--comments", action="store_true", help="Remove comments.")
    parser.add_argument("--docstrings", action="store_true", help="Remove docstrings.")

    args = parser.parse_args()

    if not args.comments and not args.docstrings:
        print("You must provide either the --comments or --docstrings flag.")
    else:
        modified_code = {}

        for file in args.files:
            if not isfile(file):
                print(f"File not found: {file}")
            else:
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        code = f.read()

                    if args.comments:
                        lines_list = []
                        lines = code.split("\n")
                        for line in lines:
                            line = sub(r"\s*#.*$", "", line)
                            lines_list.append(line)
                        code = "\n".join(lines_list)

                    if args.docstrings:
                        code = sub(r'(?<!\\)"""[^"]*"""', "", code, flags=DOTALL)
                        code = sub(r"(?<!\\)'''[^']*'''", "", code, flags=DOTALL)

                    modified_code[file] = code

                    with open(file, "w", encoding="utf-8") as f:
                        f.write(code)
                        print(f"File '{file}' has been cleaned.")
                except IOError as exc:
                    print(f"Error processing file '{file}': {exc}")
