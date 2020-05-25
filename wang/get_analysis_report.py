from wang.data_access import DataAccess
import datetime
import time


def get_analysis_report():
    da = DataAccess()
    list_loss = da.select_loss()
    list_oee = da.select_oee()
    dict_oee = {}
    hour = min(time.localtime()[3], 18)
    for i in range(8, hour + 1):
        dict_oee[str(i) + "点"] = list_oee[i - 8]
    analysis_report = "今日侧板焊接分析报告\n" \
                      "\n" \
                      "今日OEE效能数据如下所示：\n" \
                      "{}" \
                      "\n" \
                      "*注：效率为0时未进行检测。\n" \
                      "\n" \
                      "今日设备运行情况分布如下所示：" \
                      "\n" \
                      "清理焊嘴：{} \n" \
                      "装载侧板：{} \n" \
                      "机器静止：{} \n" \
                      "机器工作：{} \n".format(dict_oee, list_loss[0], list_loss[1], list_loss[2], list_loss[3])
    return analysis_report


if __name__ == '__main__':
    print(get_analysis_report())
