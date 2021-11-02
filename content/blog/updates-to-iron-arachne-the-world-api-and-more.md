+++
title = 'Updates to Iron Arachne: The World API and more'
date = 2019-05-12
+++
It's been awhile since I blogged about [Iron Arachne](https://ironarachne.com). Much has changed since then.

The various disparate APIs have been collapsed into a single "[World API](https://github.com/ironarachne/world)." This makes it much easier to change, which means I can iterate faster and release more frequently. Also, the front-facing website is no longer a static JavaScript-powered site, but rather a full Laravel application. This lets me do a few clever things which I'll get into later.

The culture generator has added appearance generation. Skin colors, hair colors, face shapes, and so forth add to the depth of the output.

The region generator has dramatically improved economic traits. The trade goods are derived from the skill of the local artisans, the local agriculture, and the local available raw materials now. They also take into account the culture of the town.

Deities created by the pantheon generator now adhere to the culture the religion is from. Also, there are subtle improvements to how deities' domains are generated. No longer will multiple gods have the same domain.

The heraldry generator has had a few tweaks, too, though no new fields or charges have been added. Because the app was rewritten in Laravel, I now make use of caching via Redis to deliver consistent images and blazons. For example, here's one I quite like:

![](/eagles-head-erased.svg)

> Per saltire azure and argent, a lion's head erased Or

Some of the groundwork has been laid for organizing regions into countries. This is a step into a more difficult part of the world generator, since now I need to take into account location relative to other locations. Inevitably, I'll need to create a map generator. But that's a story for another day.
