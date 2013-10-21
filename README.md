# willie-karma
Karma is fun <3

```
          _ _ _ _            _
__      _(_) | (_) ___      | | ____ _ _ __ _ __ ___   __ _
\ \ /\ / / | | | |/ _ \_____| |/ / _` | '__| '_ ` _ \ / _` |
 \ V  V /| | | | |  __/_____|   < (_| | |  | | | | | | (_| |
  \_/\_/ |_|_|_|_|\___|     |_|\_\__,_|_|  |_| |_| |_|\__,_|

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
## Usage
![doc/willie-karma.png] [usage-pic]

## TODO
 - better parser 
 - you tell me

## Author
Timothy.Lee a.k.a MarlboroMoo.

## License
Released under the [MIT License].

  [Willie]: http://willie.dftba.net/ "Willie"
  [MIT License]: http://opensource.org/licenses/MIT "MIT License"
  [usage-pic]: https://github.com/marlboromoo/willie-karma/blob/master/doc/willie-karma.png "Usage"


