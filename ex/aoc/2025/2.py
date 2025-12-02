import re

TEXT = "328412-412772,1610-2974,163-270,7693600637-7693779967,352-586,65728-111612,734895-926350,68-130,183511-264058,8181752851-8181892713,32291-63049,6658-12472,720-1326,21836182-21869091,983931-1016370,467936-607122,31-48,6549987-6603447,8282771161-8282886238,7659673-7828029,2-18,7549306131-7549468715,3177-5305,20522-31608,763697750-763835073,5252512393-5252544612,6622957-6731483,9786096-9876355,53488585-53570896"


def isValid(id: str) -> bool:
    # print(id, len(id) % 2 != 0)
    if len(id) % 2 != 0:
        return True

    half = len(id) // 2

    return id[:half] != id[half:]


TEST_TEXT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def t1() -> None:
    parts = []
    for line in TEXT.split(","):
        lineParts = line.split("-")
        minNum = int(lineParts[0])
        maxNum = int(lineParts[1])
        for i in range(minNum, maxNum + 1):
            if not isValid(str(i)):
                parts.append(i)

    print(sum(parts))


def isValid2(id: str) -> bool:
    match = re.match(r"^(.+?)\1+$", id)

    return not bool(match)


def t2() -> None:
    parts = []
    for line in TEXT.split(","):
        lineParts = line.split("-")
        minNum = int(lineParts[0])
        maxNum = int(lineParts[1])
        for i in range(minNum, maxNum + 1):
            if not isValid2(str(i)):
                parts.append(i)

    print(sum(parts))


if __name__ == "__main__":
    # t1()
    t2()
