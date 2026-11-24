---
title: Creating Your Own Container Images
teaching: 20
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain the purpose of a `Dockerfile` and show some simple examples.
- Demonstrate how to build a container image with Podman from a `Dockerfile`.
- Compare the steps of creating a container image interactively versus a `Dockerfile`.
- Create an installation strategy for a container image.
- Demonstrate how to upload ('push') your container images to the Docker Hub.
- Describe the significance of the Docker Hub naming scheme.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I make my own container images with Podman?
- How do I document the 'recipe' for a container image?

::::::::::::::::::::::::::::::::::::::::::::::::::

There are lots of reasons why you might want to create your **own** container image.

- You can't find a container image with all the tools you need on Docker Hub or elsewhere.
- You want to have a container image to "archive" all the specific software versions you ran for a project.
- You want to share your workflow with someone else.

## Interactive installation

Before creating a reproducible installation, let's experiment with installing
software inside a container. Start a container from the `alpine` container image we used before, interactively:

```bash
$ podman container run -it alpine sh
```

Because this is a basic container, there's a lot of things not installed -- for
example, `python3`.

```bash
/# python3
```

```output
sh: python3: not found
```

Inside the container, we can run commands to install Python 3. The Alpine version of
Linux has a installation tool called `apk` that we can use to install Python 3.

```bash
/# apk add --update python3 py3-pip python3-dev
```

We can test our installation by running a Python command:

```bash
/# python3 --version
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Exercise: Searching for Help

Can you find instructions for installing R on Alpine Linux? Do they work?

:::::::::::::::  solution

## Solution

A quick search should hopefully show that the way to install R on Alpine Linux is:

```bash
/# apk add R
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

Once we exit, these changes are not saved to a new container image by default. There is
a command that will "snapshot" our changes, but building container images this way is
not easily reproducible. Instead, we're going to take what we've learned from this
interactive installation and create our container image from a reproducible recipe,
known as a `Dockerfile`.

If you haven't already, exit out of the interactively running container.

```bash
/# exit
```

## Put installation instructions in a `Dockerfile`

A `Dockerfile` is a plain text file with keywords and commands that
can be used to create a new container image.

:::::::::::::::::::::::::::::::::::::::::  callout

## Dockerfiles and Containerfiles

You may see references on the Internet and in documentation to both
`Dockerfile`s and `Containerfile`s. The two are essentially identical,
differing only in the file name used, and Podman is capable of using both. Due
to Docker's historical prominence it is very common for the `Dockerfile` name
to be used even in contexts which don't use Docker, and we will do so here
also -- but remember that there is no problem with using the alternate
`Containerfile` name.


::::::::::::::::::::::::::::::::::::::::::::::::::

From your shell, go to the folder you downloaded at the start of the lesson
and print out the Dockerfile inside:

```bash
$ cd ~/Desktop/podman-intro/basic
$ cat Dockerfile
```

```output
FROM <EXISTING IMAGE>
RUN <INSTALL CMDS FROM SHELL>
CMD <CMD TO RUN BY DEFAULT>
```

Let's break this file down:

- The first line, `FROM`, indicates which container image we're starting with.  It is the "base" container image we are going to start from.
- The next two lines `RUN`, will indicate installation commands we want to run. These
  are the same commands that we used interactively above.
