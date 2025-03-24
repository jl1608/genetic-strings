# Genetic String

Toy repo simulating the genetic process of evolution and its characteristics of optimisation

## Problem

Solve for a target string using a genetic algorithm. The target is a sequence of uppercase ASCII alphabet characters, A, and has a length of N.

## Background

A Genetic Algorithm (GA) is a technique mimicing natural selection to optimise or solve a particular set of problems.

There are three main steps of the algorithm: selection, mutation and crossover.

Once each step is complete, the population is replaced with the offspring and the process continues until evolutationary optimality is reached.

### Selection

Select the 'fittest' (determined by the fitness score) organisms of the population to reproduce.

Methods such as *Roulette Wheel Selection* or *Tournament Selection* can be used to decide strongest candidates.

### Crossover

Combining parts of two parent organisms (string sequences) to generate an offspring organism.

> If the parents are `HELLO` and `WORLD` the offspring may inherit the first two characters and last two characters of each parent respectively: `HELD`.

### Mutation

Mutations would edit certain characteristics of an organism. In the case of these string sequences it might randomly select a character and replace it with another character of the alphabet.

Mutation is key to ensuring variety within the population, maintaining a trajectory change of a stale evolution path (sub-optimal solution).