# importing libraries
import pygame
import time
import random
from pygame import mixer

# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("Game music 1.mp3")
# Setting the volume
mixer.music.set_volume(1.2)
mixer.music.play(10000)


X2 = 894
Y2 = 628

screen = pygame.display.set_mode((X2, Y2))
 
# set the pygame window name
pygame.display.set_caption('Rules')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Game Rules.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(10)


X1 = 894
Y1 = 628

screen = pygame.display.set_mode((X1, Y1))
 
# set the pygame window name
pygame.display.set_caption('Warning')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Don't Run Into The Wall.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(10)

X3 = 894
Y3 = 628

screen = pygame.display.set_mode((X3, Y3))
 
# set the pygame window name
pygame.display.set_caption('CountDown')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Countdown 3.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(1)

X4 = 894
Y4 = 628

screen = pygame.display.set_mode((X4, Y4))
 
# set the pygame window name
pygame.display.set_caption('CountDown')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Countdown 2.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(1)

X5 = 894
Y5 = 628

screen = pygame.display.set_mode((X5, Y5))
 
# set the pygame window name
pygame.display.set_caption('CountDown')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Countdown 1.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(1)    

X6 = 894
Y6 = 628

screen = pygame.display.set_mode((X3, Y3))
 
# set the pygame window name
pygame.display.set_caption('CountDown')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\Countdown GO!.png").convert()
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

time.sleep(1)

snake_speed = 25

# Window size
window_x = 720
window_y = 480

X = 548
Y = 352


# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
Icon = pygame.image.load('''Danger Don't touch.png''')
pygame.display.set_caption("Luigi's ghost capturing ")
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_icon(Icon)

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [120, 70]

# defining first 4 blocks of snake body
snake_body = [[100, 50]]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)

	# create the display surface object
	# score_surface
	score_surface = score_font.render('Ghost Captured : ' + str(score), True, color)

	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()

	# displaying text
	game_window.blit(score_surface, score_rect)
# game over function
def game_over():
        time.sleep(5)

        scrn = pygame.display.set_mode((X, Y))
        imp = pygame.image.load("C:\\Users\\Alexander\\Desktop\\School\\Coding class\\Python\\New folder\\Creating very own game basics\\Python Game\\King Boo GAME OVER.png").convert()
        scrn.blit(imp, (0, 0))
        pygame.display.flip()

        mixer.music.load("Game Over 1.mp3")
        mixer.music.set_volume(10.9)
        mixer.music.play()

        time.sleep(21)
        print("Your score is: " + str(score))
        pygame.quit()
        quit()
        
# Main Function
while True:
    
    
       
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
	
	# If two keys pressed simultaneously
	# we don't want snake to move into two
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

        
	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 1
		fruit_spawn = False
	else:
		snake_body.pop()

	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
						random.randrange(1, (window_y//10)) * 10]

	fruit_spawn = True
	game_window.fill(black)

	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 9, 9))
	pygame.draw.rect(game_window, red, pygame.Rect(
		fruit_position[0], fruit_position[1], 7, 7))
        
	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	#Touching the snake body
	#for block in snake_body[1:]:
	#	if snake_position[0] == block[0] and snake_position[1] == block[1]:
	#		game_over()

	# displaying score continuously
	show_score(1, white, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)
	

# fills the screen with specified colour

	
