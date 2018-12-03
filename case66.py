import ru_local
from turtle import *
from math import sqrt


def get_num_hexagons():
    try:
        number = int(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
        if 4 <= number <= 20:
            return number
        else:
            raise ValueError
    except ValueError:
        while True:
            try:
                number = int(input('Оно должно быть от 4 до 20: '))
                if 4 <= number <= 20:
                    return number
                else:
                    raise ValueError
            except ValueError:
                continue


def filling_colors():
    print('Допустимые цвета заливки: ')
    print(' ' + ru_local.RED, ru_local.BLUE, ru_local.GREEN, ru_local.YELLOW, ru_local.ORANGE, ru_local.PURPLE,
          ru_local.PINK, sep='\n ')


def get_color_choice():
    color = input('Пожалуйста, введите цвет: ')
    if color == ru_local.RED or color == ru_local.BLUE or color == ru_local.GREEN or color == ru_local.YELLOW or color == ru_local.ORANGE or color == ru_local.PURPLE or color == ru_local.PINK:
        return color
    else:
        while True:
            color = input("'" + color + "' не является верным значением. Пожалуйста, повторите попытку: ")
            if color == ru_local.RED or color == ru_local.BLUE or color == ru_local.GREEN or color == ru_local.YELLOW or color == ru_local.ORANGE or color == ru_local.PURPLE or color == ru_local.PINK:
                return color
            else:
                continue


def draw_hexagon(x, y, side_len, color):
    if color == ru_local.RED:
        color = ru_local.REDCOLOR
    elif color == ru_local.BLUE:
        color = ru_local.BLUECOLOR
    elif color == ru_local.GREEN:
        color = ru_local.GREENCOLOR
    elif color == ru_local.YELLOW:
        color = ru_local.YELLOWCOLOR
    elif color == ru_local.ORANGE:
        color = ru_local.ORANGECOLOR
    elif color == ru_local.PURPLE:
        color = ru_local.PURPLECOLOR
    elif color == ru_local.PINK:
        color = ru_local.PINKCOLOR
    fillcolor(color)
    up()
    goto(x, y)
    down()
    begin_fill()
    left(30)
    for i in range(6):
        forward(side_len)
        right(60)
    right(30)
    end_fill()
    up()


def main():
    number = get_num_hexagons()
    filling_colors()
    color1 = get_color_choice()
    color2 = get_color_choice()
    speed(0)
    screensize(500, 500)
    side_len = 500 / (number * sqrt(3))
    x = -250
    y = 200
    for j in range(number):
        if j % 2 == 0:
            color1, color2 = color2, color1
        up()
        goto(x, y)
        down()
        for i in range(number):
            if i % 2:
                draw_hexagon(x, y, side_len, color1)
            else:
                draw_hexagon(x, y, side_len, color2)
            x = x + 500 / number
        y = y - 1.5 * side_len
        if j % 2:
            x -= (number - 0.5) * (500 / number)
        else:
            x -= (number + 0.5) * (500 / number)
    mainloop()


if __name__ == '__main__':
    main()

