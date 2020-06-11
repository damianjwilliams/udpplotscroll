# udpplotscroll

Basic python script to create a server that receives socket UDP or websockets data and plots it in real-time using a scrolling graph. The scrolling plot is based on an example from pyqtgraph that can be found by running:
```
import pyqtgraph.examples
pyqtgraph.examples.run()
```
Incoming data can parsed from JSON or csv formats.

## Requirements
- [websocket-client](https://pypi.org/project/websocket_client/) (for websocket communication)

- [socket](https://docs.python.org/3/library/socket.html) (for socket communication)

- [json](https://docs.python.org/3/library/json.html)

- [pyqtgraph](http://www.pyqtgraph.org/)

- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) (for older versions of macOS, it may be necessary to install an old version of PyQt5 `pip install PyQt5==5.13.0` )

## Usage
Install  libraries above.

Currently the script uses socket communication with the incoming data in a csv format. To switch to both websocket communication and JSON format:

Uncomment lines 15 and 16 and change the websocket address appropriately.
```
websock_data = websocket.WebSocket()
websock_data.connect("ws://192.100.4.1:81/")
```
Remove lines 30 to 34:
```
#host = '0.0.0.0'
#port = 4444
#buffer_size = 20
#sock_data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock_data.bind((host, port))

```
Uncomment line 55 and remove line 56

```
temp, hum, press = websocketparse()
#temp, hum, press, alt = socketparse()
```

Uncomment line 90 and remove line 91
```
temp, hum, press, alt = websocketparse()
#temp, hum, press, alt = socketparse()
```

The code can be easily adapted but was written to plot data from an ESP32 microcontroller connected to a LSM9DS1 movement sensor. The partner ESP32 aduino code is  [esp32_lsm9ds1_udp](https://github.com/damianjwilliams/esp32_lsm9ds1_udp). A more sophisicated python application, [socscrollsave](https://github.com/damianjwilliams/socscrollsave) allows real-time data to be plotted and the data to be saved.

See my [website](www.ephys.org/ESP32) for examples.

## License
The project is distributed under MIT License
