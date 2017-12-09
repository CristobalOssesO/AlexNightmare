import pygame as pg
from Vector2 import *
vec = Vec2d
from Tilemap import collide_hit_rect


#Configuracion del juego

WIDTH = 1200
HEIGHT = 727
FPS = 60

TITLE =  "Alex's Nightmare"
TILESIZE = 48
GREEN = (255,255,0)
BLACK = (0,0,0)
# Player settings
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'front1.png'
PLAYER_IMG2 = 'adelante1.png'
PLAYER_IMG3 = 'adelante2.png'
PLAYER_IMG4 = 'adelante3.png'
PLAYER_IMG5 = 'back1.png'
PLAYER_IMG6 = 'back2.png'
PLAYER_IMG7= 'back3.png'
PLAYER_IMG8 = 'left1.png'
PLAYER_IMG9= 'left2.png'
PLAYER_IMG10= 'left3.png'
PLAYER_IMG11= 'right1.png'
PLAYER_IMG12= 'right2.png'
PLAYER_IMG13 = 'right3.png'

PLAYER_HIT_RECT = pg.Rect(0, 0, 10, 10)
BARREL_OFFSET = vec(30, 10)
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.20

#enemy settings

ENEMY_IMG = 'front_A_1.png'
ENEMY_IMG1 = 'front_A_2_1.png'
ENEMY_IMG2 = 'front_A_3_2.png'
ENEMY_IMG3 = 'front_A_1.png'
ENEMY_IMG4 = 'back_A_1.png'
ENEMY_IMG5 = 'back_A_2.png'
ENEMY_IMG6 = 'back_A_3.png'
ENEMY_IMG7 = 'left_A_1.png'
ENEMY_IMG8 = 'left_A_2.png'
ENEMY_IMG9 = 'left_A_3.png'
ENEMY_IMG10= 'right_A_1.png'
ENEMY_IMG11= 'right_A_2.png'
ENEMY_IMG12= 'right_A_3.png'


