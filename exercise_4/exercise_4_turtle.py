""" Exercise 4 - Turtle"""
import abc
import argparse
import ast
import turtle


class Command(abc.ABC):
    # pylint: disable=too-few-public-methods
    """Interface for all turtle commands"""

    @abc.abstractmethod
    def execute(self, t: turtle.Turtle, param=None):
        """Executes this command w/ the supplied `param`"""
        raise NotImplementedError


class Movement(Command):
    # pylint: disable=too-few-public-methods
    """Moves the turtle in the direction specified by :attr:`heading`"""

    def __init__(self, heading):
        self.heading = heading

    def execute(self, t: turtle.Turtle, param=None):
        t.setheading(self.heading)
        t.forward(int(param))


class Pen(Command):
    # pylint: disable=too-few-public-methods
    """Sets pen attributes as in :func:`~turtle.pen`"""

    def execute(self, t: turtle.Turtle, param=None):
        t.pen(ast.literal_eval(param))


class PenDown(Command):
    # pylint: disable=too-few-public-methods
    """Puts pen down"""

    # noinspection PyMethodMayBeStatic
    def execute(self, t: turtle.Turtle, _=None):
        t.pendown()


class PenUp(Command):
    # pylint: disable=too-few-public-methods
    """Raises pen up"""

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
    """Maps the one letter command to its implementation :class:`Command`"""
    return COMMANDS[abbreviation.upper()]


PARSER = argparse.ArgumentParser()
PARSER.add_argument('command', type=translate_command)
PARSER.add_argument('param', nargs='?')


def parse_command(command):
    """Parse user input to :class:`Command` & its `param`"""
    return PARSER.parse_args(command.split())


def main():
    # pylint: disable=missing-function-docstring
    t = turtle.Turtle()
    while True:
        command = t.screen.textinput('Next turtle move', 'e.g. S 100')
        if 0 == len(command):
            break
        args = parse_command(command)
        args.command.execute(t, args.param)


if '__main__' == __name__:
    main()
