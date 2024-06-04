---
title: "Importing Docker Images into Singularity"
teaching: 5
exercises: 10
questions:
- "Why would I want to import Docker images into Singularity?"
- "How do I use Docker images with Singularity?"
objectives:
- "Learn how to run Singularity containers based on Docker images."
keypoints:
- "Singularity can be used without root permission, making it more flexible for HPC systems."
- "Singularity can start a container from a Docker image, which can be pulled directly from Docker Hub."
---

## What is Singularity? 
[Singularity](https://sylabs.io/singularity/) is another type a container platform, which is similar to Docker. 
Both allow users to create isolated, reproducible environments by selectively installing only specific applications and dependencies.


## Singularity versus Docker 
In some ways, using Docker is very similar to using Singularity from a user perspective.
However behind the scenes in the system's architecture, they are fundamentally different. 
In general, the approach of Docker is to isolate, whereas with Singularity it is more to integrate with the user's system. 
Another key difference is that Singularity was developed specifically for HPC systems due to security issues arising from the requirement of root access when running Docker.

## Why Use Singularity? 
Docker is typically unavailable on shared computing platforms such as lab desktops, research clusters or HPC platforms because the design of Docker presents potential security risks on shared platforms with multiple users. 
Singularity, on the other hand, can be run by end-users entirely in their own "user space", without requiring any special administrative privileges .
As such, Singularity is more versatile in the sense that it can be run on both distributed, High Performance Computing (HPC) infrastructure, as well as a Linux laptop or desktop. 

## How to Run Existing Docker Images Singularity

Singularity can start containers directly from Docker images, allowing users to access the large number of existing container images on [Docker Hub](https://hub.docker.com/) and other registries.

However, instead of running Docker images directly, Singularity first converts a docker image to a format suitable for use by Singularity. 
When you direct Singularity to run a container based on a pulled Docker image, Singularity pulls the slices or _layers_ that make up the Docker image and converts them into a single-file Singularity SIF image.

For example, to revisit the simple _Hello World_ examples that we looked at previously, let's pull one of the [official Docker Python images](https://hub.docker.com/_/python). We'll use the image with the tag `3.9.6-slim-buster` which has Python 3.9.6 installed on Debian's [Buster](https://www.debian.org/releases/buster/) (v10) Linux distribution:

~~~
$ singularity pull python-3.9.6.sif docker://python:3.9.6-slim-buster
~~~
{: .language-bash}

~~~
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Getting image source signatures
Copying blob 33847f680f63 done  
Copying blob b693dfa28d38 done  
Copying blob ef8f1a8cefd1 done  
Copying blob 248d7d56b4a7 done  
Copying blob 478d2dfa1a8d done  
Copying config c7d70af7c3 done  
Writing manifest to image destination
Storing signatures
2021/07/27 17:23:38  info unpack layer: sha256:33847f680f63fb1b343a9fc782e267b5abdbdb50d65d4b9bd2a136291d67cf75
2021/07/27 17:23:40  info unpack layer: sha256:b693dfa28d38fd92288f84a9e7ffeba93eba5caff2c1b7d9fe3385b6dd972b5d
2021/07/27 17:23:40  info unpack layer: sha256:ef8f1a8cefd144b4ee4871a7d0d9e34f67c8c266f516c221e6d20bca001ce2a5
2021/07/27 17:23:40  info unpack layer: sha256:248d7d56b4a792ca7bdfe866fde773a9cf2028f973216160323684ceabb36451
2021/07/27 17:23:40  info unpack layer: sha256:478d2dfa1a8d7fc4d9957aca29ae4f4187bc2e5365400a842aaefce8b01c2658
INFO:    Creating SIF file...
~~~
{: .output}

Note how we see singularity saying that it's "_Converting OCI blobs to SIF format_". We then see the layers of the Docker image being downloaded and unpacked and written into a single SIF file. Once the process is complete, we should see the python-3.9.6.sif image file in the current directory.

We can now run a container from this image as we would with any other singularity image.

> ## Running the Python 3.9.6 image that we just pulled from Docker Hub
>
> Try running the Python 3.9.6 image. What happens?
> 
> Try running some simple Python statements...
> 
> > ## Running the Python 3.9.6 image
> >
> > ~~~
> > $ singularity run python-3.9.6.sif
> > ~~~
> > {: .language-bash}
> > 
> > This should put you straight into a Python interactive shell within the running container:
> > 
> > ~~~
> > Python 3.9.6 (default, Jul 22 2021, 15:24:21) 
> > [GCC 8.3.0] on linux
> > Type "help", "copyright", "credits" or "license" for more information.
> > >>> 
> > ~~~
> > Now try running some simple Python statements:
> > ~~~
> > >>> import math
> > >>> math.pi
> > 3.141592653589793
> > >>> 
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

In addition to running a container and having it run the default run script, you could also start a container running a shell in case you want to undertake any configuration prior to running Python. This is covered in the following exercise:

> ## Open a shell within a Python container
>
> Try to run a shell within a singularity container based on the `python-3.9.6.sif` image. That is, run a container that opens a shell rather than the default Python interactive console as we saw above.
> See if you can find more than one way to achieve this.
> 
> Within the shell, try starting the Python interactive console and running some Python commands.
> 
> > ## Solution
> >
> > Recall from the earlier material that we can use the `singularity shell` command to open a shell within a container. To open a regular shell within a container based on the `python-3.9.6.sif` image, we can therefore simply run:
> > ~~~
> > $ singularity shell python-3.9.6.sif
> > ~~~
> > {: .language-bash}
> > 
> > ~~~
> > Singularity> echo $SHELL
> > /bin/bash
> > Singularity> cat /etc/issue
> > Debian GNU/Linux 10 \n \l
> > 
> > Singularity> python
> > Python 3.9.6 (default, Jul 22 2021, 15:24:21) 
> > [GCC 8.3.0] on linux
> > Type "help", "copyright", "credits" or "license" for more information.
> > >>> print('Hello World!')
> > Hello World!
> > >>> exit()
> > 
> > Singularity> exit
> > $ 
> > ~~~
> > {: .output}
> > 
> > It is also possible to use the `singularity exec` command to run an executable within a container. We could, therefore, use the `exec` command to run `/bin/bash`:
> > 
> > ~~~
> > $ singularity exec python-3.9.6.sif /bin/bash
> > ~~~
> > {: .language-bash}
> > 
> > ~~~
> > Singularity> echo $SHELL
> > /bin/bash
> > ~~~
> > {: .output}
> > 
> > You can run the Python console from your container shell simply by running the `python` command.
> {: .solution}
{: .challenge}

More information about importing Docker images into Singularity can be found in the [Singularity User Guide](https://sylabs.io/guides/2.6/user-guide/singularity_and_docker.html). 

## References

\[1\] Gregory M. Kurzer, Containers for Science, Reproducibility and Mobility: Singularity P2. Intel HPC Developer Conference, 2017. Available at: https://www.intel.com/content/dam/www/public/us/en/documents/presentation/hpc-containers-singularity-advanced.pdf
