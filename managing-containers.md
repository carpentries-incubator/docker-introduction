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

- How do I interact with a container on my computer?
- How do I manage my containers and container images?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Removing images

The container images and their corresponding containers can start to take up a lot of disk space if you don't clean them up occasionally, so it's a good idea to periodically remove containers and container images that you won't be using anymore.

In order to remove a specific container image, you need to find out details about the container image,
specifically, the "Image ID". For example, say my laptop contained the following container image:

```bash
$ podman image ls
```

```output
REPOSITORY                TAG         IMAGE ID      CREATED        SIZE
quay.io/podman/hello      latest      83fc7ce1224f  14 months ago  580 kB
```

You can remove the container image with a `podman image rm` command that includes the *Image ID*, such as:

```bash
$ podman image rm 83fc7ce1224f
```

or use the container image name, like so:

```bash
$ podman image rm quay.io/podman/hello
```

You can also drop `quay.io/podman/` and only use the short name `hello` as there is no other image with this name. If you had another image called `hello` from another registry, you would need to specify the full name to distinguish between them.

```bash
podman image rm hello
```

However, you may see this output:

```output
Error: image used by 2061ddb499b6e0d856cfd1d2dee2b0a365f577256ff76d6e29615f1701ddb420: image is in use by a container: consider listing external containers and force-removing image
```

This happens when Podman hasn't cleaned up some of the previously running containers
based on this container image. So, before removing the container image, we need to be able
to see what containers are currently running, or have been run recently, and how
to remove these.

## What containers are running?

Working with containers, we are going to shift back to the command: `podman container`.  Similar to `podman image`, we can list running containers by typing:

```bash
$ podman container ls
```

```output
CONTAINER ID  IMAGE                            COMMAND               CREATED        STATUS                    PORTS       NAMES
```

Notice that this command didn't return any containers because our containers all exited and thus stopped running after they completed their work.

:::::::::::::::::::::::::::::::::::::::::  callout

## `podman ps`

The command `podman ps` serves the same purpose as `podman container ls`, and comes
from the Unix shell command `ps` which describes running processes.


::::::::::::::::::::::::::::::::::::::::::::::::::

## What containers have run recently?

There is also a way to list running containers, and those that have completed recently, which is to add the `--all`/`-a` flag to the `podman container ls` command as shown below.

```bash
$ podman container ls --all
```

```output
CONTAINER ID  IMAGE                            COMMAND               CREATED        STATUS                    PORTS       NAMES
2061ddb499b6  quay.io/podman/hello:latest      /usr/local/bin/po...  8 minutes ago  Exited (0) 8 minutes ago              suspicious_swanson
6091eac31f58  quay.io/podman/hello:latest      /usr/local/bin/po...  2 seconds ago  Exited (0) 2 seconds ago              ecstatic_nash
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Keeping it clean

You might be surprised at the number of containers Podman is still keeping track of.
One way to prevent this from happening is to add the `--rm` flag to `podman container run`. This
will completely wipe out the record of the run container when it exits. If you need
a reference to the running container for any reason, **don't** use this flag.


::::::::::::::::::::::::::::::::::::::::::::::::::

## How do I remove an exited container?

To delete an exited container you can run the following command, inserting the `CONTAINER ID` for the container you wish to remove.
It will repeat the `CONTAINER ID` back to you, if successful.

```bash
$ podman container rm 6091eac31f58
```

```output
6091eac31f58
```

You can equivalently provide the `NAME` of the container to remove it.

```bash
$ podman container rm suspicious_swanson
```

An alternative option for deleting exited containers is the `podman container prune` command. Note that this command doesn't accept a container ID as an
option because it deletes ALL exited containers!
**Be careful** with this command as deleting the container is **forever**.
**Once a container is deleted you can not get it back.**
If you have containers you may want to reconnect to, you should **not** use this command.
It will ask you if to confirm you want to remove these containers, see output below.
If successful it will print the full `CONTAINER ID` back to you for each container it has
removed.

```bash
$ podman container prune
```

```output
WARNING! This will remove all non running containers.
Are you sure you want to continue? [y/N] y
400f00fc395f2e995130970dc0efe0b27e9a43a0a2bc9389aad9c62810a6573a
670bfc78bcc54332c1d9de5e09dc3cf4478e12ebb37e9d00d6e228decbb1c25a
```

## Removing images, for real this time

Now that we've removed any potentially running or stopped containers, we can try again to
delete the `hello` **container image**.

```bash
$ podman image rm hello
```

```output
Untagged: quay.io/podman/hello:latest
Deleted: 83fc7ce1224f5ed3885f6aaec0bb001c0bbb2a308e3250d7408804a720c72a32
```

The image you deleted may have been formed by merging multiple underlying layers.
In this case, you may see multiple lines of deletions when running `podman image
rm` on what appears to be a single image. Any layers that are used by multiple
container images will only be stored once. Now the result of `podman image ls`
should no longer include the `hello` container image.

:::::::::::::::::::::::::::::::::::::::::  callout

## Using the GUI

If you have installed the Podman Desktop GUI, you should be able to use it
to view and delete containers and container images. It will provide the same
information as the command line `podman` tools, and you will still need to
delete containers before the associated container image. Nevertheless, it's still
worth learning to use `podman` on the terminal as this underpins the rest of the
technology and it's not guaranteed that all systems you work on will have a
GUI to use!

::::::::::::::::::::::::::::::::::::::::::::::::::


<!--  LocalWords:  keypoints amd64 fce289e99eb9 zen_dubinsky links.md
 -->

<!--  LocalWords:  eager_engelbart endcomment
 -->

:::::::::::::::::::::::::::::::::::::::: keypoints

- `podman container` has subcommands used to interact and manage containers.
- `podman image` has subcommands used to interact and manage container images.
- `podman container ls` or `podman ps` can provide information on currently running containers.

::::::::::::::::::::::::::::::::::::::::::::::::::
