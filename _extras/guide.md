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

## Learner Pathways

Docker, and containers more generally, represent a very large area encompassing significant
technical information. Depending on the domain they work in, and their motivation for
taking a course covering this material, learners are likely to have various different reasons
for wanting to learn about Docker. The material in this lesson covers a set of core concepts,
introducing containers and then looking at the key features of Docker and how to use them.

Moving beyond the core features there are a number of topics that are likely to only be
of interest to different sub-groups of learners. To support these different groups of
learners we have developed a set of "_learner pathways_" that provide suggested routes
through the material based on different use cases or areas of interest.

You are, of course, welcome to mix and match lesson content to offer a course that best
suits your target audience but we have identified the pathways detailed below to offer you
some guidance and examples of the different routes through the material that you might
want to consider. Each has a slightly different emphasis on specific sets of topics.

We also consider different learner profiles which we believe map well to specific
learner pathways.

_Note that at present, not all the of content highlighted in these pathways exists.
We are working to add new lesson content but also welcome contributions if you have
expertise in areas that are currently missing material._

### Learners

We consider three core groups of learners here. While also recognising that there are
likely to be many learners who don't fit into one of the following groups, or who span
more than one of them, we hope that highlighting these groups helps to provide an
example of the different skills and expertise that learners engaging with this material
may have.

 - **Researchers:** For researchers, even those based in non-computational domains, software
 is an increasingly important element of their day-to-day work. Whether they are writing
 code or installing, configuring and/or running software to support their research, they
 will eventually need to deal with the complexities of running software on different
 platforms, handling complex dependencies and potentially submitting their code and data to
 repositories to support the reproduction of research outputs by other researchers, or to
 meet the requirements of publishers or funders. Container technologies are a valuable
 skill for a researcher to help them address these challenges.

- **RSEs:** RSEs - Research Software Engineers - provide software development, training
and technical guidance to support the development of reliable, maintainable, sustainable
research software. They will generally have extensive technical skills but they may not
have experience of working with or managing containers. In addition to working with
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
and upgradability.

**_COMMENT TO REMOVE:_** Add some links between the learner profiles here and those in
the main lesson content. Also add an RSE profile to the lesson content.

### Pathways

The Docker lesson contains a set of core content that we expect to be relevant for all
learner pathways. This involves introducing container concepts and the Docker software
and then running through the basic use of Docker including running containers and the
basics of building containers. Beyond this, different pathways bring in different
episodes containing different lesson content to support different target audiences.

<hr/>

_Content from sprint notes to complete and integrate_

- Learner pathways: providing recommended training paths/schedules - i.e. groups of core and optional episodes that work well for particular use cases -> goal: instructor notes that include a couple example schedules (target audience: cloud usages, bundling up for reproduciblity)
    - Write out some options and create some example schedules
        - Currently Docker is often taught over 4 hours - 2 x 2 hour blocks. Following on from that
            - cloud 
                - episodes: 
            - reproduciblity
                - episodes: 
            - docker+singularity together
                - episodes: 
            - 

<hr/>

## Common Points of Confusion

* difference between a container and container image
* what it means for a container to be stopped (but not removed)
* differences in container behaviour between hosts that are running Linux compared to hosts running macOS or Microsoft Windows
    * on Linux hosts there is usually only one OS kernel shared between the host and the containers, so less separation than is typical when using macOS or Windows hosts. This can lead to effects such as volume mounts behaving differently, e.g., regarding filesystem permissions, user and group mappings between the host and the container.

{% include links.md %}
