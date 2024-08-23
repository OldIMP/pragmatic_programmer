import abc
import argparse
import ast
import turtle


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, t: turtle.Turtle, param=None):
        raise NotImplementedError


class Movement(Command):
    def __init__(self, heading):
        self.heading = heading

    def execute(self, t: turtle.Turtle, param=None):
        t.setheading(self.heading)
        t.forward(int(param))


class Pen(Command):
    def execute(self, t: turtle.Turtle, param=None):
        t.pen(ast.literal_eval(param))


class PenDown(Command):
    # noinspection PyMethodMayBeStatic
    def execute(self, t: turtle.Turtle, _=None):
        t.pendown()


class PenUp(Command):
    # noinspection PyMethodMayBeStatic
    def execute(self, t: turtle.Turtle, _=None):
        t.penup()


COMMANDS = {
    'N': Movement(90),
    'S': Movement(270),
    'W': Movement(180),
    'E': Movement(0),
    'P': Pen(),
    'D': PenDown(),
    'U': PenUp(),
}


def translate_command(abbreviation):
    return COMMANDS[abbreviation.upper()]


PARSER = argparse.ArgumentParser()
PARSER.add_argument('command', type=translate_command)
PARSER.add_argument('param', nargs='?')


def parse_command(command):
    return PARSER.parse_args(command.split())


def main():
    t = turtle.Turtle()
    while True:
        command = t.screen.textinput('Next turtle move', 'e.g. S 100')
        if 0 == len(command): break
        args = parse_command(command)
        args.command.execute(t, args.param)


if '__main__' == __name__:
    main()
