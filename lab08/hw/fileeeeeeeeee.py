with open("string1.py", "r") as fin, open("string1_clean.py", "w") as fout:
    for l in fin:
        stripped = l.strip()
        if not stripped.startswith("#"):
            print(l)
            fout.write(l)


with open("string1_vol2.py", "r") as fin, open("string1_clean_vol2.py", "w") as fout:
    for l in fin:
        stripped = l.strip()
        if not stripped.startswith("#"):
            print(l)
            fout.write(l)
