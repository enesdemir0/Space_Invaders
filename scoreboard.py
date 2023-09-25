from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.g_over_write = Turtle()
        self.g_over_write.hideturtle()

        self.g_rule_write = Turtle()
        self.g_rule_write.hideturtle()

        self.g_victory = Turtle()
        self.g_victory.hideturtle()

        self.score = 0
        self.color("#05ff43")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score} ", False, "center", ("Arial", 16, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} ", False, "center", ("Arial", 16, "normal"))

    def new_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.g_over_write.color("#ea4435")
        self.g_over_write.penup()
        self.g_over_write.goto(0, 0)
        self.g_over_write.write("GAME OVER", False, "center", ("Arial", 32, "normal"))

    def game_rule(self):
        self.g_rule_write.color("#aaaaaa")
        self.g_rule_write.penup()
        self.g_rule_write.goto(-10, 210)
        self.g_rule_write.write("Use cursor keys ← → to move, Space to fire. ", False, "center", ("Arial", 10, "normal"))

    def victory(self):
        self.g_victory.color("#146eff")
        self.g_victory.penup()
        self.g_victory.goto(0, 0)
        self.g_victory.write("VICTORY", False, "center", ("Arial", 32, "normal") )




