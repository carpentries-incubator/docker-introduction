---
title: "Exploring and Running Containers"
teaching: 10
exercises: 0
questions:
- "How do I interact with a Docker container on my computer?"
objectives:
- "Demonstrate how to create an instance of a container from an image."
- "Explain how to list (container) images on your laptop."
- "Explain how to list running and completed containers."
keypoints:
- "Containers are usually created using command line invocations."
- "The `docker run` command creates containers from images."
- "The `docker image` command lists images that are (now) on your computer."
- "The `docker container` command lists containers that have been created."
---


If you need to reclaim space, you will need to remove image files.
On macOS and Windows, when you uninstall the overall Docker software, it should have the effect of removing all of your image files, although I have not explicitly tested this.

### Removing images
If you want to explicitly remove a container image, you will need to find out details such as the "image ID". For example say my laptop contained the following image.
~~~
$ docker image ls
~~~
{: .language-bash}
~~~
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
ubuntu                 trusty              dc4491992653        12 months ago       222MB
~~~
{: .output}

I can remove the image with a `docker image rm` command that includes the image ID, such as:
~~~
$ docker image rm dc4491992653
~~~
{: .language-bash}
~~~
Untagged: ubuntu:trusty
Untagged: ubuntu@sha256:e1c8bff470c771c6e86d3166607e2c74e6986b05bf339784a9cab70e0e03c7c3
Deleted: sha256:dc4491992653ecf02ae2d0e9d3dbdaab63af8ccdcab87ee0ee7e532f7087dd73
Deleted: sha256:1239c33230909cc231da97b851df65e252dc9811dcee2af0ecf3b225e2805a31
Deleted: sha256:ce4caf69568d9109febd1f5307b62d85ab84e7a947fded041be49c847b412e5a
Deleted: sha256:4c711cc0452303f0fb6ce885c84130e32bb649b03f690fd0e4626a874b1cc8cf
Deleted: sha256:a375921af0e34b1cb09a35af24265db01b1eb65edabadaf70d56505a60a6de2b
Deleted: sha256:c41b9462ea4bbc2f578e42bd915214d54948d960b9b8c6815daf8586811c2d38
~~~
{: .output}

The reason that there is so much output, is that a given image may be created by merging multiple underlying layers. Any layers that are used by multiple Docker images will only be stored once.

### What containers are running?
The command to list the containers that are currently running is
~~~
docker container ls
~~~
{: .language-bash}

... although the output should be blank, since the instances of hello-world containers will have been wiped away as soon as they completed. However the container image remains on your computer so that it is quick for you to create future such instances of hello-world containers.

### What containers have run recently?
There is also a way to list running containers, and those that have completed recently, which is to add the `--all` flag to the `docker container ls` command as shown below.
~~~
$ docker container ls --all
~~~
{: .language-bash}
~~~
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
9c698655416a        hello-world         "/hello"            2 minutes ago       Exited (0) 2 minutes ago                       zen_dubinsky
6dd822cf6ca9        hello-world         "/hello"            3 minutes ago       Exited (0) 3 minutes ago                       eager_engelbart
~~~
{: .output}

### Removing images

If you need to reclaim disk space, you can remove image files.
The images and their corresponding containers can start to take up a lot of disk space if you don't clean them up occasionally.
On macOS and Windows, when you uninstall the overall Docker software, it should have the effect of removing all of your image files, although we have not explicitly tested this.

If you want to explicitly remove a container image, you will need to find out details such as the "image ID" or name of the repository. For example say my laptop contained the following image.
~~~
$ docker image ls
~~~
{: .language-bash}
~~~
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
ubuntu                 trusty              dc4491992653        12 months ago       222MB
hello-world            latest              fce289e99eb9        4 months ago        1.84kB
~~~
{: .output}

We can try to remove remove the `hello-world` image with a `docker image rm` command that includes the repository name, like so but...:
~~~
$ docker image rm hello-world
~~~
{: .language-bash}
~~~
Error response from daemon: conflict: unable to remove repository reference "hello-world" (must force) - container e7d3b76b00f4 is using its referenced image fce289e99eb9
~~~
{: .output}
We get this error because there are containers created that depend on this image.

### What containers are running?
As indicated by the error above there is still an existing container from this image.
We can list the running containers by typing.
~~~
$ docker container ls
~~~
{: .language-bash}
~~~
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
~~~
{: .output}

The first version of the command is orthogonal to what we know from the Unix shell but we might want to use the shorter version. For reference, "ps" stands for “Process Status”.
We should also notice that this command didn't return any containers because our containers all exited and thus stopped running after they completed their work.


### What containers have run recently?
There is also a way to list running containers, and those that have completed recently, which is to add the `--all`/`-a` flag to the `docker container ls`/`docker ps` command as shown below.
~~~
$ docker container ls --all
~~~
{: .language-bash}
~~~
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
9c698655416a        hello-world         "/hello"            2 minutes ago       Exited (0) 2 minutes ago                       zen_dubinsky
6dd822cf6ca9        hello-world         "/hello"            3 minutes ago       Exited (0) 3 minutes ago                       eager_engelbart
~~~
{: .output}

We will talk more about how you might use these exited containers and how to restart a container later in this lesson.


### How do I remove an exited container?
To delete an exited container you can run the following command, inserting the `CONTAINER ID` for the container you wish to remove.
It will repeat the `CONTAINER ID` back to you, if successful.
~~~
$ docker container rm 9c698655416a
~~~
{: .language-bash}
~~~
9c698655416a
~~~
{: .output}

If you want to remove all exited containers at once you can use the `docker containers prune` command.
**Be careful** with this command.
If you have containers you may want to reconnect to, you should not use this command.
It will ask you if to confirm you want to remove these containers, see output below.
If successfull it will print the full `CONTAINER ID` back to you.
~~~
$ docker container prune
~~~
{: .language-bash}
~~~
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
9c698655416a848278d16bb1352b97e72b7ea85884bff8f106877afe0210acfc
6dd822cf6ca92f3040eaecbd26ad2af63595f30bb7e7a20eacf4554f6ccc9b2b
~~~
{: .output}

### Removing images, for real this time

~~~
$ docker image rm hello-world
~~~
{: .language-bash}
~~~
Untagged: hello-world:latest
Untagged: hello-world@sha256:5f179596a7335398b805f036f7e8561b6f0e32cd30a32f5e19d17a3cda6cc33d
Deleted: sha256:fce289e99eb9bca977dae136fbe2a82b6b7d4c372474c9235adc1741675f587e
Deleted: sha256:af0b15c8625bb1938f1d7b17081031f649fd14e6b233688eea3c5483994a66a3
~~~
{: .output}

The reason that there are a few lines of output, is that a given image may have been formed by merging multiple underlying layers.
Any layers that are used by multiple Docker images will only be stored once.
Now the result of `docker images` should no longer include the `hello-world` image.

> ## The Docker official documentation is helpful!
> There is lots of great documentation at <https://docs.docker.com/>, for example, detailed reference material and tutorials covering the use of the commands mentioned above.
{: .callout}

### Conclusion

You have now successfully acquired a Docker image file to your computer,
and have created a Docker container from it.
While this already effects a reproducible computational environment,
the image contents are not under your control, so we look at this topic,
after a quick discussion about the Docker Hub.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints amd64 fce289e99eb9 zen_dubinsky links.md
 -->
<!--  LocalWords:  eager_engelbart endcomment
 -->
{% endcomment %}
