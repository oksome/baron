#!/usr/bin/python
# -*- coding:Utf-8 -*-

from indentation_marker import mark_indentation
from itertools import izip_longest


def check(input, output):
    for i, j in izip_longest(mark_indentation(input + [('ENDMARKER', ''), None]), output + [('ENDMARKER', ''), None]):
        print "DEBUG", i, j
        assert i == j


def test_empty():
    ""
    check([], [])


def test_dummy():
    "a"
    check([
        ('NAME', 'a'),
    ], [
        ('NAME', 'a'),
    ])


def test_dumy_if():
    """
    if a:
        pass
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('DEDENT', ''),
    ])


def test_dumy_if_if():
    """
    if a:
        if b:
            pass
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '        '),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '',  '        '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
    ])

def test_dummy_if_followed():
    """
    if a:
        pass
    pouet
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])

def test_dummy_if_followed_blank_line():
    """
    if a:

        pass
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('INDENT', ''),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ])

def test_dumy_if_dendent_quite_a_lot():
    """
    if a:
        if b:
            if c:
                pass

    pouet
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*1),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('IF', 'if', '', ' '),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*1),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])

def test_dumy_if_dendent_a_lot():
    """
    if a:
        if b:
            if c:
                pass
        if d:
            pass
            if e:
                pass

    pouet
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*1),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('IF', 'if', '', ' '),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', '    '*1),
        ('IF', 'if', '', ' '),
        ('NAME', 'd'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', '    '*2),
        ('IF', 'if', '', ' '),
        ('NAME', 'e'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*1),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', '    '*1),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'd'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*2),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', '    '*2),
        ('IF', 'if', '', ' '),
        ('NAME', 'e'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '*3),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])
