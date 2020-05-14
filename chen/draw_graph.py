import datetime

import numpy as np
import matplotlib.pyplot as plt

from chen.database import MySql
from utils.image_process import fig2img, array_to_QImage


def draw_bar_graph(names: [str], values: [int]) -> np.ndarray:
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    fig, ax = plt.subplots()
    ax.bar(names, values)
    ax.set_facecolor("darkgray")
    plt.xticks(rotation=60, fontsize=8)
    # ax.set_xlabel('')
    ax.set_ylabel('异常记录次数')
    img = fig2img(fig)
    return img


def draw_records(production_line: str):
    time_interval = datetime.timedelta(hours=2)
    end_datetime = datetime.datetime.now()
    start_datetime = end_datetime - time_interval

    datetime_periods = []
    temp_datetime = start_datetime + time_interval
    while temp_datetime < end_datetime:
        datetime_periods.append([start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                                 temp_datetime.strftime("%Y-%m-%d %H:%M:%S")])
        start_datetime = temp_datetime
        temp_datetime += time_interval
    if temp_datetime != end_datetime or len(datetime_periods) == 0:
        start_datetime = temp_datetime - time_interval
        datetime_periods.append([start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                                 end_datetime.strftime("%Y-%m-%d %H:%M:%S")])

    # print(len(datetime_periods), datetime_periods)
    count_records = MySql.count_records_multi_datetime_periods(production_line, datetime_periods)
    # print(len(count_records), count_records)
    names = [x[1].split(' ')[1] for x in datetime_periods]
    # print(names)
    img = draw_bar_graph(names, count_records)
    return img
