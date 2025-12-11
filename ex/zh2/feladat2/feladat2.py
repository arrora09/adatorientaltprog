#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv)!=2:
        print("Error: provide exactly one argument")
        return

    fileName= sys.argv[1]

    try:
        urlList = []
        with open(fileName,"r",encoding="utf-8") as inF:
            print(f"-- reading {fileName}")
            lines = inF.readlines()[1:]

            for line in lines:
                stripped = line.strip()
                parts = stripped.split(";")
                url = parts[-1]
                url = url.split("/")
                url= "/".join(url[:-2])
                url=url.replace("amazon.com/","https://amazon.com/")
                urlList.append(url)

        with open("amazon_urls.txt","w",encoding="utf-8") as outF:
            print("-- amazon_urls.txt was created")
            for url in urlList:
                outF.write(url+"\n")

        print("-- done")
    except FileNotFoundError:
        print("Error: I/O error")

if __name__ == '__main__':
    main()