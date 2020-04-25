from imagesearch import *

#Sweeper Square size
ipx = 16

#Border thickness
iDistToOneOne = 10

def main():
    x=0
    global iDistToOneOne


    while x<1:
        play()
        restart()
        x+=1
        

def play():
    #Is gameover
    pos2 = imagesearch("dead.png")

    #if not gameover
    while pos2[0] == -1:
        #Get unclicked square
        pos = imagesearch("onesquare.png")
        #if unclicked exist
        if pos[0] != -1:
            #debugprint pos
            print("positon : ", pos[0], pos[1])
            #Move to it and click it
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0]+3,pos[1]+3, 2, 0, 'left')
            #see if that killed you
            pos2 = imagesearch("dead.png")
        #if not...
        else:
            print("image not found")

def restart():
    pos2 = imagesearch("dead.png")
    pyautogui.click(pos2[0]+2, pos2[1]+2)

main()