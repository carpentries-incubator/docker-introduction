---
title: "Finding Containers on the Docker Hub"
teaching: 10
exercises: 10
questions:
- "What is the Docker Hub, and why is it useful?"
objectives:
- "Explain how the Docker Hub augments Docker use."
- "Explore the Docker Hub webpage for a popular Docker image."
- "Find the list of tags for a particular Docker image."
- "Identify the three components of a container's identifier."
keypoints:
- "The Docker Hub is an online repository of container images."
- "Many Docker Hub images are public, and may be officially endorsed."
- "Each Docker Hub page about an image provides structured information and subheadings"
- "Most Docker Hub pages about images contain sections that provide examples of how to use those images."
- "Many Docker Hub images have multiple versions, indicated by tags."
- "The naming convention for Docker containers is: `OWNER/CONTAINER:TAG`"
---

In the previous episode, we ran a few different containers: `hello-world`, `alpine`,
and maybe `busybox`. Where did these containers come from?  The Docker Hub!

## Introducing the Docker Hub

The Docker Hub is an online repository of container images, a vast number of which are publicly available. A large number of the images are curated by the developers of the software that they package. Also, many commonly used pieces of software that have been containerised into images are specifically endorsed, which means that you can trust the containers to have been checked for functionality, stability, and that they don't contain malware.

> ## Docker can be used without connecting to the Docker Hub
>
> Note that while the Docker Hub is well integrated into Docker functionality, the Docker Hub is certainly not required for all types of use of Docker containers. For example, some organisations may run container infrastructure that is entirely disconnected from the Internet.
{: .callout}

## Exploring an Example Docker Hub Page

As an example of a Docker Hub page, let's explore the page for the python language. The most basic form of containerised python is in the "python" image (which is endorsed by the Docker team). Open your web browser to <https://hub.docker.com/_/python> to see what is on a typical Docker hub software page.

The top-left provides information about the name, short description, popularity (i.e., over a million downloads in the case of this image), and endorsements.

The top-right provides the command to pull this image to your computer.

The main body of the page contains many used headings, such as:
- Which tags (i.e., image versions) are supported;
- Summary information about where to get help, which computer architectures are supported, etc.;
- A longer description of the package;
- Examples of how to use the image; and
- The licence that applies.

At least in my experience, the "Examples of how to use the image" section of most images' pages will provide examples that are likely to adequately cover your intended use of the image.

## Exploring Image Versions

A single Docker Hub page can have many different versions of container images,
based on the version of the software inside.  These
versions are indicated by "tags". When referring to the specific version of a container
by its tag, you use a colon, `:`, like this:

```
CONTAINERNAME:TAG
```

So if I wanted to download the `python` container, with Python 3.8, I would use this name:

```
$ docker pull python:3.8
```
{: .bash}

But if I wanted to download a Python 3.6 container, I would use this name:

```
$ docker pull python:3.6
```
{: .bash}

The default tag (which is used if you don't specify one) is called `latest`.

So far, we've only seen containers that are maintained by the Docker team. However,
it's equally common to use containers that have been produced by individual owners
or organizations. The most useful R containers are developed by an organization called
`rocker`. The name for these containers have this format:

```
OWNER/CONTAINERNAME:TAG
```

> ## Repositories
>
> The technical name for the contents of a Docker Hub page is a "repository."
> The tag indicates the specific version of the container image that you'd like
> to use from a particular repository. So a slightly more accurate version of
> the above example is:
>
> ```
> OWNER/REPOSITORY:TAG
> ```
{: .callout}

> ## What's in a name?
>
> How would I download the Docker container produced by the `rocker` group that
> has version 3.6.1 of R and the tidyverse installed?
>
> > ## Solution
> >
> > First, search for `rocker` in Docker Hub. Then look for their `tidyverse` image.
> > You can look at the list of tags, or just guess that the tag is `3.6.1`. Altogether,
> > that means that the name of the container we want to download is:
> >
> > ~~~
> > $ docker pull rocker/tidyverse:3.6.1
> > ~~~
> > {: .bash}
> {: .solution}
{: .challenge}

## Many Different Containers

There are many different containers on Docker Hub. This is where the real advantage
of using containers shows up -- each container represents a complete software
installation that you can use and access without any extra work!

The easiest way to find containers is to search on Docker Hub, but sometimes
software pages have a link to their containers from their home page.

> ## What container is right for you?
>
> Find a Docker container that's relevant to you. If you're unsuccessful in your search,
> or don't know what to look for, you can use the R or Python containers we've
> already seen.
>
> Once you find a container, use the skills from the previous episode to download
> the image and explore it.
{: .challenge}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
