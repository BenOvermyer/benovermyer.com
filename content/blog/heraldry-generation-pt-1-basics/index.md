+++
title = 'Heraldry Generation Pt. 1: Basics'
date = 2018-03-12
+++
Awhile back I noted that I was beginning to work on a random fantasy setting generation project. This is the first piece of that.

It represents part of the design philosophy of the setting generator: each piece does one thing, it does it well, and it does it in a way that can be shared amongst the ecosystem.

The heraldry generator starts out life, then, with this guiding principle: output an image in a common format that can be programmatically modified, along with the necessary metadata to describe what's in the image for both humans and machines.

For the image format, I chose SVG. It's basically just XML, which makes it easy to modify, and it's relatively small. Also, it's a vector format, which makes it trivial to scale without degradation.

For rapidity of development, I chose to code the generator in PHP. I may rewrite it in a more performant language later if necessary. For now though, this serves my purposes.

Initially, I used a pre-existing library that handles SVG. However, after I got the initial plain-field version working, I discovered that the library doesn't support `<mask>` elements yet, which meant I wouldn't be able to easily generate field divisions and clip them.

The second iteration, then, stripped out that library and went straight for raw XML manipulation. This ended up working much better for several other things, including arbitrary attribute manipulation.

Heraldry adheres to certain rules. Coats of arms are basically like modern-day road signs; they exist to communicate clearly at a distance. So here are the rules I'm assuming for the generator:

1.  If a charge is a metal, its field may not be primarily a metal, and likewise with colors.
2.  Only fields and charges common to Continental heraldry in the era between the 10th and 16th centuries will be considered.
3.  Tinctures will include colors, metals, and furs common for the era. English “stains” like _sanguine_ will not be included.

I may modify this list later, but it's my guiding set right now.

At the moment, the generator only creates coats of arms with basic fields. It's either a single color, or includes _per fess_ or _per pale_ divisions, also in colors. Metals are being reserved for charges at the moment, which are not included yet.

Here's a simple example of a plain field:

![Basic Field](/heraldry-basic-field.svg)

The tincture generation is being done at a higher level so that the program is aware of which tinctures are used in the entire design. This is so it can avoid violating the first rule.

However, sometimes the divisions are generated in the same color (e.g., _azure_ next to _azure_). I'll need to fix this in the next iteration.

The below image may look identical to the first one, but it's actually divided, just with both halves being _vert_.

![Duplicate Colors in a Division](/heraldry-duplicate-colors.svg)

Still, the basic design looks reasonable thus far. Here's a simple _per fess_ example:

![Basic Division](/heraldry-basic-division.svg)

The source code for the generator is available [on GitHub](https://github.com/ironarachne/heraldry).
