'''расчет штрафных очков'''
import math
class penalty:
    def cow_penalty_points(number):

        units = math.trunc(number % 10)
        tens = math.trunc(number / 10)
        if units == 5 & tens == 5:
            return 7
        if units == tens:
            return 5
        if units == 0:
            return 3
        if units == 5:
            return 2
        return 1