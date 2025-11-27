import sys


def cat(fname):
    try:
        with open(fname) as f:
            for line in f:
                line = line.rstrip("\n")
                print(f"--- {fname}")
                print(line)
    except FileNotFoundError as e:
        print(f"Error: file '{fname}' not found ")


#####

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        cat(arg)
