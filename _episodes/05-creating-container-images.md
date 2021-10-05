---
title: "Creating Your Own Container Images"
teaching: 20
exercises: 15
questions:
- "How can I make my own Docker images?"
- "How do I document the 'recipe' for a Docker image?"
objectives:
- "Explain the purpose of a `Dockerfile` and show some simple examples."
- "Demonstrate how to build a Docker image from a `Dockerfile`."
- "Compare the steps of creating a container interactively versus a `Dockerfile`."
- "Create an installation strategy for a container."
- "Demonstrate how to upload ('push') your container images to the Docker Hub."
- "Describe the significance of the Docker Hub naming scheme."
keypoints:
- "`Dockerfile`s specify what is within Docker images."
- "The `docker build` command is used to build an image from a `Dockerfile`."
- "You can share your Docker images through the Docker Hub so that others can create Docker containers from your images."
---

There are lots of reasons why you might want to create your **own** Docker image.
- You can't find a container with all the tools you need on Docker Hub.
- You want to have a container to "archive" all the specific software versions you ran for a project.
- You want to share your workflow with someone else.

## Interactive installation

Before creating a reproducible installation, let's experiment with installing
software inside a container. Start the `alpine` container from before, interactively:

~~~
$ docker run -it alpine sh
~~~
{: .language-bash}

Because this is a basic container, there's a lot of things not installed -- for
example, `python3`.

~~~
/# python3
~~~
{: .language-bash}
~~~
sh: python3: not found
~~~
{: .output}

Inside the container, we can run commands to install Python3. The Alpine version of
Linux has a installation tool called `apk` that we can use to install Python3.

~~~
/# apk add --update python3 py3-pip python3-dev
~~~
{: .language-bash}

We can test our installation by running a Python command:
~~~
/# python3 --version
~~~
{: .language-bash}

Once Python is installed, we can add Python packages using the pip package installer:
~~~
/# pip install cython
~~~
{: .language-bash}

> ## Exercise: Searching for Help
>
> Can you find instructions for installing R on Alpine Linux? Do they work?
>
> > ## Solution
> >
> > A quick search should hopefully show that the way to install R on Alpine Linux is:
> > ~~~
> > /# apk add R
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

Once we exit, these changes are not saved to a new container by default. There is
a command that will "snapshot" our changes, but building containers this way is
not easily reproducible. Instead, we're going to take what we've learned from this
interactive installation and create our container from a reproducible recipe,
known as a `Dockerfile`.

If you haven't already, exit out of the interactively running container.

~~~
/# exit
~~~
{: .language-bash}


## Put installation instructions in a `Dockerfile`

A `Dockerfile` is a plain text file with keywords and commands that
can be used to create a new container image.

From your shell, go to the folder you downloaded at the start of the lesson
and print out the Dockerfile inside:

~~~
$ cd ~/Desktop/docker-intro/basic
$ cat Dockerfile
~~~
{: .language-bash}
~~~
FROM <EXISTING IMAGE>
RUN <INSTALL CMDS FROM SHELL>
RUN <INSTALL CMDS FROM SHELL>
CMD <CMD TO RUN BY DEFAULT>
~~~
{: .output}

Let's break this file down:

