# GPS
## Notes for GPS

The GPS used was this model
[Ublox GPS NEO-M8N](https://www.ebay.co.uk/itm/Ublox-NEO-M8N-GPS-Compass-with-shell-for-PIX-PX4-Pixhawk-Flight-Controller-UK/252111344885?epid=1088850025&hash=item3ab301d4f5:g:JbQAAOSwQTVV-osy)

GPS Baud rate: 38400  

>Wire colours:
>
>| USB pins | Jumper Colours |  GPS Wire colours |
>|---|---|---|
>| **3V3** |	Green |	Red |
>| **TXD** |	Orange |	White |
>| **RXD**	| Yellow |	Yellow |
>| **GND** |	Red |	Black |


### Run python directly
In terminal,
```
sudo chmod 777 /dev/ttyUSB0 
python gps_pyserial.py 
```

### Run ROS
1. Download  nmea_navsat_driver
2. In terminal,
```
git clone https://github.com/ros-drivers/nmea_navsat_driver.git
```
3. Place nmea_navsat_driver package in src of catkin workspace, locate the files:
 * nmea_serial_driver 
 * nmea_topic_serial_reader  
   
   and ensure that the following line is set:
```python
serial_baud = rospy.get_param('~baud',38400)  #sets the baud rate to 38400
```

4. Add the gps_readable.py file in the same location as the previous 2 files.
5. In terminal,
```
roscore
source /devel/setup.bash
rosrun nmea_navsat_driver nmea_topic_serial_reader
rosrun nmea_navt_driver gps_readable.py 
```
