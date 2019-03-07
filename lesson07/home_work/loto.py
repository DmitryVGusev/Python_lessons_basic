#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
from random import randint, shuffle


class LotoCard:
    def __init__(self, owner_name):  # TODO переделать этот метод
        """Рандомный инициализватор карточки"""
        self.owner_name = owner_name

        # Генерируется массив уникальных чисел
        nums = []
        while len(nums) < 15:
            rnd = randint(1, 90)
            if rnd not in nums:
                nums.append(rnd)

        self.matrix = []
        for i in range(3):
            self.matrix.append(sorted([nums[j] for j in range(i*5, i*5 + 5)]))


    def show_card(self):  # TODO переделать этот метод
        """Отображает карточку"""
        print("--{}--".format(self.owner_name))
        for i in self.matrix:
            print(*i)
        print("------------")
        pass

    def num_is_in_card(self, num: int):
        """Проверить наличие номера на карточке"""
        return any(num in line for line in self.matrix)

    def cross_out_num_in_card(self, num: int):  # TODO реализовать метод
        """Зачеркнуть номер на карточке"""
        for line in self.matrix:
            try:
                ind = line.index(num)
                line[ind] = '-'
            except ValueError:
                continue

    def is_win(self):
        """Проверить что карточка выиграла"""
        for line in self.matrix:
            if any(str(i) != '-' for i in line):
                return False
        return True


def burrel_bag():
    """
    Достает боченок из мешка
    :return: Номер баченка, количество оставшишся в мешке баченков
    """
    bag = [x for x in range(1, 91)]
    while len(bag) > 0:
        num = bag.pop(randint(0, len(bag)-1))
        yield num, len(bag)


if __name__ == '__main__':
    print("Старт игры.")
    your_card = LotoCard("Ваша карточка")
    comp_card = LotoCard("Карточка компьютера")
    answers = []
    for burrel, elapse in burrel_bag():
        print("\nНовый бочонок: {} (осталось {})".format(burrel, elapse))
        your_card.show_card()
        comp_card.show_card()
        # if your_card.num_is_in_card(burrel):
        #     ans = input("Зачеркнуть цифру? (y/n) ")
        #     if ans.lower() in ['y', 'yes']:
        #         your_card.cross_out_num_in_card(burrel)
        #     else:
        #         print("Вы проиграли.")
        #         break
        # else:
        #     ans = input("Продолжить игру? (y/n) ")
        #     if ans.lower() in ['n', 'no']:
        #         print("Вы проиграли.")
        #         break

        if your_card.num_is_in_card(burrel):
            your_card.cross_out_num_in_card(burrel)

        if comp_card.num_is_in_card(burrel):
            comp_card.cross_out_num_in_card(burrel)

        if your_card.is_win():
            print("Поздравляем, вы выиграли!")
            break
        elif comp_card.is_win():
            print("Компьютер выиграл!")
            break

    print("Конец игры.")
