#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_reys(reys):
    pynkt = input("Пункта назначения рейса: ")
    numb = int(input("Номер рейса: "))
    samolet = input("Тип самолета: ")

    # Создать словарь.
    rey = {
        'pynkt': pynkt,
        'numb': numb,
        'samolet': samolet,
    }

    # Добавить словарь в список.
    reys.append(rey)

    # Отсортировать список в случае необходимости.
    if len(reys) > 1:
        reys.sort(key=lambda item: item.get('numb', ''))
    return reys
