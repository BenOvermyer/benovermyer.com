---
title: "Heraldry Generation Pt. 3: Animal Charges and Windows Builds"
date: 2018-05-05T08:00:00-06:00
description: "A few updates make the program more accessible to others."
draft: false
---
Since the last entry, I've made several changes to both the program logic and its features.

The main change to the logic is in how charges are rendered. Instead of all of the SVG rendering code being in one file, now the more complex charges each have their own file. This was necessary, since the lines of text required for each complex charge (e.g., animals) is enormous. SVG files lay out pathways as a series of points, and with the large number of points involved in these shapes, the line count gets huge.

The main feature update is that now I've added a handful of animal charges. I got the first four (dragon passant, fox passant, gryphon passant, and eagle displayed) from [an open source repository by Victor Westmann](https://github.com/victorwestmann/Heraldry). The fifth, the lion rampant, is from a vector stock set that I purchased from VectorStock and converted to SVG myself. This last one was an experiment to see if I could do translations myself. Future images will likely come from public domain images, since I don't fully trust the wording of the license VectorStock granted me.

Here are some examples of the new charges:

![Per bend sable and vert, a fox passant Or](/heraldry-pt-3/fox-device.svg)
![Per bend sinister purpure and sable, a eagle displayed argent](/heraldry-pt-3/eagle-device.svg)
![Per bend sinister argent and Or, a gryphon passant azure](/heraldry-pt-3/gryphon-device.svg)
![Per pale purpure and vert, a dragon passant argent](/heraldry-pt-3/dragon-device.svg)
![Per bend sinister gules and sable, a lion rampant Or](/heraldry-pt-3/lion-device.svg)

Finally, the last update is that I'm now building macOS and Windows executables for the heraldry generator. You can find them here:

[Heraldry Releases](https://github.com/ironarachne/heraldry/releases)