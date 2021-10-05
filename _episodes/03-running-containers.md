---
title: "Exploring and Running Containers"
teaching: 20
exercises: 10
questions:
- "How do I interact with a Docker container on my computer?"
objectives:
- "Use the correct command to see which Docker images are on your computer."
- "Be able to download new Docker images."
- "Demonstrate how to start an instance of a container from an image."
- "Describe at least two ways to execute commands inside a running Docker container."
keypoints:
- "The `docker image pull` command downloads Docker images from the internet."
- "The `docker image ls` command lists Docker images that are (now) on your computer."
- "The `docker container run` command creates running containers from images and can run commands inside them."
- "When using the `docker container run` command, a container can run a default action (if it
has one), a user specified action, or a shell to be used interactively."
---

> ## Reminder of terminology: images and containers
> Recall that a container "image" is the template from which particular instances of containers will be created.
{: .callout}

Let's explore our first Docker container. The Docker team provides a simple container
image online called `hello-world`. We'll start with that one.

## Downloading Docker images

The `docker image` command is used to interact with Docker images.
You can find out what container images you have on your computer by using the following command ("ls" is short for "list"):
~~~
$ docker image ls
~~~
{: .language-bash}

If you've just
installed Docker, you won't see any images listed.

To get a copy of the `hello-world` Docker image from the internet, run this command:
~~~
$ docker image pull hello-world
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

> ## Docker Hub
>
> Where did the `hello-world` image come from? It came from the Docker Hub
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
`ls` by itself to check.) The image is not a file like our normal programs and documents;
Docker stores it in a specific location that isn't commonly accessed, so it's necessary
to use the special `docker image` command to see what Docker images you have on your
computer.

## Running the `hello-world` container

To create and run containers from named Docker images you use the `docker container run` command. Try the following `docker container run` invocation. Note that it does not matter what your current working directory is.

~~~
$ docker container run hello-world
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

What just happened? When we use the `docker container run` command, Docker does three things:

| 1. Starts a Running Container | 2. Performs Default Action | 3. Shuts Down the Container
| --------------------|-----------------|----------------|
| Starts a running container, based on the image. Think of this as the "alive" or "inflated" version of the container -- it's actually doing something. | If the container has a default action set, it will perform that default action. This could be as simple as printing a message (as above) or running a whole analysis pipeline! | Once the default action is complete, the container stops running (or exits). The image is still there, but nothing is actively running. |

The `hello-world` container is set up to run an action by default --
namely to print this message.

> ## Using `docker container run` to get the image
>
> We could have skipped the `docker image pull` step; if you use the `docker container run`
> command and you don't already have a copy of the Docker image, Docker will
> automatically pull the image first and then run it.
{: .callout}

## Running a container with a chosen command

But what if we wanted to do something different with the container? The output
just gave us a suggestion of what to do -- let's use a different Docker image
to explore what else we can do with the `docker container run` command. The suggestion above
is to use `ubuntu`, but we're going to run a different type of Linux, `alpine`
instead because it's quicker to download.

> ## Run the Alpine Docker container
>
> Try downloading and running the `alpine` Docker container. You can do it in
> two steps, or one. What are they?
{: .challenge}

What happened when you ran the Alpine Docker container?

~~~
$ docker container run alpine
~~~
{: .language-bash}

If you never used the *alpine* docker image on your computer, docker probably printed a message that it couldn't find the image and had to download it.
If you used the alpine image before, the command will probably show no output. That's because this particular container is designed for you to
provide commands yourself. Try running this instead:

~~~
$ docker container run alpine cat /etc/os-release
~~~
{: .language-bash}

You should see the output of the `cat /etc/os-release` command, which prints out
the version of Alpine Linux that this container is using and a few additional bits of information.

> ## Hello World, Part 2
> Can you run the container and make it print a "hello world" message?
>
> Give it a try before checking the solution.
>
> > ## Solution
> >
> > Use the same command as above, but with the `echo` command to print a message.
> > ~~~
> > $ docker container run alpine echo 'Hello World'
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

So here, we see another option -- we can provide commands at the end of the `docker container run`
command and they will execute inside the running container.

## Running containers interactively

In all the examples above, Docker has started the container, run a command, and then
immediately shut down the container. But what if we wanted to keep the container
running so we could log into it and test drive more commands? The way to
do this is by adding the interactive flag `-it`
to the `docker container run` command and provide a shell (`bash`,`sh`, etc.)
as our command. The alpine docker image doesn't include `bash` so we need to use `sh`.

~~~
$ docker container run -it alpine sh
~~~
{: .language-bash}

> ## Technically...
>
> Technically, the interactive flag is just `-i` -- the extra `-t` (combined
> as `-it` above) is the "pseudo-TTY" option, a fancy term that means a text interface.
> This allows you to connect to a shell, like `bash`, using a command line. Since you usually
> want to have a command line when running interactively, it makes sense to use the two together.
{: .callout}


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
* `cat /etc/os-release`

All of these are being run from inside the running container, so you'll get information
about the container itself, instead of your computer. To finish using the container,
just type `exit`.

~~~
/ # exit
~~~
{: .language-bash}

> ## Practice Makes Perfect
> Can you find out the version of Linux installed on the `busybox` container?
> (Hint: If you search online, you'll find that there are a few different ways
> to find out what version of Linux a computer or container is running. Because
> the `busybox` container is very simplified, you'll want to use a command that prints out
> the contents of the file `/proc/version`.)
>
> Can you also find the `busybox` program? What does it do? (Hint: try passing `--help`
> to almost any command will give you more information.)
>
>
> > ## Solution 1 -- Interactive
> >
> > Run the busybox container interactively -- you can use `docker image pull` first, or just
> > run it with this command:
> > ~~~
> > $ docker container run -it busybox sh
> > ~~~
> > {: .language-bash}
> >
> > Then try, running these commands
> >
> > ~~~
> > /# cat /proc/version
> > /# busybox --help
> > ~~~
> > {: .language-bash}
> >
> > Exit when you're done.
> > ~~~
> > /# exit
> > ~~~
> > {: .language-bash}
> {: .solution}
>
> > ## Solution 2 -- Run commands
> >
> > Run the busybox container, first with a command to read out the Linux version:
> > ~~~
> > $ docker container run busybox cat /proc/version
> > ~~~
> > {: .language-bash}
> >
> > Then run the container again with a command to print out the busybox help:
> > ~~~
> > $ docker container run busybox busybox --help
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

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
