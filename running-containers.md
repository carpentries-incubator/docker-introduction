---
title: Exploring and Running Containers
teaching: 20
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Use the correct command to see which container images are on your computer.
- Be able to download new container images.
- Demonstrate how to start an instance of a container from a container image.
- Describe at least two ways to execute commands inside a running container.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I interact with Podman containers and container images on my computer?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Reminder of terminology: container images and containers

Recall that a *container image* is the template from which particular instances of *containers* will be created.


::::::::::::::::::::::::::::::::::::::::::::::::::

Let's explore our first Podman container. The Podman team provides a simple container
image online called `hello`. We'll start with that one.

## Downloading Podman images

The `podman image` command is used to interact with Podman container images.
You can find out what container images you have on your computer by using the following command ("ls" is short for "list"):

```bash
$ podman image ls
```

If you've just installed Podman, you won't see any container images listed.

To get a copy of the `hello` Podman container image from the internet, run this command:

```bash
$ podman image pull hello
```

You should see output like this:

```output
Resolved "hello" as an alias (/etc/containers/registries.conf.d/000-shortnames.conf)
Trying to pull quay.io/podman/hello:latest...
Getting image source signatures
Copying blob sha256:1ff9adeff4443b503b304e7aa4c37bb90762947125f4a522b370162a7492ff47
Copying config sha256:83fc7ce1224f5ed3885f6aaec0bb001c0bbb2a308e3250d7408804a720c72a32
Writing manifest to image destination
83fc7ce1224f5ed3885f6aaec0bb001c0bbb2a308e3250d7408804a720c72a32
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Docker Hub

Where did the `hello` container image come from? If you look carefully in the 
output when you pulled the image, you will see that it came from the Quay container
registry, which is a place to share container images with other people. Specifically,
Podman expanded the short container name to `quay.io/podman/hello`.
Other container registries exist, sometimes with differing use cases. Docker Hub is probably the
most widely used. Although under the 'Docker' name, Docker Hub can be used by any
compatible containerization service, including Podman and Singularity. We can get Docker's
version of a `hello` image by instead pulling `docker.io/hello-world`.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Exercise: Check on Your Images

What command would you use to see if the `hello` container image had downloaded
successfully and was on your computer?
Give it a try before checking the solution.

:::::::::::::::  solution

## Solution

To see if the `hello` container image is now on your computer, run:

```bash
$ podman image ls
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

Note that the downloaded `hello` container image is not in the folder where you are in the terminal! (Run
`ls` by itself to check.) The container image is not a file like our normal programs and documents;
Podman stores it in a specific location that isn't commonly accessed, so it's necessary
to use the special `podman image` command to see what Podman container images you have on your
computer.

## Running the `hello` container

To create and run containers from named Podman container images you use the `podman container run` command. Try the following `podman container run` invocation. Note that it does not matter what your current working directory is.

```bash
$ podman container run hello
```

