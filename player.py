from turtle import Turtle

position = [-170, -130, - 90]


class Player:
    def __init__(self):
        self.player_list = []
        self.create_player()
        self.bullet_list = []

    def create_player(self):
        for number in range(3):
            new_player = Turtle("triangle")
            new_player.penup()
            new_player.color("#05ff43")
            new_player.goto(position[number], -260)
            self.player_list.append(new_player)

    def go_play(self):
        if len(self.player_list) > 0:
            current_player = self.player_list[-1]
            current_player.goto(-170, -210)
            current_player.left(90)
        else:
            pass

    def right(self):
        if len(self.player_list) > 0:
            current_player = self.player_list[-1]
            current_player.goto(current_player.xcor() + 15, current_player.ycor())

    def left(self):
        if len(self.player_list) > 0:
            current_player = self.player_list[-1]
            current_player.goto(current_player.xcor() - 15, current_player.ycor())

    def create_bullet(self):
        if len(self.bullet_list) == 0:
            current_player = self.player_list[-1]
            bullet = Turtle("circle")
            bullet.penup()
            bullet.color("white")
            bullet.left(90)
            bullet.shapesize(0.3)
            self.bullet_list.append(bullet)
            bullet.goto(current_player.xcor(), current_player.ycor())
        else:
            pass

    def move_bullet(self):
        if len(self.bullet_list) == 1 and self.bullet_list[0].ycor() < 300:
            self.bullet_list[0].forward(20)

        elif len(self.bullet_list) == 1:
            self.delete_bullet()

    def delete_bullet(self):
        self.bullet_list[0].hideturtle()
        self.bullet_list.remove(self.bullet_list[0])
