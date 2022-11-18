#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_reys(re, pynkt_pr):
    # Сформировать список рейсов.
    result = [employee for employee in re if employee.get('pynkt') == pynkt_pr]

    # Возвратить список выбранных рейсов.
    return result