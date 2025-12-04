import json


def write_file():
    person = {
        "last": "Doe",
        "first": "John",
        "age": 39,
        "sex": "M",
        "registered": True,
        "salary": 70000,
    }

    with open("janoska_out.json", "w") as f:
        json.dump(person, f, indent=4)
        # lehet sortolni is kulcsok szerint sort_keys=True


write_file()
