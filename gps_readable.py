#! /usr/bin/env python
import rospy
from nmea_msgs.msg import Sentence

def GetGPS(data):
	#rospy.loginfo(rospy.get_caller_id()+@'Heard',data.data)
	#print data.sentence
	#print type(data.sentence)
	parse_GPS(data)

def GPS_listener():
	rospy.init_node('GPS_listener',anonymous=True)
	rospy.Subscriber('nmea_sentence',Sentence,GetGPS)
	rospy.spin()

def parse_GPS(data):
	
	if data.sentence[0:6] == '$GNGLL':
		if data.sentence[7]!=',':
			latitude=data.sentence[7:17]
			#latitude[2],latitude[3],latitude[4]=latitude[4],latitude[2],latitude[3]
			NS_indicator=data.sentence[18]
			longitude=data.sentence[20:31]
			#longitude[3],longitude[4],longitude[5]=longitude[5],longitude[3],longitude[4]
			EW_indicator=data.sentence[32]
			time="{}:{}:{}{}".format(data[34:36],data[36:38],data[38:40],data[40:43])
			if data.sentence[44]=='A':
				status='Valid'
			else:
				status='Invalid'
			print latitude+NS_indicator+' '+longitude+EW_indicator
			print 'UTC Time:'+ time
			print status
		else:
			print 'No GPS details'

if __name__=='__main__':
	GPS_listener()
