---
title: "Containers in Research Workflows: Reproducibility and Granularity"
teaching: 20
exercises: 0
questions:
- "How can I use container images to make my research more reproducible?"
- "How do I incorporate containers into my research workflow?"
- "What are container orchestration tools and how can they potentially help me?"
objectives:
- "Understand how container images can help make research more reproducible."
- "Understand what practical steps I can take to improve the reproducibility of my research using containers."
- "Know that container orchestration tools are and what they can do."
keypoints:
- "Container images allow us to encapsulate the computation (and data) we have used in our research."
- "Using a service such as Docker Hub allows us to easily share computational work we have done."
- "Using container images along with a DOI service such as Zenodo allows us to capture our work and enables reproducibility."
- "Tools such as Docker Compose, Docker Swarm and Kubernetes allow us to describe how multiple containers work together."
---

Although this workshop is titled "Reproducible computational environments using containers",
so far we have mostly covered the mechanics of using Docker with only passing reference to
the reproducibility aspects. In this section, we discuss these aspects in more detail.

> ## Work in progress...
> Note that reproducibility aspects of software and containers are an active area of research, discussion and development so are subject to many changes. We will present some ideas and approaches here but best practices will likely evolve in the near future.
{: .callout}

## Reproducibility

By *reproducibility* here we mean the ability of someone else (or your future self) being able to reproduce
what you did computationally at a particular time (be this in research, analysis or something else)
as closely as possible even if they do not have access to exactly the same hardware resources
that you had when you did the original work.

Some examples of why containers are an attractive technology to help with reproducibility include:

  - The same computational work can be run across multiple different technologies seamlessly (e.g. Windows, macOS, Linux).
  - You can save the exact process that you used for your computational work (rather than relying on potentially incomplete notes).
  - You can save the exact versions of software and their dependencies in the image.
  - You can access legacy versions of software and underlying dependencies which may not be generally available any more.
  - Depending on their size, you can also potentially store a copy of key data within the image.
  - You can archive and share the image as well as associating a persistent identifier with an image to allow other researchers to reproduce and build on your work.

## Sharing images

As we have already seen, the Docker Hub provides a platform for sharing images publicly. Once you have uploaded an image, you can point people to its public location and they can download and build upon it.

This is fine for working collaboratively with images on a day-to-day basis but the Docker Hub is not a good option for long time archive of images in support of research and publications as:

  - free accounts have a limit on how long an image will be hosted if it is not updated
  - it does not support adding persistent identifiers to images
  - it is easy to overwrite tagged images with newer versions by mistake.

## Archiving and persistently identifying images using Zenodo

When you publish your work or make it publicly available in some way it is good practice to make images that you used for computational work available in an immutable, persistent way and to have an identifier that allows people to cite and give you credit for the work you have done. [Zenodo](https://zenodo.org/) provides this functionality.

Zenodo supports the archiving of *tar* archives and we can capture our Docker images as tar archives using the `docker save` command.
For example, to export the image we created earlier in this lesson:

~~~
docker save alice/alpine-python:v1 -o alpine-python.tar
~~~
{: .bash}

These tar images can become quite large and Zenodo supports uploads up to 50GB so you may need to compress your archive to make it fit on Zenodo using a tool such as gzip (or zip):

~~~
gzip alpine-python.tar
~~~
{: .bash}

Once you have your archive, you can [deposit it on Zenodo](https://zenodo.org/deposit/) and this will:

   - Create a long-term archive snapshot of your Docker image which people (including your future self) can download and reuse or reproduce your work.
   - Create a persistent DOI (*Digital Object Identifier*) that you can cite in any publications or outputs to enable reproducibility and recognition of your work.

In addition to the archive file itself, the deposit process will ask you to provide some basic metadata to classify the image and the associated work.

Note that Zenodo is not the only option for archiving and generating persistent DOIs for images. There are other services out there -- for example, some organizations may provide their own, equivalent, service.

## Reproducibility good practice

   - Make use of images to capture the computational environment required for your work.
   - Decide on the appropriate granularity for the images you will use for your computational work -- this will be different for each project/area. Take note of accepted practice from contemporary work in the same area. What are the right building blocks for individual images in your work?
   - Document what you have done and why -- this can be put in comments in the `Dockerfile` and the use of the image described in associated documentation and/or publications. Make sure that references are made in both directions so that the image and the documentation are appropriately linked.
   - When you publish work (in whatever way) use an archiving and DOI service such as Zenodo to make sure your image is captured as it was used for the work and that is obtains a persistent DOI to allow it to be cited and referenced properly.

## Container Granularity

As mentioned above, one of the decisions you may need to make when containerising your research workflows
is what level of *granularity* you wish to employ. The two extremes of this decision could be characterised
as:

  - Create a single container image with all the tools you require for your research or analysis workflow
  - Create many container images each running a single command (or step) of the workflow and use them in
    sequence

Of course, many real applications will sit somewhere between these two extremes.

> ## Positives and negatives
> What are the advantages and disadvantages of the two approaches to container granularity for research
> workflows described above? Think about this
> and write a few bullet points for advantages and disadvantages for each approach in the course Etherpad.
> > ## Solution
> > This is not an exhaustive list but some of the advantages and disadvantages could be:
> > ### Single large container
> > - Advantages:
> >   + Simpler to document
> >   + Full set of requirements packaged in one place
> >   + Potentially easier to maintain (though could be opposite if working with large, distributed group)
> > - Disadvantages:
> >   + Could get very large in size, making it more difficult to distribute
> >     + Could use Docker multi-stage build docs.docker.com/develop/develop-images/multistage-build to reduce size
> >     + Singularity also has a multistage build feature: sylabs.io/guides/3.2/user-guide/definition_files.html#multi-stage-builds
> >   + May end up with same dependency issues within the container from different software requirements
> >   + Potentially more complex to test
> >   + Less re-useable for different, but related, work
> >
> > ### Multiple smaller containers
> > - Advantages:
> >   + Individual components can be re-used for different, but related, work
> >   + Individual parts are smaller in size making them easier to distribute
> >   + Avoid dependency issues between different pieces of software
> >   + Easier to test
> > - Disadvantage:
> >   + More difficult to document
> >   + Potentially more difficult to maintain (though could be easier if working with large, distributed group)
> >   + May end up with dependency issues between component containers if they get out of sync
> {: .solution}
{: .challenge}

> ## Next steps with containers
>
> Now that we're at the end of the lesson material, take a moment to reflect on
> what you've learned, how it applies to you, and what to do next.
>
> 1. In your own notes, write down or diagram your understanding of Docker containers:
> concepts, commands, and how they work.
> 2. In the workshop's shared notes document, write down how you think you might
> use containers in your daily work. If there's something you want to try doing with
> containers right away, what is a next step after this workshop to make that happen?
>
{: .challenge}

