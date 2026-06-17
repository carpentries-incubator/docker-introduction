---
permalink: index.html
site: sandpaper::sandpaper_site
---

This session aims to introduce the use of Podman containers with the goal of using them to effect reproducible computational environments. Such environments are useful for ensuring reproducible research outputs, for example.

::::::::::::::::::::::::::::::::::::::  objectives

## After completing this session you should:

- Have an understanding of what Podman containers are, why they are useful
  and the common terminology used
- Have a working Podman installation on your local system to allow you to
  use containers
- Understand how to use existing Podman containers for common tasks
- Be able to build your own Podman containers by understanding both the role
  of a `Dockerfile`/`Containerfile` in building containers, and the syntax used in `Dockerfile`s
- Understand how to manage Podman containers on your local system
- Appreciate issues around reproducibility in software, understand how
  containers can address some of these issues and what the limits to
  reproducibility using containers are
  

::::::::::::::::::::::::::::::::::::::::::::::::::

The practical work in this lesson is primarily aimed at using Podman on your own laptop. Beyond your laptop, software container technologies such as Podman can also be used in the cloud and on high performance computing (HPC) systems. Some of the material in this lesson will be applicable to those environments too.

:::::::::::: callout

## Why Podman instead of Docker

This lesson was originally written to use the tool Docker and the associated Docker Desktop.
All the commands within this lesson can be run using `docker` instead of `podman`, though the output may vary slightly.

The maintainers of this lesson typically advocate for researchers using open source software.
In the past Docker, had a free tier for research/academic software though eventually removed that option leaving only exceptions for education and open source software.
In 2024, Docker changed their terms of service and removed their exception for open source software.
This change prompted the lesson maintainers to switch the lesson to `podman`, an open source alternative.

::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::::  callout

## Containers on HPC systems

On HPC systems it is more likely that *Apptainer* (formerly Singularity) rather than Podman or Docker will be the available container technology.
If you are looking for a lesson on using Apptainer containers (instead of Docker), see this lesson on Singularity:

- [Reproducible Computational Environments Using Containers: Introduction to Singularity](https://carpentries-incubator.github.io/singularity-introduction/)
  

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::  prereq

## Prerequisites

- You should have basic familiarity with using a command shell, and the lesson text will at times request that you "open a shell window", with an assumption that you know what this means.
  - Under Linux or macOS it is assumed that you will access a `bash` shell (usually the default), using your Terminal application.
  - Under Windows, Powershell and Git Bash should allow you to use the Unix instructions. We will also try to give command variants for Windows `cmd.exe`.
- The lessons will sometimes request that you use a text editor to create or edit files in particular directories. It is assumed that you either have an editor that you know how to use that runs within the working directory of your shell window (e.g. `nano`), or that if you use a graphical editor, that you can use it to read and write files into the working directory of your shell.
  

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Target audience

This lesson on the use of Podman is intended to be relevant to a wide range of
researchers, as well as existing and prospective technical professionals. It is
intended as a beginner level course that is suitable for people who have no
experience of containers.

We are aiming to help people who want to develop their knowledge of container
tooling to help improve reproducibility and support their research work, or
that of individuals or teams they are working with.

We provide more detail on specific roles that might benefit from this course on
the [Learner Profiles](/profiles.html) page.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## A note about Podman

Podman is a mature, robust and very widely used application. Nonetheless,
it is still under extensive development. New versions are released regularly
often containing a range of updates and new features.

While we do our best to ensure that this lesson remains up to date and the
descriptions and outputs shown match what you will see on your own computer,
inconsistencies can occur.

If you spot inconsistencies or encounter any problems, please do report them
by [opening an issue][open a lesson issue] in the [GitHub repository][docker-introduction repository]
for this lesson.


::::::::::::::::::::::::::::::::::::::::::::::::::



<!-- TODO: systematically check for Windows-isms -->

<!--  LocalWords:  prereq links.md endcomment
 -->
