def xor(c1, c2):
    if not bool(c1) and bool(c2) or bool(c1) and not bool(c2):
        return True
    else:
        return False


print(xor(None, "kjhkj"))
print(xor(True, "kjhhkjh"))
print(xor(None, False))
print(xor(True, False))
