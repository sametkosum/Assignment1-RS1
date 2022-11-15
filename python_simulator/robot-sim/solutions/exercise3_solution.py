from __future__ import print_function
import time
from sr.robot import *
a_th = 2.0
d_th = 0.4
silver = True
R = Robot()
arr = []

def drive(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


#################################################################################


def find_silver_token():

    offset_silver=None
    dist=100
    
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
	    rot_y=token.rot_y
	    offset_silver=token.info.offset
    if dist==100:
	return -1, -1 , offset_silver
    else:
   	return dist, rot_y , offset_silver


 ################################################################################
 
 
def find_golden_token():
 
    offset_golden= None
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
	    offset_golden=token.info.offset
    if dist==100:
	return -1, -1 ,offset_golden
    else:
   	return dist, rot_y ,offset_golden


###############################################################################


while 1:
  if silver == True: # if silver is True, than we look for a silver token, otherwise for a golden one
    dist, rot_y,offset = find_silver_token()
    if offset in arr:
	
		turn(+40, 0.2)
	        #drive(80, 0.5)
   
    elif dist==-1: # if no token is detected, we make the robot turn 
	print("I don't see any token!!")
	turn(+20, 2)
    elif dist <d_th: # if we are close to the token, we try grab it.
        print("Found it!")
        if R.grab(): # if we grab the token, we move the robot forward and on the right, we release the token, and we go back to the initial position
            print("Gotcha!")
            #print("offset number : {0}" .format(offset))
            arr.append(offset) 
            turn(-20,2.1)
	    drive(5,2)
	    #R.release()
	    #drive(-20,2)
	    #turn(-20,2) 
	    silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token
	else:
            print("Aww, I'm not close enough.")
    elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
	print("Ah, that'll do.")
        drive(120, 0.5)
    elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        print("Left a bit...")
        turn(-2, 0.5)
    elif rot_y > a_th:
        print("Right a bit...")
        turn(+2, 0.5)
  else:
	dist, rot_y,offset = find_golden_token()
	if dist==-1: # if no token is detected, we make the robot turn 
		print("I don't see any token!!")
		turn(+50, 0.1)
    	elif dist <0.6: # if we are close to the token, we try grab it.
        	print("Found it!")
        	if R.release(): # if we grab the token, we move the robot forward and on the right, we release the token, and we go back to the initial position
            		print("Gotcha!")
	    		drive(-80,0.5)
	    		turn(+2,0.5)
	    		#print("offset number : {0}" .format(offset))
                        arr.append(offset)
            
	    		
	    		silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token
		else:
            		print("Aww, I'm not close enough.")
    	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
        	drive(80, 0.1)
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	print("Left a bit...")
        	turn(-2, 0.5)
    	elif rot_y > a_th:
        	print("Right a bit...")
        	turn(+2, 0.5)

  if len(arr)==12:
    		
    		print("Well done assignment completed successfully")
    		exit()

