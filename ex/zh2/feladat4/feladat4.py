#!/usr/bin/env python3

def main():
    with open("input.txt","r",encoding="utf-8") as f:
        words = []
        for line in f:
            words.append(line.strip())

        wordCounter=dict()

        for word in words:
            if word in wordCounter:
                wordCounter[word]+=1
            else:
                wordCounter[word]=1

        sortedKeys = sorted(wordCounter, key=lambda x:wordCounter[x])

        print(f"{sortedKeys[0]}: {wordCounter[sortedKeys[0]]}")
        print(f"{sortedKeys[-1]}: {wordCounter[sortedKeys[-1]]}")

if __name__ == '__main__':
    main()