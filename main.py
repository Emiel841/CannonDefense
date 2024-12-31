import pygame
from tower import Tower
from Enemy import Enemy

HEIGHT = 720
WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

towers = pygame.sprite.Group()

world = pygame.image.load('Assets/Maps/Map1.png')
world = pygame.transform.scale(world, (WIDTH, HEIGHT))

path = ((1, 5), (2, 5), (3, 5), (3, 6), (3, 7),
        (4, 7), (5, 7), (5, 8), (6, 8), (7, 8),
        (8, 8), (8, 7), (8, 6), (8, 5), (7, 5),
        (6, 5), (6, 4), (6, 3), (6, 2), (7, 2),
        (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
        (12, 3), (12, 4), (13, 4), (14, 4), (14, 5),
        (14, 6), (14, 7), (14, 8), (14, 8), (15, 8),
        (16, 8))

path_scaled = []

enemy_path = ["L", "L", "L", "D", "D", "L", "L", "D", "L",
              "L", "L", "U", "U", "U", "R", "R", "U", "U",
              "U", "L", "L", "L", "L", "L", "L", "D", "D",
              "L", "L", "D", "D", "D", "D", "L", "L", "L", "L", "K"]

money = 400
tower_cost = 140

enemy_hp = 4

#text
pygame.font.init()
game_font = pygame.font.SysFont('MS Gothic', 30)
score_board = game_font.render(str(money) + "$", False, (250, 180, 0))

round_count_text = game_font.render("round: " + str(0), False, (0, 0, 0))
hp = 5
hp_count = game_font.render("hp:  " + str(hp), False, (250, 10, 10))

tower_cost_text = game_font.render("Tower cost:  100", False, (20, 10, 240))

for location in path:
    path_scaled.append([(16-location[0]) * 80, location[1] *80 -80])

notallowed_list = path_scaled

SPAWN_TIME = 1
actual_spawn_time = SPAWN_TIME * 60
min_spawn_time = 15
enemies = pygame.sprite.Group()

amount_per_wave = 1
wave_time = 180
max_wave_time = 300
wave_counter = 0
counter = 0
enemies_in_wave = 0
round_count = 0

enemy_speed = 5
max_enemy_speed = 8

wave_rn = True

def is_there_wave(counter):
    if counter >= wave_time:
        return True
    return False

def enemy_handler(c):
    if c >= actual_spawn_time:
        c = 0
        enemies.add(Enemy(1314, 360, enemy_speed, enemy_hp))
        return c
    return c

def towers_handler(enemy_pos):
    towers.update(enemy_pos)

def draw(money):
    screen.blit(world, (0, 0))
    enemies.draw(screen)
    towers.draw(screen)
    screen.blit(score_board, (20, 100))
    screen.blit(round_count_text, (640, 50))
    screen.blit(hp_count, (20, 50))
    screen.blit(tower_cost_text, (20, 150))
    if enemies:
        for tower in towers:
            tower.bullets.draw(screen)
            if not enemies: break
            if pygame.sprite.spritecollide(enemies.sprites()[0], tower.bullets, True):
                if enemies.sprites()[0].lose_hp(1):
                    money += 10


    pygame.display.update()
    return money


def snap(cords, width, height):
    cords = [(cords[0] // 80) * 80 + width, (cords[1] // 80) * 80 + height]
    return cords

def handle_enemy():
    enemies.update(enemy_path)
    if enemies:
        if enemies.sprites()[0].rect.x <= -80:
            enemies.sprites()[0].kill()
            return True
    return False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            check_pos = snap(pos, 0, 0)
            placable = True
            for position in notallowed_list:
                if check_pos == position:
                    placable = False
                    break
            if money < tower_cost:
                placable = False
            if placable:
                money -= tower_cost
                tower_cost += 20
                tower_cost_text = game_font.render("Tower cost:  " + str(tower_cost), False, (20, 10, 240))
                score_board = game_font.render(str(money) + "$", False, (250, 180, 0))
                notallowed_list.append(check_pos)
                pos = snap(pos, 40, 40)
                tower = Tower(pos[0], pos[1])
                towers.add(tower)

    if not wave_rn:
         wave_counter += 1
         wave_rn = is_there_wave(wave_counter)
    else:
        if enemies_in_wave < amount_per_wave:
            counter += 1
            counter = enemy_handler(counter)
            if counter == 0:
                enemies_in_wave += 1

        else:
            round_count += 1
            round_count_text = game_font.render("round: " + str(round_count), False, (0, 0, 0))
            amount_per_wave += amount_per_wave // 5 + 1
            wave_time += 15
            if wave_time > max_wave_time:
                wave_time = max_wave_time
            actual_spawn_time -= 2
            if actual_spawn_time < min_spawn_time:
                actual_spawn_time = min_spawn_time
            if round_count == 8:
                enemy_speed = max_enemy_speed

            if round_count == 10:
                enemy_hp += 2
            if round_count == 15:
                enemy_hp += 2
            if enemy_speed > max_enemy_speed:
                enemy_speed = max_enemy_speed

            wave_counter = 0
            enemies_in_wave = 0

            wave_rn = False

    if enemies:
        towers_handler(enemies)
    if handle_enemy():
        hp -= 1
        hp_count = game_font.render("hp:  " + str(hp), False, (250, 10, 10))
    if hp <= 0:
        running = False

    prevm = money
    money = draw(money)

    if prevm != money:
        score_board = game_font.render(str(money) + "$", False, (250, 180, 0))

    clock.tick(60)

pygame.quit()