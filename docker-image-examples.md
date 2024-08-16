---
title: Examples of Using Container Images in Practice
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Use existing container images and Docker in a research project.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I use Docker for my own work?

::::::::::::::::::::::::::::::::::::::::::::::::::

Now that we have learned the basics of working with Docker container images and containers,
let's apply what we learned to an example workflow.

You may choose one or more of the following examples to practice using containers.

## GitHub Actions Example

In this [GitHub Actions example](../instructors/e01-github-actions.md), you can learn more about
continuous integration in the cloud and how you can use container images with GitHub to
automate repetitive tasks like testing code or deploying websites.

<!--- Placeholder for
## Geospatial Example

Ask @mkuzak to make a PR to add extra for <https://github.com/escience-academy/docker-gdal-demo>

-->

## Using Containers on an HPC Cluster

It is possible to run containers on shared computing systems run by a university or national
computing center. As a researcher, you can build container images and test containers on your own
computer and then run your full-scale computing work on a shared computing
system like a high performance cluster or high throughput grid.

The catch? Most university and national computing centers do not support *running*
containers with Docker commands, and instead use a similar tool called Singularity or
Shifter. However, both of these programs can be used to run containers based on Docker container images,
so often people create their container image as a Docker container image, so they can
run it using either of Docker or Singularity.

There isn't yet a working example of how to use Docker container images on a shared
computing system, partially because each system is slightly different, but the
following resources show what it can look like:

- [Introduction to Singularity](https://carpentries-incubator.github.io/singularity-introduction/): See the episode titled "Running MPI parallel jobs using Singularity containers"
- [Container Workflows at Pawsey](https://pawseysc.github.io/container-workflows/): See the episode titled "Run containers on HPC with Shifter (and Singularity)"

## Seeking Examples

Do you have another example of using Docker in a workflow related to your field?  Please [open a lesson issue] or [submit a pull request] to add it to this episode and the extras section of the lesson.



[submit a pull request]: https://github.com/carpentries-incubator/docker-introduction/pulls


:::::::::::::::::::::::::::::::::::::::: keypoints

- There are many ways you might use Docker and existing container images in your research project.

::::::::::::::::::::::::::::::::::::::::::::::::::
