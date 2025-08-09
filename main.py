import pgzrun
from pgzero.actor import Actor
from pygame import Rect
import math
import random

# CONFIGURAÇÕES GERAIS
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 16

map_tiles = [
    [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 2, 2, 6, 1, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3],
    [3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 3],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3],
    [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
]

tiles = [
    'kenney_tiny-dungeon/tiles/tile_0000', #0 Ground
    'kenney_tiny-dungeon/tiles/tile_0012', #1 Stones
    'kenney_tiny-dungeon/tiles/tile_0049', #2 Road
    'kenney_tiny-dungeon/tiles/tile_0039', #3 Outside Wall
    'kenney_tiny-dungeon/tiles/tile_0037', #4 Outside Wall 
    'kenney_tiny-dungeon/tiles/tile_0010', #5 Door
    'kenney_tiny-dungeon/tiles/tile_0014', #6 Wall
    'kenney_tiny-dungeon/tiles/tile_0011', #7 Door
    'kenney_tiny-dungeon/tiles/tile_0026', #8 Wall down
]

collidable_tiles = [3,4,6] # Tiles que vão ter colisão

# CLASSE DO PERSONAGEM (PLAYER)

class Player:
    def __init__(self, pos, speed):
        # O PgZero carrega automaticamente o primeiro frame como a imagem inicial
        self.actor = Actor('sprites/lelia000', pos)
        self.speed = speed

        # Dicionario para armazenar os nomes dos arquivos para cada animacao
        self.animations = {
            'walk_up': ['sprites/lelia000', 'sprites/lelia001', 'sprites/lelia002'],
            'walk_right': ['sprites/lelia003', 'sprites/lelia004', 'sprites/lelia005'],
            'walk_down': ['sprites/lelia006', 'sprites/lelia007', 'sprites/lelia008'],
            'walk_left': ['sprites/lelia009', 'sprites/lelia010', 'sprites/lelia011']
        }
        self.current_animation = 'walk_down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frame_timer = 0
        self.is_moving = False

    def update_animation(self):
        # Atualiza o frame de animacao com base no tempo
        self.frame_timer += self.animation_speed
        
        if self.frame_timer >= 1:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
            # Altera a imagem do ator para o proximo arquivo na sequencia
            self.actor.image = self.animations[self.current_animation][self.frame_index]
            self.frame_timer = 0

    def update(self):
        self.is_moving = False
        new_x = self.actor.x
        new_y = self.actor.y

        if keyboard.up:
            new_y -= self.speed
            self.current_animation = 'walk_up'
            self.is_moving = True
        elif keyboard.down:
            new_y += self.speed
            self.current_animation = 'walk_down'
            self.is_moving = True
        elif keyboard.left:
            new_x -= self.speed
            self.current_animation = 'walk_left'
            self.is_moving = True
        elif keyboard.right:
            new_x += self.speed
            self.current_animation = 'walk_right'
            self.is_moving = True

        future_rect = get_actor_rect(new_x, new_y)
        if can_move_to(future_rect):
            self.actor.x = new_x
            self.actor.y = new_y


        if self.is_moving:
            self.update_animation()
        else:
            self.actor.image = self.animations[self.current_animation][0]
            self.frame_index = 0
    
    def draw(self):
        self.actor.draw() # Desenha o ator na tela
        
class Enemy:
    def __init__(self, x, y):
        self.actor = Actor('enemy_idle_0', (x, y))  # primeiro frame
        self.speed = 1
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        # Dicionario para armazenar os nomes dos arquivos para cada animacao
        self.animations = {
            'idle': ['enemy_idle_0', 'enemy_idle_1'],
            'walk': ['enemy_walk_0', 'enemy_walk_1', 'enemy_walk_2']
        }
        self.current_animation = 'walk'
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_speed = 0.2

    def update(self):
        dx, dy = 0, 0 # movimento simples bem padrão
        if self.direction == 'up': dy = -self.speed
        elif self.direction == 'down': dy = self.speed
        elif self.direction == 'left': dx = -self.speed
        elif self.direction == 'right': dx = self.speed

        # checa colisão antes de mover
        new_x = self.actor.x + dx
        new_y = self.actor.y + dy
        if can_move_to(get_actor_rect(new_x, new_y)):
            self.actor.x = new_x
            self.actor.y = new_y
        else:
            self.direction = random.choice(['up', 'down', 'left', 'right']) # bateu na parede → muda de direção

        # animação
        self.frame_timer += self.frame_speed
        if self.frame_timer >= 1:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
            self.actor.image = self.animations[self.current_animation][self.frame_index]

    def draw(self):
        self.actor.draw()

def get_actor_rect(x, y):
    width, height = lelia.actor.width - 6, lelia.actor.height - 6  # Ajuste o tamanho do retângulo para ficar um pouco menor que a imagem real
    left = x - width // 3
    top = y - height // 3 # Ajusta o topo para cobrir melhor o personagem
    return Rect(left, top, width, height)

def can_move_to(rect):
    tile_x_start = rect.left // TILE_SIZE
    tile_y_start = rect.top // TILE_SIZE
    tile_x_end = (rect.right - 1) // TILE_SIZE
    tile_y_end = (rect.bottom - 1) // TILE_SIZE

    # Verifica limites do mapa
    if tile_x_start < 0 or tile_y_start < 0 or tile_x_end >= len(map_tiles[0]) or tile_y_end >= len(map_tiles):
        return False

    # Para cada tile dentro do retângulo
    for ty in range(tile_y_start, tile_y_end + 1):
        for tx in range(tile_x_start, tile_x_end + 1):
            tile = map_tiles[ty][tx]
            if tile in collidable_tiles:
                tile_rect = Rect(tx * TILE_SIZE, ty * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if rect.colliderect(tile_rect):
                    return False
    return True

# LÓGICA PRINCIPAL

lelia = Player((15, 550), 2)

def update():
    lelia.update()

def draw():
    screen.clear()
    for row_index, row in enumerate(map_tiles):
        for col_index, tile_index in enumerate(row):
            tile_image = tiles[tile_index]
            screen.blit(tile_image, (col_index * TILE_SIZE, row_index * TILE_SIZE))
    lelia.draw()

pgzrun.go()