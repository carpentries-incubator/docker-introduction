---
title: "Exploring and Running Containers"
teaching: 20
exercises: 10
questions:
- "How do I interact with a Docker container on my computer?"
objectives:
- "Use the correct command to see which Docker images are on your computer."
- "Download new Docker images."
- "Demonstrate how to start an instance of a container from an image."
- "Describe at least two ways to run commands inside a running Docker container."
keypoints:
- "The `docker pull` command downloads Docker images from the internet."
- "The `docker image` command lists Docker images that are (now) on your computer."
- "The `docker run` command creates running containers from images and can run commands inside them."
- "When using the `docker run` command, a container can run a default action (if it
has one), a user specified action, or a shell to be used interactively."
---

> ## Reminder of terminology: images and containers
> Recall that a container "image" is the template from which particular instances of containers will be created.
{: .callout}

Let's explore our first Docker container. The Docker team provides a simple container
image online called `hello-world`. We'll start with that one.

## Downloading Docker images

The `docker image` command is used to list and modify Docker images.
You can find out what container images you have on your computer by using the following command ("ls" is short for "list"):
~~~
$ docker image ls
~~~
{: .language-bash}

If you've just
installed Docker, you won't see any images listed.

To get a copy of the `hello-world` Docker image from the internet, run this command:
~~~
$ docker pull hello-world
~~~
{: .language-bash}

You should see output like this:
~~~
Using default tag: latest
latest: Pulling from library/hello-world
1b930d010525: Pull complete
Digest: sha256:f9dfddf63636d84ef479d645ab5885156ae030f611a56f3a7ac7f2fdd86d7e4e
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
~~~
{: .output}

> ## DockerHub
>
> Where did the `hello-world` image come from? Technically, it came from the DockerHub
> website, which is a place to share Docker images with other people. More on that
> in a later episode.
{: .callout}

> ## Exercise: Check on Your Images
>
> What command would you use to see if the `hello-world` Docker image had downloaded
> successfully and was on your computer?
> Give it a try before checking the solution.
>
> > ## Solution
> >
> > To see if the `hello-world` image is now on your computer, run:
> > ~~~
> > $ docker image ls
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

Note that the downloaded `hello-world` image is not in the folder where you are in the terminal! (Run
`ls` by itself to check.) The image is not a file like our normal programs and files;
Docker stores it in a specific location that isn't commonly accessed, so it's necessary
to use the special `docker image` command to see what Docker images you have on your
computer.

## Running the `hello-world` container

To create and run containers from named Docker images you use the `docker run` command. Try the following `docker run` invocation. Note that it does not matter what your current working directory is.

~~~
$ docker run hello-world
~~~
{: .language-bash}
~~~
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
~~~
{: .output}

What just happened? When we use the `docker run` command, Docker does three things:

| 1. Starts a Running Container | 2. Performs Default Action | 3. Shuts Down the Container
| --------------------|-----------------|----------------|
| starts a running container, based on the image. Think of this as the "alive" or"inflated" version of the container -- it's actually doing something | If the container has a default action set, it will perform that default action. This could be as simple as printing a message (as above) or running a whole analysis pipeline! | Once the default action is complete, the container stops running (or exits). The image is still there, but nothing is actively running. |

The `hello-world` container is set up to run an action by default -
namely to print this message.

> ## Using `docker run` to get the image
>
> Technically, we could have skipped the `docker pull` step; if you use the `docker run`
> command and you don't already have a copy of the Docker image, Docker will
> automatically pull the image first and then run it.
{: .callout}

## Running a container with a chosen command

But what if we wanted to do something different with the container? The output
just gave us a suggestion of what to do -- let's use a different Docker image
to explore what else we can do with the `docker run` command. The suggestion above
is to use `ubuntu`, but we're going to run a different type of Linux, `alpine`
instead because it's quicker to download.

> ## Run the Alpine Docker container
>
> Try downloading and running the `alpine` Docker container. You can do it in
> two steps, or one. What are they?
{: .callout}

What happened when you ran the Alpine Docker container?

~~~
$ docker run alpine
~~~
{: .language-bash}

Probably nothing! That's because this particular container is designed for you to
provide commands yourself. Try running this instead:

~~~
$ docker run alpine cat /proc/version
~~~
{: .language-bash}

You should see the output of the `cat /proc/version` command, which prints out
the version of Linux that this container is using.

> ## Exercise
> Can you run the container and make it print a "hello world" message?
>
> Give it a try before checking the solution.
>
> > ## Solution
> >
> > Use the same command as above, but with the `echo` command to print a message.
> > ~~~
> > $ docker run alpine echo 'Hello World'
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

So here, we see another option -- we can provide commands at the end of the `docker run`
command and they will execute inside the running container.

## Running containers interactively

In all the examples above, Docker has started the container, run a command, and then
immediately shut down the container. But what if we wanted to keep the container
running so we could log into it and test drive more commands? The way to
do this is by adding the interactive flag `-it` to the `docker run` command and
by providing a shell (usually `bash` or `sh`) as our command.

~~~
$ docker run -it alpine sh
~~~
{: .language-bash}

Your prompt should change significantly to look like this:
~~~
/ #
~~~
{: .language-bash}

That's because you're now inside the running container! Try these commands:

* `pwd`
* `ls`
* `whoami`
* `echo $PATH`
* `cat /proc/version`

All of these are being run from inside the running container, so you'll get information
about the container itself, instead of your computer. To finish using the container,
just type `exit`.

~~~
/ # exit
~~~
{: .language-bash}

## Conclusion

So far, we've seen how to download Docker images, use them to run commands inside
running containers, and even how to explore a running container from the inside.
Next, we'll take a closer look at all the different kinds of Docker images that are out there.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints amd64 fce289e99eb9 zen_dubinsky links.md
 -->
<!--  LocalWords:  eager_engelbart endcomment
 -->
{% endcomment %}
