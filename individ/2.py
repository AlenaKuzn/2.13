#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from get_reys import get_reys
from display import display_reys
from select_reys import select_reys
from help import help


def main():
    #Список рейсов
    reys = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            reys = get_reys(reys)

        elif command == 'list':
            display_reys(reys)

        elif command.startswith('select '):
            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый город.
            pynkt_pr = str(parts[1])

            selected = select_reys(reys, pynkt_pr)
            display_reys(selected)

        elif command == 'help':
            help()

        else:
            print("неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
