# import random 
class GameState:
    def __init__(self):
        self.map=[
            ["","","","","","","","",""],
            ["","r","k","b","q","g","b","k","r"],
            ["","p","p","p","p","p","p","p","p"],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","P","P","P","P","P","P","P","P"],
            ["","R","K","B","Q","G","B","K","R"],
            ]
        self.white_to_move = True
        # self.map[8][1:]
        # self.l=["R","K","B","Q","G","B","K","R"]
        # self.randomlist = random.sample(range(0, 8), 8)
        # for i in range(8):
        #     self.map[8][i]=self.l[self.randomlist[i]]
        # self.map[8][0]=""
    
    def move(self,sr, sc, er, ec):
        self.map[er][ec] = self.map[sr][sc] 
        self.map[sr][sc] = ""
        self.selected = []
        self.playerClicks = []
        self.white_to_move = not self.white_to_move
    
    def getPawnMoves(self,sr,sc,er,ec):
        if self.white_to_move==True:
            if sr == 2:
                if self.map[sr-1][sc]==""  and er==sr-1 and ec==sc:
                    self.move(sr,sc,er,ec) 
                    self.map[sr-1][sc]="Q"
                if self.map[sr-1][sc-1].islower() and self.map[sr-1][sc-1]!="" and er == sr-1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
                    self.map[sr-1][sc-1]="Q"
                elif self.map[sr-1][sc+1].islower() and self.map[sr-1][sc+1]!="" and er == sr-1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
                    self.map[sr-1][sc+1]="Q"
            if sr-1 >= 1:
                if self.map[sr-1][sc]=="" and er == sr-1 and ec == sc:
                    self.move(sr,sc,er,ec) 
            if sr-1 >= 1 and sc-1 >=1:
                if self.map[sr-1][sc-1].islower() and self.map[sr-1][sc-1]!="" and er == sr-1 and ec == sc-1:
                    self.move(sr,sc,er,ec) 
            if sr-1 >= 1 and sc+1 <=8:
                if self.map[sr-1][sc+1].islower() and self.map[sr-1][sc+1]!="" and er == sr-1 and ec == sc+1:
                    self.move(sr,sc,er,ec) 
            if sr == 7:
                for i in range(1,3):
                    if self.map[sr-i][sc]=="" and er == sr-i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc]!="":
                        break 
        else:
            if sr == 7:
                if self.map[sr+1][sc]==""  and er==sr+1 and ec==sc:
                    self.move(sr,sc,er,ec) 
                    self.map[sr+1][sc]="q"
                if self.map[sr+1][sc+1].isupper() and self.map[sr+1][sc+1]!="" and er == sr+1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
                    self.map[sr+1][sc+1]="q"
                elif self.map[sr+1][sc-1].isupper() and self.map[sr+1][sc-1]!="" and er == sr+1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
                    self.map[sr+1][sc-1]="q"
            if sr+1 <= 8:
                if self.map[sr+1][sc]=="" and er == sr+1 and ec == sc:
                    self.move(sr,sc,er,ec) 
            if sr+1 <= 8 and sc+1 <=8:
                if self.map[sr+1][sc+1].isupper() and self.map[sr+1][sc+1]!="" and er == sr+1 and ec == sc+1:
                    self.move(sr,sc,er,ec) 
            if sr+1 <= 8 and sc-1 >=1:
                if self.map[sr+1][sc-1].isupper() and self.map[sr+1][sc-1]!="" and er == sr+1 and ec == sc-1:
                    self.move(sr,sc,er,ec) 
            if sr == 2:
                for i in range(1,3):
                    if self.map[sr+i][sc]=="" and er == sr+i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc]!="":
                        break
    def getPawnWay(self,sr,sc):
        if self.white_to_move == True:
            if self.map[sr-1][sc]=="" and sr-1 >= 1:
                self.map[sr-1][sc]="M"
            if self.map[sr-1][sc]=="M" and sr-2 >= 1 and self.map[sr-2][sc]=="" and sr==7:
                self.map[sr-2][sc]="M"
        else:
            if self.map[sr+1][sc]=="" and sr+1 <= 8:
                self.map[sr+1][sc]="M"
            if self.map[sr+1][sc]=="M" and sr+2 <= 8 and self.map[sr+2][sc]=="" and sr==2:
                self.map[sr+2][sc]="M"

    def getRookMoves(self,sr, sc, er, ec):
        if self.white_to_move == True:
            for i in range(1,8):
                if sr-i >= 1:
                    if (self.map[sr-i][sc]=="" or (self.map[sr-i][sc].islower() and self.map[sr-i][sc]!="")) and er == sr-i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8:
                    if (self.map[sr+i][sc]=="" or (self.map[sr+i][sc].islower() and self.map[sr+i][sc]!="")) and er == sr+i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc]!="":
                        break
            for i in range(1,8):
                if sc-i >= 1:
                    if (self.map[sr][sc-i]=="" or (self.map[sr][sc-i].islower() and self.map[sr][sc-i]!="")) and er == sr and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr][sc-i]!="":
                        break
            for i in range(1,8):
                if sc+i <= 8:
                    if (self.map[sr][sc+i]=="" or (self.map[sr][sc+i].islower() and self.map[sr][sc+i]!="")) and er == sr and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr][sc+i]!="":
                        break
        else:
            for i in range(1,8):
                if sr-i >= 1 and sc >= 1:
                    if (self.map[sr-i][sc]=="" or (self.map[sr-i][sc].isupper() and self.map[sr-i][sc]!="")) and er == sr-i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8 and sc <= 8:
                    if (self.map[sr+i][sc]=="" or (self.map[sr+i][sc].isupper() and self.map[sr+i][sc]!="")) and er == sr+i and ec == sc:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc]!="":
                        break
            for i in range(1,8):
                if sr >= 1 and sc-i >= 1:
                    if (self.map[sr][sc-i]=="" or (self.map[sr][sc-i].isupper() and self.map[sr][sc-i]!="")) and er == sr and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr][sc-i]!="":
                        break
            for i in range(1,8):
                if sr <= 8 and sc+i <= 8:
                    if (self.map[sr][sc+i]=="" or (self.map[sr][sc+i].isupper() and self.map[sr][sc+i]!="")) and er == sr and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr][sc+i]!="":
                        break
    def getRookWay(self, sr, sc):
        for i in range(1,8):
            if sr-i >= 1:
                if self.map[sr-i][sc]=="":
                    self.map[sr-i][sc]="M"
                elif self.map[sr-i][sc]!="":
                    break  
        for i in range(1,8):
            if sr+i <= 8:
                if self.map[sr+i][sc]=="":
                    self.map[sr+i][sc]="M"
                elif self.map[sr+i][sc]!="":
                    break
        for i in range(1,8):
            if sc+i <= 8:
                if self.map[sr][sc+i]=="":
                    self.map[sr][sc+i]="M"
                elif self.map[sr][sc+i]!="":
                    break
        for i in range(1,8):
            if sc-i >= 1:
                if self.map[sr][sc-i]=="":
                    self.map[sr][sc-i]="M"
                elif self.map[sr][sc-i]!="":
                    break
    def getBishopMoves(self,sr, sc, er, ec):
        if self.white_to_move == True:
            for i in range(1,8):
                if sr-i >= 1 and sc+i <= 8:
                    if (self.map[sr-i][sc+i]=="" or (self.map[sr-i][sc+i].islower() and self.map[sr-i][sc+i]!="")) and er == sr-i and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc+i]!="":
                        break
            for i in range(1,8):
                if sr-i >= 1 and sc-i >= 1:
                    if (self.map[sr-i][sc-i]=="" or (self.map[sr-i][sc-i].islower() and self.map[sr-i][sc-i]!="")) and er == sr-i and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc-i]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8 and sc+i <= 8:
                    if (self.map[sr+i][sc+i]=="" or (self.map[sr+i][sc+i].islower() and self.map[sr+i][sc+i]!="")) and er == sr+i and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc+i]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8 and sc-i >= 1:
                    if (self.map[sr+i][sc-i]=="" or (self.map[sr+i][sc-i].islower() and self.map[sr+i][sc-i]!="")) and er == sr+i and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc-i]!="":
                        break
        else:
            for i in range(1,8):
                if sr-i >= 1 and sc+i <= 8:
                    if (self.map[sr-i][sc+i]=="" or (self.map[sr-i][sc+i].isupper() and self.map[sr-i][sc+i]!="")) and er == sr-i and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc+i]!="":
                        break
            for i in range(1,8):
                if sr-i >= 1 and sc-i >= 1:
                    if (self.map[sr-i][sc-i]=="" or (self.map[sr-i][sc-i].isupper() and self.map[sr-i][sc-i]!="")) and er == sr-i and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr-i][sc-i]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8 and sc+i <= 8:
                    if (self.map[sr+i][sc+i]=="" or (self.map[sr+i][sc+i].isupper() and self.map[sr+i][sc+i]!="")) and er == sr+i and ec == sc+i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc+i]!="":
                        break
            for i in range(1,8):
                if sr+i <= 8 and sc-i >= 1:
                    if (self.map[sr+i][sc-i]=="" or (self.map[sr+i][sc-i].isupper() and self.map[sr+i][sc-i]!="")) and er == sr+i and ec == sc-i:
                        self.move(sr,sc,er,ec)
                    elif self.map[sr+i][sc-i]!="":
                        break
    def getBishopWay(self, sr, sc):
        for i in range(1,8):
            if sr-i >= 1 and sc+i <=8:
                if self.map[sr-i][sc+i]=="":
                    self.map[sr-i][sc+i]="M"
                elif self.map[sr-i][sc+i]!="":
                    break  
        for i in range(1,8):
            if sr+i <= 8 and sc+i <=8:
                if self.map[sr+i][sc+i]=="":
                    self.map[sr+i][sc+i]="M"
                elif self.map[sr+i][sc+i]!="":
                    break
        for i in range(1,8):
            if sr+i <= 8 and sc-i >=1:
                if self.map[sr+i][sc-i]=="":
                    self.map[sr+i][sc-i]="M"
                elif self.map[sr+i][sc-i]!="":
                    break
        for i in range(1,8):
            if sr-i >= 1 and sc-i >=1:
                if self.map[sr-i][sc-i]=="":
                    self.map[sr-i][sc-i]="M"
                elif self.map[sr-i][sc-i]!="":
                    break
    def getQueenMoves(self, sr, sc, er, ec):
        self.getBishopMoves(sr,sc,er,ec)
        self.getRookMoves(sr,sc,er,ec)
    def getQueenWay(self, sr, sc):
        self.getBishopWay(sr,sc)
        self.getRookWay(sr,sc)
    def getKnightMoves(self, sr, sc, er, ec):
        if self.white_to_move == True:
            if sr-1 >= 1 and sc+2 <= 8:
                if (self.map[sr-1][sc+2]=="" or (self.map[sr-1][sc+2].islower() and self.map[sr-1][sc+2]!="")) and er == sr-1 and ec == sc+2:
                    self.move(sr,sc,er,ec) 
            if sr-2 >= 1 and sc+1 <= 8:
                if (self.map[sr-2][sc+1]=="" or (self.map[sr-2][sc+1].islower() and self.map[sr-2][sc+1]!="")) and er == sr-2 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1 and sc-2 >= 1:
                if (self.map[sr-1][sc-2]=="" or (self.map[sr-1][sc-2].islower() and self.map[sr-1][sc-2]!="")) and er == sr-1 and ec == sc-2:
                    self.move(sr,sc,er,ec) 
            if sr-2 >= 1 and sc-1 >= 1:
                if (self.map[sr-2][sc-1]=="" or (self.map[sr-2][sc-1].islower() and self.map[sr-2][sc-1]!="")) and er == sr-2 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc+2 <= 8:
                if (self.map[sr+1][sc+2]=="" or (self.map[sr+1][sc+2].islower() and self.map[sr+1][sc+2]!="")) and er == sr+1 and ec == sc+2:
                    self.move(sr,sc,er,ec) 
            if sr+2 <= 8 and sc+1 <= 8:
                 if (self.map[sr+2][sc+1]=="" or (self.map[sr+2][sc+1].islower() and self.map[sr+2][sc+1]!="")) and er == sr+2 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc-2 >= 1:
                if (self.map[sr+1][sc-2]=="" or (self.map[sr+1][sc-2].islower() and self.map[sr+1][sc-2]!="")) and er == sr+1 and ec == sc-2:
                    self.move(sr,sc,er,ec) 
            if sr+2 <= 8 and sc-1 >= 1:
                if (self.map[sr+2][sc-1]=="" or (self.map[sr+2][sc-1].islower() and self.map[sr+2][sc-1]!="")) and er == sr+2 and ec == sc-1:
                    self.move(sr,sc,er,ec)
        else:
            if sr-1 >= 1 and sc+2 <= 8:
                if (self.map[sr-1][sc+2]=="" or (self.map[sr-1][sc+2].isupper() and self.map[sr-1][sc+2]!="")) and er == sr-1 and ec == sc+2:
                    self.move(sr,sc,er,ec) 
            if sr-2 >= 1 and sc+1 <= 8:
                if (self.map[sr-2][sc+1]=="" or (self.map[sr-2][sc+1].isupper() and self.map[sr-2][sc+1]!="")) and er == sr-2 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1 and sc-2 <= 8:
                if (self.map[sr-1][sc-2]=="" or (self.map[sr-1][sc-2].isupper() and self.map[sr-1][sc-2]!="")) and er == sr-1 and ec == sc-2:
                    self.move(sr,sc,er,ec) 
            if sr-2 >= 1 and sc-1 <= 8:
                if (self.map[sr-2][sc-1]=="" or (self.map[sr-2][sc-1].isupper() and self.map[sr-2][sc-1]!="")) and er == sr-2 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc+2 <= 8:
                if (self.map[sr+1][sc+2]=="" or (self.map[sr+1][sc+2].isupper() and self.map[sr+1][sc+2]!="")) and er == sr+1 and ec == sc+2:
                    self.move(sr,sc,er,ec) 
            if sr+2 <= 8 and sc+1 <= 8:
                if (self.map[sr+2][sc+1]=="" or (self.map[sr+2][sc+1].isupper() and self.map[sr+2][sc+1]!="")) and er == sr+2 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr+1 >= 1 and sc-2 >= 1:
                if (self.map[sr+1][sc-2]=="" or (self.map[sr+1][sc-2].isupper() and self.map[sr+1][sc-2]!="")) and er == sr+1 and ec == sc-2:
                    self.move(sr,sc,er,ec) 
            if sr+2 <= 8 and sc-1 >= 1:
                 if (self.map[sr+2][sc-1]=="" or (self.map[sr+2][sc-1].isupper() and self.map[sr+2][sc-1]!="")) and er == sr+2 and ec == sc-1:
                    self.move(sr,sc,er,ec)
    def getKnightWay(self,sr,sc):
        if sr-1 >= 1 and sc+2 <=8:
            if self.map[sr-1][sc+2]=="":
                self.map[sr-1][sc+2]="M"  
        if sr-2 >= 1 and sc+1 <=8:
            if self.map[sr-2][sc+1]=="":
                self.map[sr-2][sc+1]="M"
        if sr-1 >= 1 and sc-2 >=1:
            if self.map[sr-1][sc-2]=="":
                self.map[sr-1][sc-2]="M"
        if sr-2 >= 1 and sc-1 >=1:
            if self.map[sr-2][sc-1]=="":
                self.map[sr-2][sc-1]="M"
        if sr+1 <= 8 and sc+2 <=8:
            if self.map[sr+1][sc+2]=="":
                self.map[sr+1][sc+2]="M"  
        if sr+2 <= 8 and sc+1 <=8:
            if self.map[sr+2][sc+1]=="":
                self.map[sr+2][sc+1]="M"
        if sr+1 <= 8 and sc-2 >=1:
            if self.map[sr+1][sc-2]=="":
                self.map[sr+1][sc-2]="M"
        if sr+2 <= 8 and sc-1 >=1:
            if self.map[sr+2][sc-1]=="":
                self.map[sr+2][sc-1]="M"
    def getKingMoves(self,sr,sc,er,ec,cnt):
        if self.white_to_move == True:
            if sr-1 >= 1 and sc+1 <= 8:
                if (self.map[sr-1][sc+1]=="" or (self.map[sr-1][sc+1].islower() and self.map[sr-1][sc+1]!="")) and er == sr-1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1:
                if (self.map[sr-1][sc]=="" or (self.map[sr-1][sc].islower() and self.map[sr-1][sc]!="")) and er == sr-1 and ec == sc:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1 and sc-1 >= 1:
                if (self.map[sr-1][sc-1]=="" or (self.map[sr-1][sc-1].islower() and self.map[sr-1][sc-1]!="")) and er == sr-1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sc-1 >= 1:
                if (self.map[sr][sc-1]=="" or (self.map[sr][sc-1].islower() and self.map[sr][sc-1]!="")) and er == sr and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sc+1 <= 8:
                if (self.map[sr][sc+1]=="" or (self.map[sr][sc+1].islower() and self.map[sr][sc+1]!="")) and er == sr and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8:
                if (self.map[sr+1][sc]=="" or (self.map[sr+1][sc].islower() and self.map[sr+1][sc]!="")) and er == sr+1 and ec == sc:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc-1 >= 1:
                if (self.map[sr+1][sc-1]=="" or (self.map[sr+1][sc-1].islower() and self.map[sr+1][sc-1]!="")) and er == sr+1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc+1 <= 8:
                if (self.map[sr+1][sc+1]=="" or (self.map[sr+1][sc+1].islower() and self.map[sr+1][sc+1]!="")) and er == sr+1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr==8 and sc==5 and cnt==1:
                if self.map[sr][sc+1]=="" and self.map[sr][sc+2]=="" and self.map[sr][sc+3]=="R" and er == sr and ec == sc+2:
                    self.move(sr,sc,er,ec)
                    self.map[sr][sc+1] = "R"
                    self.map[sr][sc+3] = ""
                if self.map[sr][sc-1]=="" and self.map[sr][sc-2]=="" and self.map[sr][sc-3]=="" and self.map[sr][sc-4]=="R" and er == sr and ec == sc-2:
                    self.move(sr,sc,er,ec)
                    self.map[sr][sc-1] = "R"
                    self.map[sr][sc-4] = ""
        else:
            if sr-1 >= 1 and sc+1 <= 8:
                if (self.map[sr-1][sc+1]=="" or (self.map[sr-1][sc+1].isupper() and self.map[sr-1][sc+1]!="")) and er == sr-1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1:
                if (self.map[sr-1][sc]=="" or (self.map[sr-1][sc].isupper() and self.map[sr-1][sc]!="")) and er == sr-1 and ec == sc:
                    self.move(sr,sc,er,ec)
            if sr-1 >= 1 and sc-1 >= 1:
                if (self.map[sr-1][sc+1]=="" or (self.map[sr-1][sc-1].isupper() and self.map[sr-1][sc-1]!="")) and er == sr-1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sc-1 >= 1:
                if (self.map[sr][sc-1]=="" or (self.map[sr][sc-1].isupper() and self.map[sr][sc-1]!="")) and er == sr and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sc+1 <= 8:
                if (self.map[sr][sc+1]=="" or (self.map[sr][sc+1].isupper() and self.map[sr][sc+1]!="")) and er == sr and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8:
                if (self.map[sr+1][sc]=="" or (self.map[sr+1][sc].isupper() and self.map[sr+1][sc]!="")) and er == sr+1 and ec == sc:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc-1 >= 1:
                if (self.map[sr+1][sc-1]=="" or (self.map[sr+1][sc-1].isupper() and self.map[sr+1][sc-1]!="")) and er == sr+1 and ec == sc-1:
                    self.move(sr,sc,er,ec)
            if sr+1 <= 8 and sc+1 <= 8:
                if (self.map[sr+1][sc+1]=="" or (self.map[sr+1][sc+1].isupper() and self.map[sr+1][sc+1]!="")) and er == sr+1 and ec == sc+1:
                    self.move(sr,sc,er,ec)
            if sr==1 and sc==5 and cnt==1:
                if self.map[sr][sc+1]=="" and self.map[sr][sc+2]=="" and self.map[sr][sc+3]=="r" and er == sr and ec == sc+2:
                    self.move(sr,sc,er,ec)
                    self.map[sr][sc+1] = "r"
                    self.map[sr][sc+3] = ""
                if self.map[sr][sc-1]=="" and self.map[sr][sc-2]=="" and self.map[sr][sc-3]=="" and self.map[sr][sc-4]=="r" and er == sr and ec == sc-2:
                    self.move(sr,sc,er,ec)
                    self.map[sr][sc-1] = "r"
                    self.map[sr][sc-4] = ""
    def getKingWay(self,sr,sc):
        if sr-1 >= 1 and sc+1 <=8:
            if self.map[sr-1][sc+1]=="":
                self.map[sr-1][sc+1]="M"  
        if sr-1 >= 1:
            if self.map[sr-1][sc]=="":
                self.map[sr-1][sc]="M"
        if sr-1 >= 1 and sc-1 >=1:
            if self.map[sr-1][sc-1]=="":
                self.map[sr-1][sc-1]="M"
        if sc-1 >=1:
            if self.map[sr][sc-1]=="":
                self.map[sr][sc-1]="M"
        if sc+1 <=8:
            if self.map[sr][sc+1]=="":
                self.map[sr][sc+1]="M"  
        if sr+1 <= 8:
            if self.map[sr+1][sc]=="":
                self.map[sr+1][sc]="M"
        if sr+1 <= 8 and sc-1 >=1:
            if self.map[sr+1][sc-1]=="":
                self.map[sr+1][sc-1]="M"
        if sr+1 <= 8 and sc+1 <=8:
            if self.map[sr+1][sc+1]=="":
                self.map[sr+1][sc+1]="M"

                