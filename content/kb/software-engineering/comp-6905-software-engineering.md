+++
title = "COMP 6905: Introduction to Software Engineering"
+++

The following are my notes for COMP 6905, "Introduction to Software Engineering." It starts with a lot of copying from slides verbatim, and then tapers off as I start getting very bored and disillusioned with the course material.

# Notes

The term "Software Engineering" originated with Anthony Oettinger, in "The hardware-software complentarity". Communications of the ACM, 1967.

The first software engineering conference was in 1968.

The discipline was created to get projects exceeding time and budget under control. In the 1960s, 84% of projects ran behind schedule. They were over-budget, on average, by 189%. 30% of them were cancelled.

The cost of owning and maintaining software in the 1980s was twice as expensive as developing it.

During the 1990s, this increased by 30%.

An engineering project proceeds along clearly defined phases.

Fundamental principles:

1. Systems should be developed using a managed and understood development process. Of course, different processes are used for different types of software.
2. Dependability and performance are important for all types of system.
3. Understanding and managing the software specification and requirements are important.
4. Where appropriate, reuse software that has already been developed rather than write new software.

Main software engineering activities:

- Requirements/specification
- Design
- Deployment
- Development/implementation/coding
- Validation/testing
- Integration
- Evolution/maintenance

These can be boiled down to:

- Specification
- Development
- Validation
- Evolution

## Requirement/Specification

The process of establishing what services are required and the contraints on the system's operation and development.

The process:

- Requirements elicitation and analysis
- Requirements specification
- Requirements validation

## Design and Implementation

The process of converting the specification into an executable system.

- Software design
- Implementation

### Design Activities

- Architectural design
- Database design
- Interface design
- Component selection and design

### System Implementation

- The software is implemented either by developing a program(s) r by configuring an application system.
- Design and implmentation are interleaved activities for most types of software system.
- Programming is an individual activity with no standard process.
- Debugging is the activity of finding program faults and correcting these faults.

## Validation/Testing

- Individual components are tested independently
- Components may be functions or objects or coherent groupings of these entities.
- Done by the person who writes the code
- Often considered as part of coding
- Testing of the system as a whole, with a focus on emergent properties.
- Feature testing and performance testing
- Regression testing
- Testing with customer data to check that the system meets the customer's needs
- Acceptance testing
- Field testing

## Software Evolution

- Software is inherently flexible and can change.
- As requirements change through changing business circumstances, the software that supports the business must also evolve and change
- Although there has been a demarcation between development and evol;ution, this is increasingly irrelevant as fewer and fewer systems are completely new.

## Development process types

### The code-and-fix model

1. Write code
2. Fix code

### Waterfall

1. Requirements definition
2. System and software design
3. Implementation and unit testing
4. Integration and system testing
5. Operations and maintenance

Waterfall is document-driven. Documents from each step are needed for the next step.

It only really works for embedded systems and safety-critical systems where the cost of errors is high.

### V-Model

The V-model just includes validation/testing for _every_ component of the design process, not just software development. E.g., validating the requirements. It's otherwise a variant of Waterfall.

### Incremental Development

1. Initial description
2. Specification <-> Implementation <-> Validation

Basically, just iteration.

### Agile

Minimal documentation, focus is on working code.

- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

## Types of Agile

- Extreme Programming
- Test-Driven Development
- Pair Programming
- Scrum