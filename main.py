import pygame as pg
import sys
import MenuPausa
from os import path
import pytmx
from settings import *
from Tilemap import *
#from Player import *
from sprites import*

screen = pg.display.set_mode((WIDTH,HEIGHT),pg.FULLSCREEN)
position = 0

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.music.load("Musica/Hall.mp3")
        pg.mixer.music.play(-1)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):

        game_folder= path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        map_folder = path.join(game_folder,'maps')
        self.map = TileMap(path.join(map_folder,'Hall.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
        self.player_img2f = pg.image.load(path.join(img_folder, PLAYER_IMG2)).convert_alpha()
        self.player_img3f = pg.image.load(path.join(img_folder, PLAYER_IMG3)).convert_alpha()
        self.player_img4f = pg.image.load(path.join(img_folder, PLAYER_IMG4)).convert_alpha()
        self.player_imgup1 = pg.image.load(path.join(img_folder, PLAYER_IMG5)).convert_alpha()
        self.player_imgup2= pg.image.load(path.join(img_folder, PLAYER_IMG6)).convert_alpha()
        self.player_imgup3 = pg.image.load(path.join(img_folder, PLAYER_IMG7)).convert_alpha()
        self.player_imgleft1 = pg.image.load(path.join(img_folder, PLAYER_IMG8)).convert_alpha()
        self.player_imgleft2 = pg.image.load(path.join(img_folder, PLAYER_IMG9)).convert_alpha()
        self.player_imgleft3 = pg.image.load(path.join(img_folder, PLAYER_IMG10)).convert_alpha()
        self.player_imgright1 = pg.image.load(path.join(img_folder, PLAYER_IMG11)).convert_alpha()
        self.player_imgright2 = pg.image.load(path.join(img_folder, PLAYER_IMG12)).convert_alpha()
        self.player_imgright3 = pg.image.load(path.join(img_folder, PLAYER_IMG13)).convert_alpha()
        self.enemy_img = pg.image.load(path.join(img_folder,ENEMY_IMG)).convert_alpha()
        self.enemy_img2f = pg.image.load(path.join(img_folder, ENEMY_IMG1)).convert_alpha()
        self.enemy_img3f = pg.image.load(path.join(img_folder, ENEMY_IMG2)).convert_alpha()
        self.enemy_img4f = pg.image.load(path.join(img_folder, ENEMY_IMG3)).convert_alpha()
        self.enemy_img_up = pg.image.load(path.join(img_folder, ENEMY_IMG4)).convert_alpha()
        self.enemy_img_up1 = pg.image.load(path.join(img_folder, ENEMY_IMG5)).convert_alpha()
        self.enemy_img_up2 = pg.image.load(path.join(img_folder, ENEMY_IMG6)).convert_alpha()
        self.enemy_img_left = pg.image.load(path.join(img_folder, ENEMY_IMG7)).convert_alpha()
        self.enemy_img_left1 = pg.image.load(path.join(img_folder, ENEMY_IMG8)).convert_alpha()
        self.enemy_img_left2 = pg.image.load(path.join(img_folder, ENEMY_IMG9)).convert_alpha()
        self.enemy_img_right = pg.image.load(path.join(img_folder, ENEMY_IMG10)).convert_alpha()
        self.enemy_img_right1 = pg.image.load(path.join(img_folder, ENEMY_IMG11)).convert_alpha()
        self.enemy_img_right2 = pg.image.load(path.join(img_folder, ENEMY_IMG12)).convert_alpha()
        self.camera = Camera(self.map.width, self.map.height)



    def new(self):
        # inicializacion de objetos
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)

            if tile_object.name == 'wall':
                self.obs = Obstaculo(self,tile_object.x,tile_object.y,
                          tile_object.width,tile_object.height)
            if tile_object.name == 'enemy':
                self.enemy = Enemy(self, tile_object.x, tile_object.y)
        self.camera = Camera(self.map.width, self.map.height)


    def draw(self):

        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pg.display.flip()

    def run(self):
        # loop del juego
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):

        self.all_sprites.update()
        self.camera.update(self.player)


    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                elif event.key == pg.K_x:
                    MenuPausa.Pausa()

    def quit(self):
        pg.quit()
        sys.exit()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
    
g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()



