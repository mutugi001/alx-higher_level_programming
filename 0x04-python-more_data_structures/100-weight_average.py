#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_1 = 0
    av_weight = 0
    if my_list is None:
        return(0)
    for i in my_list:
        sum_1 = sum_1 + int(i[0] * i[1])
    for j in my_list:
        av_weight = av_weight + int(j[1])
    return(sum_1 / av_weight)
