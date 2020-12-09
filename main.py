import pygame
from enemy import Enemy

# This has to be the first line always
FPS = 30
pygame.init()
clock = pygame.time.Clock()

# -------------- RESOURCE LOADIN ------------------
icon = pygame.image.load('ufo.png')
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')

# -------------- INITIAL STATE --------------------
running = True
player_x = 370
player_y = 400

left_pressing = False
right_pressing = False

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

def calculate_player_position():
    global player_x
    global left_pressing
    global right_pressing

    direction = 0
    movement = 5

    if left_pressing:
        direction = -1
    elif right_pressing:
        direction = +1

    player_x += direction * movement

    # Check boundaries and correct anything
    if player_x < 0.0:
        player_x = 0

    if player_x > 736.0:
        player_x = 736.0


def event_handling(event):
    global left_pressing
    global right_pressing

    run = True

    # Window events
    if event.type == pygame.QUIT:
        run = False

    # Arrow key events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            left_pressing = True
        elif event.key == pygame.K_RIGHT:
            right_pressing = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            left_pressing = False
        elif event.key == pygame.K_RIGHT:
            right_pressing = False

    return run

# -------------- GAME LOOP ------------------------
while running:
    for event in pygame.event.get():
        running = event_handling(event)

    # Refreshing screen
    screen.fill((0, 0, 0))

    calculate_player_position()
    draw_player()
    draw_enemies()

    pygame.display.update()

    # Run whole game on 30 fps
    clock.tick(FPS)
