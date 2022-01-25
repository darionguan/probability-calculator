import copy
import random


# Consider using the modules imported above.

# class Hat for representing a hat with different balls
class Hat:
    def __init__(self, **kwargs):  # use **kwargs for variable number of colored balls
        contents = []
        colors = []
        for attr in kwargs.keys():
            self.__dict__[attr] = kwargs[attr]
        # acquire the list of colors
        for color in kwargs:
            colors.append(color)
        # for each color
        for color in colors:
            # for number of balls of this color, extend the list with the string rep of the color
            # extend adds something to a list
            contents.extend([color for i in range(kwargs.get(color))])  # list comprehension
        self.contents = contents

    # method representing drawing a certain number of balls out of a hat
    def draw(self, number):
        lst = []
        # if the input is greater than number of balls in the hat, return the contents
        if number > len(self.contents):
            return self.contents
        else:
            # repeat draws for number in input
            for i in range(0, number):
                # select a random integer from 0 to the number of balls in the hat
                rand = random.randint(0, len(self.contents) - 1)
                # append that ball to my list
                lst.append(self.contents[rand])
                # remove it from the hat
                self.contents.remove(self.contents[rand])
        return lst

# function to do an n simulation of draws
# returns the percentage of getting the expected balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n = num_experiments
    # repeat experiments based on input
    for i in range(num_experiments):
        # copy variables so we don't edit the inputs
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        new_draw = hat_copy.draw(num_balls_drawn)
        check = True
        # for each dictionary key we check each color in expected balls
        for key in expected_copy:
            # count number of times the key color shows up in the new draw
            new_draw_count = new_draw.count(key)
            # value of expected balls
            expected_balls_count = expected_copy.get(key)
            # if the number in the draw is less than the expected we mark False
            if new_draw_count < expected_balls_count:
                check = False
            else:
                # if number in the draw is greater than or equal to expected we use pass to keep check = True
                pass
        # if check is True through the loop, then we met the expected balls and add 1 to m
        if check is True:
            m += 1
    return m / n
