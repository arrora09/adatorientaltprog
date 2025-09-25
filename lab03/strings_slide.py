s = "hello"
print(s)

s = 'hello'
print(s)

s = 'She said "get out!"'
print(s)

s = "She said \"get out!\""
print(s)

s = "She isn't"
print(s)

s = "batman"
print(len(s))

print(s[0])

print(s.upper())

s = "joker"
print(s.find("k"))
print(s.find("ke"))
print(s.find("asd"))

s = "batman"
s = s.upper()
print(s)

s = "aNNa"
print(s.capitalize())


s = "          asdfasdfasf asdfffffff                       sadfuksdfhkasdj f            ksudfhjkasdfhjkasdfksd fksdjf hsdfjksd                  "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = "2025"
print(s.isdigit())
s = "2025a"
print(s.isdigit())

url = "https://google.com"
print(url.startswith("asd"))
print(url.startswith("https://"))

print(url.endswith(".com"))
print(url.endswith(".hu"))

s = "cat dog cat cat"
print(s.replace("cat", "kitten"))
print(s.replace("cat", "kitten",2))
