#!/bin/python3

import math
import os
import random
import re
import sys

def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2

# Create array
N = int(input())
VALUES = list(map(int, input().split()))
FREQUENCY = list(map(int, input().split()))

ARRAY = []

for i in range(N):
    ARRAY += [VALUES[i]] * FREQUENCY[i]
ARRAY = sorted(ARRAY)

# Find interquartile_range
INTERQUARTILE_RANGE = float(find_median(ARRAY[len(ARRAY) // 2 + len(ARRAY) % 2:]) - find_median(ARRAY[:len(ARRAY)//2]))

print(INTERQUARTILE_RANGE)