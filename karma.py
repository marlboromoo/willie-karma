#!/usr/bin/env python
# encoding: utf-8

"""
karma.py - A karma module for willie.
Copyright 2013, Timothy Lee <marlboromoo@gmail.com>
Licensed under the MIT License.
"""

import string
import willie

MODULE = 'karma'
WHO = 'who'
KARMA = 'karma'
REASON = 'reason'

def setup(bot):
    """Setup the database, create the table if not exist.

    :bot: willie.bot.Willie

    """
    if bot.db:
        key, name = WHO, KARMA
        columns = [key, KARMA, REASON]
        if not getattr(bot.db, name):
                try:
                    bot.db.add_table(name, columns, key)
                except Exception, e:
                    print "%s: Table init fail - %s" % (MODULE, e)
    print "%s: DB init fail, setup the DB first!" % MODULE

def get_table(bot):
    """Return the table instance.

    :bot: willie.bot.Willie
    :returns: willie.db.Table

    """
    return getattr(bot.db, KARMA)

def get_karma(table, who):
    """Get karma status from the table.

    :table: willie.db.Table instance
    :who: nickname of IRC user
    :returns: (karma, reason)

    """
    karma, reason = str(0), str(None)
    try:
        karma, reason = table.get(who, (KARMA, REASON))
    except Exception, e:
        print "%s: get karma fail - %s." % (MODULE, e)
    return karma, reason

def _update_karma(table, who, reason, method='+'):
    """Update karma for specify IRC user.

    :table: willie.db.Table
    :who: nickname of IRC user
    :reason: reason
    :method: '+' or '-'

    """
    karma = get_karma(table, who)[0]
    karma = int(karma) if karma else 0
    try:
        if method == '+':
            table.update(who, dict(karma=str(karma + 1), reason=reason))
        else:
            table.update(who, dict(karma=str(karma - 1), reason=reason))
    except Exception, e:
        print "%s : update karma fail, e: %s" % (MODULE, e)

def add_karma(table, who, reason):
    """Add karma for specify IRC user.

    :table: willie.db.Table
    :who: nickname of IRC user
    :reason: reason

    """
    return _update_karma(table, who, reason, '+')

def subtract_karma(table, who, reason):
    """Subtract karma for specify IRC user.

    :table: willie.db.Table
    :who: nickname of IRC user
    :reason: reason

    """
    return _update_karma(table, who, reason, '-')

def _parse_msg(msg, method='+'):
    """Parse the message.

    :msg: message
    :returns: (who, reason)

    """
    try:
        who = msg.split(method)[0].strip().split().pop()
        reason = msg.split(method)[2].strip()
        if '#' in reason:
            reason = reason.split('#')[1].strip()
        if len(reason) == 0:
            reason = None
        #. check if nickname only contain [a-Z_]
        for s in who:
            if s not in "%s_" % string.ascii_letters:
                who = None
                break
    except Exception, e:
        print "%s: parse message fail - %s." % (MODULE, e)
        return None, None
    return who, reason

def parse_add(msg):
    """Parse the message with '++'.

    :msg: message
    :returns: (who, reason)

    """
    return _parse_msg(msg, method='+')

def parse_subtract(msg):
    """Parse the message with '--'.

    :msg: message
    :returns: (who, reason)

    """
    return _parse_msg(msg, method='-')

def _meet_karma(bot, trigger, parse_fun, karma_fun):
    """Update karma status for specify IRC user

    :bot: willie.bot.Willie
    :trigger: willie.bot.Willie.Trigger

    """
    table = get_table(bot)
    if table:
        msg = trigger.bytes
        who, reason = parse_fun(msg)
        if who:
            reason = reason if reason else str(None)
            karma_fun(table, who, reason)

@willie.module.rule('.*\+\+')
def meet_add_karma(bot, trigger):
    """Update karma status for specify IRC user if get '++' message.
    """
    return _meet_karma(bot, trigger, parse_add, add_karma)

@willie.module.rule('.*\-\-')
def meet_subtract_karma(bot, trigger):
    """Update karma status for specify IRC user if get '--' message.
    """
    return _meet_karma(bot, trigger, parse_subtract, subtract_karma)

@willie.module.commands('karma')
def karma(bot, trigger):
    """Command to show the karma status for specify IRC user.
    """
    table = get_table(bot)
    if table:
        if trigger.group(2):
            who = trigger.group(2).strip().split()[0]
            karma, reason= get_karma(table, who)
            bot.say("%s: %s, reason: %s" % (who, karma, reason))
        else:
            bot.say(".karma <nick> - Reports karma status for <nick>.")
    else:
        bot.say("Setup the database first, contact your bot admin.")


