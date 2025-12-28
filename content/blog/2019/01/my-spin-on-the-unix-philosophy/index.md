+++
title = 'My Spin on the Unix Philosophy'
date = 2019-01-22
+++
The Unix philosophy guides the development of both Unix and its derivatives. It's a good philosophical core to judge new projects by. I'm increasingly using the Unix philosophy in my own works. This is particularly true of new versions of Iron Arachne command line tools. There are multiple versions of the Unix philosophy bouncing around on the web. Some are longer or more stringent than others. What follows is my own interpretation of it.

# Rule One: Tight Focus

Each program should do one thing well. **Corollary:** Each program should do _only_ one thing.

# Rule Two: Predictable Flexibility

Expect each program's output to be the input for some unknown other program. Design for flexibility. **Corollary:** Also design first for command-line interfaces, and avoid interactive interfaces. Assume machines will use your program more often than humans.

# Rule Three: Rapid Iteration

Release early and often. **Corollary:** It's not only OK but desirable to have minimal change between iterations.

# Rule Four: Automated Development

Write tools to assist development instead of seeking out human help. **Corollary:** It's fine to ask for help when you've tried the above to no success.
