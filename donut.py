'''lets start by creating our pygame window'''
#import pygame library
import pygame
import math
import colorsys
#initialize the pygame library
pygame.init()
white=(255,255,255)
black=(0,0,0)
#set python window size
width=1920
height=1080 
x_start,y_start=0,0
x_separator=10
y_separator=20
rows=height//y_separator
columns=width// x_separator
screen_size=rows*columns
x_offset=columns/2
y_offset=rows/2
A,B =0,0 #rotation animation
theta_spacing=10
phi_spacing=1
char=".,-~:;=!#$@" #luminance index
#create a screen for the pygame window
screen=pygame.display.set_mode((width,height))
#fullscreen instead of predefined width and height
display_surface=pygame.display.set_mode((width,height))
# display_surface=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#set caption for our display window
pygame.display.set_caption('donut')
#since drawing donut will require use of ascii characters set a font
font=pygame.font.SysFont('Arial',18,bold=True)
#text display function with parameters  one for charcter and another for coordinates
def text_display(letter, x_start,y_start):
#for character to appear on a screen you have to render it 
   text=font.render(str(letter),True,white)
   #blit our text in certain positions defines by coordinates
   display_surface.blit(text,(x_start,y_start))


# because pygame is run in a while loop 
run=True
while run:
   screen.fill((black))
   z=[0]*screen_size #Donut.Fills the donut space 
   b=[""]*screen_size#Background.Fills the empty space
   for j in range(0, 628, theta_spacing):
    for i in range(0, 628, phi_spacing):
     c=math.sin(i)
     d=math.cos(j)
     e=math.sin(A)
     f=math.sin(j)
     g=math.cos(A)
     h=d+2
     D=1/(c*h*e+f*g+5)
     l=math.cos(i)
     m=math.cos(B)
     n=math.sin(B)
     t=c*h*g-f*e
     x = int(x_offset + 40 * D * (l * h * m - t * n))# 3d x coordiantes after rotation
     y = int(y_offset + 20 * D * (l * h * n + t * m))# 3d x coordiantes after rotatio
     o=int(x+columns*y) # 3d z coordinate after rotation
     N=int(8*((f *e-c *d*g) *m -c *d *e -f * g -l * d*e-f*g-l*d*n))
     if rows > y and y>0 and x>0 and columns >x and D>z[o]:
      z[o]=D
      b[o] = [N if N > 0 else 0]
   if (y_start == rows*y_separator-y_separator) :
    y_start=0
   for i in range (len(b)):
     A+=0.000002
     B+=0.000001
     if i == 0 or i % columns :
       text_display(b[i],x_start,y_start)
       x_start+=x_separator
     else:
       y_start+=y_separator
       x_start=0
       text_display(b[i],x_start,y_start)   
       x_start+=x_separator
         
   
   pygame.display.update()
   
   for event in pygame.event.get():
    if event.type==pygame.QUIT:
     run=False
   
   

