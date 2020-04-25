from enum import Enum

class blockVal(Enum):
    unk = ' '
    empty = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five ='5'  
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    flag = 'f'

class Block:
    lPxCrds=[0,0]
    lBoardPos=[0,0]
    sVal = blockVal.unk

    def __init__(self,pxCrds,boardPos,val):
        self.lPxCrds=pxCrds
        self.lBoardPos=boardPos
        self.sVal=val

    