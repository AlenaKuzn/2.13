#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def a(type: str):
    def b(value):
        gen = (e for e in value.split())
        if type == 'list':
            return "Список ", list(gen)
        return "Кортеж ", tuple(gen)
    return b
