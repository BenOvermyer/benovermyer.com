+++
title = "2023 Year in Review"
date = 2023-12-31
description = "Looking back at my 2023"
+++

2023 was a year of important changes and improvements in my life.
My goals for the year according to last year's ["Looking Ahead to 2023"](@/blog/2022-year-in-review/index.md) post
ended up going wide of the mark. I didn't succeed at the SGG goals
and I abandoned #dungeon23 early in January. I also didn't keep to
my ban on new entertainment. Where I did succeed, though, was in
the fitness goals for the year. More on that in a moment.

This year, I'll start including a few notes about what I accomplish
at my day job.

## Apiture

At my day job this year the biggest achievement was converting our
monitoring stack from New Relic to Prometheus+Grafana. The one gap
that remains is the profiling (what New Relic calls "APM"). I also
continued to make small improvements in several areas, like the new
ECS-based Wordpress architecture.

## Iron Arachne

Iron Arachne had a big year this year. In March, it reached its fifth
anniversary. Over the course of the year I made many updates to the
code to clean it up and reorganize it. The most important updates,
though, were the SvelteKit migration and the rework of the planet generator.

Prior to the SvelteKit migration, Iron Arachne was running as a static site
on Netlify. However, when I migrated it, it became a Node.js application
running on my own web server. This made it more difficult to manage, but
gave me way more freedom in the long run.

The planet generator rework happened in the last quarter of the year. Previously,
the images were set up as 3D scenes in THREE.js, with a sphere for the planet,
another sphere for clouds if they were present, a plane for the starfield, and
camera and light rigging. The rework turned them into a single shader capturing
everything. I finally implemented atmospheric scattering and dramatically improved
how the various planets looked. I also used this new rendering approach for the
star nation and star system generators.

## Self Hosting

Besides Iron Arachne, I also began to self host more things. I bought a mini PC,
installed Ubuntu on it, and set up several services on it. It's accessible via
our Tailscale network, meaning I can access it from any device that is part of
that network. Right now I have the following hosted on it:

- Jellyfin: for media
- Kavita: for browsing and reading PDFs
- IT Tools: for lots of little convenience utilities
- Paperless: for scanning and storing important documents

While Paperless is set up, I didn't really start using it properly in 2023. Same
for Jellyfin. I've used Kavita and IT Tools more.

## My Old Sites

I recreated as many of my old websites as I could find archived online and put them
online again on a subdomain of my main site. Some of these I'd completely forgotten
existed. In the course of this work, I also took inspiration from my old art galleries
to rework the art section of my main site. It reminded me of how much I used to love
making and sharing art.

## Reading Books

Holy crap. I read 34 books in 2023, which is three times what I read in 2022, and twice
my previous record. Granted, a lot of it was light fiction, but I still spent way
more time reading this year.

One reason for this is that I decided to create a new fan site for one of the fictional
cultures in the Valdemar novels by Mercedes Lackey. Before I can do that, I wanted to
refamiliarize myself with them, and so I began the process of reading every single novel
that they appear in. I forgot how much I enjoy these books. It's been a delight reading
them. Some of them are completely new to me, too, which is awesome.

I also finished the Honor Harrington series of novels by David Weber. Those were a harder
read, full of exposition and dense text. I enjoyed them too though.

## Health and Fitness

I started 2023 with a ban on alcohol that ended somewhere near the end of January. Running
became a regular routine for me; I ran in the morning on Mondays, Wednesdays, and Fridays
before work. My cardio health improved a lot; my VO2 max went from a low of 33.9 in January
to a high of 37.4 in April and a more sustained peak of 36.8 in the latter half of the year.
My cardio recovery went from 19 BPM in January to 37 BPM by the end of the year.

I stopped running in November when I undertook a self-imposed wellness challenge. For the
month of November, I drank no alcohol and began a bodybuilding routine at the gym. Four
days of the week I would go to the gym and lift weights. Cardio was limited to only a few
minutes of cooldown walking at the end of each workout.

The amount of weight I can lift improved a bit, but what really improved was my confidence
and interest in bodybuilding. Now I just need to reincorporate my cardio exercises and I'll
have a more complete fitness regimen.

## Silver Gryphon Games

We didn't make nearly as much progress on SGG in 2023 as I expected. I had planned on releasing
at least one new book by the end of March. We only released two playtest books later in the
summer; the new Aether and Ingenium editions. Despite trying to keep on top of Aethermancy it
ended up being a struggle to get the manuscript finished. As of this writing, it's still not
done.

Aether and Ingenium's second editions got completed manuscripts. Aether got a lot of editing.
The rise of AI art has made it a lot more difficult to find cheap artwork made by real artists.

## Previous Years

- [2022](@/blog/2022-year-in-review/index.md)
- [2021](@/blog/2021-year-in-review/index.md)
- [2020](@/blog/2020-year-in-review/index.md)
- [2018](@/blog/2018-year-in-review/index.md)
- [2016](@/blog/looking-back-on-2016-and-forward-to-2017/index.md)
- [2015](@/blog/2015-year-in-review/index.md)
- [2013](@/blog/2013-year-in-review/index.md)
