NAME
####

::

 LIBBOT - the python3 bot namespave


DESCRIPTION
===========

::

 LIBBOT is a python3 library implementing the 'bot' package. It
 provides all the tools to program a bot, such as disk perisistence
 for configuration files, event handler to handle the client/server
 connection, code to introspect modules for commands, deferred
 exception handling to not crash on an error, a parser to parse
 commandline options and values, etc.

 LIBBOT provides a demo bot, it can connect to IRC, fetch and
 display RSS feeds, take todo notes, keep a shopping list
 and log text. You can also copy/paste the service file and run
 it under systemd for 24/7 presence in a IRC channel.

 LIBBOT is a contribution back to society and is Public Domain.


SYNOPSIS
========

::

 bot <cmd> [key=val] 
 bot <cmd> [key==val]
 bot [-c] [-d] [-v] [-i]


INSTALL
=======

::

 pipx install libbot


USAGE
=====


default action is doing nothing::

 $ bot
 $

first argument is a command::

 $ bot cmd
 cfg,cmd,dlt,dne,dpl,fnd,log,met,mod,mre,
 nme,pwd,rem,rss,sts,tdo,thr,ver

starting a console requires an option::

 $ bot -c
 >

list of modules::

 $ bot mod
 bsc,err,flt,irc,log,mod,rss,shp,sts,tdo,
 thr,udp

to start the bot as daemon::

 $ bot -d
 $ 

add -v if you want to have verbose logging::

 $ bot -cv
 BOT started Wed Nov 8 15:38:56 2023 CVI
 >


CONFIGURATION
=============


irc configuration is done with the cli interface
using the ``cfg`` command::

 $ bot cfg server=<server>
 $ bot cfg channel=<channel>
 $ bot cfg nick=<nick>

sasl need a nickserv nick/password pair to generate
a password for sasl::

 $ bot pwd <nsnick> <nspass>
 $ bot cfg password=<frompwd>

rss has several configuration commands::

 $ bot rss <url>
 $ bot dpl <url> <item1,item2>
 $ bot rem <url>
 $ bot nme <url> <name>


COMMANDS
========

here is a list of the most basic commands::

 cfg - irc configuration
 cmd - commands
 dlt - remove a user
 dne - mark todo as done
 dpl - sets display items
 fnd - find objects 
 log - log some text
 met - add a user
 mre - displays cached output
 nme - display name of a feed
 pwd - sasl nickserv name/pass
 rem - removes a rss feed
 rss - add a feed
 sts - show status
 tdo - add todo item
 thr - show the running threads


SYSTEMD
=======

save the following it in /etc/systems/system/botd.service and
replace "<user>" with the user running pipx::

 [Unit]
 Description=library to program bots
 Requires=network.target
 After=network.target

 [Service]
 Type=simple
 User=<user>
 Group=<user>
 WorkingDirectory=/home/<user>/.bot
 ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/bot -d
 RemainAfterExit=yes

 [Install]
 WantedBy=multi-user.target

then run this::

 sudo systemctl enable botd --now

 default channel/server is #bot on localhost


FILES
=====

::

 ~/.bot
 ~/.local/bin/bot
 ~/.local/bin/botd
 ~/.local/pipx/venvs/libbot/


AUTHOR
======

::

 libbot <libbotx@gmail.com>


COPYRIGHT
=========

::

 LIBBOT is a contribution back to society and is Public Domain.
