import copy
import random

# random.seed(95)


# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        self.balls_drawn = []
        for color, ball_num in self.balls.items():
            for num in range(ball_num):
                # print(num)
                self.contents.append(color)

    def draw(self, times):
        self.contents.clear()
        for color, ball_num in self.balls.items():
            for num in range(ball_num):
                # print(num)
                self.contents.append(color)
        # print(self.contents)
        limit = len(self.contents)
        if times > limit:
            return self.contents

        for i in range(times):
            draw_ball = random.randrange(0, limit)
            self.balls_drawn.append(self.contents.pop(draw_ball))
            limit = len(self.contents)
        # print(self.balls_drawn)
        return self.balls_drawn

        # print(self.contents_copy)
        # if not self.contents_copy:
        #     self.contents_copy = copy.deepcopy(self.contents)
        #     # print(self.contents_copy)
        # limit = len(self.contents_copy)
        # if times <= limit != 0:
        #     for i in range(times):
        #         draw_ball = random.randrange(0, limit)
        #         # print('limit->', limit)
        #         # print('draw ball->', draw_ball)
        #         self.balls_drawn.append(self.contents_copy.pop(draw_ball))
        #         limit = len(self.contents_copy)
        #         # print('ball no:', i)
        #         # print(self.contents_copy.pop(draw_ball))
        #         # print(self.contents)
        #     # print(self.balls_drawn)
        #     return self.balls_drawn
        # else:
        #
        #     return self.contents_copy


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_to_match = expected_balls
    check_list = []
    got_result = 0
    for i in range(num_experiments):
        # print('Number of Experiment:', i+1)
        drawn_list = hat_copy.draw(num_balls_drawn)
        # print("drawn_list:", drawn_list)
        for color, ball_num in balls_to_match.items():
            # print('Ball Color:', color, 'Num:', ball_num)
            # print(drawn_list.count(color))
            # print(drawn_list.count(color) >= ball_num)
            if drawn_list.count(color) >= ball_num:
                # print('True:', color)
                # print('True:', ball_num)
                check_list.append(True)
            else:
                # print('False')
                check_list.append(False)
        # print(check_list)
        if False in check_list:
            check_list.clear()
            drawn_list.clear()
            continue
        else:
            got_result += 1
            # print(got_result)
        # print("Reset->", check_list)
        check_list.clear()
        drawn_list.clear()
    return got_result / num_experiments


hat = Hat(blue=3,red=2,green=6)
# print(hat.contents)
# hat.draw(2)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
