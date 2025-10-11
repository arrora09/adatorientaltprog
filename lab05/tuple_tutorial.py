t = (2, 3, 5, 8)

print(t)

# van indexeles
print(t[0])
print(t[-1])

# van szeleteles
print(t[:2])

# immutable, nem lehet indexszel modositani


# lehet tarolni tobb tipusu elemeket

m = ("Total Recall", 1990, 7.5)
print(m)

single = ("hi",)
print(single)
print(type(single))
# ha , nelkul akkor string


x = 2
y = 3
print(x, y)
x, y = (2, 3)
print(x, y)
# ez ugyan az
# a zarojelek elhagyhatoak


x, y = y, x
print(x, y)

print()
print()


def get_movie_info():
    return ("Total Recall", 1990, 7.5)


title, year, rating = get_movie_info()
print(title, year, rating)
# vagy
print(get_movie_info()[0], get_movie_info()[1], get_movie_info()[2])
# de ez ronda