- The first line, `FROM`, indicates which container we're starting with.  It is the "base" image we are going to start from.
- The next two lines `RUN`, will indicate installation commands we want to run. These
are the same commands that we used interactively above.
- The last line, `CMD`, indicates the default command we want the
container to run, if no other command is provided. It is recommended
to provide `CMD` in *exec-form* (see the
[`CMD` section](https://docs.docker.com/engine/reference/builder/#cmd)
of the Dockerfile documentation for more details). It is written as a
list which contains the executable to run as its first element,
optionally followed by any arguments as subsequent elements. The list
is enclosed in square brackets (`[]`) and its elements are
double-quoted (`"`) strings which are separated by commas. For
example, `CMD ["ls", "-lF", "--color", "/etc"]` would translate
to `ls -lF --color /etc`.

> ## *shell-form* and *exec-form* for CMD
> Another way to specify the parameter for the
> [`CMD` instruction](https://docs.docker.com/engine/reference/builder/#cmd)
> is the *shell-form*. Here you type the command as you would call it
> from the command line. Docker then silently runs this command in the
> image's standard shell.  `CMD cat /etc/passwd` is equivalent to `CMD
> ["/bin/sh", "-c", "cat /etc/passwd"]`. We recommend to prefer the
> more explicit *exec-form* because we will be able to create more
> flexible container command options and make sure complex commands
> are unambiguous in this format.
{: .callout}

> ## Exercise: Take a Guess
>
> Do you have any ideas about what we should use to fill in the sample Dockerfile
> to replicate the installation we did above?
>
> > ## Solution:
> > Based on our experience above, edit the `Dockerfile` (in your text editor of choice)
> > to look like this:
> > ~~~
> > FROM alpine
> > RUN apk add --update python3 py3-pip python3-dev
> > RUN pip install cython
> > CMD ["python3", "--version"]
> > ~~~
> {: .solution}
{: .challenge}

The recipe provided by the `Dockerfile` shown in the solution to the preceding exercise will use Alpine Linux as the base container,
add Python and the Cython library, and set a default command to request Python to report its version information.

## Create a new Docker image

So far, we only have a text file named `Dockerfile` -- we do not yet have a container image.
We want Docker to take this `Dockerfile`,
run the installation commands contained within it, and then save the
resulting container as a new container image. To do this we will use the
`docker build` command.

We have to provide `docker build` with two pieces of information:
- the location of the `Dockerfile`
- the name of the new image. Remember the naming scheme from before? You should name
your new image with your Docker Hub username and a name for the container, like this: `USERNAME/CONTAINERNAME`.

All together, the build command that you should run on your computer, will have a similar structure to this:

~~~
$ docker build -t USERNAME/CONTAINERNAME .
~~~
{: .language-bash}

The `-t` option names the container; the final dot indicates that the `Dockerfile` is in
our current directory.

For example, if my user name was `alice` and I wanted to call my
image `alpine-python`, I would use this command:
~~~
$ docker build -t alice/alpine-python .
~~~
{: .language-bash}

> ## Build Context
>
> Notice that the final input to `docker build` isn't the Dockerfile -- it's
> a directory! In the command above, we've used the current working directory (`.`) of
> the shell as the final input to the `docker build` command. This option provides
> what is called the *build context* to Docker -- if there are files being copied
> into the built container [more details in the next episode](/05b-advanced-containers)
> they're assumed to be in this location. Docker expects to see a Dockerfile in the
> build context also (unless you tell it to look elsewhere).
>
> Even if it won't need all of the files in the build context directory, Docker does
> "load" them before starting to build, which means that it's a good idea to have
> only what you need for the container in a build context directory, as we've done
> in this example.
{: .callout}


> ## Exercise: Review!
>
> 1. Think back to earlier. What command can you run to check if your image was created
> successfully? (Hint: what command shows the images on your computer?)
>
> 2. We didn't specify a tag for our image name. What tag did Docker automatically use?
>
> 3. What command will run the container you've created? What should happen by default
> if you run the container? Can you make it do something different, like print
> "hello world"?
>
> > ## Solution
> >
> > 1. To see your new image, run `docker image ls`. You should see the name of your new
> > image under the "REPOSITORY" heading.
> >
> > 2. In the output of `docker image ls`, you can see that Docker has automatically
> > used the `latest` tag for our new image.
> >
> > 3. We want to use `docker run` to run the container.
> >
> > The following command should run the container and print out our default message, the version
> > of Python:
> > ~~~
> > $ docker run alice/alpine-python
> > ~~~
> > {: .language-bash}
> >
> > To run the container and print out "Hello world" instead:
> > ~~~
> > $ docker run alice/alpine-python echo "Hello World"
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

While it may not look like you have achieved much, you have already effected the combination of a lightweight Linux operating system with your specification to run a given command that can operate reliably on macOS, Microsoft Windows, Linux and on the cloud!

## Boring but important notes about installation

There are a lot of choices when it comes to installing software -- sometimes too many!
Here are some things to consider when creating your own container:

- **Start smart**, or, don't install everything from scratch! If you're using Python
as your main tool, start with a [Python container](https://hub.docker.com/_/python). Same with [R](https://hub.docker.com/r/rocker/r-ver/). We've used Alpine Linux as an example
in this lesson, but it's generally not a good container to start with for initial development and experimentation because it is
a less common distribution of Linux; using [Ubuntu](https://hub.docker.com/_/ubuntu), [Debian](https://hub.docker.com/_/debian) and [CentOS](https://hub.docker.com/_/centos) are all
good options for scientific software installations. The program you're using might
recommend a particular distribution of Linux, and if so, it may be useful to start with a container image for that distribution.
- **How big?** How much software do you really need to install? When you have a choice,
lean towards using smaller starting images and installing only what's needed for
your software, as a bigger image means longer download times to use.
- **Know (or Google) your Linux**. Different distributions of Linux often have distinct sets of tools for installing software. The `apk` command we used above is the software package installer for Alpine Linux. The installers for various common Linux distributions are listed below:
    - Ubuntu: `apt` or `apt-get`
    - Debian: `deb`
    - CentOS: `yum`
  Most common software installations are available to be installed via these tools.
  A web search for "install X on Y Linux" is usually a good start for common software
  installation tasks; if something isn't available via the Linux distribution's installation
  tools, try the options below.
- **Use what you know**. You've probably used commands like `pip` or `install.packages()`
before on your own computer -- these will also work to install things in containers (if the basic scripting
language is installed).
- **README**. Many scientific software tools have a README or installation instructions
that lay out how to install software. You want to look for instructions for Linux. If
the install instructions include options like those suggested above, try those first.

In general, a good strategy for installing software is:
- Make a list of what you want to install.
- Look for pre-existing containers.
- Read through instructions for software you'll need to install.
- Try installing everything interactively in your base container -- take notes!
- From your interactive installation, create a `Dockerfile` and then try to build
the container again from that.

## Share your new container on Docker Hub

Images that you release publicly can be stored on the Docker Hub for free.  If you
name your image as described above, with your Docker Hub username, all you need to do
is run the opposite of `docker pull` -- `docker push`.

~~~
$ docker push alice/alpine-python
~~~
{: .language-bash}

Make sure to substitute the full name of your container!

In a web browser, open <https://hub.docker.com>, and on your user page you should now see your container listed, for anyone to use or build on.

> ## Logging In
>
> Technically, you have to be logged into Docker on your computer for this to work.
> Usually it happens by default, but if `docker push` doesn't work for you,
> run `docker login` first, enter your Docker Hub username and password, and then
> try `docker push` again.
{: .callout}

## What's in a name? (again)

You don't *have* to name your containers using the `USERNAME/CONTAINER:TAG` naming scheme. On your own computer, you can call containers whatever you want, and refer to
them by the names you choose. It's only when you want to share a container that it
needs the correct naming format.

You can rename images using the `docker tag` command. For example, imagine someone
named Alice has been working on a workflow container and called it `workflow-test`
on her own computer. She now wants to share it in her `alice` Docker Hub account
with the name `workflow-complete` and a tag of `v1`. Her `docker tag` command
would look like this:
~~~
$ docker tag workflow-test alice/workflow-complete:v1
~~~
{: .language-bash}

She could then push the re-named container to Docker Hub,
using `docker push alice/workflow-complete:v1`

{% include links.md %}
