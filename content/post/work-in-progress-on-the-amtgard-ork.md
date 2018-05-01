---
title: "Work in progress on the Amtgard O.R.K."
date: 2016-06-28T06:48:52-05:00
description: ""
draft: false
---
I belong to an international live action role-playing game called
Amtgard. I'm a relatively new player at the time of writing this, with
less than a dozen credits in the game. However, I've been spending many
dozens of hours working on a web application we use called the Online
Record Keeper. While not the sole source of truth for Amtgard game
records, it has certainly become a popular tool among players. The
application is written in PHP and is backed by a MySQL database. It
doesn't use a framework or a caching mechanism. The source code can be
found [on Amtgard's GitHub](https://github.com/amtgard/ORK3). It has
great potential. There is a lot of awesome hidden in that code. But
there's also a lot of things that need to be fixed, and others that
need to be iterated on. After several months of working (on Saturdays,
usually) on doing a complete rewrite of the UI from scratch in Laravel,
I decided that the better move would be to fully own the existing code
and bring it up to modern standards. By doing this, I get more buy-in
from stakeholders and build trust for the future, but more importantly,
gain a much deeper understanding of how the system is *intended* to
work, not just how it appears to work. One of the ways in which I'll be
doing this is by blogging about the work I'm doing on the ORK from time
to time. This is the first such post. There are three big issues which
I'm concentrating on first.

Autoloading, Standards Compliance, and Dependency Management
------------------------------------------------------------

The current version of the code has its own autoloader and organizes
most of its code in classes. However, it doesn't use namespacing and
doesn't even come close to the [PSR-4
specification](http://www.php-fig.org/psr/psr-4/) set out by PHP-FIG. It
also checks its dependencies into the repo itself, without versioning or
documentation. I intend to bring the entire code base into line with
PSR-4 and convert it to using Composer to manage dependencies. As an
attendant update that fits in well with making the code base PSR-4
compliant, I also intend to make it
[PSR-1](http://www.php-fig.org/psr/psr-1/) compliant.

A New ORM: Propel
-----------------

The current ORM is a very, very old one that makes use of deprecated
MySQL functions. I plan to replace this with [Propel, a modern
ORM](http://propelorm.org/). It still uses the ActiveRecord pattern that
the old ORM uses, so the transition should be less onerous than it would
be if I used
[Doctrine](http://www.doctrine-project.org/projects/orm.html) instead.

A New Templating Engine
-----------------------

Currently the system uses a house-built templating engine. I plan to
replace this with [Twig](http://twig.sensiolabs.org/), a well-known and
well-supported templating engine for PHP. Though the PSR-4 task has the
most thought involved, this task has the most mind-numbing busywork,
since I'll have to convert all of the .tpl files (which use raw PHP)
into .twig files. I'm greatly looking forward to the end result,
however.

Where does ORK 4 fit in all this?
---------------------------------

You might question how my work on ORK 3.5/ORK 4 fits in with all of this
effort on ORK 3. One of the deliverables for ORK 4 is a JSON API that
replaces the ORK 3 JSON API. If I do all of the work specified above,
then writing a new ORK API from scratch will be unnecessary. However, I
have not yet dug into the code for the current API, so I might reverse
this position. ORK 4, rather than replacing ORK 3, will build on top of
it. At the moment, though, how that will be done is a bit nebulous.
We'll see where we're at after the above changes. �