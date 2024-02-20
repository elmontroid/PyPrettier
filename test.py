import prettier

if __name__ == "__main__":
    import json
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        prog="prettier", description="Pretty prints a json string/python-object"
    )

    parser.add_argument(
        "-j",
        "--json",
        default='{"string" : "hello world", "number" : 0.3, "boolean" : false, "dict" : {"test" : "hello wolrd"}, "list" : ["test", 3, false]}',
        type=str,
    )

    parser.add_argument("-f", "--file", default=None, required=False, type=str)

    arguments = parser.parse_args()

    if arguments.file is not None:
        file_path = Path(arguments.file)

        if not file_path.exists():
            raise FileNotFoundError("Test file not found")

        json_content = json.loads(file_path.read_text())
    else:
        json_content = json.loads(arguments.json)

    print(f"highlighted json\n{prettier.pretty(json_content)}")
