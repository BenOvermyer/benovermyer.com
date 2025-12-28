+++
title = "Running Linux on my gaming PC again"
date = 2025-10-22
description = "I switched to Linux again. This time, I think it'll stick."
+++

With everything that's going on in the world right now, I am increasingly sensitive to the security and privacy implications of the tech I use. While most of my devices are in the Apple ecosystem, there has been one big hole in my device privacy footprint: my gaming PC.

I have been restricted to the Windows ecosystem on my gaming PC because of the games I regularly play. A few months ago, I reluctantly "upgraded" from Windows 10 to Windows 11. This made me anxious at the time, but then it faded into the background as other things took up my mental bandwidth.

Recently, though, Linux came back into my awareness. This past month, KDE celebrated its 29th birthday. This news was all over [Hacker News](https://news.ycombinator.com/item?id=45578117), Mastodon, and some other online social circles I run in. And with Windows 10 formally being sunset, I decided it was probably time to finally switch. Again.

See, I've tried running a Linux desktop before. Generally it works fine. However, two areas have made me stumble hard in the past: design software and games. I've relied on Affinity Suite for the former, which has no Linux version and no plans to have a Linux version. For the latter, I tend to play games that somehow always have game-breaking bugs on Linux, even with Proton.

This time around, I've tried a mixture of the latest developments in Linux and a willingness to change what software I use and what kinds of games I play in order to permanently break from Windows.

So, here's how it's going.

I chose [Debian](https://www.debian.org/) 13 with [Plasma](https://kde.org/plasma-desktop/) and [Wayland](https://wayland.freedesktop.org/). Debian is familiar because I've used Ubuntu a lot in the past, but has none of the bloat of the latter distribution. Wayland solves a lot of problems with some games I play, though it does create new problems with some other software. I'm still working through some of those, like Visual Studio Code having bad flickering unless I use a specific set of startup flags.

Incidentally, here're the options I use to fix the flickering for VSCode on Wayland:

```bash
code --use-gl=egl --ignore-gpu-blocklist --enable-gpu-rasterization --ozone-platform=wayland
```

Choosing new software for old problems has been the bigger jump. Instead of Affinity Photo, I'm trying out [GIMP](https://www.gimp.org/). GIMP is way better than it used to be. There's still a big learning curve, so it's an ongoing challenge. For vector work, I'm using Inkscape, which does what I need it to do. For office software, I've already been using LibreOffice on Windows for a long time, so that wasn't a hurdle.

I discovered that Fastmail has a desktop client for Linux. It's pretty new, apparently, but so far it works really well for me.

For games, well, that's been interesting. A lot of games that didn't work well on X11 now work on Wayland. Some don't. [The Finals](https://www.reachthefinals.com/), which is my primary shooter these days, currently has a shader bug that makes it unplayable. It was just introduced, so I don't know when it will get fixed. [Monster Train 2](https://store.steampowered.com/app/2742830/Monster_Train_2/), though, works flawlessly. I'm starting to explore new games that are built for Linux specifically, though, which is where things are getting more interesting. I might write a future post just about that.

Spotify works just fine on Linux, but I'm starting to make use of and grow my MP3 library again. I just discovered KDE's [JuK](https://juk.kde.org/) for playing music yesterday, and it's surprisingly awesome. That started me down the path of exploring [other KDE tools](https://apps.kde.org/), and I'm discovering a lot to love.

I think this is just the beginning of a paradigm shift in how I use my gaming PC. My Mac Mini and Macbook Pro feel a lot less necessary now, too. Time will tell how this shakes out.
