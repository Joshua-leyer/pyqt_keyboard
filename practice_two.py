from PyQt5.Qt import *
from pynput import keyboard
import threading

#能识别键盘了。保证不报错。 终端输出字符

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('第一次练习')
        self.resize(500,500)
        self.setup_ui()


    def on_press(self,key):
        # try:
        #     print('alphanumeric key {0} pressed'.format(
        #         key.char))
        # except AttributeError:
        #     print('special key {0} pressed'.format(
        #         key))
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
    
    def on_release(self,key):
        # print('{0} released'.format(
        #     key))
        # 
        print(key)
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        elif key == 'q':
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