# coding=utf-8
import datetime
import pymysql


def generate_report(scx, days, bq, warn):
    text = ""
    if days == "日平均(7日)":
        x = [(datetime.datetime.now() - datetime.timedelta(days=6)).strftime("%Y-%m-%d"),
             (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d"),
             (datetime.datetime.now() - datetime.timedelta(days=4)).strftime("%Y-%m-%d"),
             (datetime.datetime.now() - datetime.timedelta(days=3)).strftime("%Y-%m-%d"),
             (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d"),
             (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
             datetime.datetime.now().strftime("%Y-%m-%d")]
        y = []
        end_time = datetime.datetime.now().strftime("%Y-%m-%d")
        start_time = (datetime.datetime.strptime(end_time, "%Y-%m-%d") - datetime.timedelta(days=6)).strftime("%Y-%m-%d")
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     db='opc',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        if scx == "houban":
            sql = "select * from" + "`" + "s7300warning" + "`" + "WHERE BQ = %s AND SJ > %s AND SJ < %s AND BJ = '报警'"
            cursor.execute(sql, (bq, start_time, (datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")))
            day1 = cursor.fetchall()
            y.clear()
            y.append(len(day1))
            cursor.execute(sql, (bq, (
                        datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                    days=1)).strftime("%Y-%m-%d"), (
                        datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                    days=2)).strftime("%Y-%m-%d")))
            day2 = cursor.fetchall()
            y.append(len(day2))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=2)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=3)).strftime("%Y-%m-%d")))
            day3 = cursor.fetchall()
            y.append(len(day3))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=3)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=4)).strftime("%Y-%m-%d")))
            day4 = cursor.fetchall()
            y.append(len(day4))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=4)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=5)).strftime("%Y-%m-%d")))
            day5 = cursor.fetchall()
            y.append(len(day5))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=5)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=6)).strftime("%Y-%m-%d")))
            day6 = cursor.fetchall()
            y.append(len(day6))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=6)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=7)).strftime("%Y-%m-%d")))
            day7 = cursor.fetchall()
            y.append(len(day7))
        if scx == "hanjie":
            sql = "select * from" + "`" + "dcbhj" + "`" + "WHERE BQ = %s AND SJ > %s AND SJ < %s AND ZT = '0-1'"
            cursor.execute(sql, (bq, start_time, (
                        datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime(
                "%Y-%m-%d")))
            day1 = cursor.fetchall()
            y.clear()
            y.append(len(day1))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=1)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                                     days=2)).strftime("%Y-%m-%d")))
            day2 = cursor.fetchall()
            y.append(len(day2))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=2)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=3)).strftime("%Y-%m-%d")))
            day3 = cursor.fetchall()
            y.append(len(day3))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=3)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=4)).strftime("%Y-%m-%d")))
            day4 = cursor.fetchall()
            y.append(len(day4))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=4)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=5)).strftime("%Y-%m-%d")))
            day5 = cursor.fetchall()
            y.append(len(day5))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=5)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=6)).strftime("%Y-%m-%d")))
            day6 = cursor.fetchall()
            y.append(len(day6))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=6)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=7)).strftime("%Y-%m-%d")))
            day7 = cursor.fetchall()
            y.append(len(day7))
        if scx == "xinsawanini":
            sql = "select * from" + "`" + "xinsawanini" + "`" + "WHERE BQ = %s AND SJ > %s AND SJ < %s"
            cursor.execute(sql, (bq, start_time, (
                        datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime(
                "%Y-%m-%d")))
            day1 = cursor.fetchall()
            y.clear()
            y.append(len(day1))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=1)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                                     days=2)).strftime("%Y-%m-%d")))
            day2 = cursor.fetchall()
            y.append(len(day2))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=2)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=3)).strftime("%Y-%m-%d")))
            day3 = cursor.fetchall()
            y.append(len(day3))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=3)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=4)).strftime("%Y-%m-%d")))
            day4 = cursor.fetchall()
            y.append(len(day4))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=4)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=5)).strftime("%Y-%m-%d")))
            day5 = cursor.fetchall()
            y.append(len(day5))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=5)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=6)).strftime("%Y-%m-%d")))
            day6 = cursor.fetchall()
            y.append(len(day6))
            cursor.execute(sql, (bq, (
                    datetime.datetime.strptime(start_time, "%Y-%m-%d") + datetime.timedelta(
                days=6)).strftime("%Y-%m-%d"), (
                                         datetime.datetime.strptime(start_time,
                                                                    "%Y-%m-%d") + datetime.timedelta(
                                     days=7)).strftime("%Y-%m-%d")))
            day7 = cursor.fetchall()
            y.append(len(day7))
        count_list = [x[0] + ": " + str(y[0]) + "次", x[1] + ": " + str(y[1]) + "次", x[2] + ": " + str(y[2]) + "次",
                      x[3] + ": " + str(y[3]) + "次", x[4] + ": " + str(y[4]) + "次", x[5] + ": " + str(y[5]) + "次",
                      x[6] + ": " + str(y[6]) + "次"]
        text = bq + days + warn + ":\n"
        for i in range(len(count_list)):
            text = text + count_list[i] + "\n"
    return text


def report_summarize():
    text = '多生产线数据分析报告\n' + '生产线：侧板焊接线\n'
    for node in ['焊丝启动', '送丝', '油泵开']:
        rep = generate_report("hanjie", "日平均(7日)", node, "计数")
        text += rep

    text += '生产线：新萨瓦尼尼线\n'
    for node in ['门板前左角度', '门板中部左角度', '门板后左角度', '门板前右角度', '门板中部右角度', '门板后右角度']:
        rep = generate_report("xinsawanini", "日平均(7日)", node, "计数")
        text += rep

    return text


if __name__ == '__main__':
    print(report_summarize())
