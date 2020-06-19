
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import websocket
import socket
try:
    import thread
except ImportError:
    import _thread as thread
import json


#Capture and parse ESP32 data from websocket in a json format
##connect to websocket
#websock_data = websocket.WebSocket()
#websock_data.connect("ws://192.168.4.1:81/")

def websocketparse():

    jresult = websock_data.recv()
    result = json.loads(jresult)
    temp = float(result['Temperature'])
    press = float(result['Pressure'])
    alt = float(result['Altitude'])
    hum = float(result['Humidity'])

    return temp, hum, press, alt

#Capture and parse ESP32 data from websocket in a json format
host = '0.0.0.0'
port = 4444
buffer_size = 90
sock_data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_data.bind((host, port))
#pare
def socketparse():
    csv_data = sock_data.recv(buffer_size).decode()
    csv_data_parsed = csv_data.split(',')
    acc_x = float(csv_data_parsed[0])
    acc_y = float(csv_data_parsed[1])
    acc_z = float(csv_data_parsed[2])
    gyr_x = float(csv_data_parsed[3])
    gyr_y = float(csv_data_parsed[4])
    gyr_z = float(csv_data_parsed[5])
    mag_x = float(csv_data_parsed[6])
    mag_y = float(csv_data_parsed[7])
    mag_z = float(csv_data_parsed[8])
    #print(csv_data_parsed)
    return acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z,mag_x, mag_y, mag_z

#Create empty arrays
list_acc_x = []
list_acc_y = []
list_acc_z = []
list_gyr_x = []
list_gyr_y = []
list_gyr_z = []
list_mag_x = []
list_mag_y = []
list_mag_z = []

#Fill empty arrays with initial values for each measurement
for x in range(100):
    #temp, hum, press = websocketparse()
    acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, mag_x, mag_y, mag_z = socketparse()

    list_acc_x.append(acc_x)
    list_acc_y.append(acc_y)
    list_acc_z.append(acc_z)
    list_gyr_x.append(gyr_x)
    list_gyr_y.append(gyr_y)
    list_gyr_z.append(gyr_z)
    list_mag_x.append(mag_x)
    list_mag_y.append(mag_y)
    list_mag_z.append(mag_z)


#Create plots
win = pg.GraphicsWindow()
win.setWindowTitle('LSM9DS1 scrolling plot example')

p1 = win.addPlot(row = 1, col = 1,left = "x position")
p1.setYRange(-1, +1, padding=0)

p2 = win.addPlot(row = 1, col = 2,left = "y position")
p2.setYRange(-1, +1, padding=0)

p3 = win.addPlot(row = 1, col = 3,left = "z position")
p3.setYRange(-1, +1, padding=0)

p4 = win.addPlot(row = 2, col = 1,left = "x acceleration")
p4.setYRange(+100, -100, padding=0)

p5 = win.addPlot(row = 2, col = 2,left = "y acceleration")
p5.setYRange(+100, -100, padding=0)

p6 = win.addPlot(row = 2, col = 3,left = "z acceleration")
p6.setYRange(+100, -100, padding=0)

p7 = win.addPlot(row = 3, col = 1,left = "x magnetometer")
p7.setYRange(+1, -1, padding=0)

p8 = win.addPlot(row = 3, col = 2,left = "y magnetometer")
p8.setYRange(+1, -1, padding=0)

p9 = win.addPlot(row = 3, col = 3,left = "z magnetometer")
p9.setYRange(+1, -1, padding=0)

#Create lines for plot
curve1 = p1.plot(list_acc_x, pen=pg.mkPen('r', width=2))
curve2 = p2.plot(list_acc_y, pen=pg.mkPen('r', width=2))
curve3 = p3.plot(list_acc_z, pen=pg.mkPen('r', width=2))
curve4 = p4.plot(list_gyr_x, pen=pg.mkPen('g', width=2))
curve5 = p5.plot(list_gyr_y, pen=pg.mkPen('g', width=2))
curve6 = p6.plot(list_gyr_z, pen=pg.mkPen('g', width=2))
curve7 = p7.plot(list_mag_x, pen=pg.mkPen('b', width=2))
curve8 = p8.plot(list_mag_y, pen=pg.mkPen('b', width=2))
curve9 = p9.plot(list_mag_z, pen=pg.mkPen('b', width=2))

ptr1 = 0

#update lists of measurments and add to plots
def updatelist():
    global list_acc_x, list_acc_y, list_acc_z,\
        list_gyr_x, list_gyr_y, list_gyr_z,\
        list_mag_x, list_mag_y, list_mag_z,\
        curve1, curve2, curve3, curve4,\
        curve5, curve6, curve7, curve8, curve9, ptr1
    #temp, hum, press, alt = websocketparse()
    acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, mag_x, mag_y, mag_z = socketparse()

    #acceleration x plot
    list_acc_x[:-1] = list_acc_x[1:]
    list_acc_x[-1] = acc_x
    curve1.setData(list_acc_x)

    #acceleration y plot
    list_acc_y[:-1] = list_acc_y[1:]
    list_acc_y[-1] = acc_y
    curve2.setData(list_acc_y)

    #acceleration z plot
    list_acc_z[:-1] = list_acc_z[1:]
    list_acc_z[-1] = acc_z
    curve3.setData(list_acc_z)

    #gyroscope x plot
    list_gyr_x[:-1] = list_gyr_x[1:]
    list_gyr_x[-1] = gyr_x
    curve4.setData(list_gyr_x)

    # gyroscope y plot
    list_gyr_y[:-1] = list_gyr_y[1:]
    list_gyr_y[-1] = gyr_y
    curve5.setData(list_gyr_y)

    # gyroscope z plot
    list_gyr_z[:-1] = list_gyr_z[1:]
    list_gyr_z[-1] = gyr_z
    curve6.setData(list_gyr_z)

    # magnetometer x plot
    list_mag_x[:-1] = list_mag_x[1:]
    list_mag_x[-1] = mag_x
    curve7.setData(list_mag_x)

    # magnetometer y plot
    list_mag_y[:-1] = list_mag_y[1:]
    list_mag_y[-1] = mag_y
    curve8.setData(list_mag_y)

    # magnetometer z plot

    list_mag_z[:-1] = list_mag_z[1:]
    list_mag_z[-1] = mag_z
    curve9.setData(list_mag_z)



    ptr1 += 1


# update all plots
def updateplot():
    updatelist()


timer = pg.QtCore.QTimer()
timer.timeout.connect(updateplot)
timer.start(20)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
