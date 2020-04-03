---
title: "Creating your own container images"
teaching: 20
exercises: 15
questions:
- "How can I make my own Docker images?"
objectives:
- "Explain the purpose of a `Dockerfile` and show some simple examples."
- "Demonstrate how to build a Docker image from a `Dockerfile`."
- "Demonstrate how to upload ('push') your container images to the Docker Hub."
keypoints:
- "`Dockerfiles` specify what is within Docker images."
- "The `docker build` command is used to build an image from a `Dockerfile`"
- "You can share your Docker images through the Docker Hub so that others can create Docker containers from your images."
---

There are lots of reasons why you might want to create your **own** Docker image.
- You can't find a container with all the tools you need on Docker Hub.
- You want to have a container to "archive" all the specific software versions you ran for a project
- You want to share your workflow with someone else.

## Interactive installation

Before creating a reproducible installation, let's experiment with installing
software inside a container. Start the `alpine` container from before, interactively:

~~~
$ docker run -it alpine sh
~~~
{: .language-bash}

Because this is a basic container, there's a lot of things not installed -- for
example, `python`!

~~~
/# python
~~~
{: .language-bash}
~~~
sh: python: not found
~~~
{: .output}

Inside the container, we can run commands to install Python. The "alpine" version of
Linux has a installation tool called `apk` that we can use to install Python.

~~~
apk add --update python py-pip python-dev
~~~
{: .language-bash}

We can test our installation by running a Python command:
~~~
python --version
~~~
{: .language-bash}

Once Python is installed, we can add Python packages using the pip package installer:
~~~
pip install cython
~~~
{: .language-bash}

> ## Searching for Help
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

Once we exit - these changes are not saved to a new container by default. In order
to build a new container, we are going to create a text file
with our list of installation instructions and build the container from that text file. This is
more reproducible and creates more portable Docker images.

## Put installation instructions in a `Dockerfile`

In a shell window:
- `cd` to your `container-playground`;
- create a new directory named `my-container-spec` within `container-playground`;
- `cd` into your `my-container-spec` directory.

Within the new `my-container-spec` directory, use your favourite editor to create a file named `Dockerfile` that contains the following:

~~~
FROM alpine
RUN apk add --update python py-pip python-dev
RUN pip install cython
CMD cat /proc/version && python --version
~~~

Let's break this file down:
- The first line, `FROM`, indicates which container we're starting with.
- The next two lines `RUN`, indicate installation commands we want to run. These
are the same commands that we used interactively above.
- The last line, `CMD` indicates the default command we want the container to run,
if no other command is provided.

## Create a new Docker image

So far, we've just created a file. We want Docker to take this file,
run the install commands inside, and then save the
resulting container as a new container image. To do this we will use the
`docker build` command. We have to provide `docker build` with two pieces of information:
- the location of the `Dockerfile`
- the name of the new image. Remember the naming scheme from before? You should name
your new image with your Docker Hub username and a name for the container, like this:
    ```
    USERNAME/CONTAINERNAME
    ```
All together, the build command will look like this:

~~~
$ docker build -t USERNAME/CONTAINERNAME .
~~~
{: .language-bash}

The `-t` option names the container; the final dot indicates that the `Dockerfile` is in
our current directory.

If my user name was `alice` and I wanted to call my image `alpine-python`, I would use
this command:
~~~
$ docker build -t alice/alpine-python .
~~~
{: .language-bash}

> ## Review!
>
> 1. Think back to earlier. What command can you run to check if your image was created
> successfully? (Hint: what command  shows the images on your computer?)
>
> 2. We didn't specific a tag for our image name. What did Docker automatically use?
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
> > ~~~
> > $ docker run alice/alpine-python
> > ~~~
> > {: .language-bash}
> > should run the container and print out our default message, including the version
> > of Linux and Python.
> > ~~~
> > $ docker run alice/alpine-python echo "Hello World"
> > ~~~
> > {: .language-bash}
> > will run the container and print out "Hello world" instead.
> {: .solution}
{: .challenge}

While it may not look like you have achieved much, you have already effected the combination of a lightweight Linux operating system with your specification to run a given command that can operate reliably on macOS, Microsoft Windows, Linux and on the cloud!

## Share your new container on Docker Hub

Images that you release publicly can be stored on the Docker Hub for free.  If you
name your image as described above, with your Docker Hub username, all you need to do
is run the opposite of `docker pull` -- `docker push`

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

> ## What's in a name? (again)
>
> You don't *have* to name your containers using the `USERNAME/CONTAINER:TAG` naming
> scheme. On your own computer, you can call containers whatever you want and refer to
> them by the names you choose. It's only when you want to share a container that it
> needs the correct naming format.
>
> You can rename images using the `docker tag` command. For example, imagine someone
> named Alice has been working on a workflow container and called it `workflow-test`
> on her own computer. She now wants to share it in her `alice` Docker Hub account
> with the name `workflow-complete` and a tag of `v1`. Her `docker tag` command
> would look like this:
> ~~~
> $ docker tag workflow-test alice/workflow-complete:v1
> ~~~
> {: .language-bash}
>
> She could then push the re-named container to Docker Hub,
> using `docker push alice/workflow-complete:v1`
>
{: .callout}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints Dockerfiles Dockerfile docker.io WORKDIR
 -->
<!--  LocalWords:  test.py 43288b101abf fc145d33ea49 csv numpy cmap
 -->
<!--  LocalWords:  csv-to-scatter-plot.py matplotlib.pyplot viridis
 -->
<!--  LocalWords:  np.genfromtxt seaborn-whitegrid the_plot.colorbar
 -->
<!--  LocalWords:  f.savefig matplotlib links.md endcomment
 -->
<!--  LocalWords:  5377596cb1c035c102396f5934237a046f80da69974026f90bee5db8b7ba
 -->
{% endcomment %}
<!--  LocalWords:  PowerShell
 -->
