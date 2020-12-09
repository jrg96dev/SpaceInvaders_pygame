import pygame
from enemy import Enemy

# This has to be the first line always
pygame.init()
pygame.key.set_repeat(1, 2)
clock = pygame.time.Clock()

# -------------- RESOURCE LOADIN ------------------
icon = pygame.image.load('ufo.png')
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')

# -------------- INITIAL STATE --------------------
running = True
player_x = 370
player_y = 400

enemies = [Enemy()]

# -------------- SETTINGS -------------------------
screen = pygame.display.set_mode([800, 480])
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)

# -------------- GAME FUNCTIONS -------------------
def draw_player():
    screen.blit(player_img, (player_x, player_y))

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy.sprite, (enemy.pos_x, enemy.pos_y))

def calculate_player_position(direction):
    global player_x

    movement = 0.4
    player_x += direction * movement

    # Check boundaries and correct anything
    if player_x < 0.0:
        player_x = 0

    if player_x > 736.0:
        player_x = 736.0


def event_handling(event):
    run = True

    # Window events
    if event.type == pygame.QUIT:
        run = False

    # Arrow key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        calculate_player_position(-1)
    elif keys[pygame.K_RIGHT]:
        calculate_player_position(+1)

    return run

# -------------- GAME LOOP ------------------------
while running:
    for event in pygame.event.get():
        running = event_handling(event)

    # Refreshing screen
    screen.fill((0, 0, 0))
    draw_player()
    draw_enemies()
    pygame.display.update()

    # Run whole game on 30 fps
    clock.tick(30)
