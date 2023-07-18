+++
title = "2022 Year in Review"
date = 2022-12-31
description = "Looking back at my 2022"
+++

2022 was a year of big changes. Some were foreseen and others came out of nowhere.

## 40th birthday trip to Hawai'i

At the end of February, we went to Hawai'i for my 40th birthday. Our trip was exclusively to the Big Island. We stayed in three different places - a small Bali-themed apartment, a treehouse in the rainforest, and a resort hotel. The treehouse was definitely both the scariest and the most interesting. I say "scariest" because the bottom floor was open and there's a ton of wildlife, including wild pigs. However, it was gorgeous. I would stay there again.

We went on a tour of a coffee plantation. I gained a newfound appreciation for Kona coffee because of that. Sadly, it's hard to get locally here in North Carolina. We also went to some interesting restaurants. My favorite was a sushi restaurant with only three tables that I managed to get a reservation at, despite reservations being hard to come by.

One day when we were staying at the treehouse we went to see a big volcano. It was gorgeous, and the walk was fun. We got a lot of great photos from the trip, and some of the volcano shots were among the best.

## Moving to Wilmington, North Carolina

In January, I spent the month in Wilmington, North Carolina looking for a place to rent. A few days into my stay at my boss's condo on the beach, I found the perfect house and got everything signed and sorted out. I moved out of the condo and into the completely empty house. I bought a few things - really, just enough to survive for the month. Sarah visited for a couple weeks to see the place and explore the area.

Before Sarah visited, I'd had another panic attack in January - my second ever - and it made me nervous. Throughout the first half of 2022, I experienced symptoms that would be near to the start of a panic attack, but I'd learned how to stave them off.

The month of February we spent getting everything ready to move, and taking that trip to Hawai'i.

March was the month we moved from Minneapolis to Wilmington. We packed up the house, and then I took Mojave and Kalahari in my Seltos and drove to our new home. The cats didn't much care for the road trip - they spent the majority of it curled up together behind the center console. The drive took three days. I hope to never make such a long drive again, especially with cats in tow. Sarah drove down after the movers came and hauled away all of our stuff. This was the first time I had personally hired movers for an interstate move. It didn't go as well as I'd hoped, but it also didn't go as badly as I'd feared. The weirdest part was having to pay in cash instead of with a card.

Over the course of the next month or so, we got unpacked and moved in. Exploring Wilmington was not as much of a priority as establishing a sense of normalcy. We didn't go to the beach as much as we perhaps should have this first year in Wilmington. However, I did bike to the beach twice after we got our bicycles. That's a 45 minute bike ride, which is the longest I've ever taken, I think. The climate here on the coast is a welcome change from Minneapolis, especially now in the cold months. As I write this it's 48 degrees Fahrenheit, with the expected high being 66. Not bad for December 30.

## Iron Arachne

Iron Arachne saw a great many updates over the course of the year. In June, I launched a dungeon generator for it. That was a huge project that I'd never quite figured out before and I was pretty proud of what I'd built. It wasn't as full-featured as others around the web, but it was mine. Writing it required a ton of small subsystems like room layout and distributing keys and monsters and whatnot. I added a ton of new sentient species. I rewrote the word generation system from scratch, and added a utility generator to the site to help me come up with new seed patterns for the generator. The region generator, too, saw a bunch of changes - in particular, adding nearby regions, including vassal states; as well as making name set generation for it configurable.

After awhile I noticed that the language generator in the code base wasn't complete and wasn't used anywhere. So, I started expanding that. It's not complete yet, and I haven't touched it in months. I intend to get back to it at some point, but it's not a priority. In November, I changed the build system to use Node.js 18, and then later in the month migrated it to Vite. At the end of November, I also moved all the navigation to a dedicated page. This change was a long time in coming and finally made the site usable on mobile.

At the end of 2021, I wrote that I'd update the culture, heraldry, and region generators. Well, I didn't touch the culture generator much, other than to flesh out some details and swap out the religion generator for it. I did add new charges to the heraldry generator. The region generator really saw the bulk of the changes. In addition to the dungeon generator, I also added an AD&D 2e character generator. That was the first time I'd ever written a complex generator as the result of a poll. I don't think I'll do that again any time soon; I really prefer working on generators of my own interest. In January I'd added a DCC character generator. That was more fun.

