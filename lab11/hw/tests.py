from hamming import hamming
from brackets import brackets
from certainchars import valid


def test_valid():
    assert valid("Barking!") == "B"
    assert valid("KL754", "0123456789") == "754"
    assert valid("BEAN", "abcdefghijklmnopqrstuvwxyz") == ""


def test_brackets():
    assert brackets("((5+3)*2+1)") == True
    assert brackets("{[(3+1)+2]+}") == True
    assert brackets("(3+{1-1)}") == False
    assert brackets("[1+1]+(2*2)-{3/3}") == True
    assert brackets("(({[(((1)-2)+3)-3]/3}-3)") == False


def test_hamming():
    assert hamming("asd", "dsa") == 2
    assert hamming("asd", "da") == "A hossz különböző, Hamming nem értelmezett"
    assert hamming("görög", "török") == 2
