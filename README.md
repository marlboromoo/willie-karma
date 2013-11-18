# willie-karma
Karma is fun <3

```
Willie -
 __  __
/\ \/\ \
\ \ \/'/'     __     _ __    ___ ___      __
 \ \ , <    /'__`\  /\`'__\/' __` __`\  /'__`\
  \ \ \\`\ /\ \L\.\_\ \ \/ /\ \/\ \/\ \/\ \L\.\_
   \ \_\ \_\ \__/.\_\\ \_\ \ \_\ \_\ \_\ \__/.\_\
    \/_/\/_/\/__/\/_/ \/_/  \/_/\/_/\/_/\/__/\/_/

```

## Requirments 
 - Python
 - [Willie] []

## Install

### Dependency
```
sudo su -
apt-get install python python-dev python-pip build-essential
pip install willie
```

### willie-karma
```
cd ~/.willie/modules/
git clone https://github.com/marlboromoo/willie_karma.git
ln -s willie_karma/karma.py ./
willie --configure-database #. setup the database for module to use
willie #. start the irc-bot
```
## Upgrade
```
cd ~/.willie/modules/willie_karma/
git pull
willie -q
williee -d
```
## Configuration
| [karma] | example | purpose |
| ------- | ------- | ------- |
| feedback | True | Notify by bot |
| byself | False | Self (pro&#124;de)mote |

## Usage
 * Use `.karma <nickname>` to get karma status.
 * Input `<nickname>++ [#] [Reason]` to promote.
 * Input `<nickname>-- [#] [Reason]` to demote.

## TODO
 - better parser 
 - you tell me

## Status
[![Travis CI Build Status] []] [Travis CI]

## Author
Timothy.Lee a.k.a MarlboroMoo.

## License
Released under the [MIT License].

  [Willie]: http://willie.dftba.net/ "Willie"
  [MIT License]: http://opensource.org/licenses/MIT "MIT License"
  [Usage example]: https://raw.github.com/marlboromoo/willie-karma/master/doc/willie-karma.png
  [Travis CI Build Status]: https://api.travis-ci.org/marlboromoo/willie-karma.png 
  [Travis CI]: https://travis-ci.org/marlboromoo/willie-karma


