#!/usr/bin/env python
# encoding: utf-8

"""
karma.py - A karma module for willie.
Copyright 2013, Timothy Lee <marlboromoo@gmail.com>
Licensed under the MIT License.
"""

import willie

WHO = 'who'
KARMA = 'karma'
REASON = 'reason'

def init_table(bot, name):
    """Return the table instance, create it if not exist.

    :name: table name
    :returns: willie.db.Table

    """
    if bot.db:
        key = WHO
        columns = [key, KARMA, REASON]
        if not getattr(bot.db, name):
                bot.db.add_table(name, columns, key)
        return getattr(bot.db, name)
    print 'DB init fail!'

def get_karma(table, who):
    """Get karma status from the table.

    :table: willie.db.Table instance
    :who: nickname of irc user
    :returns: (karma, reason)

    """
    karma, reason = str(0), str(None)
    try:
        karma, reason = table.get(who, (KARMA, REASON))
    except Exception, e:
        print e
    return karma, reason

def parse_msg(msg):
    """Parse the message send from irc user.

    :msg: message
    :returns: (who, reason)

    """
    try:
        who = msg.split('+')[0].strip().split().pop()
        reason = msg.split('+')[2].strip()
    except Exception, e:
        print e
        return None, None
    return who, reason

@willie.module.rule('.*\+\+')
def meet_karma(bot, trigger):
    """Update karma status for specify irc user.
    """
    table = init_table(bot, KARMA)
    if table:
        msg = trigger.bytes
        who, reason = parse_msg(msg)
        karma = get_karma(table, who)[0]
        if all([who , reason, karma]):
            if len(reason) == 0:
                reason = str(None)
            try:
                table.update(who, dict(karma=str(int(karma) + 1), reason=reason))
            except Exception, e:
                print "Update fail, e: %s" % (e)

@willie.module.commands('karma')
def karma(bot, trigger):
    """Command to show the karma status for specify irc user.
    """
    table = init_table(bot, KARMA)
    if table:
        if trigger.group(2):
            who = trigger.group(2).strip()
            karma, reason= get_karma(table, who)
            bot.say("%s: %s, reason: %s" % (who, karma, reason))
        else:
            bot.say(".karma <nick> - Reports karma status for <nick>.")
    else:
        bot.say("Setup the database first, contact your bot admin.")
