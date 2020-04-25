from imagesearch import *
from block import *

iWidth = 16

upperOffset = 8
lowerOffset = 0

numSquaresX=0
numSquaresY=0

blockGrid=[]

def main():
    
    squares = findBox()
    genGrid(squares)
    print(squares)

    ###DEBUG
    global blockGrid
    a=(blockGrid[5][5]).lBoardPos
    pyautogui.moveTo(a[0]+2,a[1]+2)

    ##
    x=1
    while x<1:
        play()
        restart()
        x+=1


def genGrid(sweeperxy):
    #creates a grid of "box"
    global numSquaresX
    global numSquaresY
    grid = []
    for x in range(int(numSquaresX)):
        row = []
        for y in range(int(numSquaresY)):
            block = Block([x,y],[sweeperxy[0]+x*16,sweeperxy[1]+y*16],blockVal.unk)
            row.append(block)
        grid.append(row)
    global blockGrid
    blockGrid=grid
    print(grid[0])
    printer(grid)

def printer(gr):
    
    for x in range(0,len(gr)):
        strout = ""
        for y in range(0,len(gr[x])):
            cds = (gr[x][y]).lPxCrds
            #print (cds)
            strout += " ["+str(cds[0])+", "+str(cds[1])+"] |"
        print(strout)
            


#Returns [TopLeftCoord] of minesweeper
#Assigns value to numSquaresX and numSquaresY
def findBox():
    
    #25x25
    #block starts at 8,8
    topLeftCoord = imagesearch("findUpperleft.png")
    firstSquare = [0,0]
    firstSquare[0] = topLeftCoord[0] + 8
    firstSquare[1] = topLeftCoord[1] + 8
   
    #24x24
    #block ends at 15,15
    botRightCoords = imagesearch("findBottomRight.png")
    lastSquare = [0,0]
    lastSquare[0] = botRightCoords[0]+15
    lastSquare[1] = botRightCoords[1]+15

            #Returns [[TopLeftCoord],[xwidth,ywidth]]
    retval = calcBox(firstSquare,lastSquare)
   
    global numSquaresX 
    numSquaresX = retval[0] /16
    print ("numSquaresX",numSquaresX)
   
    global numSquaresY 
    numSquaresY = retval[1] /16
    print ("numSquaresY",numSquaresY)

    return firstSquare




#Returns [[TopLeftCoord],[xwidth,ywidth]]
def calcBox(fSq,lSq):
    ##0,0
    ##144,144
    x = lSq[0]-fSq[0]
    y = lSq[1]-fSq[1]
    print("Minesweeper located at",fSq[0],fSq[1])
    return [x,y]


def play():
    pos2 = imagesearch("dead.png")
    while pos2[0] == -1:
        pos = imagesearch("onesquare.png")
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(pos[0]+3,pos[1]+3, 2, 0, 'left')
            pos2 = imagesearch("dead.png")
        else:
            print("image not found")

def restart():
    pos2 = imagesearch("dead.png")
    pyautogui.click(pos2[0]+2, pos2[1]+2)

main()