import random


def shuffled(l):
    shuffled_list = l[:]
    random.shuffle(shuffled_list)
    return shuffled_list


def my_choice(l):
    rand_index = random.randrange(len(l))
    return l[rand_index]


if __name__ == "__main__":
    print(random.random())
    print(random.random())
    print(random.random())
    print()
    print(random.randint(1, 3))
    print(random.randint(1, 3))
    print(random.randint(1, 3))
    print()
    print(random.randrange(1, 5))
    print(random.randrange(1, 5))
    print(random.randrange(1, 5))
    print()
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    print(li)
    print(random.shuffle(li))
    print(li)
    print(random.shuffle(li))
    print(li)
    print()
    print(li)
    print(shuffled(li))
    print(li)
    print()
    print(random.choice(li))
    print(random.choice(li))
    print(random.choice(li))
    print()
    print(my_choice(li))
    print(my_choice(li))
    print(my_choice(li))
