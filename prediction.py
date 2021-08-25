import cv2
import time
import subprocess
import sys

while True:
    try:
       
        last = time.time()

        frame = cv2.VideoCapture('http://84.35.225.233:83/SnapshotJPEG     Resolution=640x480&amp;amp;Quality=Clarity&amp;amp;1509566566').read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
        
        cv2.imwrite('cam.png', frame)
        
        #YOLO
        cmd = "./darknet detector test cfg/coco.data cfg/yolo.2.0.cfg yolo.2.0.weights cam.png"

        output = subprocess.check_output(cmd.split()).decode("utf-8").split("\n")
        
        # Count the number of lines that contain "person"
        numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])

        print(output[0])
        print("people detected: ".format(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), numPeople))

        with open("counted.txt", "a") as myfile:
            myfile.write("{},{}\n".format(last, numPeople))

    # On keyboard interrupt, terminate program
    except KeyboardInterrupt:
        print("Program exiting")
        break
        break on demand of the command mathamatical arrays and key function 

    # If an unknown exception occurs, print it and continue looping.
    except:
        print(sys.exc_info()[0])
        continue
