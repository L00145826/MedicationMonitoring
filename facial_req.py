#! /usr/bin/python

# import the necessary packages

from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import RPi.GPIO as GPIO
import datetime
import pywhatkit
import pyautogui
import pyrebase
import webbrowser
import pyrebase



##variables

firebaseConfig = {
  "apiKey": "AIzaSyBpgjeUFiTnkw7bXeZt2d9eeqnL0nuEN-g",
  "authDomain": "medicationmonitoring-39ad3.firebaseapp.com",
  "databaseURL": "https://medicationmonitoring-39ad3-default-rtdb.firebaseio.com",
  "projectId": "medicationmonitoring-39ad3",
  "storageBucket": "medicationmonitoring-39ad3.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
 
};


#allows the database to be worked with
firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()
db = firebase_storage.database()




#upload
##storage.child("image.jpg").put("image.jpg")
#storage.child("nightimeHour)".put("nightimeHour")

#time =  {"morningHour": 9,"morningMinute": 30,
#"afternoonHour": 14,"afternoonMinute": 30,
#"nighttimeHour": 19,"nighttimeMinute": 30 } 

#
#db.child("times").child("times needed").set(time)
#db.push(time)

# gets the valies from the database
morningHour = db.child("times").child("times needed").child("morningHour").get()
morningMinute = db.child("times").child("times needed").child("morningMinute").get()

afternoonHour = db.child("times").child("times needed").child("afternoonHour").get()
afternoonMinute = db.child("times").child("times needed").child("afternoonMinute").get()

nighttimeHour = db.child("times").child("times needed").child("nighttimeHour").get()
nighttimeMinute = db.child("times").child("times needed").child("nighttimeMinute").get()

#turns the values into usable values
mornval = morningHour.val()
mornmin = morningMinute.val()
afval =afternoonHour.val()
afminval = afternoonMinute.val()
nval = nighttimeHour.val()
nmin = nighttimeMinute.val()

print(str(mornval)   +"  " + str(mornmin))
	

#Initialize 'currentname' to trigger only when a new person is identified.
currentname = "unknown"
nameLookedFor = "Mandy"
unknownname = "Unknown"
Unknown =False 

#goes to true if the box was opened at the right time to take the medication by the right user
morningTablets = False
afternoonTablets = False
nightimeTablets = False





