+++
title = "Generating Worlds: Faking Realism"
date = 2020-04-14
+++

> Note: this was a draft I never completed. However, it's useful enough as notes that I wanted to keep it around, so here it is.

Introduction: why I'm interested in this

From the ground up: beginning with the ground

Why I don't want to model plate tectonics

- it's hard
- it's computationally expensive (is this true?)
- it's not necessary

Creating a heightmap

- Diamond-Square vs Simplex noise
- Start with Simplex noise (point out the difference between Simplex and Perlin noise)
- Tweaking the noise to create more land-like patterns
- Reworking this by placing areas that should be land, then applying the noise to make it land-like
- Creating areas of mountains, rolling hills, and flat land
- Deciding on sea level
- Classifying cells based on altitude and whether it's underwater or not

Modelling air flow (reference Here Dragons Abound)

- Hadley Cells and related concepts
- Wind speed and direction

Generating climates based on air flow, humidity, temperature, and altitude

- Precipitation as a function of air flow
- Rain shadows

Generating biomes based on the results

Different types of biome models (e.g., Whittaker)

- I love diversity of classification, so I choose the most complex model

Placing rivers and simulating erosion over time

- River joins, why rivers never fork, and when that rule is broken

Below the surface: generating soil composition

- Soil is complicated, so let's only go as far as we need to model interesting areas

Generating mineral resources

- Meteor strikes are not part of the plan
- Veins of ore and their size, composition, and placement
- two primary methods of vein formation - open space filling and crack-seal growth
- I'm not modelling plate tectonics, so modelling realistic veining is not happening
- Instead, mimicking the frequency and shape of veins by random line generation and asymmetrical extrusion

Populating regions with flora and fauna

- Predators and prey
- How vegetation is chosen
