import random

import pygame as p


def random_start():
    global ball_speed_y, ball_speed_x
    ball_speed_y = random.choice([-7, 7])
    ball_speed_x = random.choice([-7, 7])


def ball_animation():
    global ball_speed_y, ball_speed_x, score_one, score_two
    ball.y += ball_speed_y
    ball.x += ball_speed_x

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        soundtrack.play()

def ball_start():
    global score_one, score_two, win_text, game_is_over
    if ball.left <= 0:
        score_two += 1
        ball.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        random_start()
    if ball.right >= SCREEN_WIDTH:
        score_one += 1
        ball.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        random_start()

    if score_one == 3:
        win_text = 'Игрок 1 победил'
        game_over()
        game_is_over = True
    if score_two == 3:
        win_text = 'Игрок 2 победил'
        game_over()
        game_is_over = True


def game_over():
    global ball_speed_x, ball_speed_y, win_text
    ball_speed_y, ball_speed_x = 0, 0
    text_end = game_font.render(str(win_text), 1, (255, 153, 51))
    text_rect = text_end.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text_end, text_rect)


def ai():
    global opponent_speed
    if ball.top < opponent.top:
        opponent_speed -= 7
    if ball.bottom > opponent.bottom:
        opponent_speed += 7


def stop():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 960:
        player.bottom = 960
    if opponent.bottom <= 0:
        opponent.bottom = 0
    if opponent.bottom >= 960:
        opponent.bottom= 960



p.init()
clock = p.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption('ping-pong')


soundtrack = p.mixer.Sound('123.mp3')
soundtrack.set_volume(0.5)


# Цвета
# 97, 255, 97
bg_color = ('darkblue')
another_color = p.Color('darkgreen')

# Игровые объекты
player = p.Rect(30, SCREEN_HEIGHT/2-70, 10, 140)
opponent = p.Rect(SCREEN_WIDTH-30, SCREEN_HEIGHT/2-70, 10, 140)
ball = p.Rect(SCREEN_WIDTH/2-10, SCREEN_HEIGHT/2-10, 20, 20)

# Игровые переменные
score_one = 0
score_two = 0
player_speed = 0
opponent_speed = 0
ball_speed_y = 7
ball_speed_x = -7
win_text = 0
game_is_over = False
game_font = p.font.Font('freesansbold.ttf', 50)


running = True
while running:
    # Обработка ввода
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        if event.type == p.KEYDOWN:
            if event.key == p.K_w:
                player_speed -= 7
            if event.key == p.K_s:
                player_speed += 7

        if event.type == p.KEYUP:
            if event.key == p.K_w:
                player_speed += 7
            if event.key == p.K_s:
                player_speed -= 7


        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE and game_is_over == True:
                game_is_over = False
                ball_speed_y = random.choice([-7, 7])
                ball_speed_x = random.choice([-7, 7])
                score_one, score_two = 0, 0

    player.y += player_speed
    opponent.y += opponent_speed

    screen.fill(bg_color)
    ball_animation()
    ai()
    stop()

    # https://w3schools.com/colorpicker


    player_one_text = game_font.render(str(score_one), 1, (0, 0, 0))
    player_two_text = game_font.render(str(score_two), 1, (0, 0, 0))
    screen.blit(player_one_text, (SCREEN_WIDTH/2-45, 100))
    screen.blit(player_two_text, (SCREEN_WIDTH/2+35, 100))

    p.draw.rect(screen, (255, 255, 255), player)
    p.draw.rect(screen, (255, 255, 255), opponent)
    p.draw.ellipse(screen, (255, 255, 255), ball)
    # p.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, 960))
    # p.draw.line(screen, (0, 0, 0), (0, SCREEN_HEIGHT/2), (1280, SCREEN_HEIGHT/2))
    ball_start()
    # Обновление экрана
    p.display.flip()
    clock.tick(60)
