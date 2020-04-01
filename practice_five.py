from PyQt5.Qt import *
from pynput import keyboard
from PyQt5.QtCore import pyqtSignal
import threading

class Window(QWidget):
    change_signal = pyqtSignal(str)
    back_signal = pyqtSignal(str)
    style_one='''
        QPushButton{
            color:rgba(241, 134, 57, 0.87);
            border-width:2px;
            border-style:solid;
            border-color:rgba(241, 134, 57, 0.87);
            border-radius:10%;
        }
    '''
    style_two ='''
        QPushButton{
            color:rgba(255, 255, 255, 0.85);
            border-width:2px;
            border-style:solid;
            border-color:rgba(255, 255, 255, 0.85);
            border-radius:10%;
            
        }
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('第一次练习')
        self.resize(750,300)
        self.move(50,700)
        self.setup_ui()
        self.setWindowFlags(Qt.WindowStaysOnTopHint) 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1)
        
        #  print(self.__dict__)   我不确定self里面有什么我就输出这个试一试。
        self.change_signal.connect(self.do_change)
        self.back_signal.connect(self.back_change)
    
    def do_change(self,key):

        # print('我要改变颜色了。')
        if key == 'q':
            self.btn_q.setStyleSheet(self.style_two)
        elif key == 'w':
            self.btn_w.setStyleSheet(self.style_two)
        elif key == 'e':
            self.btn_e.setStyleSheet(self.style_two)
        elif key == 'r':
            self.btn_r.setStyleSheet(self.style_two)
        elif key == 't':
            self.btn_t.setStyleSheet(self.style_two)
        elif key == 'y':
            self.btn_y.setStyleSheet(self.style_two)
        elif key == 'u':
            self.btn_u.setStyleSheet(self.style_two)
        elif key == 'i':
            self.btn_i.setStyleSheet(self.style_two)
        elif key == 'o':
            self.btn_o.setStyleSheet(self.style_two)
        elif key == 'p':
            self.btn_p.setStyleSheet(self.style_two)


        elif key == 'a':
            self.btn_a.setStyleSheet(self.style_two)
        elif key == 's':
            self.btn_s.setStyleSheet(self.style_two)
        elif key == 'd':
            self.btn_d.setStyleSheet(self.style_two)
        elif key == 'f':
            self.btn_f.setStyleSheet(self.style_two)
        elif key == 'g':
            self.btn_g.setStyleSheet(self.style_two)
        elif key == 'h':
            self.btn_h.setStyleSheet(self.style_two)
        elif key == 'j':
            self.btn_j.setStyleSheet(self.style_two)
        elif key == 'k':
            self.btn_k.setStyleSheet(self.style_two)
        elif key == 'l':
            self.btn_l.setStyleSheet(self.style_two)

        elif key == 'z':
            self.btn_z.setStyleSheet(self.style_two)
        elif key == 'x':
            self.btn_x.setStyleSheet(self.style_two)
        elif key == 'c':
            self.btn_c.setStyleSheet(self.style_two)
        elif key == 'v':
            self.btn_v.setStyleSheet(self.style_two)
        elif key == 'b':
            self.btn_b.setStyleSheet(self.style_two)
        elif key == 'n':
            self.btn_n.setStyleSheet(self.style_two)
        elif key == 'm':
            self.btn_m.setStyleSheet(self.style_two)
        else:
            pass

    def back_change(self,key):
        # print('back clor ~!')
        if key == 'q':
            self.btn_q.setStyleSheet(self.style_one)
        elif key == 'w':
            self.btn_w.setStyleSheet(self.style_one)
        elif key == 'e':
            self.btn_e.setStyleSheet(self.style_one)
        elif key == 'r':
            self.btn_r.setStyleSheet(self.style_one)
        elif key == 't':
            self.btn_t.setStyleSheet(self.style_one)
        elif key == 'y':
            self.btn_y.setStyleSheet(self.style_one)
        elif key == 'u':
            self.btn_u.setStyleSheet(self.style_one)
        elif key == 'i':
            self.btn_i.setStyleSheet(self.style_one)
        elif key == 'o':
            self.btn_o.setStyleSheet(self.style_one)
        elif key == 'p':
            self.btn_p.setStyleSheet(self.style_one)

        elif key == 'a':
            self.btn_a.setStyleSheet(self.style_one)
        elif key == 's':
            self.btn_s.setStyleSheet(self.style_one)
        elif key == 'd':
            self.btn_d.setStyleSheet(self.style_one)
        elif key == 'f':
            self.btn_f.setStyleSheet(self.style_one)
        elif key == 'g':
            self.btn_g.setStyleSheet(self.style_one)
        elif key == 'h':
            self.btn_h.setStyleSheet(self.style_one)
        elif key == 'j':
            self.btn_j.setStyleSheet(self.style_one)
        elif key == 'k':
            self.btn_k.setStyleSheet(self.style_one)
        elif key == 'l':
            self.btn_l.setStyleSheet(self.style_one)

        elif key == 'z':
            self.btn_z.setStyleSheet(self.style_one)
        elif key == 'x':
            self.btn_x.setStyleSheet(self.style_one)
        elif key == 'c':
            self.btn_c.setStyleSheet(self.style_one)
        elif key == 'v':
            self.btn_v.setStyleSheet(self.style_one)
        elif key == 'b':
            self.btn_b.setStyleSheet(self.style_one)
        elif key == 'n':
            self.btn_n.setStyleSheet(self.style_one)
        elif key == 'm':
            self.btn_m.setStyleSheet(self.style_one)
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
        self.btn_q.setStyleSheet(self.style_one)
        self.btn_q.move(40,100)

        self.btn_w = QPushButton(self)
        self.btn_w.setText('W')
        self.btn_w.resize(50,50)
        self.btn_w.setStyleSheet(self.style_one)
        self.btn_w.move(100,100)
       #  self.btn_w.setFlat(True)  #设置扁平化，就不能绘制背景

        self.btn_e = QPushButton(self)
        self.btn_e.setText('E')
        self.btn_e.resize(50,50)
        self.btn_e.setStyleSheet(self.style_one)
        self.btn_e.move(160,100)

        self.btn_r = QPushButton(self)
        self.btn_r.setText('R')
        self.btn_r.resize(50,50)
        self.btn_r.setStyleSheet(self.style_one)
        self.btn_r.move(220,100)

        self.btn_t = QPushButton(self)
        self.btn_t.setText('T')
        self.btn_t.resize(50,50)
        self.btn_t.setStyleSheet(self.style_one)
        self.btn_t.move(280,100)

        self.btn_y = QPushButton(self)
        self.btn_y.setText('Y')
        self.btn_y.resize(50,50)
        self.btn_y.setStyleSheet(self.style_one)
        self.btn_y.move(340,100)

        self.btn_u = QPushButton(self)
        self.btn_u.setText('U')
        self.btn_u.resize(50,50)
        self.btn_u.setStyleSheet(self.style_one)
        self.btn_u.move(400,100)

        self.btn_i = QPushButton(self)
        self.btn_i.setText('I')
        self.btn_i.resize(50,50)
        self.btn_i.setStyleSheet(self.style_one)
        self.btn_i.move(460,100)

        self.btn_o = QPushButton(self)
        self.btn_o.setText('O')
        self.btn_o.resize(50,50)
        self.btn_o.setStyleSheet(self.style_one)
        self.btn_o.move(520,100)

        self.btn_p = QPushButton(self)
        self.btn_p.setText('P')
        self.btn_p.resize(50,50)
        self.btn_p.setStyleSheet(self.style_one)
        self.btn_p.move(580,100)
        ###########------------##############
        self.btn_a = QPushButton(self)
        self.btn_a.setText('A')
        self.btn_a.resize(50,50)
        self.btn_a.setStyleSheet(self.style_one)
        self.btn_a.move(70,155)
    
        self.btn_s = QPushButton(self)
        self.btn_s.setText('S')
        self.btn_s.resize(50,50)
        self.btn_s.setStyleSheet(self.style_one)
        self.btn_s.move(130,155)
    
        self.btn_d = QPushButton(self)
        self.btn_d.setText('D')
        self.btn_d.resize(50,50)
        self.btn_d.setStyleSheet(self.style_one)
        self.btn_d.move(190,155)

        self.btn_f = QPushButton(self)
        self.btn_f.setText('F')
        self.btn_f.resize(50,50)
        self.btn_f.setStyleSheet(self.style_one)
        self.btn_f.move(250,155)

        self.btn_g = QPushButton(self)
        self.btn_g.setText('G')
        self.btn_g.resize(50,50)
        self.btn_g.setStyleSheet(self.style_one)
        self.btn_g.move(310,155)

        self.btn_h = QPushButton(self)
        self.btn_h.setText('H')
        self.btn_h.resize(50,50)
        self.btn_h.setStyleSheet(self.style_one)
        self.btn_h.move(370,155)

        self.btn_j = QPushButton(self)
        self.btn_j.setText('J')
        self.btn_j.resize(50,50)
        self.btn_j.setStyleSheet(self.style_one)
        self.btn_j.move(430,155)

        self.btn_k = QPushButton(self)
        self.btn_k.setText('K')
        self.btn_k.resize(50,50)
        self.btn_k.setStyleSheet(self.style_one)
        self.btn_k.move(490,155)

        self.btn_l = QPushButton(self)
        self.btn_l.setText('L')
        self.btn_l.resize(50,50)
        self.btn_l.setStyleSheet(self.style_one)
        self.btn_l.move(550,155)

        #############-----------############
        self.btn_z = QPushButton(self)
        self.btn_z.setText('Z')
        self.btn_z.resize(50,50)
        self.btn_z.setStyleSheet(self.style_one)
        self.btn_z.move(100,210)

        self.btn_x = QPushButton(self)
        self.btn_x.setText('X')
        self.btn_x.resize(50,50)
        self.btn_x.setStyleSheet(self.style_one)
        self.btn_x.move(160,210)

        self.btn_c = QPushButton(self)
        self.btn_c.setText('C')
        self.btn_c.resize(50,50)
        self.btn_c.setStyleSheet(self.style_one)
        self.btn_c.move(220,210)

        self.btn_v = QPushButton(self)
        self.btn_v.setText('V')
        self.btn_v.resize(50,50)
        self.btn_v.setStyleSheet(self.style_one)
        self.btn_v.move(280,210)

        self.btn_b = QPushButton(self)
        self.btn_b.setText('B')
        self.btn_b.resize(50,50)
        self.btn_b.setStyleSheet(self.style_one)
        self.btn_b.move(340,210)

        self.btn_n = QPushButton(self)
        self.btn_n.setText('N')
        self.btn_n.resize(50,50)
        self.btn_n.setStyleSheet(self.style_one)
        self.btn_n.move(400,210)

        self.btn_m = QPushButton(self)
        self.btn_m.setText('M')
        self.btn_m.resize(50,50)
        self.btn_m.setStyleSheet(self.style_one)
        self.btn_m.move(460,210)
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