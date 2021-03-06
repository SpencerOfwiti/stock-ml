import math


def get_threshold(data):
    threshold = math.ceil(len(data) - 5)
    return threshold


def get_overflow(data):
    overflow = len(data) - get_threshold(data)
    return overflow
