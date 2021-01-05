##Friday2.0 revamping##

import speech_recognition as sr
import pyttsx3
import wikipedia
import pygame
import os
import datetime

# The Loading Screen
#os.system("python GIF.py")


#Colors
BLACK = ( 0, 0, 0)
GREEN = ( 0, 255, 0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
ORANGE = ( 255, 115, 0)
YELLOW = ( 242, 255, 0)
BROWN = ( 115, 87, 39)
PURPLE = ( 298, 0, 247)
GRAY = (168, 168, 168)
PINK = ( 255, 0, 234)
pygame.init()
#The Screen
screen = pygame.display.set_mode([1280,720], pygame.FULLSCREEN)
#Name of the window
pygame.display.set_caption("Friday MK:2")
#Pygame Clock
clock = pygame.time.Clock()

# Positions of graphics
background_position = [0,0]

#Loading The Background
background_image = pygame.image.load("background.jpg")

#The Function How The System speaks
def say(word):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(word)
    engine.runAndWait()
#This Function Understands Speech and turns it into text
def speechtext():
    rc = sr.Recognizer()
    with sr.Microphone() as source:
        rc.adjust_for_ambient_noise(source)
        audio = rc.listen(source)
    try:
        command = rc.recognize_google(audio)
    except sr.UnknownValueError:
        speechtext()

    return command
# this search's the wikipedia for a specific word
def searchwiki(srch):
    search = wikipedia.summary(srch, sentences=1)
    print(search)
    say(search)
    return search

#this class creats a button
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textcolor = (255,255,255)
        self.fontsize = 50
        self.text = text
    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.fontsize)
            text = font.render(self.text, 1, self.textcolor)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
def redrawWindow(bt):

    bt.draw(screen, [0,0,0])

done = True
Button = button((131,139,139), 0, 130, 175, 50, 'Opera')
Button1 = button((131,139,139), 0, 200, 175, 50, 'PyCharm')
Button1.fontsize = 45
Button2 = button((131,139,139), 0, 270, 175, 50, 'Fortnite')
Button3 = button((131,139,139), 0, 340, 175, 50, 'PUBG')
Button4 = button((131,139,139), 0, 410, 175, 50, 'Utorrent')
Button5 = button((131,139,139), 465, 565, 70, 30, 'Documents')
Button5.fontsize = 20
Button6 = button((131,139,139), 755, 565, 70, 30, 'Music')
Button6.fontsize = 20
Button7 = button((131,139,139), 507, 600, 70, 30, 'User')
Button7.fontsize = 20
Button8 = button((131,139,139), 537, 633, 70, 30, 'Pictures')
Button8.fontsize = 20
Button9 = button((131,139,139), 612, 645, 70, 30, 'Downloads')
Button9.fontsize = 20
Button10 = button((131,139,139), 687, 633, 70, 30, 'Facebook')
Button10.fontsize = 20
Button11 = button((131,139,139), 720, 600, 70, 30, 'Youtube')
Button11.fontsize = 20
Button12 = button((BLACK), 300, 100, 90, 40, 'QUIT')

now = datetime.datetime.now()
currentdate = now.strftime("%d")
str(currentdate)
currentmonth = now.strftime("%B")
currentday = now.strftime("%A")

pygame.font.init()
#Fonts and their Sizes
myfont = pygame.font.SysFont('Inconsolata', 100)
myfont1 = pygame.font.SysFont('Inconsolata', 20)
myfont2 = pygame.font.SysFont('Inconsolata', 31)
date = myfont.render(currentdate, False, (255, 255, 255))
month = myfont1.render(currentmonth, False, (0, 0, 0))
day = myfont2.render(currentday, False, (255, 255, 255))

