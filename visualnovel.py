#  visualnovel.py
#  
#  Copyright 2015 Imagine Publishing
#  Written by: Rob Zwetsloot

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA

import pygame, time, script
pygame.init()

size = width, height = 1000, 563
grey = 128, 128, 128
white = 255, 255, 255
black = 0, 0, 0
title_font = pygame.font.Font('TitilliumWeb.ttf', 72)
menu_font = pygame.font.Font('TitilliumWeb.ttf', 32)
game_font = pygame.font.Font('TitilliumWeb.ttf', 28)
school_front = pygame.image.load('school_front.png')
school_classroom = pygame.image.load('school_classroom.png')
brother = pygame.image.load('brother.png')
game_script = 1
game_running = True
location = {'school_front' : school_front, 'school_classroom' : school_classroom}
character = {'brother' : brother}

screen = pygame.display.set_mode(size)

def menu_screen():
    screen.fill(grey)
    screen.blit(title_font.render('VN SCHOOL', 1, black), (330, 100))
    start_button = pygame.draw.rect(screen, (black), pygame.Rect(410, 310, 180, 55))
    screen.blit(menu_font.render('Start game', 1, white), (425, 310))
    pygame.display.flip()
    while True:
        pygame.event.get()
        click_pos = pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed())[0] == 1 and 410 < click_pos[0] < 590 and 310 < click_pos[1] < 365:
            start_game()
        

def start_game():
    global game_script, location, character
    turn = 0
    game_state = 1
    
    while game_state == 1:
        line = getattr(script, ('scene' + str(game_script)))(turn)
        pygame.event.get()
        click_state = pygame.mouse.get_pressed()
        if turn == 0:
            scene_start = 0
            for i in range (4):
                if scene_start == 0:
                    screen.blit(location[line[0]], [0, 0])
                elif scene_start == 1:
                    time.sleep(1)
                    screen.blit(character[line[1]], [377, 113])
                elif scene_start == 2:
                    time.sleep(1)
                    pygame.draw.rect(screen, (grey), pygame.Rect(130, 423, 740, 120))
                elif scene_start == 3:
                    time.sleep(1)
                    screen.blit(game_font.render(line[2], 1, white), (135, 430))
                    turn += 1
                    clicked = 0
                
                scene_start += 1
                pygame.display.flip()
                
        elif turn > 0 and click_state[0] == 1:
            line_start = 0
            for i in range (4):
                if line_start == 0 and line[0] != '0':
                    print (line[0])
                    screen.blit(location[line[0]], [0, 0])
                    time.sleep(1)
                elif line_start == 1 and line[1] != '0':
                    screen.blit(character[line[1]], [377, 113])
                    time.sleep(1)
                elif line_start == 2:
                    pygame.draw.rect(screen, (grey), pygame.Rect(130, 423, 740, 120))
                elif line_start == 3:
                    screen.blit(game_font.render(line[2], 1, white), (135, 430))
                    turn += 1
                    if  line[3] != '0':
                        game_script = line[3]
                        time.sleep(0.5)
                    game_state = line[4]
                    clicked = 0
                
                line_start += 1
                pygame.display.flip()
    

def game():
    global game_running
    while game_running == True:
        menu_screen()

game()
