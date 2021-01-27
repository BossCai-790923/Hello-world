import turtle
import time
import random
fleet=[]
fleetxy=[0,0,0,0,0]
enemy=[]
enemyxy=[800,800,800,800,800]
x=[0,0,0,0,0]
win=0
attack=True
line=turtle.Pen()
line.speed(0)
for i in range(7):
    line.up()
    line.goto(-500,300-100*i)
    line.down()
    line.fd(1000)
line.up()
line.ht()

for i in range(5):
    t=turtle.Pen()
    t.shape("turtle")
    t.color("red")
    t.up()
    t.speed(0)
    t.goto(-400+200*i,400)
    t.down()
    t.rt(90)
    t.speed(3)
    enemy.append(t)
    
for i in range(5):
    t=turtle.Pen()
    t.shape("triangle")
    t.color("blue")
    t.up()
    t.speed(0)
    t.goto(-400+200*i,-400)
    t.down()
    t.lt(90)
    t.speed(3)
    fleet.append(t)
    
while attack:
    for i in range(5):
        x[i]=int(input())
    for i in range(5):
        if x[i]==1:
            fleet[i].fd(100)
            fleetxy[i]+=100
    for i in range(5):
        if enemyxy[i]-fleetxy[i]==100:
            win+=1
    if win==5:
        line.goto(0,0)
        line.color("red")
        line.write("WIN", font=("Arial", 50), align="center")
        break
    for i in range(5):
        x=random.randint(0,1)
        if x==1:
            enemy[i].fd(100)
            enemyxy[i]-=100
    for i in range(5):
        if fleetxy[i]==enemyxy[i]:
            line.goto(0,0)
            line.color("blue")
            line.write("LOSE", font=("Arial", 50), align="center")
            attack=False
            break
    x=[0,0,0,0,0]
    win=0
time.sleep(10)