LED_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# initialize the video stream and allow the camera sensor to warm up
# Set the ser to the followng
# src = 0 : for the build in single web cam, could be your laptop webcam
# src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
#vs = VideoStream(src=2,framerate=10).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	# Detect the fce boxes
	boxes = face_recognition.face_locations(frame)
	# compute the facial embeddings for each face bounding box
	encodings = face_recognition.face_encodings(frame, boxes)
	names = []

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown" #if face is not recognized, then print Unknown
		if name =="Unknown":
			Unknown = True
		

		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number
			# of votes (note: in the event of an unlikely tie Python
			# will select first entry in the dictionary)
			name = max(counts, key=counts.get)
            
			#If someone in your dataset is identified, print their name on the screen
			if currentname != name:
				currentname = name
				print(currentname)
				
			
				
				
			if currentname == nameLookedFor:
				now_time = datetime.datetime.now().time()
				print(now_time)
				#morning
				#check value isnt -1 which would mean there is no medication stops errors happening
				if mornval >= 0:
					if mornval == 23:
						if now_time >= datetime.time(mornval,mornmin) and now_time <= datetime.time(00,mornmin):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							morningTablets = True
							print("morningTablets")
							
					else:
						if now_time >= datetime.time(mornval,mornmin) and now_time <= datetime.time(mornval+1,mornmin):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							morningTablets = True
							print("morningTablets")
				#afternoon	
				#check value isnt -1 which would mean there is no medication stops errors happening
				if afval >= 0:	
					if afval == 23:
						if now_time >= datetime.time(afval,afminval) and now_time <= datetime.time(00,afminval):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							afternoonTablets = True
							print("afternoon tablets")
							
					else:
						if now_time >= datetime.time(afval,afminval) and now_time <= datetime.time(afval+1,afminval):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							afternoonTablets = True
							print("afternoon tablets")
				#nighttime
				#check value isnt -1 which would mean there is no medication stops errors happening
				if nval >= 0:
					if nval == 23:
						if now_time >= datetime.time(nval,nmin) and now_time <= datetime.time(00,nmin):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							nightimeTablets = True
							print("nighttime tablets")
							
					else:
						if now_time >= datetime.time(nval,nmin) and now_time <= datetime.time(nval+1,nmin):
							#print("in")
							GPIO.output(LED_PIN,GPIO.HIGH)
							time.sleep(5)
							GPIO.output(LED_PIN,GPIO.LOW)
							nightimeTablets = True
							print("nighttime tablets")
			

				
			#print("sending message")
			#if datetime.time(15,49):
		##if morningTablets is False:
			#send notifcation
			##print("sending message")
			#pywhatkit.sendwhatmsg("+353877997643" , "You missed your morning medication", 15,56)
			#time.sleep(20)
			#pyautogui.click(1620,1020)
                
                
			#if now.strftime("%y-%m-%d %H:%M:%S") == 22-02-23 10:00:00
            

                

		# update the list of names
		names.append(name)
		

        
        
    
	# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image - color is in BGR
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 225), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			.8, (0, 255, 255), 2)

	# display the image to our screen
	# by 90 degrees clockwise
	#image = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
	cv2.imshow("Facial Recognition is Running",frame)
	key = cv2.waitKey(1) & 0xFF
	#print(Unknown)
	
	if Unknown == True:
		print("unknown detected")
		Unknown= False
		## it will only upload image if it is not the correct user
		if currentname != nameLookedFor:
				## connect to firebase to upload images
				firebaseConfig = {
				  "apiKey": "AIzaSyBpgjeUFiTnkw7bXeZt2d9eeqnL0nuEN-g",
				  "authDomain": "medicationmonitoring-39ad3.firebaseapp.com",
				  "databaseURL": "https://medicationmonitoring-39ad3-default-rtdb.firebaseio.com",
				  "projectId": "medicationmonitoring-39ad3",
				  "storageBucket": "medicationmonitoring-39ad3.appspot.com",
				  "serviceAccount": "serviceAccountKey.json"
				 
				};


				##upload image of unknown person to database
				firebase_storage = pyrebase.initialize_app(firebaseConfig)
				storage = firebase_storage.storage()
				
				#upload the image of the unauthorised user
				image = "Unknown.jpg"
				#creates the image
				cv2.imwrite(image,frame)
				curtime = datetime.datetime.now().time()
				#uploads the image with the time they tried to access the box
				upload = "unnauthorised user "+ str(curtime)
				
				##uploads images of the unauthorised user to firebase where it can be seen
				storage.child(upload).put(image)
				#sets unknown as false so it has to recognise a unauthorised user to upload again
				Unknown = False
				#time.sleep(5)
    
	#code sends messages to the user if they have missed any of their medication
	# it also checks if they are meant to take the medication at that time if they
	# are not meant to the value will be -1 for the time
	d = time.localtime()
	ctime = time.strftime("%H:%M:%S", d)
	#check value isnt -1 which would mean there is no medication stops errors happening
	if mornval >= 0:
		if mornval == 23:
			if datetime.time(00,mornmin).strftime("%H:%M:%S") == ctime :
				print("in")
				if morningTablets is False:
					if mornval == 23:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your morning medication", 00,mornmin+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your morning medication", mornval+1,mornmin+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
		else:
			if datetime.time(mornval+1,mornmin).strftime("%H:%M:%S") == ctime :
				if morningTablets is False:
					if mornval == 23:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your morning medication", 00,mornmin+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your morning medication", mornval+1,mornmin+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
	#check value isnt -1 which would mean there is no medication stops errors happening
	if afval >=0:		
		if afval == 23:
			if datetime.time(00,afminval).strftime("%H:%M:%S") == ctime :
				print("in")
				if afternoonTablets is False:
					if afval == 23:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your afternoon medication", 00,afminval+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your afternoon medication", afval+1,afminval+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
		else:
			if datetime.time(afval+1,afminval).strftime("%H:%M:%S") == ctime :
				if afternoonTablets is False:
					if afval == 23:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your afternoon medication", 00,afminval+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						print("sending message")
						pywhatkit.sendwhatmsg("+353877997643" , "You missed your afternoon medication", afval+1,afminval+1)
						time.sleep(20)
						pyautogui.click(1620,1020)
	#check value isnt -1 which would mean there is no medication stops errors happening
	if nval >= 0:			
		if nval == 23:
			if datetime.time(00,nmin).strftime("%H:%M:%S") == ctime :
				print("in")
				if nightimeTablets is False:
					if nval == 23:
						#send notifcation
						#print("sending message")
						#send whatsapp message to user that they missed medication
						pywhatkit.sendwhatmsg("+353861620453" , "You missed your nighttime medication", 00,nmin+1)
						time.sleep(20)
						#click send button
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						#send whatsapp message to user that they missed medication
						pywhatkit.sendwhatmsg("+353861620453" , "You missed your nighttime medication", nval+1,nmin+1)
						time.sleep(20)
						#click send button
						pyautogui.click(1620,1020)
		else:
			if datetime.time(nval+1,nmin).strftime("%H:%M:%S") == ctime :
				if nightimeTablets is False:
					if nval == 23:
						#send notifcation
						#print("sending message")
						#send whatsapp message to user that they missed medication
						pywhatkit.sendwhatmsg("+353861620453" , "You missed your nighttime medication", 00,nmin+1)
						time.sleep(20)
						#click send button
						pyautogui.click(1620,1020)
					else:
						#send notifcation
						#print("sending message")
						#send whatsapp message to user that they missed medication
						pywhatkit.sendwhatmsg("+353861620453" , "You missed your nighttime medication", nval+1,nmin+1)
						time.sleep(20)
						#click send button
						pyautogui.click(1620,1020)
						
						
						
	#check value isnt -1 which would mean there is no medication stops errors happening				
	if mornval >= 0:					
		if datetime.time(mornval,mornmin).strftime("%H:%M:%S") == ctime :
				if mornmin == 59:
					if mornval ==23:
						mornval = 0
						mornmin = 0
					else:
						mornval = mornval+1
						mornmin = 0
				#send notifcation
				print("sending message")
				pywhatkit.sendwhatmsg("+353861620453" , "Its time for your morning medication", mornval,mornmin+1)
				time.sleep(20)
				pyautogui.click(1620,1020)
			
	#check value isnt -1 which would mean there is no medication stops errors happening					
	if afval >= 0:					
		if datetime.time(afval,afminval).strftime("%H:%M:%S") == ctime :
			if afminval == 59:
					if afval ==23:
						afval = 0
						afminval = 0
					else:
						afval = afval+1
						afminval = 0
			#send notifcation,30
			print("sending message")
			pywhatkit.sendwhatmsg("+353877997643" , "Its time for your afternoon medication", afval,afminval+1)				
			time.sleep(20)
			pyautogui.click(1620,1020)
							
							
	#check value isnt -1 which would mean there is no medication stops errors happening					
	if nval >= 0:					
		if datetime.time(nval,nmin).strftime("%H:%M:%S") == ctime :
			if nmin == 59:
					if nval ==23:
						nval = 0
						nmin = 0
					else:
						nval = nval+1
						nmin = 0
						
			#send notifcation
			print("sending message")
			pywhatkit.sendwhatmsg("+353877997643" , "Its time for your nighttime medication", nval,nmin+1)
			time.sleep(20)
			pyautogui.click(1620,1020)
							

					
					
	
	#gets the current time to check
	d = time.localtime()
	ctime = time.strftime("%H:%M:%S", d)
	
	#print(morningTablets)
	#print(afternoonTablets)
	#print(nightimeTablets)
	
	#resets if the medication was taken or not at the start of each day
	if datetime.time(00,00).strftime("%H:%M:%S") == ctime :
		morningTablets = False
		afternoonTablets = False
		nightimeTablets = False
            
    
	# quit when 'q' key is pressed
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()
#error handling done in the other program -1 means there is no medication at this time
#if values are -1 the program wont use them numbers
if mornval <= 0:
	print("no morning tablets")
else:
	print("morning tablets")

if afval <= 0:
	print("no afternoon tablets")
else:
	print("afternoon tablets")

if nval <= 0:
	print("no nighttime tablets")
else:
	print("nighttime tablets")


# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
