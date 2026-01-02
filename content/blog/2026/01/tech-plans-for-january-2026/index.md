+++
title = "Tech plans for January 2026"
date = 2026-01-02
description = "My tech-related plans for the first month of the year"
+++

This is a look into my tech-related plans for January. Originally I considered making this a "tech plans for 2026" post, but I have a feeling my plans are going to change as the year progresses.

## Iron Arachne's Huge Update

Iron Arachne is getting a massive update this month. I've been working on a huge update to the random number generation paradigm across the entire code base, and while I was digging into literally everything, I ended up deciding to make several other sweeping changes.

Among these is a complete rewrite of the dungeon generator. Since the dungeon generator is built out of several subsystems, I have been slowly rewriting each of those in turn. The first was the treasure generator. The new version is much better than the old version, by leaps and bounds. I resisted introducing randomness until I felt I had built enough complexity into the deterministic version. It's still deterministic, but one of the inputs is an alphanumeric seed that the local random number generator uses. It's much easier to test. Because of how I've written it, the treasure generator can be independent. So, it will be, with a new generator page just for treasure.

My next subsystem is equipment. Again, this is sufficiently complex that I imagine it will be its own independent generator page. The underlying item system is another complete rewrite. Other generators rely on the old system and will need to be rewritten to use the new system. For example, the religion generator uses the item system for holy items. The magic weapon generator also uses it. The new item system is both less complex than the old system and more versatile, so I should be able to do much more with it.

After I rewrite the equipment subsystem, I'll need to incorporate that into the treasure generator. Then I'll begin working on the encounter generator. The encounter generator is going to be a big rewrite because it relies on the character generator, which is by far the most complex generator in the entire code base. I will try and resist rewriting the character generator right now, because that would be an enormous task in itself. There is a completely new subsystem, the faction generator, that will be used as an input for the encounter generator. So, once the encounter generator is done, I'll probably work on that.

I won't go into all of the various subsystems here, since there are a lot of them. However, I'll list them out, mentioning whether they're new or a rewrite.

- Grid manager (new): for handling the coordinate space of the dungeon, including bounds-checking and such.
- Layout architect (new): for deciding where rooms go. This replaces the existing layout function, which is a big mess and inefficient.
- Corridor pathbuilder (new): for connecting rooms.
- Door and gateway builder (rewrite): for figuring out where walls should be breached, as well as locked, trapped, and secret doors.
- Theme applier (new): for applying biomes and other themes to areas of a dungeon.
- Lighting and shadow engine (new): for figuring out where lighting goes and what its effects are.
- Acoustics generator (new): for figuring out what sounds are present in various rooms, for description purposes mostly.
- Faction generator (new): for creating appropriate factions to the dungeon.
- Encounter generator (rewrite): for populating the dungeon with characters, creatures, and monsters.
- History generator (new): for mutating the dungeon to add, remove, or change various aspects over time.
- Treasure generator (rewrite): for generating treasure hoards as well as loot for individual characters.
- Trap and hazard generator (new): for adding traps and other environmental hazards to the dungeon.
- Lock and key generator (rewrite): for making sure all locked doors and chests have a key in a way that is solvable.
- Prop and clutter placer (new): for adding flavor to rooms.
- Lore generator (new): for adding details to plaques, books, and so on that are consistent with the history of the dungeon.
- Connectivity checker (new): for making sure all rooms are reachable from the entrance.

I think that's all of them. As you can see, it's a long list, and a big project. It's entirely possible that I won't be able to finish it all in January.

While I've been working on this, I also rewrote a couple other generators or otherwise made big changes to them. The Dungeon Crawl Classics generator got a complete rewrite, though this should be transparent to users, except for a few bugs being fixed. The heraldry generator got a _ton_ more charges and a few other updates and bug fixes.

## Switching Away From US-Based Services

In 2025, I made an effort to migrate away from US-based services. Here's a list of all the changes I made.

- Cloudflare DNS to [Bunny](https://bunny.net) DNS
- Google Drive, iCloud, and Sync to [Filen](https://filen.io)
- AWS to Scaleway
- Crunchyroll, Hulu, Disney+, Paramount+, and Max just got dropped altogether
- Replaced Firefox with Vivaldi

Now, I'm looking to replace the following.

- Google Maps: going to try [Here WeGo](https://wego.here.com/) and [Magic Earth](https://www.magicearth.com)
- Todoist: not sure, maybe I can use Obsidian plus my calendar. I hear good things about [Super Productivity](https://super-productivity.com/?ref=github), though
- GitHub: [Codeberg](https://codeberg.org) for everything public, and maybe [SourceTube](https://source.tube) for private repos
- VS Code: possibly [VSCodium](https://vscodium.com), but I'm also considering [JetBrains](https://www.jetbrains.com), or maybe [Helix](https://helix-editor.com) if I can set it up like an IDE
- DuckDuckGo: not sure, this will require research
- Netflix: not sure, maybe [Crave](https://www.crave.ca/en)? But also more DVDs and Blu-rays
- Spotify: moving to mostly [Bandcamp](https://bandcamp.com) and local MP3s
- Fastmail: [Proton Mail](https://mail.proton.me) is the obvious choice, but I want to do more research
- Fly.io: Probably [Scaleway](https://www.scaleway.com/en/), since I use that anyway
- Netlify: maybe [Coolify](https://coolify.io), hosted on a Hetzner VPS?

Replacing all of these won't happen in just one month. I will probably need to work on this over several months, especially for the things that are connected to more of my life, like Fastmail.
