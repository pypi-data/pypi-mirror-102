import numpy as np
import pandas as pd
from ssr.utils import down_sample

def bezier_curve(p0, p1, p2, p3, inserted):
    """
    三阶贝塞尔曲线
    p0, p1, p2, p3  - 点坐标，tuple、list或numpy.ndarray类型
    inserted        - p0和p3之间插值的数量
    """
    if isinstance(p0, (tuple, list)):
        p0 = np.array(p0)
    if isinstance(p1, (tuple, list)):
        p1 = np.array(p1)
    if isinstance(p2, (tuple, list)):
        p2 = np.array(p2)
    if isinstance(p3, (tuple, list)):
        p3 = np.array(p3)

    points = list()
    for t in np.linspace(0, 1, inserted + 2):
        points.append(p0 * np.power((1 - t), 3) + 3 * p1 * t * np.power((1 - t), 2) + 3 * p2 * (1 - t) * np.power(t,2) + p3 * np.power(t, 3))

    return np.vstack(points)


def smoothing_base_bezier(data, inserted, k=0.3):
    """
    三阶贝塞尔曲线的数据平滑算法
    data        - pd.DataFrame [X, Y, P, T]
    k           - 调整平滑曲线形状的因子，取值一般在0.2~0.6之间。默认值为0.5
    inserted    - 两个原始数据点之间插值的数量。默认值为10
    """
    date_x, date_y, date_p = np.array(data["X"]), np.array(data["Y"]), np.array(data["P"])
    # 第1步：生成原始数据折线中点集
    mid_points = list()
    for i in range(1, date_x.shape[0]):
        mid_points.append({
            'start': (date_x[i - 1], date_y[i - 1], date_p[i - 1]),
            'end': (date_x[i], date_y[i], date_p[i]),
            'mid': (
            (date_x[i] + date_x[i - 1]) / 2.0, (date_y[i] + date_y[i - 1]) / 2.0, (date_p[i] + date_p[i - 1]) / 2.0)
        })

    # 第2步：找出中点连线及其分割点
    split_points = list()
    for i in range(len(mid_points) - 1):
        j = i + 1
        x00, y00, p00 = mid_points[i]['start']  # 第i段左端点
        x01, y01, p01 = mid_points[i]['end']  # 第i段右端点
        x10, y10, p10 = mid_points[j]['start']  # 第j段左端点
        x11, y11, p11 = mid_points[j]['end']  # 第j段右端点
        d0 = np.sqrt(np.power((x00 - x01), 2) + np.power((y00 - y01), 2)) + 1e-8  # 第i段长度
        d1 = np.sqrt(np.power((x10 - x11), 2) + np.power((y10 - y11), 2)) + 1e-8  # 第j段长度
        k_split = 1.0 * d0 / (d0 + d1)
        kp_split = 1. * (abs(p00 - p01) + 1e-8) / (abs(p10 - p11) + abs(p00 - p01) + 1e-8)

        mx0, my0, mp0 = mid_points[i]['mid']  # 第i段中点
        mx1, my1, mp1 = mid_points[j]['mid']  # 第j段中点

        split_points.append({
            'start': (mx0, my0, mp0),
            'end': (mx1, my1, mp1),
            'split': (mx0 + (mx1 - mx0) * k_split, my0 + (my1 - my0) * k_split, mp0 + (mp1 - mp0) * kp_split)
        })

    # 第3步：平移中点连线，调整端点，生成控制点
    crt_points = list()
    for i in range(len(split_points)):
        vx, vy, vp = mid_points[i]['end']  # 第i段右端点
        dx = vx - split_points[i]['split'][0]  # 平移线段x偏移量
        dy = vy - split_points[i]['split'][1]  # 平移线段y偏移量
        dp = vp - split_points[i]["split"][2]  # p偏移量

        sx, sy, sp = split_points[i]['start'][0] + dx, split_points[i]['start'][1] + dy, split_points[i]['start'][
            2] + dp  # 平移后线段起点坐标
        ex, ey, ep = split_points[i]['end'][0] + dx, split_points[i]['end'][1] + dy, split_points[i]['end'][
            2] + dp  # 平移后线段终点坐标

        cp0 = sx + (vx - sx) * k, sy + (vy - sy) * k, sp + (vp - sp) * k  # 控制点坐标
        cp1 = ex + (vx - ex) * k, ey + (vy - ey) * k, ep + (vp - ep) * k  # 控制点坐标

        if crt_points:
            crt_points[-1].insert(2, cp0)
        else:
            crt_points.append([mid_points[0]['start'], cp0, mid_points[0]['end']])

        if i < (len(mid_points) - 2):
            crt_points.append([mid_points[i + 1]['start'], cp1, mid_points[i + 1]['end']])
        else:
            crt_points.append([mid_points[i + 1]['start'], cp1, mid_points[i + 1]['end'], mid_points[i + 1]['end']])
            crt_points[0].insert(1, mid_points[0]['start'])

    # 第4步：应用贝塞尔曲线方程插值
    out = list()
    for item in crt_points:
        group = bezier_curve(item[0], item[1], item[2], item[3], inserted)
        out.append(group[:-1])

    out.append(group[-1:])
    out = np.vstack(out)

    return out.T[0], out.T[1], out.T[2]

def hr2lr2sr(hr_data, down_pps=60, k=0.3):
    """
    hr_data: pd.DataFrame ["X", "Y", "P", "T"]
    sr_data: pd.DataFrame ["X", "Y", "P", "T"]
    k: 贝塞尔曲线超参数
    """
    lr_data, pps, down_pps = down_sample(hr_data, down_pps)
    dots = int((pps - down_pps) / down_pps)
    interval = int(hr_data["T"].diff().mean())
    x, y, p = smoothing_base_bezier(lr_data, dots, k)
    sr_data = pd.DataFrame({"X": x, "Y": y, "P": p, "T": np.linspace(0, (len(x) - 1) * interval, len(x))})
    return sr_data


def ssr_bezier(data, pps, k=0.3):
    """
    data: pd.DataFrame ["X", "Y", "P", "T"], data["T"]非间隔，从0开始
    pps: 要重建到的设备采样率
    k: 贝塞尔曲线超参数
    """
    lr_pps = 1000 / (data["T"].diff().mean())

    dots = int((pps - lr_pps) / lr_pps)
    interval = int(1000 / pps)
    x, y, p = smoothing_base_bezier(data, dots, k)
    sr_data = pd.DataFrame({"X": x, "Y": y, "P": p, "T": np.linspace(0, (len(x) - 1) * interval, len(x))})
    return sr_data