# Infinite Loop That keeps the Program Running
while done:
    now = datetime.datetime.now()
    currenttime = now.strftime("%I:%M:%S %p")
    time = myfont2.render(currenttime, False, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                say("Listening")
                command = speechtext()
                mycommand = command.split()
                lencommand = len(mycommand)
                if 'hello' in command:
                    say("Hello")
                if 'what is' in command:
                    if 3 == lencommand:
                        searchwiki(mycommand[3])
                    if 4 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4]
                        searchwiki(kmnd)
                    if 5 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4] +' '+ mycommand[5]
                        searchwiki(kmnd)
                if 'tell me about' in command:
                    if 4 == lencommand:
                        searchwiki(mycommand[3])
                    if 5 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4]
                        searchwiki(kmnd)
                    if 6 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4] +' '+ mycommand[5]
                        searchwiki(kmnd)
                if 'tell me who is' in command:
                    if 5 == lencommand:
                        searchwiki(mycommand[3])
                    if 6 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4]
                        searchwiki(kmnd)
                    if 7 == lencommand:
                        kmnd = mycommand[3] +' '+ mycommand[4] +' '+ mycommand[5]
                        searchwiki(kmnd)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if Button.isOver(mouse_pos):
                os.system("opera")
            if Button1.isOver(mouse_pos):
                os.system("pycharm64.exe")
            if Button2.isOver(mouse_pos):
                os.system("FortniteLauncher.exe")
            if Button3.isOver(mouse_pos):
                os.system("\"D:/program files/txgameassistant/appmarket/AppMarket.exe\" -from AppMarketQuickStar")
            if Button4.isOver(mouse_pos):
                os.system("\"C:/Users/GAMING/AppData/Roaming/uTorrent/uTorrent.exe\"")
            if Button5.isOver(mouse_pos):
                os.system("C:/Windows/explorer.exe C:/Users/GAMING/Documents")
            if Button6.isOver(mouse_pos):
                os.system(r"C:/Windows/explorer.exe C:\Users\GAMING\Music")
            if Button7.isOver(mouse_pos):
                os.system(r"C:/Windows/explorer.exe C:\Users\GAMING")
            if Button8.isOver(mouse_pos):
                os.system(r"C:/Windows/explorer.exe C:\Users\GAMING\Pictures")
            if Button9.isOver(mouse_pos):
                os.system(r"C:/Windows/explorer.exe C:\Users\GAMING\Downloads")
            if Button10.isOver(mouse_pos):
                os.system("start https://www.facebook.com")
            if Button11.isOver(mouse_pos):
                os.system("start https://www.youtube.com")
            if Button12.isOver(mouse_pos):
                done = False


        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if Button.isOver(mouse_pos):
                Button.color = (255, 255, 255)
                Button.textcolor = (0,0,0)
            else:
                Button.color = (131,139,139)
                Button.textcolor = (255, 255, 255)
            if Button1.isOver(mouse_pos):
                Button1.color = (255, 255, 255)
                Button1.textcolor = (0,0,0)
            else:
                Button1.color = (131,139,139)
                Button1.textcolor = (255, 255, 255)
            if Button2.isOver(mouse_pos):
                Button2.color = (255, 255, 255)
                Button2.textcolor = (0,0,0)
            else:
                Button2.color = (131,139,139)
                Button2.textcolor = (255, 255, 255)
            if Button3.isOver(mouse_pos):
                Button3.color = (255, 255, 255)
                Button3.textcolor = (0,0,0)
            else:
                Button3.color = (131,139,139)
                Button3.textcolor = (255, 255, 255)
            if Button4.isOver(mouse_pos):
                Button4.color = (255, 255, 255)
                Button4.textcolor = (0,0,0)
            else:
                Button4.color = (131,139,139)
                Button4.textcolor = (255, 255, 255)
            if Button5.isOver(mouse_pos):
                Button5.color = (255, 255, 255)
                Button5.textcolor = (0,0,0)
            else:
                Button5.color = (GRAY)
                Button5.textcolor = (255, 255, 255)
            if Button6.isOver(mouse_pos):
                Button6.color = (255, 255, 255)
                Button6.textcolor = (0,0,0)
            else:
                Button6.color = (GRAY)
                Button6.textcolor = (255, 255, 255)
            if Button7.isOver(mouse_pos):
                Button7.color = (255, 255, 255)
                Button7.textcolor = (0,0,0)
            else:
                Button7.color = (131,139,139)
                Button7.textcolor = (255, 255, 255)
            if Button8.isOver(mouse_pos):
                Button8.color = (255, 255, 255)
                Button8.textcolor = (0,0,0)
            else:
                Button8.color = (131,139,139)
                Button8.textcolor = (255, 255, 255)
            if Button9.isOver(mouse_pos):
                Button9.color = (255, 255, 255)
                Button9.textcolor = (0,0,0)
            else:
                Button9.color = (131,139,139)
                Button9.textcolor = (255, 255, 255)
            if Button10.isOver(mouse_pos):
                Button10.color = (255, 255, 255)
                Button10.textcolor = (0,0,0)
            else:
                Button10.color = (GRAY)
                Button10.textcolor = (255, 255, 255)
            if Button11.isOver(mouse_pos):
                Button11.color = (255, 255, 255)
                Button11.textcolor = (0,0,0)
            else:
                Button11.color = (GRAY)
                Button11.textcolor = (255, 255, 255)
            if Button12.isOver(mouse_pos):
                Button12.color = (255, 255, 255)
                Button12.textcolor = (BLACK)
            else:
                Button12.color = (BLACK)
                Button12.textcolor = (255, 255, 255)

    screen.blit(background_image, background_position)
    screen.blit(date, [1180, 65])
    screen.blit(month, [1190, 150])
    screen.blit(day, [1185, 160])
    screen.blit(time, [220, 505])
    redrawWindow(Button)
    redrawWindow(Button1)
    redrawWindow(Button2)
    redrawWindow(Button3)
    redrawWindow(Button4)
    redrawWindow(Button5)
    redrawWindow(Button6)
    redrawWindow(Button7)
    redrawWindow(Button8)
    redrawWindow(Button9)
    redrawWindow(Button10)
    redrawWindow(Button11)
    redrawWindow(Button12)
    pygame.display.flip()










