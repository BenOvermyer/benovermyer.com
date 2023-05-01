+++
title = "Site Reliability Engineering book notes"
description = "My notes on the SRE book by Google"
+++

# The SRE Book

What follow are my notes on the SRE book put out by Google.

## Troubleshooting

### Problem Reports

-   automated where possible, including helpful data for troubleshooting in the body of the alert
-   submit tickets for everything; you want a paper trail

### Triage

-   "make the system work as well as it can under the circumstances"

### Examine

-   monitoring
-   logging
-   distributed tracing

### Logging

-   be able to change log levels on the fly
-   be able to do statistical sampling
-   be able to turn on logging quickly, easily, and selectively

### Diagnose

-   inject test data into each component in a misbehaving system to confirm normal operation
-   inject test data meant to expose particular types of suspected errors
-   "what, where, and why": figure out what the system is _actually_ doing, not just what it's supposed to be doing
    -   what it's doing
    -   where its resources are being used
    -   why it's doing what it's doing

### What Touched It Last

-   a system in motion stays in motion until something acts on it
-   things to log
    -   deployments
    -   configuration changes
    -   packages installed

### Testing

-   an ideal test should have mutually exclusive alternatives, in order to rule in/out competing hypotheses
-   perform tests in decreasing order of likelihood
-   keep in mind the side effects of active testing (e.g., increasing available CPU may compound race conditions)
-   take clear notes of ideas, tests, and results

### Cure

-   once you've reduced the possible causes to one, try to prove it's the cause
-   produce a post mortem
    -   what went wrong
    -   how you tracked down the problem
    -   how you fixed the problem
    -   how to prevent it from happening again
