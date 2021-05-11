import turtle
import time
import random

sc=turtle.Screen()
sc.setup(420,420)
# Defining Turtle instance
t=turtle.Turtle()
t.hideturtle()
# setting up turtle color to green
t.color("Red")
# Setting Up width to 2
t.width("2")
# Setting up speed to 0 for fastest
t.speed(0)

def buildBoard():
  x=-150
  y=-150
  t.penup()
  t.goto(x,y)
  t.pendown()
  for num in range (4):
    t.forward(300)
    t.left(90)

  for i in range(4):
    y+=75
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(300)
  
  t.right(90)

  for z in range(4):
    x+=75
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(300)
  
  t.penup()
  t.goto(-120,-185)
  t.write("CLICK TO PLAY!",font= ("Verdana",20,"bold"))

buildBoard()

centerGridPos = [(-113,108),(-40,108),(30,107),(110,109),
  (-114,36),(-45,34),(39,33),(110,39),
  (-111,-40),(-42,-40),(36,-39),(108,-40),
  (-113,-112),(-40,-116),(33,-117),(107,-114)
]

first_card = -1
second_card = -1
tempPen = ""
matches = 0

def check_win():
  if(matches == 8):
    winPen = turtle.Turtle() 
    winPen.hideturtle()
    winPen.color("green")
    winPen.penup()
    winPen.goto(-80,165)
    winPen.write("YOU WIN!",font= ("Verdana",20,"bold"))

def check_card(click):
  global first_card,second_card, tempPen, matches
   
  if first_card == -1:
    tempPen = turtle.Turtle()
    tempPen.hideturtle()
    tempPen.penup()
    first_card = click
    tempPen.goto(centerGridPos[click])
    tempPen.write(deck[click]) 
  elif second_card == -1 and click != first_card:
    second_card = click
    tempPen.goto(centerGridPos[click])
    tempPen.write(deck[click])
    time.sleep(2)
    if deck[first_card] is not deck[second_card]:
      tempPen.clear()
    else:
      matches +=1
      check_win()
    first_card = -1
    second_card = -1
 
  


def zoneDetect(x,y): 
  #print(x,y)
  if (x >-150 and x<-75) and (y>75 and y<150):
    check_card(0)
  if (x >-75 and x<-0) and (y>75 and y<150):
    check_card(1)
  if (x >0 and x<75) and (y>75 and y<150):
    check_card(2)
  if (x >75 and x<150) and (y>75 and y<150):
    check_card(3)
  
  if (x >-150 and x<-75) and (y>0 and y<75):
    check_card(4)
  if (x >-75 and x<-0) and (y>0 and y<75):
    check_card(5)
  if (x >0 and x<75) and (y>0 and y<75):
    check_card(6)
  if (x >75 and x<150) and (y>0 and y<75):
    check_card(7)

  if (x >-150 and x<-75) and (y>-75 and y<0):
    check_card(8)
  if (x >-75 and x<-0) and (y>-75 and y<0):
    check_card(9)
  if (x >0 and x<75) and (y>-75 and y<0):
    check_card(10)
  if (x >75 and x<150) and (y>-75 and y<0):
    check_card(11)

  if (x >-150 and x<-75) and (y>-150 and y<-75):
    check_card(12)
  if (x >-75 and x<-0) and (y>-150 and y<-75):
    check_card(13)
  if (x >0 and x<75) and (y>-150 and y<-75):
    check_card(14)
  if (x >75 and x<150) and (y>-150 and y<-75):
    check_card(15)

turtle.onscreenclick(zoneDetect)

deck = []
def create_deck():
    for i in range(2):
        deck.append("A")
        deck.append("B")
        deck.append("C")
        deck.append("D")
        deck.append("E")
        deck.append("F")
        deck.append("G")
        deck.append("H")
create_deck()

def shuffle_deck():
    for i in range(len(deck) - 1):
        temp = deck[i]
        rand = random.randint(i + 1, len(deck) - 1)
        deck[i] = deck[rand]
        deck[rand] = temp
shuffle_deck()
