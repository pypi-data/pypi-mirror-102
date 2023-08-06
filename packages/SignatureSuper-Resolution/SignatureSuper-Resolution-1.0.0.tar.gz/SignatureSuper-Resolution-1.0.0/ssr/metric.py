import pandas as pd
import numpy as np
def metric_dtw(s1, s2):
    l1, l2 = len(s1), len(s2)
    s1 = np.array(s1[["X", "Y", "P"]])
    s2 = np.array(s2[["X", "Y", "P"]])
    dp = np.full((l1 + 1, l2 + 1), np.inf)
    dp[0, 0] = 0
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            dis = np.square(s1[i - 1] - s2[j - 1]).sum()
            dp[i, j] = dis + min(dp[i - 1 , j], dp[i, j - 1], dp[i - 1, j - 1])
    length, i, j = 0, l1, l2
    while i + j:
        _, i, j = min((dp[i - 1, j - 1], i - 1, j - 1), (dp[i, j - 1], i, j - 1), (dp[i - 1, j], i - 1, j))
        length += 1
    dp[l1, l2] = dp[l1, l2] / length
    dp = np.sqrt(dp)
    return dp[l1, l2], length

def metric(hr_data, lr_data, sr_data):
    return 1 - (metric_dtw(sr_data, hr_data) / metric_dtw(lr_data, hr_data))

def metric_rmse(s1 ,s2):
    s1 = np.array(s1[["X", "Y", "P"]])
    s2 = np.array(s2[["X", "Y", "P"]])
    return (np.square(s1 - s2).sum() / len(s1)) ** 0.5