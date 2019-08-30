---
title: "Visiting the Docker Hub"
teaching: 10
exercises: 0
questions:
- "What is the Docker Hub, and why is it useful?"
objectives:
- "Explain how the Docker Hub augments Docker use."
- "Explore the Docker Hub webpage for a popular Docker image."
keypoints:
- "The Docker Hub is an online repository of container images."
- "Many Docker Hub images are public, and may be officially endorsed."
- "Each Docker Hub page about an image provides structured information and subheadings"
- "Most Docker Hub pages about images contain sections that provide examples of how to use those images."
---
### Introducing the Docker Hub
The Docker Hub is an online repository of container images, a vast number of which are publicly available. A large number of the images are curated by the developers of the software that they package. Also, many commonly used pieces of software that have been containerised into images are specifically endorsed, which means that you can trust the containers to have been checked for functionality, stability, and that they don't contain malware.

> ## Docker can be used without connecting to the Docker Hub
> Note that while the Docker Hub is well integrated into Docker functionality, the Docker Hub is certainly not required for all types of use of Docker containers. For example, some organisations may run container infrastructure that is entirely disconnected from the Internet.
{: .callout}

### Exploring r-base as an example Docker Hub page
As an example of a Docker Hub page, let's explore the page for the R statistics language. The most basic form of containerised R is in the "r-base" image (which is endorsed by the Docker team). Open your web browser to <https://hub.docker.com/_/r-base> to see what is on a typical Docker hub software page.

The top-left provides information about the name, short description, popularity (i.e., over a million downloads in the case of this image), and endorsements.

The top-right provides the command to pull this image to your computer.

The main body of the page contains many used headings, such as:
- Which tags (i.e., image versions) are supported;
- Summary information about where to get help, which computer architectures are supported, etc.;
- A longer description of the package;
- Examples of how to use the image; and
- The licence that applies.

At least in my experience, the "Examples of how to use the image" section of most images' pages will provide examples that are likely to adequately cover your intended use of the image.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
