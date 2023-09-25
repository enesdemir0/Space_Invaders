from turtle import Screen, Turtle
from player import Player
from enemy import Enemy
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=400, height=600)
screen.bgcolor("#232629")
screen.title("My Space Invaders")

screen.tracer(0)

player = Player()

player_choice = screen.textinput(title="Which mode do you want to play ", prompt="for easy type 'e' for normal type 'n'"
                                                                                 "for hard type 'h': ")

turtle = Turtle("square")
turtle.shapesize(0.005, 100)
turtle.color("#05ff43")
turtle.penup()
turtle.goto(0, -230)

if player_choice == "e":
    speed = 0.05
    enemy_number = 6
elif player_choice == "n":
    speed = 0.02
    enemy_number = 9
else:
    speed = 0.01
    enemy_number = 12

scoreboard = Scoreboard()
scoreboard.game_rule()

enemy = Enemy(enemy_number)

screen.listen()
screen.onkeypress(player.right, "Right")
screen.onkeypress(player.left, "Left")

screen.onkeypress(player.create_bullet, " ")

game_on = True
player.go_play()

x_pos = -200
y_pos = 10
x = 1

for _ in range(enemy_number):
    if len(enemy.all_enemy) % 3 == 0:
        y_pos += 50
        x_pos = -200

    if len(enemy.all_enemy) < enemy_number:
        x_pos += 100
        enemy.create_enemy(x_pos, y_pos)

enemy.enemy_bullet()


def control(enemy_list):
    if len(player.bullet_list) == 1:
        for enemy in enemy_list:
            if enemy.distance(player.bullet_list[0]) < 10:
                enemy.color("#05ff43")
                enemy.goto(700, 700)
                player.bullet_list[0].goto(700, 700)
                scoreboard.new_score()
    else:
        pass


def control_1():
    for enemy_bullet in enemy.bullet_list:
        if len(player.player_list) > 0 and enemy_bullet.distance(player.player_list[-1]) < 10:
            player.player_list[-1].goto(700, 700)
            player.player_list.remove(player.player_list[-1])
            player.go_play()
        elif len(player.player_list) == 0:
            scoreboard.game_over()


def control_2():
    if len(player.bullet_list) == 1:
        enemy_list_index = -1
        for enemy_bullet in enemy.bullet_list:
            enemy_list_index += 1
            if enemy_bullet.distance(player.bullet_list[0]) < 10:
                player.bullet_list[0].goto(700, 700)
                enemy.num_of_bullet[enemy_list_index] = 0
                enemy.bullet_list[enemy_list_index].goto(enemy.all_enemy[enemy_list_index].xcor(),
                                                         enemy.all_enemy[enemy_list_index].ycor())
    else:
        pass


while game_on:
    screen.update()

    enemy.forward_move()

    enemy.move_bullet()

    player.move_bullet()

    control(enemy.all_enemy)

    if len(player.player_list) == 0:
        game_on = False

    if scoreboard.score == enemy_number:
        scoreboard.victory()
        game_on = False

    control_1()

    control_2()

    time.sleep(speed)

    screen.update()

screen.exitonclick()
