---
title: "Finding Containers on Docker Hub"
teaching: 10
exercises: 10
questions:
- "What is the Docker Hub, and why is it useful?"
objectives:
- "Explain how the Docker Hub augments Docker use."
- "Explore the Docker Hub webpage for a popular Docker container image."
- "Find the list of tags for a particular Docker container image."
- "Identify the three components of a container image's identifier."
keypoints:
- "The Docker Hub is an online repository of container images."
- "Many Docker Hub container images are public, and may be officially endorsed."
- "Each Docker Hub page about a container image provides structured information and subheadings"
- "Most Docker Hub pages about container images contain sections that provide examples of how to use those container images."
- "Many Docker Hub container images have multiple versions, indicated by tags."
- "The naming convention for Docker container images is: `OWNER/CONTAINER_IMAGE_NAME:TAG`"
---

In the previous episode, we ran a few different containers derived from different 
container images: `hello-world`, `alpine`,
and maybe `busybox`. Where did these container images come from?  The Docker Hub!

## Introducing the Docker Hub

The Docker Hub is an online repository of container images, a vast number of which are publicly available. A large number of the container images are curated by the developers of the software that they package. Also, many commonly used pieces of software that have been containerized into images are officially endorsed, which means that you can trust the container images to have been checked for functionality, stability, and that they don't contain malware.

> ## Docker can be used without connecting to the Docker Hub
>
> Note that while the Docker Hub is well integrated into Docker functionality, the Docker Hub is certainly not required for all types of use of Docker containers. For example, some organizations may run container infrastructure that is entirely disconnected from the Internet.
{: .callout}

## Exploring an Example Docker Hub Page

As an example of a Docker Hub page, let's explore the page for the official Python language container images. The most basic form of containerized Python is in the `python` container image (which is endorsed by the Docker team). Open your web browser to <https://hub.docker.com/_/python> to see what is on a typical Docker Hub software page.

The top-left provides information about the name, short description, popularity (i.e., more than a billion downloads in the case of this container image), and endorsements.

The top-right provides the command to pull this container image to your computer.

The main body of the page contains many used headings, such as:
- Which tags (i.e., container image versions) are supported;
- Summary information about where to get help, which computer architectures are supported, etc.;
- A longer description of the container image;
- Examples of how to use the container image; and
- The license that applies.

The "How to use the image" section of most container images' pages will provide examples that are likely to cover your intended use of the container image.

## Exploring Container Image Versions

A single Docker Hub page can have many different versions of container images,
based on the version of the software inside.  These
versions are indicated by "tags". When referring to the specific version of a container image
by its tag, you use a colon, `:`, like this:

```
CONTAINER_IMAGE_NAME:TAG
```

So if I wanted to download the `python` container image, with Python 3.8, I would use this name:

```
$ docker image pull python:3.8
```
{: .language-bash}

But if I wanted to download a Python 3.6 container image, I would use this name:

```
$ docker image pull python:3.6
```
{: .language-bash}

The default tag (which is used if you don't specify one) is called `latest`.

So far, we've only seen container images that are maintained by the Docker team. However,
it's equally common to use container images that have been produced by individual owners
or organizations. Container images that you create and upload to Docker Hub would fall
into this category, as would the container images maintained by organizations like
[ContinuumIO](https://hub.docker.com/u/continuumio) (the folks who develop the Anaconda Python environment) or community
groups like [rocker](https://hub.docker.com/u/rocker), a group that builds community R container images.

The name for these group- or individually-managed container images have this format:

```
OWNER/CONTAINER_IMAGE_NAME:TAG
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
> How would I download the Docker container image produced by the `rocker` group that
> has version 3.6.1 of R and the tidyverse installed?
>
> Note: the container image described in this exercise is large and won't be used
> later in this lesson, so you don't actually need to pull the container image --
> constructing the correct `docker pull` command is sufficient.
>
> > ## Solution
> >
> > First, search for `rocker` in Docker Hub. Then look for their `tidyverse` container image.
> > You can look at the list of tags, or just guess that the tag is `3.6.1`. Altogether,
> > that means that the name of the container image we want to download is:
> >
> > ~~~
> > $ docker image pull rocker/tidyverse:3.6.1
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

## Finding Container Images on Docker Hub

There are many different container images on Docker Hub. This is where the real advantage
of using containers shows up -- each container image represents a complete software
installation that you can use and access without any extra work!

The easiest way to find container images is to search on Docker Hub, but sometimes
software pages have a link to their container images from their home page.

Note that anyone can create an account on Docker Hub and share container images there,
so it's important to exercise caution when choosing a container image on Docker Hub. These
are some indicators that a container image on Docker Hub is consistently maintained,
functional and secure:

- The container image is updated regularly.
- The container image associated with a well established company, community, or other group that is well-known.
- There is a Dockerfile or other listing of what has been installed to the container image.
- The container image page has documentation on how to use the container image.

If a container image is never updated, created by a random person, and does not have a lot
of metadata, it is probably worth skipping over. Even if such a container image is secure, it
is not reproducible and not a dependable way to run research computations.

> ## What container image is right for you?
>
> Find a Docker container image that's relevant to you. Take into account the suggestions
> above of what to look for as you evaluate options. If you're unsuccessful in your search,
> or don't know what to look for, you can use the R or Python container image we've
> already seen.
>
> Once you find a container image, use the skills from the previous episode to download
> the container image and explore it.
{: .challenge}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
