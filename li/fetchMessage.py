# encoding: utf-8
# author: LISICHENG
# software: PyCharm
# file: fetchMessage.py
# time: 2020/5/20 10:39
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from li.utils import Utils
from inOut.menu import Menu


class Message:
    @staticmethod
    def transmitReporter(name):
        msg = ""
        # name = self.comboBox_1.currentText()
        menu = Menu()
        nameList = menu.readerTitle("../menuFile/" + str(name) + ".txt")
        util = Utils()
        header = name + "\n今日故障报告如下：\n"
        msg += header
        title = "点位名                                      " + "故障次数(/次)        " + "故障时长(/分钟)        " + "报警次数(/分钟)        \n"
        msg += title
        result = []
        multipleFrequencyOfTaday = util.selectMultipleFrequencyOfToday(name)
        for x in nameList:
            i = 27 - len(x)
            singleFrequencyAndTimeToday = util.selectSingleFrequencyAndTimeCostByName(x)[6]
            count = 0
            for each in multipleFrequencyOfTaday:
                if each[0] == x:
                    count = each[1]
                    break
            data = str(x) + " " * i * 2 + str(singleFrequencyAndTimeToday[1]) + " " * 20 + str(
                singleFrequencyAndTimeToday[2]) + " " * 20 + str(count) + "\n"
            suggest = ""
            if singleFrequencyAndTimeToday[2] > 120:
                suggest += "故障时间过长，请维修！"
            elif singleFrequencyAndTimeToday[1] > 5 and singleFrequencyAndTimeToday[2] < 120:
                suggest += "存在隐藏故障，请检查！"
            else:
                suggest += "该点位表现良好！"
            result.append(str(x) + '------' + suggest)
            msg += data
        msg += "-" * 80 + "\n"
        msg += "建议：\n"
        for x in result:
            msg += x + '\n'
        msg += "-" * 80 + '\n'
        msg += "-" * 80 + '\n'
        return msg


if __name__ == '__main__':
    print(Message().transmitReporter("OP30"))
