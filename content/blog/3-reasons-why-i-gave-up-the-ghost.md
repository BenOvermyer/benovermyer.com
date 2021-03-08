+++
title = '3 Reasons why I gave up the Ghost'
date = 2016-04-25
+++
This's about why I quit paying $10/month for a hosted Ghost blog and migrated everything back to a self-hosted WordPress blog. It wasn't easy, and I lost all images in the process, but here's why I made that leap.

# Getting my finances in order

$10.00 USD per month isn't much for someone in my socioeconomic class. It covers two deluxe lattés. However, I recently got hit with the Hammer of Reality, and I'm culling all unnecessary expenses. My definition of "unnecessary" got a big revision. As someone who makes roughly six figures a year, I can afford to spend money on things that have no real bearing on my happiness but satisfy temporary impulses. But I don't want to do that anymore. My family (id est, my dad) has always done that, and I inherited that behavior. But I'm not cool with it anymore. Not when over 30% of my take-home income is spent on debt. So, with [the teachings of Dave Ramsey](http://www.daveramsey.com/get-started/debt) once again firmly in my mind, and the experience of life recently burned in there, I'm improving the efficiency of my expenses. In this case, that means self-hosting my blog, since I already pay for a [Digital Ocean droplet](https://www.digitalocean.com/) to host other sites I manage.

# WordPress is more mature

Over the past year, not much has changed with Ghost. It's still the same basic Markdown-based blog engine that it was two years ago. Its market share (and, more importantly, developer mind share) has not significantly increased. By comparison, WordPress has seen thousands of new plugins, hundreds of new themes, and unmeasurable numbers of code contributions to plugins, themes, and WordPress core over the same time period. I could hate WordPress. It's written in PHP and follows code practices that are a decade out of date. However, I must recognize the stability of the platform, and the passion and strength of its community. There are a number of people much smarter and more experienced than myself who've made significant contributions to WordPress just over the past year. When it comes to maintaining a system on your own, the predictability and resilience of that system are very important metrics to consider.

# I am in full control of my content

This is not really so much a dig on Ghost as it is a dig on self-hosting versus hosted blogs. My reason for going with a self-hosted WordPress blog is the same reason I discounted going with WordPress.com hosting. I run the database behind the blog. I am in full control of every byte stored there. Whether it's backed up or not, where it's backed up, how it's backed up, that's all in my realm of control. I determine the version of PHP, the version of MySQL, and the version of Linux that hosts it all. I alone control access to the server, and how incoming (and outgoing) connections are treated. As someone who's spent the last year and a half as a site reliability engineer/manager, that has suddenly become of vital concern to me. And renting a VPS (Virtual Private Server) is much different than trusting someone else to manage your environment for you. The next step up, fully controlling the environment from bare metal on up, is too expensive for someone like me to handle on my own.

# So, to sum up (or TL/DR)...

I changed back to self-hosted WordPress from Ghost because A) I spend less money, B) I believe that WordPress is more likely to be supported in the future, and C) I like being able to control (almost) every aspect of how my blog exists.