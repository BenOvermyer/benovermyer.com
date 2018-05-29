---
title: "Generating Fantasy Worlds"
date: 2018-02-16T13:55:46-06:00
description: "How would you go about procedurally generating an entire fantasy setting?"
draft: false
---
One of my favorite things to think about is the procedural generation of fantasy settings. There are a few people [doing interesting work](https://heredragonsabound.blogspot.com/) on procedural generation of components of settings, but no one is really looking at the big picture.

Well, that's not quite true; [Dwarf Fortress](http://www.bay12games.com/dwarves/) does a great job of simulating the evolution of a fantasy world.

However, the area that I'm focused on is on the generation of settings for the purpose of fantasy tabletop gaming. To my knowledge, no one is working on this problem. As part of my exploration of this domain, I'll have to borrow lessons from other types of procedural generation.

I once attended a game convention where Ed Greenwood (of Forgotten Realms fame) was a guest speaker. He explained how he starts working on a fantasy setting. He starts with the trade routes between towns, using exports and imports to derive what the culture of a particular area is like. I'm going to take a similar route to get started.

You can follow my efforts [here](https://github.com/BenOvermyer/country-maker). For the moment, it's written in PHP. Once I have the logic solidly in place, I will likely rewrite it in Go or something similar for performance reasons.