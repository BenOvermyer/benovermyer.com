+++
title = "Get Going with Laravel on Docker"
date = 2015-09-11
+++
_This post was updated May 14th, 2016 to significantly rework the tutorial._ Docker is slowly taking over the world of web infrastructure. It makes working with multiple different services easy, and the problem of “works in dev, not in prod” goes away, since you have the same environment on your local machine as you do in the production infra. It also makes things like trying out web apps without deploying them to servers really easy. Ever wanted to just check out a personal demo of, say, WordPress or Ghost? Docker makes that simple. Docker can be intimidating to start out with. It’s a complex beast, but once you’ve gotten it set up a couple times, it’ll become second nature. This article will walk through the entire process of having a completely new and fresh Mac OS X environment all the way to running Docker container with your own Laravel application. It’s a long tutorial, so grab a big mug of coffee and put on your favorite track and let’s get to work. _Note: This tutorial is for OS X. A lot of the pre-req stuff is different for Windows, so if you’re running that OS, you might be better off using Docker Toolbox. Until the new Docker App comes out, anyway._

# Prerequisites

The first step is getting some basic tools installed. OS X comes with git and Ruby installed, but we need to make a slight adjustment to our Ruby environment, and we’ll need Homebrew to install some other things.

## Homebrew

Let’s start with Homebrew. Paste this into a terminal prompt:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Running that will install Homebrew. Next, we’ll need Homebrew Cask:

    brew install caskroom/cask/brew-cask

This is used to install binary applications that otherwise you’d use a GUI for.

## Virtualbox

Let’s install this via Homebrew Cask to make things easy.

    brew cask install virtualbox

# Enter Docker

