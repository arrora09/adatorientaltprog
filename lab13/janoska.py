import json
from pprint import pprint


def main():
    with open("person.json") as f:
        d = json.load(f)

        print(type(d))
        print(d)
        pprint(d, indent=4)

        print()
        print(d["age"])
        print()
        print(d["daughter"]["age"])


def read_string():
    s = """{
    "path":"/home/valami",
    "user_id":123456,
    "auto_sync":true
    }"""

    d = json.loads(s)
    print(d)

    # ha file-bol, akkor json.loads(f), ha nem kontextuskezelovel


if __name__ == "__main__":
    main()
    read_string()
