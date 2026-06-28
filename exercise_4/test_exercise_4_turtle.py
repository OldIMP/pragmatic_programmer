# pylint: disable=missing-docstring
from unittest.mock import call, patch

from exercise_4_turtle import parse_command


def test_parse_movement():
    assert_parse_execute("W 3", call.setheading(180), call.forward(3))


def test_parse_pen():
    expected_call = call.pen({"pensize": 20})
    assert_parse_execute('p {"pensize":20}', expected_call)


def test_parse_pen_down():
    assert_parse_execute("d", call.pendown())


def test_parse_pen_up():
    assert_parse_execute("U", call.penup())


def assert_parse_execute(param, *expected_calls):
    with patch("turtle.Turtle") as t:
        args = parse_command(param)
        args.command.execute(t, args.param)
        assert list(expected_calls) == t.method_calls
