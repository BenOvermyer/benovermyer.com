+++
title = "Procedural generation of campaign settings"
description = "Thoughts on procedural generation of campaign settings"
+++

These are notes I took on August 17, 2015. Eventually, these notes would become Iron Arachne.

## Notes

### Keyword-based

Keywords linked to other keywords by a “social graph” - relationships (some keywords cannot co-exist, others are more likely to co-exist, etc.)

Generation begins at the world level and drills downward

For example, let’s say that the world generation part creates a mountainous region. This might provide either an underground kingdom or a barrier for other regions, or both.

Biggest question: how to make the system aware of a world’s contents? Maybe the map is divided into units, and each unit has keywords of its own.

Things to be generated:

- World map
- Countries
- Social organizations (guilds, religions, etc.)
- Characters
- Races
- Classes (or subtypes of classes, anyway)
- Languages?
- Trade routes
- Monsters

To give the setting a rich history, it would be necessary to do several iterations over thousands of years of the setting’s past. Anything can change, but not everything would change in each iteration.

Some level of abstraction would have to happen; tracking hundreds of thousands of characters’ evolution over time would be a bit much. Or would it?

### Map generation

Could use geomorphs to create the world map while still giving hexagonal or square units for generation of everything else.