Now we get to the meat of it - installing Docker and the other tools necessary to work with containers. We’re going to be using a wrapper called dinghy for this. You could use the official [Docker Toolbox](https://www.docker.com/toolbox), but the default VM that it provides, boot2docker, relies on vboxfs, which makes real-time updates (like `gulp watch`) really slow.

## Install Docker Toolbox

When I originally wrote this post, Docker Toolbox made some questionable assumptions about how people were using Docker for development. Those have now been corrected, and it’s safe to go ahead and install Docker Toolbox. You can get that here: [https://www.docker.com/products/docker-toolbox](https://www.docker.com/products/docker-toolbox)

## Docker is installed! Now what?

Now everything is all set up and ready to get container-ing. In the next section, we’ll create a basic Laravel app to get a proper Docker workflow going.

# Getting set up for Laravel {#gettingsetupforlaravel}

For this tutorial, we’re going to use the Laravel framework. This will demonstrate how to use multiple containers while not requiring us to write a ton of code to get started.

## Install Composer

PHP is installed by default with OS X, but you’re going to need Composer also. Thankfully, it’s a quick install:

    curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

Make sure that composer is in your PATH in your bash/zsh profile. Look for this line: `~/.composer/vendor/bin` If it’s nowhere in the file, you’ll need to add something like this near the bottom of the file:

    export PATH="$PATH:~/.composer/vendor/bin"

## Install the Laravel CLI tool

This tool makes starting new Laravel projects much easier and faster:

    composer global require laravel/installer

## Start a new Laravel project

In a directory that makes sense for you (I use `~/Source/` for my code projects), run this shell command:

    laravel new docker-app

This will create a new Laravel project called “docker-app” in a new docker-app directory. You’re now ready to Docker-ize this app!

# Docker-ize! {#dockerize}

The next step is to create four files that we’ll use to describe our container environment. These files are `nginx-vhost.conf`, `supervisord.conf`, `Dockerfile`, and `docker-compose.yml`. Each of these is at the root of your project. The contents of each file is as follows:

## nginx-vhost.conf

We’re using nginx as the web server for this app. We could use Apache, but for this exercise, we’ll stick with nginx. The below file configures the virtualhost that will expose our Laravel app to the container.

    server {
     listen 80;
     listen [::]:80 default ipv6only=on;
     root /srv/www/public;
     index index.php;

     # Disable sendfile as per https://docs.vagrantup.com/v2/synced-folders/virtualbox.html
     sendfile off;

     # Add stdout logging
     error_log /dev/stdout info;
     access_log /dev/stdout;

     location / {
     try_files $uri $uri/ /index.php$is_args$args;
     }

     location ~ .php$ {
     try_files $uri =404;
     fastcgi_split_path_info ^(.+.php)(/.+)$;
     fastcgi_pass unix:/var/run/php5-fpm.sock;
     fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
     fastcgi_param SCRIPT_NAME $fastcgi_script_name;
     fastcgi_index index.php;
     include fastcgi_params;
     }

     location ~* .(jpg|jpeg|gif|png|css|js|ico|xml)$ {
     expires 5d;
     }
     # deny access to . files, for security
     location ~ /. {
     log_not_found off;
     deny all;
     }
    }

## supervisord.conf

We’re using Supervisor to run nginx and PHP-FPM. It makes things a little cleaner and easier. Below is the config file for Supervisor.

    [supervisord]
    nodaemon=true

    [program:php5-fpm]
    command=/usr/sbin/php5-fpm
    autostart=true
    autorestart=true
    priority=5

    [program:nginx]
    command=/usr/sbin/nginx
    autostart=true
    autorestart=true
    priority=10
    stdout_events_enabled=true
    stderr_events_enabled=true

## Dockerfile

For a guide to the syntax you see below, check out the [official Docker documentation for Dockerfiles](https://docs.docker.com/reference/builder/).

    FROM ubuntu:14.04
    ENV DEBIAN_FRONTEND noninteractive
    RUN apt-get update -y
    RUN apt-get install -y software-properties-common
    RUN add-apt-repository ppa:nginx/development
    RUN apt-get update -y
    RUN apt-get upgrade -y
    RUN apt-get install -y supervisor nginx php5-fpm php5-cli php5-curl php5-gd php5-mysql php5-memcached php5-mcrypt

    # Clean up to reduce container size
    RUN apt-get remove --purge -y software-properties-common
    RUN apt-get autoremove -y
    RUN apt-get clean
    RUN apt-get autoclean
    RUN echo -n > /var/lib/apt/extended_states
    RUN rm -rf /var/lib/apt/lists/*
    RUN rm -rf /usr/share/man/??
    RUN rm -rf /usr/share/man/??_*

    # Configure php-fpm to not run as a daemon
    RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
    RUN sed -e 's/;listen.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
    RUN sed -e 's/;listen.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf

    # Configure nginx to not run as a daemon
    RUN echo "daemon off;" >> /etc/nginx/nginx.conf

    # This next line lets nginx write to your working directory
    RUN usermod -u 1000 www-data

    # Configure nginx virtualhost
    RUN rm -Rf /etc/nginx/conf.d/*
    RUN rm -Rf /etc/nginx/sites-available/default
    ADD ./nginx-vhost.conf /etc/nginx/sites-available/default.conf
    RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

    # Add the application code into the container
    ADD . /srv/www

    # Configure Supervisor
    ADD ./supervisord.conf /etc/supervisor/conf.d/supervisor.conf

    # Fix permissions
    RUN chown -Rf www-data:www-data /srv/www/

    # Set our working directory
    WORKDIR /srv/www

    # Expose Ports
    EXPOSE 80

    # And finally, run the command to kickstart everything
    CMD ["/usr/bin/supervisord"]

The above file is telling Docker how to build the container. It includes nginx and PHP-FPM, but it leaves database and cache store to other containers. The container’s main job is to serve the Laravel application at `/srv/www` in the container on port 80 using nginx and PHP-FPM.

## docker-compose.yml

This file is what Docker Compose will use to build our stack and link up the containers the app needs to function. It defines three containers - web, db, and cache. The “volumes” part of the web container’s definition here will map your source code directory on your host to the container’s app directory, which will let you update your container by editing files on your host without having to rebuild the container. Under the db container, you’ll see the “environment” section. This is a list of environment variables that will be set in the MySQL container. The two blank ones will use the environment variable of the same name on your host to set them inside the container, which is far more secure than putting these values into version control! Just make sure that you set them! That’ll happen in your bash/zsh profile, with lines like this:

    export MYSQL_ROOT_PASSWORD=supersecurepassword1
    export MYSQL_PASSWORD=anothersecurepassword2

Alright. Without further ado, here’s the `docker-compose.yml` file:

    web:
     build: .
     ports:
     - "8080:80"
     volumes:
     - .:/srv/www
     links:
     - db
     - cache
    db:
     image: mysql:5.6
     environment:
      MYSQL_ROOT_PASSWORD:
      MYSQL_DATABASE: dockerapp
      MYSQL_USER: dockerapp
      MYSQL_PASSWORD:
    cache:
     image: memcached:latest

# Configure your Laravel app

Laravel 5.0 and later uses a `.env` file to configure the app. This is where you’ll give your app the settings it needs to talk to the other services (in this case, memcached and MySQL).

## .env

    APP_ENV=local
    APP_DEBUG=true
    APP_KEY=dhBKg8eSVZ3tH5yuz6z40j13X13YWTJf

    DB_HOST=db
    DB_DATABASE=dockerapp
    DB_USERNAME=dockerapp
    DB_PASSWORD=anothersecurepassword2

    CACHE_DRIVER=memcached
    SESSION_DRIVER=memcached
    QUEUE_DRIVER=sync

    MEMCACHED_HOST=cache

    MAIL_DRIVER=smtp
    MAIL_HOST=mailtrap.io
    MAIL_PORT=2525
    MAIL_USERNAME=null
    MAIL_PASSWORD=null
    MAIL_ENCRYPTION=null

# Run your new application container

Alright, we’re just about ready for the finale. First we need to run Docker Compose against our app to get it running.

    docker-compose build

This will build your container and fetch the other two from Docker Hub. It shouldn’t take too long - the longest part will be downloading mysql and memcached containers. Then, put your containers online:

    docker-compose up

Now try visiting [http://192.168.99.100:8080](http://192.168.99.100:8080) in your browser of choice. You might have to change the IP address to match that of your Docker machine (`docker-machine ip default` will give you that). You should see the Laravel welcome screen, and your work here is complete. _Note: don’t worry that your command prompt didn’t come back. This runs in the foreground, so you’ll need to use a new tab in your terminal app for other things. Or, you can use the daemon mode instead:_

    docker-compose up -d

Congratulations, you’re now working with Docker!
