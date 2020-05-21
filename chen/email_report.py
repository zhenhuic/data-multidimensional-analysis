import datetime
from chen.database import MySql


def select_records(production_line: str) -> [[]]:
    end_datetime = datetime.datetime.now()
    start_datetime = end_datetime - datetime.timedelta(days=15)
    time_interval = datetime.timedelta(days=1)

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
    record_numbers = MySql.count_records_multi_datetime_periods(production_line, datetime_periods)
    # print(len(count_records), count_records)
    names = [x[1].split(' ')[0] for x in datetime_periods]
    # print(names)
    return names, record_numbers


def get_records_report() -> str:
    text = "多工位的安全监测、生产过程控制异常事件报告：\n"
    for project_name in ["sawanini_1", "sawanini_2", "zhuanjixia", "penfenshang", "baobantongyong"]:
        names, counts = select_records(project_name)
        text += "工位：" + project_name + "\n"
        for n, c in zip(names, counts):
            text += n + "：" + str(c) + "\n"
    return text
