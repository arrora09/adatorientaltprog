def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    res = [e if e in chars else "" for e in text]
    print("".join(res))
    return "".join(res)


valid("Barking!")
valid("KL754", "0123456789")
valid("BEAN", "abcdefghijklmnopqrstuvwxyz")
