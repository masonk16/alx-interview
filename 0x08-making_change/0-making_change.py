#!/usr/bin/python3
"""
Making Change Coding Challenge.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    :param coins: list of the values of the coins in your possession.
    :param total: amount to be met.
    :return: fewest number of coins needed to meet total
    """
    dp = [0] + [total + 1] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[total] == total + 1 else dp[total]