Finally, I moved the site from [Netlify](https://www.netlify.com/) to [Vercel](https://vercel.com/), to give it a little more separation from my personal sites.

## Updates to my personal website

My personal website saw a number of expansions and design changes this year. I redesigned it a bit after learning more about minimal CSS. The whole thing is designed to be quick to load even on much older and slower hardware. I added several books to my "books read" list, several blog posts, a few recipes, and a handful of new knowledge base articles.

I'm increasingly determined to make my site a proper storehouse of information and stories dear to me. It would be nice if someone out there found it useful, or at least interesting. Failing that, it's still useful to me.

## Giving up alcohol

Probably one of the biggest personal changes happened on November 10. Tired of all the negative effects of drinking, I finally gave it up completely. I had become accustomed to drinking every other night, sometimes six or more drinks. Going sober was much easier than I'd expected. The positive effects were much more noticeable than I expected, too. The most noticeable was how much more energy I had all the time after a couple weeks. Also, caffeine's effects on me changed. Instead of needing caffeine to properly function in the morning, now it makes me jittery if I have the same amount that I used to.

I'm also dreaming again for the first time in years. Starting somewhere around 2015 or so, I stopped having dreams except only occasionally. Now I dream almost every night. They're the same kind of dreams I used to have - full of action and strangeness, like little movies that don't make a ton of sense. I'd forgotten how much fun they can be.

## From individual contributor to manager to tech lead

For a brief period early in the year, I was one of two new managers on the Platform Engineering team. However, the higher-ups felt that was unnecessary and a waste of our technical talents, so we got turned into tech leads instead.

I don't handle any of the managerial duties, but I'm responsible for setting technical direction and leading standups. I didn't get a raise to go with the role change. My boss's boss assured me that was just because it fell outside the annual review cycle. I'm skeptical that I'll get a raise in the new year, though. While I make plenty, inflation means that if I don't get at least a raise matching the inflation rate, I'm actually getting a pay deduction each year. That feels kinda bad.

Also, when the legacy (but stable) side of the business merged with the "startup" side that I'd originally joined, my duties changed. I'm working with a lot of legacy tech, including Perl applications. I don't like that at all. It feels like a bait-and-switch; I was hired to work on the latest tech and explore new horizons, but now most of my time is spent modernizing legacy systems and trying to figure out how to use modern tools with ancient technology.

The pay and benefits are good, and I like the people I work with. However, I'm starting to feel stifled by some of the work, and I'm definitely not as engaged as I was before the merger.

## AWS Re:invent 2022

The last time I went to Re:invent was 2016. The conference doubled in size; there was at least 60,000 people there this year. I tried to go to a dozen different sessions, but only got into one. I later made a presentation for my team about that session.

Going sober definitely had a big impact on my Re:invent experience. At Re:invent in 2015 and 2016, I drank a _ton_ and went bar hopping with a bunch of strangers I met at the conference. This time around, I wasn't drinking at all, and a lot of the activities I used to enjoy seemed boring now. I also had a lot more energy for activities in the morning.

Re:invent had special areas and swag for people with AWS certifications, so I used the half-off voucher they gave me beforehand to get certified. This was the first certification I'd ever paid for. It took a couple weeks of studying, but I passed the exam with flying colors and got my certification. It was a very strange experience, studying for an exam. I hadn't done that since university. I didn't care for it at all.

## End of my boycott of Blizzard

I wrote at greater length about this [earlier this year](@/blog/checking-back-in-on-blizzard/index.md). Since that post, I've played a ton of Overwatch 2 and World of Warcraft. I didn't play much Diablo 2 and uninstalled it. I did preorder Diablo IV, despite the controversy surrounding its launch date. Blizzard is definitely still having problems. I don't think I'll boycott them again, as it had no material effect on anything. We'll see how things turn out. There's still the Microsoft acquisition to consider... if it goes through.

## Silver Gryphon Games comes back

In August, Kevin and I made the decision to [revive Silver Gryphon Games](https://www.silvergryphongames.com/2022/10/21/celebrate-with-us-as-silver-gryphon-games-returns/). This time around, though, I was the one to submit all the registration paperwork and manage the company side. I'm hoping that by being the driving force I can avoid the deliverables problems we had before. We committed to fulfilling the Aethermancy Kickstarter that we abandoned years ago. Also, I'm writing the new edition of Aether. This is the first time I've had an active hand in Aether. While I'm much more interested in writing OSR games, Aether reminds me a lot of what the Palladium System could have been if it was... well, good. For the first time in a long time, I'm really excited about writing for a commercial RPG. Kevin's working on Aethermancy while I work on Aether. He's heavily involved in his retail games business, though, so he's much more distracted than I am. Hopefully I can do right with Aether by him.

## Summary

This is by far my longest year-in-review post I've ever made. A ton happened in 2022. I imagine a lot is going to happen in 2023, too. Tomorrow I'll write about all my plans for the new year.

Here's a list of all the year-in-review posts I've made. I have the strange sense that I've written more of these, but they're either lost to time, or in physical journals. I might have to try and find them if that's the case.

- [2021](@/blog/2021-year-in-review/index.md)
- [2020](@/blog/2020-year-in-review/index.md)
- [2018](@/blog/2018-year-in-review/index.md)
- [2016](@/blog/looking-back-on-2016-and-forward-to-2017/index.md)
- [2015](@/blog/2015-year-in-review/index.md)
- [2013](@/blog/2013-year-in-review/index.md)
