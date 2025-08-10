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
    [3, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 6, 2, 2, 2, 6, 6, 6, 0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 6, 6, 2, 2, 2, 6, 1, 0, 0, 0, 0, 0, 0, 0, 3],
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
    [3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
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
game_state = 'menu'
buttons = [
    Actor('buttons/playbutton', (400, 300)),
     Actor('buttons/exit', (400, 450)),
]
buttons[0].name = 'start'
buttons[1].name = 'exit'
victory_bg = Actor("buttons/victory")
victory_bg.pos = (WIDTH // 2, HEIGHT // 2)
menu_music_playing = False

class Character:
    def __init__(self, sprite_prefix, pos, speed, animations):
        self.actor = Actor(animations['idle'][0], pos)
        self.speed = speed
        self.animations = animations
        self.current_animation = 'idle'  # padrão para não mover
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frame_timer = 0
        self.is_moving = False

    def update_animation(self):
        self.frame_timer += self.animation_speed
        if self.frame_timer >= 1:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
            self.actor.image = self.animations[self.current_animation][self.frame_index]

    def move(self, dx, dy):
        new_x = self.actor.x + dx
        new_y = self.actor.y + dy
        if can_move_to(get_actor_rect(new_x, new_y)):
            self.actor.x = new_x
            self.actor.y = new_y
            self.is_moving = True
        else:
            self.is_moving = False

    def update(self):
        # Só atualiza animação, subclasses fazem o movimento
        if self.is_moving or self.current_animation == 'idle':
            self.update_animation()
        else:
            self.actor.image = self.animations[self.current_animation][0]
            self.frame_index = 0

    def draw(self):
        self.actor.draw()

class Player(Character):
    def __init__(self, pos, speed):
        animations = {
            'walk_up': ['sprites/lelia000', 'sprites/lelia001', 'sprites/lelia002'],
            'walk_right': ['sprites/lelia003', 'sprites/lelia004', 'sprites/lelia005'],
            'walk_down': ['sprites/lelia006', 'sprites/lelia007', 'sprites/lelia008'],
            'walk_left': ['sprites/lelia009', 'sprites/lelia010', 'sprites/lelia011'],
            'idle': ['sprites/lelia006', 'sprites/lelia012']  # frame parado padrão para ficar parado olhando para baixo
        }
        super().__init__('sprites/lelia', pos, speed, animations)
        self.current_animation = 'idle'
        self.idle_speed = 0.08
        self.animation_speed = self.idle_speed        

    def update(self):
        self.is_moving = False
        dx, dy = 0, 0

        if keyboard.up:
            dy = -self.speed
            self.current_animation = 'walk_up'
            self.is_moving = True
        elif keyboard.down:
            dy = self.speed
            self.current_animation = 'walk_down'
            self.is_moving = True
        elif keyboard.left:
            dx = -self.speed
            self.current_animation = 'walk_left'
            self.is_moving = True
        elif keyboard.right:
            dx = self.speed
            self.current_animation = 'walk_right'
            self.is_moving = True
        else:
            self.current_animation = 'idle'
            self.is_moving = False
        
        if self.is_moving:
            self.move(dx, dy)

        super().update()
        
class Enemy(Character):
    def __init__(self, pos, patrol_start, patrol_end, speed=1):
        animations = {
            'walk_up': ['sprites/skeleton000', 'sprites/skeleton001', 'sprites/skeleton002'],
            'walk_right': ['sprites/skeleton003', 'sprites/skeleton004', 'sprites/lelia005'],
            'walk_down': ['sprites/skeleton006', 'sprites/skeleton007', 'sprites/skeleton008'],
            'walk_left': ['sprites/skeleton009', 'sprites/skeleton0010', 'sprites/skeleton0011'],
            'idle': ['sprites/skeleton006']
        }
        super().__init__('enemy', pos, speed, animations)
        self.patrol_start = patrol_start  # tupla (x, y)
        self.patrol_end = patrol_end      # tupla (x, y)
        self.target_point = patrol_end
        self.moving_to_end = True
        self.animation_speed = 0.2

    def update(self):
        dx = self.target_point[0] - self.actor.x
        dy = self.target_point[1] - self.actor.y

        dist = math.hypot(dx, dy)
        if dist < 2:  # Chegou perto do ponto alvo, troca o destino
            if self.moving_to_end:
                self.target_point = self.patrol_start
                self.moving_to_end = False
            else:
                self.target_point = self.patrol_end
                self.moving_to_end = True
            dx, dy = 0, 0  # Para não ultrapassar

        if dist != 0:
            dx = (dx / dist) * self.speed
            dy = (dy / dist) * self.speed
        else:
            dx, dy = 0, 0

        # Define animação baseado na direção do movimento (simplificado)
        if abs(dx) > abs(dy):
            if dx > 0:
                self.current_animation = 'walk_right'
            else:
                self.current_animation = 'walk_left'
        else:
            if dy > 0:
                self.current_animation = 'walk_down'
            else:
                self.current_animation = 'walk_up'

        # tenta mover, se não conseguir troca direção
        new_x = self.actor.x + dx
        new_y = self.actor.y + dy
        if can_move_to(get_actor_rect(new_x, new_y)):
            self.move(dx, dy)
            self.is_moving = True
        else:
            self.is_moving = False

        super().update()

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

def player_dies():
    lelia.actor.pos = (15, 550)

def draw_menu():
    screen.clear()
    screen.blit("menu/menu", (0, 0))  # Nome do arquivo sem extensão
    for button in buttons:
        button.draw()
                    
def on_mouse_down(pos, button):
    if game_state == "menu":
        for button in buttons:
            if button.collidepoint(pos):
                if button.name == "start":
                    start_game()
                elif button.name == "exit":
                     raise SystemExit
                    
def start_game():
    global game_state
    lelia.actor.pos = (15, 550)
    game_state = "playing"
    
def show_victory():
    global game_state
    game_state = "victory"
    screen.blit("menu/menu", (0, 0))
    clock.schedule_unique(back_to_menu, 3)

def back_to_menu():
    global game_state
    game_state = "menu"
    

lelia = Player((15, 550), 2)
enemies = [
    Enemy((230, 50), (230, 50), (230, 210)),
    Enemy((330, 50), (330, 50), (330, 210)),
    Enemy((430, 50), (430, 50), (430, 210)),
    Enemy((530, 50), (530, 50), (530, 210)),
]

def update_game():
    lelia.update()
    for e in enemies:
        e.update()
        if lelia.actor.colliderect(e.actor):
            sounds.skeleton.play() # Som quando colidir com inimigo
            player_dies()
    if lelia.actor.x == 785 and lelia.actor.y == 538:
        sounds.win.play()
        show_victory()


def draw_game():
    screen.clear()
    
    for row_index, row in enumerate(map_tiles):
        for col_index, tile_index in enumerate(row):
            tile_image = tiles[tile_index]
            screen.blit(tile_image, (col_index * TILE_SIZE, row_index * TILE_SIZE))
            
    lelia.draw()
    
    for e in enemies:
        e.draw()
        
def update():
    global menu_music_playing
    
    if game_state == "playing":
        update_game()
        if menu_music_playing:
            music.stop()
            menu_music_playing = False
    elif game_state == "menu":
        if not menu_music_playing:
            music.play('menu_music')
            menu_music_playing = True

def draw():
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()
    elif game_state == "victory":
        draw_menu()
        victory_bg.draw()

pgzrun.go()