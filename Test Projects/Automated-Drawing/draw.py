import pyautogui as pgu
import time

# print(pgu.size())

time.sleep(0.2)
# print(pgu.position()) #testing purposes

#Move mouse 
pgu.click(1566,47,1,0.2,button="left") #(x,y,number_of_clicks,click in duration,button)
pgu.click(1268,9,1,0.2,button="left")
pgu.moveTo(243,294,0.3) #starting point
time.sleep(1)
distance = 500
while distance > 0:
    pgu.dragRel(distance,0,0.1 ,button = "left")
    distance = distance - 15
    pgu.dragRel(0,distance,0.1 ,button = "left")
    pgu.dragRel(-distance,0,0.1 ,button = "left")
    distance = distance - 15
    pgu.dragRel(0,-distance,0.1 ,button = "left")
time.sleep(0.2)
pgu.click(491,3,1,0.2,button = "left")
pgu.moveTo(841,497)