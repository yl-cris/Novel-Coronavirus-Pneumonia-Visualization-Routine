import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import pandas as pd
import os
import csv
from pyecharts import options as opts
from pyecharts.charts import Geo, Map
from pyecharts.globals import ChartType, SymbolType
from pyecharts.faker import Faker
import csv
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Grid, Line, Scatter, Page

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.write_folder)
        self.pushButton.clicked.connect(self.read_file)
        self.pushButton_3.clicked.connect(self.process)

    def read_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "E:/", "All Files(*);;Text Files(*.csv)")
        print(filename, filetype)
        self.lineEdit.setText(filename)

    def write_folder(self):
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "E:/")
        print(foldername)
        self.lineEdit_2.setText(foldername)

    def process(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()
            print("1")
            # 读取文件(mbcs)
            print(file_path)
            file = open(file_path, 'r')
            my_df = csv.reader(file)
            # 中间可以进行对文件的任意操作
            print("2")
            # 图形的绘制
            position = []
            value = []
            for i in my_df:
                position.append(i[0])
                value.append(i[1])
                # 自定义色盘
            pieces = [
                {'max': 100, 'label': '100以下', 'color': 'blue'},
                {'min': 100, 'max': 1000, 'label': '100-1000', 'color': 'yellow'},
                {'min': 1000, 'max': 5000, 'label': '1000-5000', 'color': 'orange'},
                {'min': 5000, 'max': 10000, 'label': '5000-10000', 'color': 'pink'},
                {'min': 10000, 'max': 20000, 'label': '10000-20000', 'color': 'red'},
            ]

            # 绘制地图
            def drawmap():
                map1 = (
                    Map()
                        .add("湖北省感染人数—2020/2/12", [list(z) for z in zip(position, value)], "湖北")
                        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="2020/2/13湖北省感染情况"),
                        visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces),
                        legend_opts=opts.LegendOpts(),
                    )
                )
                return map1

            # 绘制柱形图
            def drawbar():
                bar = (
                    Bar()
                        .add_xaxis(position)
                        .add_yaxis("感染的人数", value)
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="2020/2/12湖北省感染情况柱状图"),
                        legend_opts=opts.LegendOpts(),
                    )
                )
                return bar
                # 组合图表
            page = Page()
            page.add(drawmap(), drawbar())
            page.render(folder_path + '/yl.html')
            success_result = r'绘制成功！'
            self.lineEdit_3.setText(success_result)
            print("4")
        except:
            fail_result = r'绘制失败！'
            self.lineEdit_3.setText(fail_result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
