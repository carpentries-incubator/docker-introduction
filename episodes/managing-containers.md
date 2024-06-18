---
title: Cleaning Up Containers
teaching: 10
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain how to list running and completed containers.
- Know how to list and remove container images.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I interact with a Docker container on my computer?
- How do I manage my containers and container images?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Removing images

The container images and their corresponding containers can start to take up a lot of disk space if you don't clean them up occasionally, so it's a good idea to periodically remove containers and container images that you won't be using anymore.

In order to remove a specific container image, you need to find out details about the container image,
specifically, the "Image ID". For example, say my laptop contained the following container image:

```bash
$ docker image ls
```

```output
REPOSITORY       TAG         IMAGE ID       CREATED          SIZE
hello-world      latest      fce289e99eb9   15 months ago    1.84kB
```

You can remove the container image with a `docker image rm` command that includes the *Image ID*, such as:

```bash
$ docker image rm fce289e99eb9
```

or use the container image name, like so:

```bash
$ docker image rm hello-world
```

However, you may see this output:

```output
Error response from daemon: conflict: unable to remove repository reference "hello-world" (must force) - container e7d3b76b00f4 is using its referenced image fce289e99eb9
```

This happens when Docker hasn't cleaned up some of the previously running containers
based on this container image. So, before removing the container image, we need to be able
to see what containers are currently running, or have been run recently, and how
to remove these.

## What containers are running?

Working with containers, we are going to shift back to the command: `docker container`.  Similar to `docker image`, we can list running containers by typing:

```bash
$ docker container ls
```

```output
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

Notice that this command didn't return any containers because our containers all exited and thus stopped running after they completed their work.

:::::::::::::::::::::::::::::::::::::::::  callout

## `docker ps`

The command `docker ps` serves the same purpose as `docker container ls`, and comes
from the Unix shell command `ps` which describes running processes.


::::::::::::::::::::::::::::::::::::::::::::::::::

## What containers have run recently?

There is also a way to list running containers, and those that have completed recently, which is to add the `--all`/`-a` flag to the `docker container ls` command as shown below.

```bash
$ docker container ls --all
```

```output
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
9c698655416a        hello-world         "/hello"            2 minutes ago       Exited (0) 2 minutes ago                       zen_dubinsky
6dd822cf6ca9        hello-world         "/hello"            3 minutes ago       Exited (0) 3 minutes ago                       eager_engelbart
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Keeping it clean

You might be surprised at the number of containers Docker is still keeping track of.
One way to prevent this from happening is to add the `--rm` flag to `docker container run`. This
will completely wipe out the record of the run container when it exits. If you need
a reference to the running container for any reason, **don't** use this flag.


::::::::::::::::::::::::::::::::::::::::::::::::::

## How do I remove an exited container?

To delete an exited container you can run the following command, inserting the `CONTAINER ID` for the container you wish to remove.
It will repeat the `CONTAINER ID` back to you, if successful.

```bash
$ docker container rm 9c698655416a
```

```output
9c698655416a
```

An alternative option for deleting exited containers is the `docker container prune` command. Note that this command doesn't accept a container ID as an
option because it deletes ALL exited containers!
**Be careful** with this command as deleting the container is **forever**.
**Once a container is deleted you can not get it back.**
If you have containers you may want to reconnect to, you should **not** use this command.
It will ask you if to confirm you want to remove these containers, see output below.
If successful it will print the full `CONTAINER ID` back to you for each container it has
removed.

```bash
$ docker container prune
```

```output
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
9c698655416a848278d16bb1352b97e72b7ea85884bff8f106877afe0210acfc
6dd822cf6ca92f3040eaecbd26ad2af63595f30bb7e7a20eacf4554f6ccc9b2b
```

## Removing images, for real this time

Now that we've removed any potentially running or stopped containers, we can try again to
delete the `hello-world` **container image**.

```bash
$ docker image rm hello-world
```

```output
Untagged: hello-world:latest
Untagged: hello-world@sha256:5f179596a7335398b805f036f7e8561b6f0e32cd30a32f5e19d17a3cda6cc33d
Deleted: sha256:fce289e99eb9bca977dae136fbe2a82b6b7d4c372474c9235adc1741675f587e
Deleted: sha256:af0b15c8625bb1938f1d7b17081031f649fd14e6b233688eea3c5483994a66a3
```

The reason that there are a few lines of output, is that a given container image may have been formed by merging multiple underlying layers.
Any layers that are used by multiple Docker container images will only be stored once.
Now the result of `docker image ls` should no longer include the `hello-world` container image.



{% comment %}

<!--  LocalWords:  keypoints amd64 fce289e99eb9 zen_dubinsky links.md
 -->

<!--  LocalWords:  eager_engelbart endcomment
 -->

{% endcomment %}

:::::::::::::::::::::::::::::::::::::::: keypoints

- `docker container` has subcommands used to interact and manage containers.
- `docker image` has subcommands used to interact and manage container images.
- `docker container ls` or `docker ps` can provide information on currently running containers.

::::::::::::::::::::::::::::::::::::::::::::::::::


