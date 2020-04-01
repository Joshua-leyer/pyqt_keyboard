from PyQt5.Qt import *
from pynput import keyboard
from PyQt5.QtCore import pyqtSignal
import threading

class Window(QWidget):
    change_signal = pyqtSignal(str)
    back_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('第一次练习')
        self.resize(500,500)
        self.setup_ui()
        #self.setWindowFlags(Qt.WindowStaysOnTopHint) 
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowOpacity(1)
        #  print(self.__dict__)   我不确定self里面有什么我就输出这个试一试。
        self.change_signal.connect(self.do_change)
        self.back_signal.connect(self.back_change)
    
    def do_change(self,key):
        print('我要改变颜色了。')
        if key == 'q':
            self.btn_q.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'w':
            self.btn_w.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'e':
            self.btn_e.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'r':
            self.btn_r.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'a':
            self.btn_a.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 's':
            self.btn_s.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'd':
            self.btn_d.setStyleSheet('background-color:rgb(239, 172, 60);')
        elif key == 'f':
            self.btn_f.setStyleSheet('background-color:rgb(239, 172, 60);')
        else:
            pass

    def back_change(self,key):
        # try:
        print('back clor ~!')
        if key == 'q':
            self.btn_q.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'w':
            self.btn_w.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'e':
            self.btn_e.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'r':
            self.btn_r.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'a':
            self.btn_a.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 's':
            self.btn_s.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'd':
            self.btn_d.setStyleSheet('background-color:rgb(60,228,181);')
        elif key == 'f':
            self.btn_f.setStyleSheet('background-color:rgb(60,228,181);')
        # except
        #     pass
    def on_press(self,key): #我多次试验，最后用key.__dict__发现返回的key不是一个变量，是个实例化的对象
        try:
            key_code = key.char
            self.change_signal.emit(key_code)
        except:
            pass


    def on_release(self,key):
        try:
            key_code = key.char
            self.back_signal.emit(key_code)
        except:
            pass

    def key_p(self):
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def setup_ui(self):

        self.btn_q = QPushButton(self)
        self.btn_q.setText('Q')
        self.btn_q.resize(50,50)
        self.btn_q.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_q.move(40,100)

        self.btn_w = QPushButton(self)
        self.btn_w.setText('W')
        self.btn_w.resize(50,50)
        self.btn_w.setStyleSheet('background-color:rgb(60, 228,181);')
        self.btn_w.move(100,100)
       #  self.btn_w.setFlat(True)  #设置扁平化，就不能绘制背景

        self.btn_e = QPushButton(self)
        self.btn_e.setText('E')
        self.btn_e.resize(50,50)
        self.btn_e.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_e.move(160,100)

        self.btn_r = QPushButton(self)
        self.btn_r.setText('R')
        self.btn_r.resize(50,50)
        self.btn_r.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_r.move(220,100) 

        self.btn_a = QPushButton(self)
        self.btn_a.setText('A')
        self.btn_a.resize(50,50)
        self.btn_a.setStyleSheet('background-color:rgb(60, 228,181);')
        self.btn_a.move(70,155)
    
        self.btn_s = QPushButton(self)
        self.btn_s.setText('S')
        self.btn_s.resize(50,50)
        self.btn_s.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_s.move(130,155)
    
        self.btn_d = QPushButton(self)
        self.btn_d.setText('D')
        self.btn_d.resize(50,50)
        self.btn_d.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_d.move(190,155)

        self.btn_f = QPushButton(self,)
        self.btn_f.setText('F')
        self.btn_f.resize(50,50)
        self.btn_f.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_f.move(250,155)



def main():
    pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    t = threading.Thread(target=window.key_p)
    t.setDaemon(True)
    t.start()
    sys.exit(app.exec_())