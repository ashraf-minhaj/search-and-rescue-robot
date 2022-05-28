""" Emergency Search and Rescue Robot

 Copyright (C) Ashraf Minhaj.
 mail: ashraf_minhaj@yahoo.com
"""


import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
from serial import Serial 


class MainWindow(QMainWindow):
    """ The main window class"""    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.bluetooth_port = 'COM8'
        self.buad_rate      = 9600

        # icon paths
        self.foward_icon    = 'res/up-arrow.png'
        self.left_icon      = 'res/left-arrow.png'
        self.right_icon     = 'res/right-arrow.png'
        self.backward_icon  = 'res/down-arrow.png'
        self.stop_icon      = 'res/stop.png'

        self.right_sideway_icon = 'res/right-sideway.png'
        self.left_sideway_icon = 'res/left-sideway.png'
        
    
        self.ui()
    
    def connect_robot(self):
        try:
            # print('Connection Status', self.robot_is_connected())
            self.serial_port = Serial(self.bluetooth_port, self.buad_rate)
            print('Connection Status', self.robot_is_connected())
        except Exception as e:
            print(e)

    def robot_is_connected(self):
        if self.serial_port.isOpen():
            self.connection_indicator_text.setText("Robot Connected")
            self.connect_btn.setDisabled(1)
            return True
        return False

    def disconnect_robot(self):
        if self.robot_is_connected():
            self.serial_port.write(b's')
            self.serial_port.close()
            print('Robot disconnected')
        return
    
    def servo_write(self, val):
        data = str(val).encode()
        # data = val.encode()
        self.serial_port.write(data)
        print(data)


    def ui(self):
        self.setWindowTitle("SAR Robot")
        self.setMaximumWidth(300)
        self.setMaximumHeight(400)

        layout = QGridLayout()

        self.title = QLabel("Search And Rescue Robot", self)
        self.title.setStyleSheet("color: skyblue")
        self.title.setFont(QFont('SimHei', 12, weight=QFont.Bold))

        self.connection_indicator_text = QLabel("Robot Not Connected", self)
        self.connection_indicator_text.setFont(QFont('SimHei', 8))

        self.connect_btn = QPushButton(self)
        self.connect_btn.setText("Connect Robot")
        self.connect_btn.clicked.connect(lambda : self.connect_robot())

        self.robot_contol_label = QLabel("Robot Movement Buttons", self)
        self.robot_contol_label.setFont(QFont('SimHei', 10, weight=QFont.Bold))

        self.forward_btn = QPushButton(self)
        self.forward_btn.setIcon(QIcon(self.foward_icon))
        self.forward_btn.clicked.connect(lambda : self.serial_port.write(b'1'))

        self.left_btn = QPushButton(self)
        self.left_btn.setIcon(QIcon(self.left_icon))
        self.left_btn.clicked.connect(lambda : self.serial_port.write(b'2'))

        self.right_btn = QPushButton(self)
        self.right_btn.setIcon(QIcon(self.right_icon))
        self.right_btn.clicked.connect(lambda : self.serial_port.write(b'3'))

        self.back_btn = QPushButton(self)
        self.back_btn.setIcon(QIcon(self.backward_icon))
        self.back_btn.clicked.connect(lambda : self.serial_port.write(b'4'))

        self.stop_btn = QPushButton(self)
        self.stop_btn.setIcon(QIcon(self.stop_icon))
        self.stop_btn.clicked.connect(lambda : self.serial_port.write(b'0'))

        # ======= Servo controllers =================
        self.servo_contol_label = QLabel("Arm Manipulators", self)
        self.servo_contol_label.setFont(QFont('SimHei', 10, weight=QFont.Bold))

        #========== servo control slider ============
        self.arm_servo_slider = QSlider(Qt.Horizontal, self)
        self.arm_servo_slider.setMinimum(10)
        self.arm_servo_slider.setMaximum(18)
        self.arm_servo_slider.setValue(18)
        self.arm_servo_slider.setTickPosition(QSlider.TicksBelow)
        self.arm_servo_slider.setTickInterval(5)
        self.arm_servo_slider.valueChanged[int].connect(self.servo_write)

        self.wrist_servo_slider = QSlider(Qt.Horizontal, self)
        self.wrist_servo_slider.setMinimum(20)
        self.wrist_servo_slider.setMaximum(28)
        self.wrist_servo_slider.setValue(24)
        self.wrist_servo_slider.setTickPosition(QSlider.TicksBelow)
        self.wrist_servo_slider.setTickInterval(5)
        self.wrist_servo_slider.valueChanged[int].connect(self.servo_write)

        self.claw_servo_slider = QSlider(Qt.Horizontal, self)
        self.claw_servo_slider.setMinimum(30)
        self.claw_servo_slider.setMaximum(38)
        self.claw_servo_slider.setValue(24)
        self.claw_servo_slider.setTickPosition(QSlider.TicksBelow)
        self.claw_servo_slider.setTickInterval(5)
        self.claw_servo_slider.valueChanged[int].connect(self.servo_write)

        #======== add everything into layout ==============
        layout.addWidget(self.title, 0, 0, 1, 5)
        layout.addWidget(self.connection_indicator_text, 1, 0, 1, 5)
        layout.addWidget(self.connect_btn, 2, 0, 1, 5)
        layout.addWidget(self.robot_contol_label, 3, 0, 1, 5)
        layout.addWidget(self.forward_btn, 4, 2)
        layout.addWidget(self.left_btn, 5, 1)
        layout.addWidget(self.stop_btn, 5, 2)
        layout.addWidget(self.right_btn, 5, 3)
        layout.addWidget(self.back_btn, 6, 2)
        layout.addWidget(self.servo_contol_label, 7, 0, 1, 2)
        layout.addWidget(self.arm_servo_slider, 8, 0, 1, 5)
        layout.addWidget(self.wrist_servo_slider, 9, 0, 1, 5)
        layout.addWidget(self.claw_servo_slider, 10, 0, 1, 5)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  #windows are hidden by default
    app.exec_()    #start event loop
