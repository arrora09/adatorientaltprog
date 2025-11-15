#!/usr/bin/env python3
# coding: utf-8

from typing import List


def match_ends(words) -> int:
    db: int = 0
    for x in words:
        if len(x) >= 2 and x[0] == x[-1]:
            db += 1
    return db


def front_x(words) -> List[str]:
    xlista: List[str] = []
    normal_lista: List[str] = []

    for x in words:
        if x[0] == "x":
            xlista.append(x)
        else:
            normal_lista.append(x)

    xlista = sorted(xlista)
    normal_lista = sorted(normal_lista)
    return xlista + normal_lista
