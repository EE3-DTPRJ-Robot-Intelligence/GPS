import serial

def parse_GPS(data):
	if data[0:6] == '$GNGLL':
		if data[7]!=',':
			latitude=data[7:17]
			#latitude[2],latitude[3],latitude[4]=latitude[4],latitude[2],latitude[3]
			NS_indicator=data[18]
			longitude=data[20:31]
			#longitude[3],longitude[4],longitude[5]=longitude[5],longitude[3],longitude[4]
			EW_indicator=data[32]
			time="{}:{}:{}{}".format(data[34:36],data[36:38],data[38:40],data[40:43])
			if data[44]=='A':
				status='Valid'
			else:
				status='Invalid'
			print latitude+NS_indicator+' '+longitude+EW_indicator
			print 'UTC Time: '+ time
			# print status
		else:
			print 'No GPS details'


gps_serial = serial.Serial('/dev/ttyUSB0', 38400)  # open serial port

while True:
	msg = parse_GPS(gps_serial.readline()) # read message
	if msg != None:
		print msg


# gps_serial.close()             # close port