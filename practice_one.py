from PyQt5.Qt import *
import sys
import pythoncom, pyHook


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('第一次练习')
        self.resize(500,500)
        self.setup_ui()
        #两个一起用会让窗口变透明，而且，没有边框。
        self.setWindowFlags(Qt.WindowStaysOnTopHint) 
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1)
        # 这三行代码有意思，你少用那个都不是很好用。就三个一起用，效果很好。
        # 可以试试单独使用的效果。
        # 我靠， 这4行代码，顺序不一样会导致程序不一样。


    def setup_ui(self):
    # self.btn1.pressed.connect(self.star)
    # def star(self):
    #   self.btn1.setStyleSheet('background-color:blue;')
        self.btn_q = QPushButton(self)
        self.btn_q.setText('Q')
        self.btn_q.resize(50,50)
        self.btn_q.setStyleSheet('background-color:rgb(60,228,181);')
        self.btn_q.move(40,100)

        self.btn_w = QPushButton(self)
        self.btn_w.setText('W')
        self.btn_w.resize(50,50)
        self.btn_w.setStyleSheet('background-color:rgb(60, 228, 181);')
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
        self.btn_a.setStyleSheet('background-color:rgb(60, 228, 181);')
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
     
    def keyPressEvent(self, e):  #wdnmd
        key = e.key()
        if key == Qt.Key_W:  #我查一万年没找到这个key()的说明文档。
            self.btn_w.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_A:
            self.btn_a.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_S:
            self.btn_s.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_D:
            self.btn_d.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_Q:
            self.btn_q.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_E:
            self.btn_e.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_F:
            self.btn_f.setStyleSheet('background-color:rgb(255, 255, 0);')
        elif key == Qt.Key_R:
            self.btn_r.setStyleSheet('background-color:rgb(255, 255, 0);')
        

    # def grabKeyboard(self,a):
    #     if a.key() == Qt.Key_W:
    #         self.btn1.setStyleSheet('background-color:red;')
    def keyReleaseEvent(self,r):
        key = r.key()
        if key == Qt.Key_W:
            self.btn_w.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_A:
            self.btn_a.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_S:
            self.btn_s.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_D:
            self.btn_d.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_Q:
            self.btn_q.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_E:
            self.btn_e.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_F:
            self.btn_f.setStyleSheet('background-color:rgb(60, 228, 181);')
        elif key == Qt.Key_R:
            self.btn_r.setStyleSheet('background-color:rgb(60, 228, 181);')

    def mousePressEvent(self,e):
        if e.buttons() == Qt.LeftButton | Qt.RightButton:
            print('关闭窗口')
            self.close()
            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())