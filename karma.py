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
    """@todo: Docstring for init_table.

    :name: @todo
    :returns: @todo

    """
    if bot.db:
        key = WHO
        columns = [key, KARMA, REASON]
        if not getattr(bot.db, name):
                bot.db.add_table(name, columns, key)
        return getattr(bot.db, name)
    print 'DB init fail!'

def get_karma(table, who):
    """@todo: Docstring for get_karma.

    :table: @todo
    :who: @todo
    :returns: @todo

    """
    karma, reason = str(0), str(None)
    try:
        karma, reason = table.get(who, (KARMA, REASON))
    except Exception:
        pass
    return karma, reason

@willie.module.rule('.*\+\+')
def meet_karma(bot, trigger):
    """@todo: Docstring for meet_karma.

    :bot: @todo
    :trigger: @todo
    :returns: @todo

    """
    table = init_table(bot, KARMA)
    msg = trigger.bytes
    who = msg.split('+')[0].strip()
    reason = msg.split('+')[2].strip()
    karma = get_karma(table, who)[0]
    table.update(who, dict(karma=str(int(karma) + 1), reason=reason))
    #bot.say("%s say: %s + 1, reason: %s" % (trigger.nick, who, reason))

@willie.module.commands('karma')
def karma(bot, trigger):
    """@todo: Docstring for karma.

    :bot: @todo
    :trigger: @todo
    :returns: @todo

    """
    if trigger.group(2):
        table = init_table(bot, KARMA)
        who = trigger.group(2).strip()
        karma, reason= get_karma(table, who)
        bot.say("%s: %s, reason: %s" % (who, karma, reason))
    else:
        bot.say("%skarma <nick> - Reports status for <nick>." % bot.config.prefix.split('\\')[1])


