---
title: "Instructor Notes"
---

## Before Teaching This Lesson

[Docker][Docker] and its associated ecosystem is rapidly developing.
While many core features will be stable, the overall environment
changes regularly with version updates and new tools for interacting with
Docker and running containers on different platforms.

In particular, there can be differences between macOS, Windows and Linux
platforms. Updates and changes introduced in Docker releases are highlighted
in the [Docker release notes][Docker release notes].

_You are strongly advised to run through the lesson content prior to teaching
the lesson to ensure that everything works as expected._

If you experience any issues, please [open an issue][open a lesson issue] in the lesson
repository describing the problem and platform(s) affected. The lesson maintainers will
aim to resolve the issue as soon as possible but we also welcome the opening
of pull requests (linked to issues) that resolve anything that doesn't work as
expected with the lesson content.

## Checking for correct setup

It has been very beneficial in an online setting to schedule a check-up session with participants to ascertain that docker has been correctly installed before the workshop starts.

Ask the participants to run the following two commands:
~~~
$ docker run docker/whalesay cowsay boo
~~~
{: .language-bash}

on Linux/Mac
~~~
$ docker run -it -v $PWD:/tmp python:slim bash
$ ls
~~~
{: .language-bash}

on Windows (powershell, wsl might also work)
~~~
$ docker run –it –v %cd%:/tmp/ python:slim bash
$ ls
~~~
{: .language-bash}

or if that fails
~~~
$ docker run –it –v C:\\Users\username:/tmp python:slim bash
$ ls
~~~
{: .language-bash}

If those two commands work on the participant's machine the lesson material should work without problems.

## Miscellaneous Tips

* **Timing**: With all the lesson episodes taken together, there's way more than three hours of material in this lesson.
Focusing on the earlier episodes (Introduction through the first half
of Creating Container Images) will take just about three hours if you
also include a brief general introduction and time to check your learners'
software installations.
* **Install Issues**: From the feedback we have received about past lessons, computers running 
Microsoft Windows have encountered the largest number of challenges setting up Docker.
Consider having people check their install in advance at a separate time or come early.
In online workshops, consider using your video conferencing software's "breakout room" functionality
to form smaller groups within which participants can troubleshoot their installations.
Note that you should use a more complex command than `docker --version` to test the installation, as the 
simplest `docker` commands to not connect to the Docker backend.
* **Virtualization Illustration**: When going through the intro to containers,
consider demonstrating what this might look like by having two shells (or shell tabs)
open, one on your host computer and one into a container you started before the
workshop. Then you can demonstrate in a simple way that from the same (host) computer,
you can access two different types of environments -- one via the shell on your
host computer and one via the shell into a running container. Sample commands could include: 
    * `whoami`
    * `pwd` and `ls`
    * something that shows the OS. On mac, this could be `sw_vers`, on linux `cat /etc/os-release`
* **Reflection Exercise**: At the beginning and end of the workshop, give participants time to
reflect on what they want to get out of the workshop (at the beginning) and what they
can apply to their work (at the end). Using the shared notes doc is a great way to
do this and a good way to make sure that you've addressed specific concerns or goals
of the participants.

## Learner Profiles and Pathways

In this section we provide some details of example learner profiles and
suggest some possible different pathways or technical focuses to consider
when teaching or planning a lesson based around this Docker material. As such,
the information in this section is not designed to define fixed approaches and
structures for teaching this material. It is instead aimed to provide ideas
and inspiration and to encourage you to think about your audience when
preparing to teach this material. The information here is based on both
discussions about the intended audiences for this material and on direct
experiences of instructors who have taught it at workshops following different
technical pathways.

### Learner profiles

We begin by providing some example learner profiles to highlight the potential
target audience and the types of different research and technical backgrounds
that you may find among learners engaging with this material. With these
profiles, we aim to encourage you to think about the learners attending your
workshop(s) and which episodes it may be most useful to teach.

**_Nelson is a graduate student in microbiology._** They have experience in running Unix shell
commands and using libraries in R for the bioinformatics workflows they have developed.
They are expanding their analysis to run on 3000 genomes in 200 samples and they have
started to use the local cluster to run their workflows. The local research computing
facilitator has advised them that Docker could be useful for running their workflows on
the cluster. They'd like to make use of existing containers that other bioinformaticians
have made so they want to learn how to use Docker. They would also be interested in
creating their own Docker images for other lab members and collaborators to re-use their
workflows.

**_Caitlin is a second year undergraduate in computer science examining Docker for the first
time._** She has heard about Docker but does not really know what it achieves or why it is
useful. She is reasonably confident in using the Unix shell, having used it briefly in
her first year modules. She is keen to find jump-off points to learn more about technical
details and alternative technologies that are also popular, having heard that container
technologies are widely used within industry.

**_Xu, a materials science researcher, wants to package her software for release with
a paper to help ensure reproducibility._** She has written some code that makes use of a
series of Python libraries to undertake analysis of a compound. She wants to (or is
required to) make her software available as part of the paper submission. She
understands why Docker is important in helping to ensure reproducibility but not the
process and low-level detail of preparing a container and archiving it to obtain a DOI
for inclusion with the paper submission.

