+++
title = 'Heraldry Generation Pt. 2: Go, Divisions, and Charges'
date = 2018-03-21
+++
This iteration had some dramatic changes. Specifically, I rewrote the entire program in Go. That part actually didn't take as much time as I'd thought. The resulting program is a bit messy, though, and I'll talk about that in a minute. First, let me tell you about the heraldry changes.

After having just the fess and pale divisions in the last iteration, I added the remainder of the basic ones: bend, bend sinister, saltire, quarterly, and chevron.

I also added the most basic of charges - those geometric shapes called “ordinaries.” Not all of the common ordinaries are in there yet, and some of them look a little askew. Since I manually created them through trial and error rather than through calculation, there are a number of problems that I'll need to sort out.

For example, here're a couple charges from the current iteration. Notice how they're a little off?

![This saltire's a little askew](/heraldry-pt-2/askew-saltire.svg) ![This pall is definitely not right](/heraldry-pt-2/askew-pall.svg)

The other issue is that many of the designs that pop out of the generator don't look very visually appealing. A possible future iteration will be to add some kind of logic to fix that.

With all of that said, it produces some pretty decent results. Here are some of them:

![This chevron is energetic](/heraldry-pt-2/bright-chevron.svg) ![A bordure to approve of](/heraldry-pt-2/nice-bordure.svg) ![The contrast here is interesting](/heraldry-pt-2/pile-charge.svg)

OK, so now, let's talk about Go.

I had always intended to rewrite the program in Go; I was using PHP as a rapid prototyping language. However, I hit a wall not too far into development. The SVG library I was using ended up not supporting a number of features of SVG that I needed. I was able to work around it by stripping out that library and dealing with the raw XML of SVG, but this was somewhat cumbersome.

Then I discovered the excellent SVG Go package called, appropriately enough, SVGo. It had several of the things I needed. So, I just pulled the trigger and spent a morning rewriting the entire codebase.

The result is a much faster program that's easy to write code for.

It's not without its problems, though.

All of the code is in one giant file. Visualization definitions are inline and contained in large `switch` or `if` blocks. There are no unit tests (which has bit me a couple times already).

Now that I'm going to be adding more complex charges (like animals), I can't keep putting all of that in the same file. That's something I hope to address in the next iteration.
