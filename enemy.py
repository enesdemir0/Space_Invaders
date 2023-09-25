from turtle import Turtle

import random

move_list = [1, 2, 3, 4, 5]


class Enemy:
    def __init__(self, number):
        super().__init__()
        self.enemy_number = number
        self.y_pos = None
        self.x_pos = None
        self.all_enemy = []
        self.num_of_bullet = []
        for _ in range(self.enemy_number):
            self.num_of_bullet.append(0)
        self.bullet_list = []

    def create_enemy(self, x_pos, y_pos):
        new_enemy = Turtle("square")
        new_enemy.penup()
        new_enemy.color("#05ff43")
        new_enemy.shapesize(0.9, 0.9)
        self.x_pos = x_pos
        self.y_pos = y_pos
        new_enemy.goto(self.x_pos, self.y_pos)
        self.all_enemy.append(new_enemy)

    def forward_move(self):
        for enemy in self.all_enemy:
            move = random.randint(1, 10)
            enemy.left(move)
            enemy.speed("fastest")
            enemy.forward(3)

    def enemy_bullet(self):
        for num in range(self.enemy_number):
            if self.num_of_bullet[num] == 0:
                enemy = self.all_enemy[num]
                enemy_bullet = Turtle("circle")
                enemy_bullet.penup()
                enemy_bullet.goto(enemy.xcor(), enemy.ycor())
                enemy_bullet.color("#34a853")
                enemy_bullet.shapesize(0.3)
                enemy_bullet.right(90)
                self.bullet_list.append(enemy_bullet)
                self.num_of_bullet[num] += 1

    def move_bullet(self):
        for num in range(self.enemy_number):
            if self.bullet_list[num].ycor() > -300:
                self.bullet_list[num].forward(9)
            else:
                self.num_of_bullet[num] = 0
                self.bullet_list[num].goto(self.all_enemy[num].xcor(), self.all_enemy[num].ycor())


