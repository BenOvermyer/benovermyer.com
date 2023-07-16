+++
title = 'First Node.js Hackathon'
date = 2014-01-14
+++
My employer is hosting an internal Node.js hackathon. I'm organizing it, but I'll also be participating since it's small enough that the logistics side is not going to take up all of my time. Everyone is charged with producing a Node app within 11 hours, and presenting to the group after that. For my project, here's what I've decided to go with. There are a few options out there for external commenting systems. You've probably heard of the big ones - Disqus and Livefyre. There are a handful of others, including Viafoura, Vicomi, and Instant Debate, but it's a space that doesn't see a lot of differentiation between the players. I propose, as my project, a commenting system that doesn't just facilitate discussion about a particular page, it uses meta information about that page to suggest similar discussions going on elsewhere on the site. Yeah, it's a little bit of a walled garden in that it focuses on only one particular site, but for commercial applications that seems ideal.

# Things that I'll need to account for:

1.  User authentication. I think I'll skip this entirely for the Hackathon, and just let users post anonymously.
2.  Retrieving meta information. I'll need to automatically populate a datastore with information on other pages. Since I only need to worry about pages that have discussion on them, this can happen when the first comment is submitted for a given URL.
3.  A rapid datastore. Commenting systems generate a lot of content very quickly, and speed is more important than integrity.
4.  A real-time widget. The front end for this needs to be real-time, but gracefully so. Websockets are necessary.
5.  Standard interactions. The widget needs to account for what are now standard interactions for commenting - replying to a previous comment, flagging a post as spam, upvoting, and downvoting.
6.  A moderation back end. An admin interface, initially accessible without authentication, needs to let admins review posts held for moderation… and approve or deny them in real time. It also needs to let admins know if a particular page is missing meta tags. Again, websockets are necessary. Planned Components

# Datastore

I decided to go with RethinkDB as my datastore of choice. It's very new and hence not production-ready, but its ease of use and blazing fast interaction suit this project well. The big problem to watch out for here is that Rethink loves eating up RAM with the current cache manager.

# Frontend Framework

My focus lately has been on ReactJS by the Facebook team. It's documented better than AngularJS, which was my go-to framework before this. It also has a more granular way of handling data binding that speeds up everything when dealing with a lot of elements on one page.

# WebSockets

Definitely going to be using SockJS. Socket.io's on its way out.

# Web Framework

Express.js. I would love to use the newer, promise-driven Koa.js, but it relies on an unstable version of Node.

# Task Running

Since the advent of Gulp, I have completely ceased to use Grunt. Gulp is just a better system, period. The only reason I've found to still use Grunt is if you need to use Yeoman to scaffold a project. So, with all that in mind, I'm using Gulp for this project.

# Package Management

I use Bower. It has its issues (security?), but I've never used anything else and have no real reason to find another option.

# Stylesheet Preprocessor

Sass. I've used both LESS and Sass, and Sass seems more reliable and predictable to me.

# Unit Testing

If I have time to do unit testing (yes, yes, I know), I'll be using Mocha. For assertions, I'll use Chai. To handle checking test coverage, I'll use CoverJS.

# Other Components

I'll be using RequireJS for sane modularization, Uglify for minification, and Twitter Bootstrap to style the whole thing quickly.
