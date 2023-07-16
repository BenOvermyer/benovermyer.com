+++
title = "Word generation in Iron Arachne"
date = 2022-07-19
description = "Iron Arachne relies heavily on its random word generation module. Now it's changing."
+++

When I first rewrote Iron Arachne as a static JavaScript website, I quickly hacked together several name generators using different methods. Most assembled pieces from several different chunks into a single word.

That quickly became insufficient. The results were predictable and small in number. After awhile, I wrote a simple module called "invented" which was meant to create words for invented languages, or conlangs. It wasn't a full language generator like previous iterations of Iron Arachne had. That still doesn't exist for the JavaScript version. However, it did have a simple pattern matching algorithm; if you passed it an array of strings, it would pick a random item from that array, and then go through that string character-by-character. Each character was a symbol representing a category of sounds - phonemes - that it would then pick from at random and return that. Most characters were lowercase letters. If a character was uppercase or not a letter, it would be returned unmodified - so a pattern like `KONG` would always return "kong" and not something with random phonemes.

The result was an invented word generator that worked well enough. I started using it in almost every part of Iron Arachne that needed made-up words.

Recently, though, things changed just a little bit. I was running out of letters of the alphabet to use as symbols representing phoneme categories. I was using two of them - `u` and `d` - to represent a doubled vowel and consonant, respectively. I decided to reclaim those letters for other things. To do so, I needed to figure out how to change the system so I could still generate doubled letters but not linearly add new symbols for them.

The solution was to add the first modifier symbol to the invented library. Instead of being a simple iterative lookup, the generate function would now store the last generated phoneme, and if the next symbol was a `+` it would return that last phoneme instead of looking up a different one.

That, in turn, made me think about a common scenario where I wanted to have a particular type of word use a random list of sounds instead of one of the pre-existing categories of phonemes. How would I do that, though? My existing module only checked each character in turn. Rather than try and continue down that route, I decided it was finally time to build an actual parser.

I'd never written a parser before. Not even in CS, way back in high school and college. I pivoted to a history degree before taking the otherwise-inevitable compilers class. Lexers and parsers were something I used, not something I wrote. Even now, I'm cheating a bit and using regular expressions to handle most of the heavy lifting.

The idea is that I'll be able to write patterns like this:

```
(K,G)LvNGON
```

And the generator will spit out words like this:

```
Klangon
Glingon
Glengon
Klungon
```

So anytime the parser encounters a series of characters in parenthesis, it returns a random unmodified item from that list instead of a random phoneme from a lookup table. I want the system to be flexible enough that I can add additional workflows later. Perhaps I might want to add a way to return a random phoneme that rhymes with a pattern, for example.

I haven't completed the new parser as I'm writing this. However, I imagine it'll be done sometime in the next few weeks.
