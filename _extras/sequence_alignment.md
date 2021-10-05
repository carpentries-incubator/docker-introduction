---
title: "sequence alignment - EMBOSS"
layout: episode
teaching: 20
exercises: 0
questions:
- "How can I align sequences without complex installation?"
- "How can I use a container from within and without?"
- "How can I share/use existing sequence files residing on my computer?"
objectives:
- "Select Docker containers from the docker hub."
- "Use a Docker container to accomplish tasks."
- "Make use of shared folder."
keypoints:
- "You can use existing container images and Docker instead of installing additional software."
- "Files can be shared with the container and used by the software within."
---

> ## EMBOSS 
> “The European Molecular Biology Open Software Suite” ([EMBOSS](http://emboss.sourceforge.net/) is a free Open Source software analysis package specially developed for the needs of the molecular biology user community. 
> EMBOSS contains a large number of sequence analysis tools, and we’ll sample a few of them via a docker method. 

The purpose of this tutorial is more about learning how to use a Docker container rather than learning EMBOSS itself. 
To learn more about EMBOSS: List of applications: [emboss_apps](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/index.html) 
grouped by [function](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/groups.html), and [emboss tutorials](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)

> ## Set-up
> Macintosh: Double click on `Terminal` icon in the `/Applications/Utilities directory`. 
> Windows: Open `PowerShell`
> Linux: open a new shell terminal

In your terminal shell window login Docker with your credentials. 
If you need to create an ID now go to the [Docker Hub](https://hub.docker.com) to register a free account.

~~~
$ docker login
~~~
{: .language-bash}
~~~
Login with your Docker ID to push and pull images from Docker Hub. 
If you don't have a Docker ID, head over to https://hub.docker.com 
to create one.
Username: YOUR_DOCKER_ID_HERE
Password: 
Login Succeeded
$ 
~~~
{: .output}

We'll use an existing container for EMBOSS version 6.6.0. The following `pull` command will make a copy of the docker image on your local computer.
Note that the lengthy tag `v6.6.0dfsg-7b1-deb_cv1` is necessary since it is not the `latest` tag.

~~~
$ docker pull biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1
~~~
{: .language-bash}
~~~
v6.6.0dfsg-7b1-deb_cv1: Pulling from biocontainers/emboss
478cd0aa93c0: Pull complete 
[...]
$ 
~~~
{: .output}

You can verify that the image now exists on your system:

~~~
$ docker image ls biocontainers/emboss
~~~
{: .language-bash}
~~~
REPOSITORY             TAG                      IMAGE ID        CREATED       SIZE
biocontainers/emboss   v6.6.0dfsg-7b1-deb_cv1   bc147a9dd825    2 years ago   638MB
~~~
{: .output}

> ## Shared directory
> We'll use the EMBOSS software on files shared from our local computer.

Download the [`docker-intro.zip`]({{ page.root }}/files/docker-intro.zip) file. _This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository][docker-introduction repository]_. Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `docker-intro`. 

Within the `docker-intro` change to the `peptides` directory. There are 4 files in the simple "fasta" sequence format.

~~~
$ cd ~/Desktop/docker-intro/peptides
$ ls
~~~
{: .language-bash}
~~~
GIP.fa		GLP-1.fa	GLP-2.fa	glucagon.fa
~~~
{: .output}

These are very short peptide sequencesthe glucagon family to keep the output simple. 
*Glucagon is the principal hyperglycemic hormone, and acts as a counterbalancing hormone to insulin. 
Glucagon is a peptide hormone of 29 amino acids that shares the same precursor molecule, proglucagon, with GLP-1 and GLP-2. 
By tissue-specific posttranslational processing, glucagon is secreted from pancreatic α cells whereas GLP-1 and GLP-2 are secreted from intestinal L cells. 
All these peptides have considerable sequence similarity (Park (2015).)*   

*GIP, a related member of the glucagon peptide superfamily, also regulates nutrient disposal via stimulation of insulin secretion (Brubaker and Drucker (2002).)*



## References

Brubaker, P. L., and D. J. Drucker. 2002. “Structure-function of the glucagon receptor family of G protein-coupled receptors: the glucagon, GIP, GLP-1, and GLP-2 receptors.” Recept. Channels 8 (3-4): 179–88. https://doi.org/10.3109/10606820213687.

Park, Min Kyun. 2015. “Subchapter 17A - Glucagon.” In Handbook of Hormones: Comparative Endocrinology for Basic and Clinical Research, 129–31. Academic Press. https://doi.org/10.1016/B978-0-12-801028-0.00138-0.