**_Bronwyn is a PhD student running Python/R scripts on her local laptop/workstation._**
She is having difficulty getting all the tools she needs to work because of conflicting
dependencies and little experience with package managers. She is also keen to reduce
the overhead of managing software so she can get on with her thesis research. She has
heard that Docker might be able to help out but is not confident to start exploring
this on her own and does not have access to any expertise in this within her local
research group. She currently wants to know how to use preexisting Docker containers
but may need to create her own containers in the future.

**_Virat is a grad student who is running an obscure bioinformatics tool (from a GitHub
repo) that depends on a number of other tools that need to be pre-installed ._** He wants to be able to
run on multiple resources and have his undergrad assistant use the same tools. Virat
has command line experience and has struggled his way through complex installations
but he has no formal CS background - he only knows to use containers because a departmental
IT person suggested it. He is usually working from a Windows computer. He needs to
understand how to create his own container, use it locally, and train his student
to use it as well.

Considering things from a higher level, we also highlight three core groups of
learners, based on job roles, who you may find attending lessons covering this
material. While recognising that there are likely to be many learners who
don't fit into one of the following groups, or who span more than one of them,
we hope that highlighting these groups helps to provide an example of the
different types of skills and expertise that learners engaging with this
material may have:

 - **Researchers:** For researchers, even those based in non-computational domains, software
 is an increasingly important element of their day-to-day work. Whether they are writing
 code or installing, configuring and/or running software to support their research, they
 will eventually need to deal with the complexities of running software on different
 platforms, handling complex software dependencies and potentially submitting their code and data to
 repositories to support the reproduction of research outputs by other researchers, or to
 meet the requirements of publishers or funders. Software container technologies are valuable
 to help researchers address these challenges.

- **RSEs:** RSEs -- Research Software Engineers -- provide software development, training
and technical guidance to support the development of reliable, maintainable, sustainable
research software. They will generally have extensive technical skills but they may not
have experience of working with or managing software containers. In addition to working with
researchers to help build and package software, they are likely to be interested in how
containers can help to support best practices for the development of research software
and aspects such as software deployment.

 - **Systems professionals:** Systems professionals represent the more technical end of
our spectrum of learners. They may be based within a central IT services environment
within a research institution or within individual departments or research groups.
Their work is likely to encompass supporting researchers with effective use of
infrastructure and they are likely to need to know about managing and orchestrating
multiple containers in more complex environments. For example, they may need to provide
database servers, web application servers and other services that can be deployed
in containerized environments to support more straightforward management, maintenance
and upgradeability.

### Learner Pathways

We now come to look at some ideas around learner pathways for learners
interested in Docker, and container technologies more generally.

Containers involve a variety of different technologies, and teaching material
about them can therefore encompass significant volumes of technical
information. Depending on the domain they work in, and their motivation for
taking a course covering this material, learners are likely to have various
different reasons for wanting to learn about Docker, that may not necessarily
all overlap. The material in this lesson covers a set of core concepts,
introducing containers and then looking at the key features of Docker and how
to use them.

Moving beyond the core features there are a number of topics that are likely
to only be of interest to different sub-groups of learners. To support these
different groups of learners we have developed a set of "_learner pathways_"
that provide suggested routes through the material based on different use
cases or areas of interest.

You are, of course, welcome to mix and match lesson content to offer a course
that best suits your target audience but we are listing some different
pathways or themes for covering this material to offer you some guidance and
examples of the different routes through the material that you might want to
consider. Each pathway will have a slightly different emphasis on specific
sets of topics. We highlight learner different profiles that we believe map
well to specific pathways.

_Note that the material in this lesson continues to develop and experience
of teaching the material is increasing. In due course we intend to offer more
detailed pathway information including specific episode schedules that we
think are most suited to the pathways highlighted._

**Core content:**

The Docker lesson contains a set of core content that we expect to be relevant
for all learner pathways. This includes:

 - Introducing container concepts and the Docker software
 - Running through the basic use of Docker including:
     - Core commands for listing and managing images and containers
     - Obtaining container images from Docker Hub
     - Running containers from container images
     - Building container images
     
Beyond this, different pathways offer scope to bring in different episodes
containing different lesson content to support different target audiences or
areas of interest

Some suggested pathways include:

 - **Reproducible research**
     - _Common learner profiles:_ Researcher; RSE

 - **Cloud computing**
     - _Common learner profiles:_ Sytems professional, RSE

 - **High performance computing**
     - _Common learner profiles:_ Researcher; RSE; Systems professional


## Common Points of Confusion

* difference between a container and container image
* what it means for a container to be stopped (but not removed)
* differences in container behaviour between hosts that are running Linux compared to hosts running macOS or Microsoft Windows
    * on Linux hosts there is usually only one OS kernel shared between the host and the containers, so less separation than is typical when using macOS or Windows hosts. This can lead to effects such as volume mounts behaving differently, e.g., regarding filesystem permissions, user and group mappings between the host and the container.

{% include links.md %}
