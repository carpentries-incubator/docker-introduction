---
title: Running Containers on HPC
teaching: 30
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Learn how to convert Docker images to SIF
- Distinguish the `run` and `exec` subcommands

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How is singularity different to Docker?
- How do I use my Docker images on a shared HPC?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

You can find more detail about using Singularity in the [singularity-introduction](https://carpentries-incubator.github.io/singularity-introduction/) Carpentries workshop.

::::::::::::::::::::::::::::::::::::::::::::::::::

Singularity is a container engine, like Docker.
However, unlike Docker, container images are stored as single files called `.sif` (Singularity Image Format).
For a number of reasons, Singularity suits shared High Performance Computing (HPC) environments much better than Docker, so is valuable to learn if you work in these environments.
A related tool called singularity is a fork of Singularity that generally has the same command line interface.

::: challenge
## Singularity Command Line Interface

Like we did with Docker, try to work out what commands Singularity has.
Which one do you think is the equivalent of `docker run`?
:::
::: solution
`singularity run` behaves similarly to `docker run`, but as we will see, the arguments are somewhat different.
:::

## Running Docker Containers

Since Singularity containers have their own file format, if we have a Docker image we want to run, it first has to be converted.
We can do this using `singularity pull`.
For example, we can pull the container we previously pushed to Docker Hub:

```bash
singularity pull docker://alice/alpine-python
```

This creates a file called `alpine_python.sif` in our working directory.
To run this container, we then use `singularity run`:

```bash
singularity run alpine_python.sif
```

## Singularity Exec

If we want to modify the command run in the container, we have to use `singularity exec`.
For example, to make Python add numbers like in our sum example, we could do:
```bash
apptainer exec alpine_python.sif python -c 'print(1 + 1)'
```
