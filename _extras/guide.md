---
title: "Instructor Notes"
---

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
host computer and one via the shell into a running container.
* **Reflection Exercise**: At the beginning and end of the workshop, give participants time to
reflect on what they want to get out of the workshop (at the beginning) and what they
can apply to their work (at the end). Using the shared notes doc is a great way to
do this and a good way to make sure that you've addressed specific concerns or goals
of the participants.

## Common Points of Confusion

* difference between a container and container image
* what it means for a container to be stopped (but not removed)

{% include links.md %}
