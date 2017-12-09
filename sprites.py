import pygame as pg, sys
from settings import*


"""class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)


    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos = self.pos + self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        #collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        #collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
"""
class Obstaculo(pg.sprite.Sprite):
    def __init__(self, game, x,y,w,h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT ##
        self.hit_rect.center = self.rect.center
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x,y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.x= x
        self.y = y

    def load_images(self):
        self.standing_frames = [self.game.player_img]

        self.walk_frames_a = [self.game.player_img2f,self.game.player_img3f,self.game.player_img4f]
        self.walk_frames_up=[self.game.player_imgup1, self.game.player_imgup2, self.game.player_imgup3]
        self.walk_frames_left=[self.game.player_imgleft1, self.game.player_imgleft2, self.game.player_imgleft3]
        self.walk_frames_right = [self.game.player_imgright1, self.game.player_imgright2, self.game.player_imgright3]



    def get_keys(self):
        self.acc = vec(0, 0)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
            # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0
        self.pos += self.vel + 0.5 * self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        #if self.pos.x > WIDTH:
            #self.pos.x = 0
        #if self.pos.x < 0:
            #self.pos.x = WIDTH

        #if self.pos.y < HEIGHT:
         #   self.pos.y = 0
        #if self.pos.y < 0:
         #   self.pos.y = HEIGHT

    def update(self):
        #self.get_keys()
        #self.rect = self.image.get_rect()
        #self.rect.center = self.pos
        #self.hit_rect.centerx = self.pos.x
        #self.collide_with_walls('x')
        #self.hit_rect.centery = self.pos.y
        #self.collide_with_walls('y')
        #self.rect.center = self.hit_rect.center
        self.animate()
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.y!=0 or self.vel.x!= 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_a)
                bottom = self.rect.bottom
                if self.vel.y >0:
                    self.image = self.walk_frames_a[self.current_frame]


                if self.vel.y < 0:
                    self.image = self.walk_frames_up[self.current_frame]
                else:
                    if self.vel.x < 0:
                        self.image = self.walk_frames_left[self.current_frame]

                    if self.vel.x > 0:
                        self.image = self.walk_frames_right[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom



        if not self.walking:
            if now - self.last_update > 100:
                for event in pg.event.get():
                    if event.type == pg.KEYUP and event.key == pg.K_UP:
                        self.image = self.game.player_imgup1
                    elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                        self.image = self.game.player_imgleft1
                    elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                        self.image = self.game.player_imgright1
                    elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                        self.image = self.game.player_img


    def collide_with_walls(self, dir):

        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if hits[0].rect.centerx < self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centery > self.hit_rect.centery:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if hits[0].rect.centery < self.hit_rect.centery:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                    self.vel.y = 0
                    self.hit_rect.centery = self.pos.y

    def teclado():
        teclado = pygame.key.get_pressed()
        if teclado[K_ESCAPE]:
            pygame.quit()
            sys.exit()         
        elif teclado[K_x]:
            MenuPausa.Pausa()
            
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT ##
        self.hit_rect.center = self.rect.center
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x,y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.x= x
        self.y = y

    def load_images(self):
        self.standing_frames = [self.game.enemy_img]

        self.walk_frames_a = [self.game.enemy_img2f,self.game.enemy_img3f,self.game.enemy_img4f]
        self.walk_frames_up=[self.game.enemy_img_up,self.game.enemy_img_up1,self.game.enemy_img_up2]
        self.walk_frames_left=[self.game.enemy_img_left,self.game.enemy_img_left1,self.game.enemy_img_left2]
        self.walk_frames_right = [self.game.enemy_img_right,self.game.enemy_img_right1,self.game.enemy_img_right2]



    def get_keys(self):
        self.acc = vec(0, 0)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
            # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0
        self.pos += self.vel + 0.5 * self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        #if self.pos.x > WIDTH:
            #self.pos.x = 0
        #if self.pos.x < 0:
            #self.pos.x = WIDTH

        #if self.pos.y < HEIGHT:
         #   self.pos.y = 0
        #if self.pos.y < 0:
         #   self.pos.y = HEIGHT

    def update(self):
        #self.get_keys()
        #self.rect = self.image.get_rect()
        #self.rect.center = self.pos
        #self.hit_rect.centerx = self.pos.x
        #self.collide_with_walls('x')
        #self.hit_rect.centery = self.pos.y
        #self.collide_with_walls('y')
        #self.rect.center = self.hit_rect.center
        self.animate()
        self.get_keys()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.y!=0 or self.vel.x!= 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_a)
                bottom = self.rect.bottom
                if self.vel.y >0:
                    self.image = self.walk_frames_a[self.current_frame]


                if self.vel.y < 0:
                    self.image = self.walk_frames_up[self.current_frame]
                else:
                    if self.vel.x < 0:
                        self.image = self.walk_frames_left[self.current_frame]

                    if self.vel.x > 0:
                        self.image = self.walk_frames_right[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom



        if not self.walking:
            if now - self.last_update > 100:
                for event in pg.event.get():
                    if event.type == pg.KEYUP and event.key == pg.K_UP:
                        self.image = self.game.enemy_img_up
                    elif event.type == pg.KEYUP and event.key == pg.K_LEFT:
                        self.image = self.game.enemy_img_left
                    elif event.type == pg.KEYUP and event.key == pg.K_RIGHT:
                        self.image = self.game.enemy_img_right
                    elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                        self.image = self.game.enemy_img



    def collide_with_walls(self, dir):

        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if hits[0].rect.centerx < self.hit_rect.centerx:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centery > self.hit_rect.centery:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                if hits[0].rect.centery < self.hit_rect.centery:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                    self.vel.y = 0
                    self.hit_rect.centery = self.pos.y