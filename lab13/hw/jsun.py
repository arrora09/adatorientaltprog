import re


with open("jsun.csv", encoding="utf-8") as f:
    li = []
    m = re.search(r".*j.*s.*u.*n.*", f.read())
    print(m.group())
