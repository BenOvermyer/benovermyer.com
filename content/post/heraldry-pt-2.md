---
title: "Heraldry Generation Pt. 2: Go, Divisions, and Charges"
date: 2018-03-21T14:28:14-05:00
draft: true
description: In which more complex divisions and basic charges are added to the heraldry generator...
---
This iteration had some dramatic changes. Specifically, I rewrote the entire program in Go. That part actually didn't take as much time as I'd thought. The resulting program is a bit messy, though, and I'll talk about that in a minute. First, the fun stuff.

After having just the fess and pale divisions in the last iteration, I added the remainder of the basic ones: bend, bend sinister, saltire, quarterly, and chevron.

I also added the most basic of charges - those geometric shapes called "ordinaries." Not all of the common ordinaries are in there yet, and some of them look a little askew. Since I manually created them through trial and error rather than through calculation, there are a number of problems that I'll need to sort out.

