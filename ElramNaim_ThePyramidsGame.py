import pygame
import random


gridDisplay = pygame.display.set_mode((400, 400)) #size of board
screen=pygame.display.get_surface().fill((200, 200, 200))  # background of board

#flip the matrix upside down
def changerows(x):
    temp1=matrix[len(matrix)-x-1]
    temp2=matrix[x]
    matrix[x]=temp1
    matrix[len(matrix)-x-1]=temp2

def createSquare(x, y, color):
         pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])

def displayChanges():#changes according to the rules
    isyellow=0
    for i in range(len(matrix)):
       is4yellow=0
       for j in range(len(matrix[i])):
        # if yellow add one to counter
         if matrix[i][j]==2:
            is4yellow+=1
        # if blue check if the position is legal
         if matrix[i][j]==0:
            if i==0:
                randcolr=random.choice(colors)
                matrix[i][j]=randcolr
            if i==j or len(matrix[0])-i==j:
                randcolr=random.choice(colors)
                matrix[i][j]=randcolr
         # if pink check if the position is legal
         if matrix[i][j]==1:
           #stay in the range
           if(i+1<len(matrix)):
            #If there is blue above it
             if(matrix[i+1][j]==0):
               randcolr=random.choice(colors)
               matrix[i][j]=randcolr
            #stay in the range
           if j-1>=0:  
            #If there is blue on the left 
             if(matrix[i][j-1]==0):
               randcolr=random.choice(colors)
               matrix[i][j]=randcolr
             #stay in the range
           if j+1<len(matrix[0]):   
             #If there is blue on the right 
             if(matrix[i][j+1]==0):
               randcolr=random.choice(colors)
               matrix[i][j]=randcolr
            #stay in the range 
           if i-1>=0:
            #If there is blue underneath
             if(matrix[i-1][j]==0):
               randcolr=random.choice(colors)
               matrix[i][j]=randcolr
         if matrix[i][j]==" ":
            matrix[i][j]=" "
         #If there are four or more yellows in a row, change the whole row
         if is4yellow>=4:
            for k in range(len(matrix[i])):
               randcolr=random.choice(colors)
               matrix[i][k]=randcolr
         


rows = 5
cols = 9
colors=[0,1,2]
    #initialization empty matrix
matrix = [[" "]*cols for _ in range(rows)]

  #initialization statring matrix
for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if i==0:
            randcolr=random.choice(colors)
            matrix[i][j]=randcolr
        if (i<=j) and i+j<len(matrix[0]) and i>0:
             randcolr=random.choice(colors)
             matrix[i][j]=randcolr
         
#for the display flip the matrix
for x in range(round(len(matrix)/2)):
    changerows(x)

#size of each cell
grid_node_width = 40  
grid_node_height = 40


def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, ("blue"))
            elif item==1:
                createSquare(x, y, ("pink"))
            elif item==2:
             createSquare(x, y, ("yellow"))
            else:
                createSquare(x, y, ("white"))

            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.flip()
    pygame.time.wait(5000)
    

#play until press quit
gameExit=False
while not gameExit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
    visualizeGrid()  # call the function   
    displayChanges()
