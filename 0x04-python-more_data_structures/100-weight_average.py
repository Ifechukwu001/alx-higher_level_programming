#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum = 0
    sum_of_weights = 0
    weighted_average = 0
    if len(my_list) == 0:
        return 0
    for score, weight in my_list:
        weighted_sum += (score * weight)
        sum_of_weights += weight
    if sum_of_weights:
        weighted_average = weighted_sum / sum_of_weights
    return weighted_average
