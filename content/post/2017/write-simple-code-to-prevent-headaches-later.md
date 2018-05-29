---
title: "Write Simple Code to Prevent Headaches Later"
date: 2017-06-05T13:35:53-05:00
description: ""
draft: false
---
Consider the following code snippet:

    someVar = false;

    if ( anotherVar >= 1 ) {
     someVar = true;
    }

Now, consider this rewrite:

    someVar = ( anotherVar >= 1 );

Both snippets work as designed, so why is the second one better? It
comes down to simplicity. The first snippet includes an *if* block. It
would be possible for another programmer to add logic into that block
that, while not modifying the final result of *someVar*, increases the
complexity of the code. This makes it harder to maintain in the long
run. The second snippet is very clear about what it does, and is more
difficult to tack additional logic onto.