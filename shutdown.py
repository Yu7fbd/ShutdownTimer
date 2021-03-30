import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
import subprocess
import os

class Shut():
    flag = False
    def initUI(self,TopWin):
        #顶层窗口
        TopWin.setWindowTitle("定时关机")
        TopWin.resize(420,260)
        #"时"输入框
        self.HourE = QtWidgets.QLineEdit(TopWin)
        self.HourE.setGeometry(QtCore.QRect(100, 50, 37, 25))
        self.HourE.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.HourE.setObjectName("label")
        #"时"标签
        self.HourL = QtWidgets.QLabel(TopWin)
        self.HourL.setGeometry(QtCore.QRect(140, 50, 20, 20))
        self.HourL.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.HourL.setText('时')
        self.HourL.setObjectName('HourL')
        #"分"输入框
        self.MinuteE = QtWidgets.QLineEdit(TopWin)
        self.MinuteE.setGeometry(QtCore.QRect(160,50,37,25))
        self.MinuteE.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.MinuteE.setObjectName("label")
        #"分"标签
        self.MinuteL = QtWidgets.QLabel(TopWin)
        self.MinuteL.setGeometry(QtCore.QRect(200, 50, 20, 20))
        self.MinuteL.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.MinuteL.setText('分')
        self.MinuteL.setObjectName('MinuteL')
        #“开始/取消”按钮
        self.sqB = QtWidgets.QPushButton(TopWin,clicked=self.StartShutdown)
        self.sqB.setGeometry(QtCore.QRect(130, 150, 101, 41))
        self.sqB.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.sqB.setText('开始')
        self.sqB.setObjectName("sqB")
        #“计划关机时间”标签
        self.SetTimeL = QtWidgets.QLabel(TopWin)
        self.SetTimeL.setGeometry(QtCore.QRect(40, 100, 400, 25))
        self.SetTimeL.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
        self.SetTimeL.setObjectName('HourL')

    def StartShutdown(self,TopWin):
        #点击开始，设置定时关机
        h = self.HourE.text()
        if h=='':
            h = 0
        else:
            try:
                h=int(h)
            except:
                self.SetTimeL.setText('请输入正确的时间')
                return
        m = self.MinuteE.text()
        if m=='':
            m = 0
        else:
            try:
                m=int(m)
            except:
                self.SetTimeL.setText('请输入正确的时间')
                return
        shut_time = m*60+h*3600
        if shut_time == 0:
            self.SetTimeL.setText('请输入正确的时间')
            return
        shut_timeM = m + h*60
        CorrentTime = datetime.datetime.now()
        SetTime = (CorrentTime + datetime.timedelta(minutes = shut_timeM)).strftime("%Y-%m-%d %H:%M:%S")
        if self.flag == False:
            self.flag = True
            try:
                subprocess.Popen('shutdown -s -t %d'%shut_time)
                #os.system('shutdown /s /t %d' %shut_time)
                #os.popen('shutdown -s -t %d' %shut_time)
                self.SetTimeL.setText('系统将于'+SetTime+'自动关机')
                self.sqB.setText('取消')
            except Exception as e:
                print(e)
        else:
            #点击取消，取消定时关机，清空label
            self.flag = False
            try:
                subprocess.Popen('shutdown -a').wait()
                #os.system('shutdown /a')
                self.sqB.setText('开始')
                self.SetTimeL.setText('定时关机计划已取消')
                self.HourE.clear()
                self.MinuteE.clear()
            except Exception as e:
                print(e)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    TopWin = QtWidgets.QWidget()
    ui = Shut()
    ui.initUI(TopWin)
    TopWin.show()
    sys.exit(app.exec_())
