---
title: "Instructor Notes"
---

## Before Teaching This Lesson

[Docker][Docker] and its associated tools are under ongoing rapid development. Things
change regularly with version updates and new tools for interacting with
Docker and running containers on different platforms.

In particular, there can be differences between macOS, Windows and Linux
platforms. Updates and changes introduced in Docker releases are highlighted
in the [Docker release notes][Docker release notes].

_You are strongly advised to run through the lesson content prior to running
the lesson to ensure that everything works as expected._

If you experience any issues, please [open an issue][open a lesson issue] in the lesson
repository describing the problem and platform(s) affected. The lesson maintainers will
aim to resolve the issue as soon as possible but we also welcome the opening
of pull requests (linked to issues) that resolve anything that doesn't work as
expected with the lesson content.

## Miscellaneous Tips

* **Timing**: As written, there's way more than 3 hours of material in this lesson.
Focusing on the earlier episodes (Introduction through the first half
of Creating Container Images) will take just about three hours if you
also include a brief general introduction and time to check people's
installations.
* **Install Issues**: Windows computers seem to consistently have issues with Docker.
Consider having people check their install in advance at a separate time or come early.
In online workshops, consider using breakout rooms to have smaller groups for
participants to demonstrate their installations. Use a more complex command than
`docker --version` to test the installation.
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

## Common Points of Confusion

* difference between a container and container image
* what it means for a container to be stopped (but not removed)
* differences in container behaviour between hosts that are running Linux compared to hosts running macOS or Microsoft Windows
    * on Linux hosts there is usually only one OS kernel shared between the host and the containers, so less separation than is typical when using macOS or Windows hosts. This can lead to effects such as volume mounts behaving differently, e.g., regarding filesystem permissions, user and group mappings between the host and the container.

{% include links.md %}
