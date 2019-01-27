"""
Maze

Description:
"""
import pygame 
pygame.init()
w=pygame.display.set_mode([520,520])
g=(40, 114, 33)
b=60
c=20
turns=0
a=b,c
pygame.draw.polygon(w,g,[(40,40),(80,40),(80,120),(120,120),(120,80),(120,120),(160,120),(160,200),(120,200),(120,240),(200,240),(200,40),(120,40),(160,40),(160,80),(160,40),(200,40),(200,240),(120,240),(120,280),(80,280),(120,280),(120,320),(40,320),(40,400),(0,400),(40,400),(40,240),(80,240),(80,200),(80,240),(40,240),(40,320),(240,320),(240,280),(160,280),(240,280),(240,360),(240,360),(280,360),(280,440),(240,440),(280,440),(280,480),(40,480),(200,480),(200,360),(200,400),(80,400),(80,440),(40,440),(160,440),(80,440),(80,400),(240,400),(200,400),(200,480),(280,480),(280,400),(360,400),(360,440),(320,440),(440,440),(440,400),(440,440),(360,440),(360,360),(400,360),(400,400),(400,360),(440,360),(440,320),(440,360),(360,360),(360,440),(400,440),(400,480),(480,480),(480,280),(440,280),(440,240),(400,240),(400,200),(400,240),(440,240),(440,280),(480,280),(480,480),(400,480),(400,440),(360,440),(360,400),(280,400),(280,360),(240,360),(240,320),(120,320),(120,200),(160,200),(160,120),(80,120),(80,40),(40,40)],5)
pygame.draw.line(w,g,(40,80),(0,80),6)
pygame.draw.polygon(w,g,[(0,200),(40,200),(40,120),(40,160),(120,160),(40,160),(40,200),(0,200)],5)
pygame.draw.line(w,g,(320,520),(320,480),6)
pygame.draw.line(w,g,(360,520),(360,480),6)
pygame.draw.polygon(w,g,[(0,240),(40,240),(40,280),(40,240),(0,240)],5)
pygame.draw.polygon(w,g,[(520,160),(480,160),(480,120),(440,120),(480,120),(480,40),(440,40),(480,40),(480,160),(520,160)],5)
pygame.draw.polygon(w,g,[(400,0),(400,120),(400,80),(440,80),(320,80),(320,40),(360,40),(320,40),(320,80),(240,80),(240,160),(240,80),(400,80),(400,0)],5)
pygame.draw.polygon(w,g,[(520,240),(480,240),(480,200),(440,200),(440,160),(360,160),(360,120),(280,120),(320,120),(320,280),(320,120),(360,120),(360,280),(400,280),(400,320),(320,320),(320,360),(320,320),(280,320),(280,240),(240,240),(280,240),(280,200),(240,200),(280,200),(280,160),(280,320),(400,320),(400,280),(360,280),(360,160),(440,160),(440,200),(480,200),(480,240),(520,240)],5)
pygame.draw.line(w,(255,0,0),(0,520),(40,520),10)
pygame.draw.line(w,(255,0,0),(40,0),(80,0),10)
pygame.draw.circle(w,(0,0,255),(a),20)
pygame.display.flip()
win=False
while not win:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                c-=40
                if c < 0:
                    c=20
                else:
                    turns+=1
            elif event.key == pygame.K_DOWN:
                c+=40
                if c > 480:
                    c=500
                else:
                    turns+=1
            elif event.key == pygame.K_LEFT:
                b-=40
                if b < 0:
                    b=20
                else:
                    turns+=1
            elif event.key == pygame.K_RIGHT:
                b+=40
                if b > 500:
                    b=500
                else:
                    turns+=1
    w.fill([255,255,255])
    a=b,c
    if a == (20,500):
        win=True
    pygame.draw.polygon(w,g,[(40,40),(80,40),(80,120),(120,120),(120,80),(120,120),(160,120),(160,200),(120,200),(120,240),(200,240),(200,40),(120,40),(160,40),(160,80),(160,40),(200,40),(200,240),(120,240),(120,280),(80,280),(120,280),(120,320),(40,320),(40,400),(0,400),(40,400),(40,240),(80,240),(80,200),(80,240),(40,240),(40,320),(240,320),(240,280),(160,280),(240,280),(240,360),(240,360),(280,360),(280,440),(240,440),(280,440),(280,480),(40,480),(200,480),(200,360),(200,400),(80,400),(80,440),(40,440),(160,440),(80,440),(80,400),(240,400),(200,400),(200,480),(280,480),(280,400),(360,400),(360,440),(320,440),(440,440),(440,400),(440,440),(360,440),(360,360),(400,360),(400,400),(400,360),(440,360),(440,320),(440,360),(360,360),(360,440),(400,440),(400,480),(480,480),(480,280),(440,280),(440,240),(400,240),(400,200),(400,240),(440,240),(440,280),(480,280),(480,480),(400,480),(400,440),(360,440),(360,400),(280,400),(280,360),(240,360),(240,320),(120,320),(120,200),(160,200),(160,120),(80,120),(80,40),(40,40)],5)
    pygame.draw.line(w,g,(40,80),(0,80),6)
    pygame.draw.polygon(w,g,[(0,200),(40,200),(40,120),(40,160),(120,160),(40,160),(40,200),(0,200)],5)
    pygame.draw.line(w,g,(320,520),(320,480),6)
    pygame.draw.line(w,g,(360,520),(360,480),6)
    pygame.draw.polygon(w,g,[(0,240),(40,240),(40,280),(40,240),(0,240)],5)
    pygame.draw.polygon(w,g,[(520,160),(480,160),(480,120),(440,120),(480,120),(480,40),(440,40),(480,40),(480,160),(520,160)],5)
    pygame.draw.polygon(w,g,[(400,0),(400,120),(400,80),(440,80),(320,80),(320,40),(360,40),(320,40),(320,80),(240,80),(240,160),(240,80),(400,80),(400,0)],5)
    pygame.draw.polygon(w,g,[(520,240),(480,240),(480,200),(440,200),(440,160),(360,160),(360,120),(280,120),(320,120),(320,280),(320,120),(360,120),(360,280),(400,280),(400,320),(320,320),(320,360),(320,320),(280,320),(280,240),(240,240),(280,240),(280,200),(240,200),(280,200),(280,160),(280,320),(400,320),(400,280),(360,280),(360,160),(440,160),(440,200),(480,200),(480,240),(520,240)],5)
    pygame.draw.line(w,(255,0,0),(0,520),(40,520),10)
    pygame.draw.line(w,(255,0,0),(40,0),(80,0),10)
    pygame.draw.circle(w,(0,0,255),(a),20)
    pygame.display.flip()
if b == 20 and c == 500:
    print("You made it!!!")
    print("It took you " +str(turns) +" turns.")
else:
    print("Better luck next time.")