import turtle
import random
import time

### CLASSES ###

def outline():
    outline=turtle.Turtle()
    outline.ht()
    outline.speed('fastest')
    outline.color('white')
    outline.pu()
    outline.goto(x=-320,y=-210)
    outline.pd()
    for i in range(2):
        outline.fd(640)
        outline.lt(90)
        outline.fd(360)
        outline.lt(90)
    for i in range(6):    
        outline.fd(640)
        outline.lt(90)
        outline.fd(60)
        outline.lt(90)
        outline.fd(640)
        outline.rt(180)
    outline.fd(630)
    outline.rt(90)
    outline.color('red')
    outline.fd(360)
    outline.rt(90)
    outline.color('white')
    outline.fd(630)
    outline.rt(90)
    outline.color('green')
    outline.fd(360)

### MAIN ###

while True:
    scr=turtle.Screen()
    scr.title(titlestring='Turtle race')
    scr.screensize(canvheight=400,canvwidth=500)
    scr.bgcolor('black')
    trtlist=[]
    colors=['red','orange','white','blue','green','indigo']
    ycordinates=[-180,-120,-60,0,60,120]
    f=scr.textinput(title=' who will win ?',prompt='\navailable colors :\n\'red\',\'orange\',\'white\',\'blue\',\'green\',\'indigo\'\n\nguess which color will win ?\n\n')
    scr.bgpic('nopic')
    if f.lower() in colors:
        outline()
        time.sleep(0.5)
        for i in range(6):
            new_guy=turtle.Turtle(shape='turtle')
            new_guy.pu()
            new_guy.color(colors[i])
            new_guy.goto(x=-320,y=ycordinates[i])
            trtlist.append(new_guy)
        d=True
        l=None
        while d:
            for i in trtlist:
                if i.xcor() > 285:
                    winner=i.color()
                    l=True
                    break
                else:
                    randomdist=random.randint(1,8)
                    i.fd(randomdist)
                    l=False
            if l:
                d=False
        else:
            time.sleep(1.5)
            turtle.ht()
            turtle.bgcolor('black')
            turtle.color('white')
            if f.lower() == winner[1]:
                turtle.write('your guess was correct !',font=("Verdana",15, "bold"),align='center')
            else:
                turtle.write(f'your guess was wrong ! {winner[1]} won',font=("Verdana",15, "bold"),align='center')
            time.sleep(3)
            scr.clearscreen()
            scr.bgcolor('black')
            j=scr.textinput(title='retry ?',prompt='do you want to try again ?\n(y/n)')
            if j.lower()=='y':
                pass
            elif j.lower()=='n':
                turtle.ht()
                turtle.color('white')
                turtle.write('program over .',font=("Verdana",15, "bold"),align='center')
                time.sleep(2)
                exit(0)
            else:
                turtle.ht()
                turtle.color('white')
                turtle.write('invalid input !\n\nprogram over',font=("Verdana",15, "bold"),align='center')
                time.sleep(2)
                exit(0)
    else:
        scr.bgpic('nopic')
        turtle.color('white')
        turtle.ht()
        turtle.write(' invalid input !',font=("Verdana",15, "bold"),align='center')
        time.sleep(1.5)
        turtle.clear()
time.sleep(3)

### END ###


