#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_total = 0
    weight_total = 0

    for score, weight in my_list:
        score_total += score * weight
        weight_total += weight
    return score_total / weight_total
