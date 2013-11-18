#!/usr/bin/env python
# encoding: utf-8

from karma import parse_promote, parse_demote

USER = 'user'
REASON = '中文測試'


def gen_expect_msgs(modify='++'):
    return [
        "%s%s %s" % (USER, modify, REASON),
        "%s%s #%s" % (USER, modify, REASON),
        "%s%s # %s" % (USER, modify, REASON),
        "hello! %s%s %s" % (USER, modify, REASON),
        "hello! %s %s %s" % (USER, modify, REASON),
        "hello! %s %s # %s" % (USER, modify, REASON),
        "hello! %s %s #%s" % (USER, modify, REASON),
    ]

def gen_unexpect_msgs(modify='++'):
    return [
        "%s%s" % (USER, modify),
        "%s%s" % (modify, USER),
        "++--",
        "--++",
        "-- %s, %s ++" % (USER, USER),
        "++ %s, %s --" % (USER, USER),
        "%s %s, %s -- # %s" % (modify, USER, USER, REASON),
        "%s %s, %s %s # %s" % (modify, USER, USER, modify, REASON),
        "<!%s #$Q#$@ %s!>" % (modify, modify),
    ]

def _test_parse(fun, modify='++'):
    for msg in gen_expect_msgs(modify):
        assert fun(msg) == (USER, REASON)
    for msg in gen_unexpect_msgs(modify):
        assert None in fun(msg)

def test_parse_promote():
    _test_parse(parse_promote, '++')

def test_parse_demote():
    _test_parse(parse_demote, '--')