```output
!... Hello Podman World ...!

         .--"--.
       / -     - \
      / (O)   (O) \
   ~~~| -=(,Y,)=- |
    .---. /`  \   |~~
 ~/  o  o \~~~~.----. ~~
  | =(X)= |~  / (O (O) \
   ~~~~~~~  ~| =(Y_)=-  |
  ~~~~    ~~~|   U      |~~

Project:   https://github.com/containers/podman
Website:   https://podman.io
Desktop:   https://podman-desktop.io
Documents: https://docs.podman.io
YouTube:   https://youtube.com/@Podman
X/Twitter: @Podman_io
Mastodon:  @Podman_io@fosstodon.org
```

What just happened? When we use the `podman container run` command, Podman does three things:

| 1\. Starts a Running Container                                                                                                                                   | 2\. Performs Default Action                                                                                                                                                     | 3\. Shuts Down the Container                                                                                                                       | 
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Starts a running container, based on the container image. Think of this as the "alive" or "inflated" version of the container -- it's actually doing something. | If the container has a default action set, it will perform that default action. This could be as simple as printing a message (as above) or running a whole analysis pipeline! | Once the default action is complete, the container stops running (or exits). The container image is still there, but nothing is actively running. | 

The `hello` container is set up to run an action by default --
namely to print this message.

:::::::::::::::::::::::::::::::::::::::::  callout

## Using `podman container run` to get the image

We could have skipped the `podman image pull` step; if you use the `podman container run`
command and you don't already have a copy of the Podman container image, Podman will
automatically pull the container image first and then run it.


::::::::::::::::::::::::::::::::::::::::::::::::::

## Running a container with a chosen command

But what if we wanted to do something different with the container? Let's use a
different container image to explore what else we can do with the `podman
container run` command. One image we could use is `ubuntu` which provides, as
the name suggests, a container running Ubuntu Linux. However, we're going to run
a different type of Linux instead, `alpine`, because it's smaller and so the
image is quicker to download.

:::::::::::::::::::::::::::::::::::::::  challenge

## Run the Alpine Podman container

Try downloading the `alpine` container image and using it to run a container. You can do it in
two steps, or one. What are they?


::::::::::::::::::::::::::::::::::::::::::::::::::

What happened when you ran the Alpine Podman container?

```bash
$ podman container run alpine
```

If you have never used the `alpine` container image on your computer, Podman probably printed a
message that it couldn't find the container image and had to download it.
If you used the `alpine` container image before, the command will probably show no output. That's
because this particular container is designed for you to provide commands yourself. Try running
this instead:

```bash
$ podman container run alpine cat /etc/os-release
```

You should see the output of the `cat /etc/os-release` command, which prints out
the version of Alpine Linux that this container is using and a few additional bits of information.

:::::::::::::::::::::::::::::::::::::::  challenge

## Hello World, Part 2

Can you run a copy of the `alpine` container and make it print a "hello world" message?

Give it a try before checking the solution.

:::::::::::::::  solution

## Solution

Use the same command as above, but with the `echo` command to print a message.

```bash
$ podman container run alpine echo 'Hello World'
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

So here, we see another option -- we can provide commands at the end of the `podman container run`
command and they will execute inside the running container.

## Running containers interactively

In all the examples above, Podman has started the container, run a command, and then
immediately stopped the container. But what if we wanted to keep the container
running so we could log into it and test drive more commands? The way to
do this is by adding the interactive flags `-i` and `-t` (usually combined as `-it`)
to the `podman container run` command and provide a shell (`bash`,`sh`, etc.)
as our command. The `alpine` container image doesn't include `bash` so we need
to use `sh`.

```bash
$ podman container run -it alpine sh
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Technically...

Technically, the interactive flag is just `-i` -- the extra `-t` (combined
as `-it` above) is the "pseudo-TTY" option, a fancy term that means a text interface.
This allows you to connect to a shell, like `sh`, using a command line. Since you usually
want to have a command line when running interactively, it makes sense to use the two together.


::::::::::::::::::::::::::::::::::::::::::::::::::

Your prompt should change significantly to look like this:

```bash
/ #
```

That's because you're now inside the running container! Try these commands:

- `pwd`
- `ls`
- `whoami`
- `echo $PATH`
- `cat /etc/os-release`

All of these are being run from inside the running container, so you'll get information
about the container itself, instead of your computer. To finish using the container,
type `exit`.

```bash
/ # exit
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Practice Makes Perfect

Can you find out the version of Ubuntu installed on the `ubuntu` container image?
(Hint: You can use the same command as used to find the version of alpine.)

Can you also find the `apt-get` program? What does it do? (Hint: try passing `--help`
to almost any command will give you more information.)

:::::::::::::::  solution

## Solution 1 -- Interactive

Run an interactive ubuntu container -- you can use `podman image pull` first, or just
run it with this command:

```bash
$ podman container run -it ubuntu sh
```

OR you can get the bash shell instead

```bash
$ podman container run -it ubuntu bash
```

Then try, running these commands

```bash
/# cat /etc/os-release
/# apt-get --help
```

Exit when you're done.

```bash
/# exit
```

:::::::::::::::::::::::::

:::::::::::::::  solution

## Solution 2 -- Run commands

Run a ubuntu container, first with a command to read out the Linux version:

```bash
$ podman container run ubuntu cat /etc/os-release
```

Then run a container with a command to print out the apt-get help:

```bash
$ podman container run ubuntu apt-get --help
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Even More Options

There are many more options, besides `-it` that can be used with the `podman container run`
command!  A few of them will be covered in [later episodes](/advanced-containers)
and we'll share two more common ones here:

- `--rm`: this option guarantees that any running container is completely
  removed from your computer after the container is stopped. Without this option,
  Podman actually keeps the "stopped" container around, which you'll see in a later
  episode. Note that this option doesn't impact the *container images* that you've pulled,
  just running instances of containers.

- `--name=`: By default, Podman assigns a random name and ID number to each container
  instance that you run on your computer. If you want to be able to more easily refer
  to a specific running container, you can assign it a name using this option.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Conclusion

So far, we've seen how to download container images, use Podman to run commands inside
running containers, and even how to explore a running container from the inside.
Next, we'll take a closer look at all the different kinds of container images that are out there.



<!--  LocalWords:  keypoints amd64 fce289e99eb9 zen_dubinsky links.md
 -->

<!--  LocalWords:  eager_engelbart endcomment
 -->

:::::::::::::::::::::::::::::::::::::::: keypoints

- The `podman image pull` command downloads container images from the internet.
- The `podman image ls` command lists Podman container images that are (now) on your computer.
- The `podman container run` command creates running containers from container images and can run commands inside them.
- When using the `podman container run` command, a container can run a default action (if it has one), a user specified action, or a shell to be used interactively.

::::::::::::::::::::::::::::::::::::::::::::::::::
