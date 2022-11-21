import pygame

# initialize pygame
pygame.init()

# create the screen
x_axis = 800
y_axis = 600
screen = pygame.display.set_mode((x_axis, y_axis))

# edit title and icon
pygame.display.set_caption("KAHMATE")
icon = pygame.image.load("img/ball.png")
pygame.display.set_icon(icon)

# player1
player1_img = pygame.image.load("img/player.png")
player1_x = 100
player1_y = 100
player1_turn = True


# player2
player2_img = pygame.image.load("img/player2.png")
player2_x = 500
player2_y = 500
player2_turn = False


def player(player_img, x, y):
    screen.blit(player_img, (x, y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if player1_turn:
                if event.key == pygame.K_LEFT:
                    player1_x -= 15
                if event.key == pygame.K_RIGHT:
                    player1_x += 15
                if event.key == pygame.K_DOWN:
                    player1_y += 15
                if event.key == pygame.K_UP:
                    player1_y -= 15
                player1_turn = False
                player2_turn = True
            elif player2_turn:
                if event.key == pygame.K_LEFT:
                    player2_x -= 15
                if event.key == pygame.K_RIGHT:
                    player2_x += 15
                if event.key == pygame.K_DOWN:
                    player2_y += 15
                if event.key == pygame.K_UP:
                    player2_y -= 15
                player2_turn = False
                player1_turn = True

    # maintain player in the screen
    if player1_x <= 0:
        player1_x = 0
    elif player1_x >= x_axis - 64:
        player1_x = x_axis - 64

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= y_axis - 64:
        player1_y = y_axis - 64

    screen.fill((30, 113, 36))
    player(player1_img, player1_x, player1_y)
    player(player2_img, player2_x, player2_y)

    pygame.display.update()
