#!/usr/bin/env python3

def hasDouble(word):
    found = False
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            found=True
    return found

def hasMin3Vowel(word):
    vowels=["a","e","i","o","u"]
    counter = 0
    for c in word:
        if c.lower() in vowels:
            counter+=1
    return counter>=3

def main():
    with open("words.txt",encoding="utf-8") as f:
        nice=[]
        for line in f:
            stripped = line.strip()
            if hasDouble(stripped) and hasMin3Vowel(stripped):
                nice.append(stripped)

        print(f"Szép szavak száma: {len(nice)}")

if __name__ == '__main__':
    main()