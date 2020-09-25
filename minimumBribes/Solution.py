#!/bin/python3

import math
import os
import random
import re
import sys

def is_in_correct_position(file_position, expected_position):
    return file_position == expected_position


def fix_this_position(q, pos):
    real_index = q.index(pos)
    pos_val = q[pos - 1]
    q[pos - 1] = pos
    q[real_index] = pos_val
    return q


def is_chaotic_position_with_sticker(position, sticker):
    return sticker - position > 2


def is_too_chaotic(q):
    for i in range(0, len(q)):
        sticker = q[i]
        position = i + 1
        if is_chaotic_position_with_sticker(position, sticker):
            print("position:%i - sticker %i" % (position, sticker))
            return True


def is_bribered_in_next_2_positions(q, position):
    index = position - 1
    return q[index + 1] == position or q[index + 2] == position


def q_with_sticker_in_correct_position(q, index_to_correct):
    real_index = q[index_to_correct] - 1
    return q[:real_index] + [q[index_to_correct]] + q[real_index:index_to_correct] + q[index_to_correct + 1:]


# Complete the minimumBribes function below.
def minimumBribes(q):
    if is_too_chaotic(q):
        print("Too chaotic")
        return 0

    swap_quantities = 0
    for i in range(0, len(q)):
        print(q)
        sticker = q[i]
        position = i + 1
        print("position:%i - sticker %i" % (position, sticker))
        if not is_in_correct_position(sticker, position):
            if is_bribered_in_next_2_positions(q, position):
                q = fix_this_position(q, position)
                swap_quantities += 1
            else:
                # Long distance bribes
                sticker_for_this_position = position
                correct_sticker_index = q.index(sticker_for_this_position)
                q = q_with_sticker_in_correct_position(q, correct_sticker_index)
                swap_quantities += correct_sticker_index - i
    print(swap_quantities)
    return swap_quantities


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
