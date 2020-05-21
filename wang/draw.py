from utils.image_process import fig2img
from wang.data_access import DataAccess
from wang.figure_plot import Figure_Pie, Figure_OEE, Figure_Loss, Figure_MT
import datetime


class Draw:
    def __init__(self):
        self.da = DataAccess()
        # 若日期发生改变，自行插入全零数据
        result_loss = self.da.select_("select * from loss ORDER BY SJ DESC limit 1")
        current_time = datetime.datetime.now().strftime('%Y-%m-%d')
        if str(result_loss[0][0]) != current_time:
            self.da.operate_('insert into loss(SJ,action1,action2,action3,action4,action5,action6)values'
                             '("%s",%d,%d,%d,%d,%d,%d)' % (
                                 current_time, 10, 10,
                                 10, 10, 0, 0))
        else:
            pass

        result_oee = self.da.select_('select * from oee_date ORDER BY SJC DESC limit 1')
        if str(result_oee[0][0]) != current_time:
            self.da.operate_('insert into oee_date(SJC,O8,O9,O10,O11,O12,O13,O14,O15,O16,O17,O18)values'
                             '("' + current_time + '",0,0,0,0,0,0,0,0,0,0,0)')
        else:
            pass

    def draw_fp(self):  # 绘制损失饼图
        fp = Figure_Pie()
        loss_data = self.da.select_loss()
        sum1 = sum(loss_data)
        loss_data = [d / sum1 for d in loss_data]
        fp.plot(*tuple(loss_data))
        return fig2img(fp.figure)

    def draw_oee(self):  # 绘制oee日推图
        self.da.update_oee()
        oee = Figure_OEE()
        l_eff = self.da.select_oee()
        oee.plot(*tuple(l_eff))  # 参数
        return fig2img(oee.figure)

    def draw_loss(self):  # 绘制损失直方图
        loss = Figure_Loss()
        loss_data = self.da.select_loss()
        loss.plot(*tuple(loss_data))
        return fig2img(loss.figure)

    # def draw_mt(self):  # 绘制耗材使用图
    #     mt = Figure_MT()
    #     mt.plot(*(4, 5, 3))
    #     return fig2img(mt.figure)
    #     graphicscene_mt = QtGui.QGraphicsScene()
    #     graphicscene_mt.addWidget(mt.canvas)
    #     self.ui.graphicsView_MT.setScene(graphicscene_mt)
    #     self.ui.graphicsView_MT.show()