- The last line, `CMD`, indicates the default command we want a
  container based on this container image to run, if no other command is provided. It is recommended
  to provide `CMD` in *exec-form* (see the
  (see the [`CMD` section](https://github.com/containers/common/blob/main/docs/Containerfile.5.md)
  of the documentation of the Containers GitHub for more details). It is written as a
  list which contains the executable to run as its first element,
  optionally followed by any arguments as subsequent elements. The list
  is enclosed in square brackets (`[]`) and its elements are
  double-quoted (`"`) strings which are separated by commas. For
  example, `CMD ["ls", "-lF", "--color", "/etc"]` would translate
  to `ls -lF --color /etc`.

:::::::::::::::::::::::::::::::::::::::::  callout

## *shell-form* and *exec-form* for CMD

Another way to specify the parameter for the
[`CMD` instruction](https://github.com/containers/common/blob/main/docs/Containerfile.5.md)
is the *shell-form*. Here you type the command as you would call it
from the command line. Podman then silently runs this command in the
image's standard shell. The *shell-form* `CMD cat /etc/passwd` is equivalent to
the *exec-form* `CMD ["/bin/sh", "-c", "cat /etc/passwd"]`. We recommend the
more explicit *exec-form* because we will be able to create more
flexible container image command options and make sure complex commands
are unambiguous in this format.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Exercise: Take a Guess

Do you have any ideas about what we should use to fill in the sample Dockerfile
to replicate the installation we did above?

:::::::::::::::  solution

## Solution:

Based on our experience above, edit the `Dockerfile` (in your text editor of choice)
to look like this:

```
FROM docker.io/alpine
RUN apk add --update python3 py3-pip python3-dev
CMD ["python3", "--version"]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

The recipe provided by the `Dockerfile` shown in the solution to the preceding exercise will use Alpine Linux as the base container image,
add Python 3, the pip package management tool and some additional Python header files, and set a default command to request Python 3 to
report its version information.

## Create a new container image

So far, we only have a text file named `Dockerfile` -- we do not yet have a container image.
We want Podman to take this `Dockerfile`,
run the installation commands contained within it, and then save the
resulting container as a new container image. To do this we will use the
`podman image build` command.

We have to provide `podman image build` with two pieces of information:

- the location of the `Dockerfile`
- the name of the new container image. Remember the naming scheme from before? You should name
  your new image with your Docker Hub username and a name for the container image, like this: `USERNAME/CONTAINER_IMAGE_NAME`.

All together, the build command that you should run on your computer, will have a similar structure to this:

```bash
$ podman image build -t URL/USERNAME/CONTAINER_IMAGE_NAME .
```

The `-t` option names the container image; the final dot indicates that the `Dockerfile` is in
our current directory.

The `URL` should be the name of the registry you are intending to upload the
image to. If you aren't intending to ever move the image elsewhere, you can skip
it and only give the `USERNAME` and `CONTAINER_IMAGE_NAME`. For example, if I
were intending to push the image to Docker Hub, my Docker Hub user name was
`alice` and I wanted to call my container image `alpine-python`, I would use
this command:

```bash
$ podman image build -t docker.io/alice/alpine-python .
```

Note, you can always re-tag an image later if the name needs to be updated.

:::::::::::::::::::::::::::::::::::::::::  callout

## Build Context

Notice that the final input to `podman image build` isn't the Dockerfile -- it's
a directory! In the command above, we've used the current working directory (`.`) of
the shell as the final input to the `podman image build` command. This option provides
what is called the *build context* to Podman -- if there are files being copied
into the built container image ([more details in the next episode](advanced-containers.md))
they're assumed to be in this location. Podman expects to see a Dockerfile in the
build context also (unless you tell it to look elsewhere).

Even if it won't need all of the files in the build context directory, Podman does
"load" them before starting to build, which means that it's a good idea to have
only what you need for the container image in a build context directory, as we've done
in this example.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Exercise: Review!

1. Think back to earlier. What command can you run to check if your container image was created
  successfully? (Hint: what command shows the container images on your computer?)

2. We didn't specify a tag for our container image name. What tag did Podman automatically use?

3. What command will run a container based on the container image you've created? What should happen by default
  if you run such a container? Without changing the Dockerfile, can you make it do something different, like print
  "hello world"?

:::::::::::::::  solution

## Solution

1. To see your new image, run `podman image ls`. You should see the name of your new
  container image under the "REPOSITORY" heading, , prepended by `localhost` as, for now,
  the image is on your local machine rather than a remote registry.

2. In the output of `podman image ls`, you can see that Podman has automatically
  used the `latest` tag for our new container image.

3. We want to use `podman container run` to run a container based on a container image.

The following command should run a container and print out our default message, the version
of Python:

```bash
$ podman container run docker.io/alice/alpine-python
```

To run a container based on our container image and print out "Hello world" instead:

```bash
$ podman container run docker.io/alice/alpine-python echo "Hello World"
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

While it may not look like you have achieved much, you have already effected the combination of a lightweight Linux operating system with your specification to run a given command that can operate reliably on macOS, Microsoft Windows, Linux and on the cloud!

## Boring but important notes about installation

There are a lot of choices when it comes to installing software -- sometimes too many!
Here are some things to consider when creating your own container image:

- **Start smart**, or, don't install everything from scratch! If you're using Python
  as your main tool, start with a [Python container
  image](https://hub.docker.com/_/python). Same with the
  [R programming language](https://hub.docker.com/r/rocker/r-ver/). We've used Alpine Linux as an
  example
  in this lesson, but it's generally not a good container image to start with for initial development and experimentation because it is
  a less common distribution of Linux; using [Ubuntu](https://hub.docker.com/_/ubuntu), [Debian](https://hub.docker.com/_/debian) and [Alma](https://hub.docker.com/_/almalinux) are all
  good options for scientific software installations. The program you're using might
  recommend a particular distribution of Linux, and if so, it may be useful to start with a container image for that distribution.
- **How big?** How much software do you really need to install? When you have a choice,
  lean towards using smaller starting container images and installing only what's needed for
  your software, as a bigger container image means longer download times to use.
- **Know (or Google) your Linux**. Different distributions of Linux often have distinct sets of tools for installing software. The `apk` command we used above is the software package installer for Alpine Linux. The installers for various common Linux distributions are listed below:
  - Ubuntu: `apt` or `apt-get`
  - Debian: `deb`
  - Alma/Rocky/Fedora: `dnf`
  - SUSE: `zypper`  
    Most common software installations are available to be installed via these tools.
    A web search for "install X on Y Linux" is usually a good start for common software
    installation tasks; if something isn't available via the Linux distribution's installation
    tools, try the options below.
- **Use what you know**. You've probably used commands like `pip` or `install.packages()`
  before on your own computer -- these will also work to install things in container images (if the basic scripting
  language is installed).
- **README**. Many scientific software tools have a README or installation instructions
  that lay out how to install software. You want to look for instructions for Linux. If
  the install instructions include options like those suggested above, try those first.

In general, a good strategy for installing software is:

- Make a list of what you want to install.
- Look for pre-existing container images.
- Read through instructions for software you'll need to install.
- Try installing everything interactively in your base container -- take notes!
- From your interactive installation, create a `Dockerfile` and then try to build
  the container image from that.

## Share your new container image on Docker Hub

Container images that you release publicly can be stored on the Docker Hub for free.  If you
name your container image as described above, with your Docker Hub username, all you need to do
is run the opposite of `podman image pull` -- `podman image push`.

```bash
$ podman image push docker.io/alice/alpine-python
```

Make sure to substitute the full name of your container image!

In a web browser, open [https://hub.docker.com](https://hub.docker.com), and on your user page you should now see your container image listed, for anyone to use or build on.

:::::::::::::::::::::::::::::::::::::::::  callout

## Logging In

Technically, you have to be logged into Docker Hub with Podman on your computer
for this to work. If you haven't yet done this, `podman image push` won't work
for you. You can do this on the command line by running `podman login docker.io`
first, entering your Docker Hub username and password, and then trying `podman
image push` again. If you installed Podman via Podman Desktop, you can also log
in with the GUI by opening Podman Desktop, then going to 'Settings', then
'Registries', then clicking 'Configure' for the Docker Hub entry.


::::::::::::::::::::::::::::::::::::::::::::::::::

## What's in a name? (again)

You don't *have* to name your containers images using the `URL/USERNAME/CONTAINER_IMAGE_NAME:TAG` naming scheme. On your own computer, you can call container images whatever you want, and refer to
them by the names you choose. It's only when you want to share a container image that it
needs the correct naming format.

You can rename container images using the `podman image tag` command. For example, imagine someone
named Alice has been working on a workflow container image and called it `workflow-test`
on her own computer. She now wants to share it in her `alice` Docker Hub account
with the name `workflow-complete` and a tag of `v1`. Her `podman image tag` command
would look like this:

```bash
$ podman image tag workflow-test docker.io/alice/workflow-complete:v1
```

She could then push the re-named container image to Docker Hub,
using `podman image push docker.io/alice/workflow-complete:v1`



:::::::::::::::::::::::::::::::::::::::: keypoints

- `Dockerfile`s specify what is within container images.
- The `podman image build` command is used to build a container image from a `Dockerfile`.
- You can share your container images through the Docker Hub so that others can create containers from your container images.

::::::::::::::::::::::::::::::::::::::::::::::::::


