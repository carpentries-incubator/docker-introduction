---
title: "Creating More Complex Container Images"
teaching: 30
exercises: 30
questions:
- "How can I make more complex container images? "
objectives:
- "Explain how you can include files within Docker images when you build them."
- "Explain how you can access files on the Docker host from your Docker containers."
keypoints:
- You can include files from your Docker host into your Docker images by using the `COPY` instruction in your `Dockerfile`.
- Docker allows containers to read and write files from the Docker host.
---

In order to create and use your own containers, you may need more information than
our previous example. You may want to use files from outside the container, copy
those files into the container, and just generally learn a little bit about software
installation. This episode will cover these. Note that the examples will get gradually
more and more complex - most day-to-day use of containers can be accomplished
using the first 1-2 sections on this page.

## Using scripts and files from outside the container

In your shell, change to the `sum` folder in the `docker-intro` folder and look at
the files inside.
~~~
$ cd ~/Desktop/docker-intro/sum
$ ls
~~~
{: .language-bash}

This folder has both a `Dockerfile` and a python script called `sum.py`. Let's say
we wanted to try running the script using our recently created `alpine-python`
container.

> ## Running containers
>
> What command would we use to run python from the `alpine-python` container?
{: .challenge}

If we try running the container and Python script, what happens?
~~~
$ docker run alice/alpine-python python sum.py
~~~
{: .language-bash}
~~~
python: can't open file 'sum.py': [Errno 2] No such file or directory
~~~
{: .output}

> ## No such file or directory
>
> What does the error message mean? Why might the Python inside the container
> not be able to find or open our script?
>
{: challenge}

The problem here is that the container and its file system is separate from our
host computer's file system. When the container runs, it can't see anything outside
itself, including any of the files on our computer. In order to use Python
(inside the container) and our script (outside the container, on our computer),
we need to create a link between the directory on our computer and the container.

This link is called a "mount" and is what happens automatically when a USB drive
or other external hard drive gets connected to a computer - you can see the
contents appear as if they were on your computer.

We can create a mount between our computer and the running container by using an additional
option to `docker run`. We'll also use the variable `$PWD` which will substitute
in our current working directory. The option will look like this

`-v $PWD:/temp`

What this means is -- link my current directory with the container, and inside the
container, name the directory `/temp`

Let's try running the command now:
~~~
$ docker run -v $PWD:/temp alice/alpine-python python sum.py
~~~
{: .language-bash}

But we get the same error!
~~~
python: can't open file 'sum.py': [Errno 2] No such file or directory
~~~
{: .output}

This final piece is a bit tricky -- we really have to remember to put ourselves
inside the container. Where is the `sum.py` file? It's in the directory that's been
mapped to `/temp` -- so we need to include that in the path to the script. This
command should give us what we need:

~~~
$ docker run -v $PWD:/temp alice/alpine-python python /temp/sum.py
~~~
{: .language-bash}

Note that if we create any files in the `/temp` directory while the container is
running, these files will appear on our host filesystem in the original directory
and will stay there even when the container stops.

> ## Exercise: Explore the script
>
> What happens if you use the `docker run` command above
> and put numbers after the script name?
>
> > ## Solution
> >
> > This script comes from [the Python Wiki](https://wiki.python.org/moin/SimplePrograms) > > and is set to add all numbers
> > that are passed to it as arguments.
> {: .solution}
{: .challenge}

> ## Exercise: Checking the options
>
> Our Docker command has gotten much longer! Can you go through each piece of
> the Docker command above the explain what it does? How would you characterize
> the key components of a Docker command?
>
> > ## Solution
> >
> > Here's a breakdown of each piece of the command above
> >
> > - `docker run`: use Docker to run a container
> > - `-v $PWD:/temp`: connect my current working directory (`$PWD`) as a folder
> > inside the container called `/temp`
> > - `alice/alpine-python`: name of the container to run
> > - `python /temp/sum.py`: what commands to run in the container
> >
> > More generally, every Docker command will have the form:
> > `docker [action] [docker options] [docker image] [command to run inside]
> >
> {: .solution}
{: .challenge}

> ## Exercise: Interactive jobs
>
> Try using the directory mount option but run the container interactively.
> Can you find the folder that's connected to your computer? What's inside?
>
> > ## Solution
> >
> > The docker command to run the container interactively is:
> > ~~~
> > $ docker run -v $PWD:/temp -it alice/alpine-python sh
> > ~~~
> > {: .language-bash}
> >
> > Once inside, you should be able to navigate to the `/temp` folder
> > and see that's contents are the same as the files on your computer:
> > ~~~
> > /# cd /temp
> > /# ls
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

Mounting a folder can be very useful when you want to run the software inside your container on many different input files.
In other situations, you may want to save or archive an authoritative version of your data by adding it to the container permanently.  That's what we will cover next.

## Including personal scripts and data in a container

Our next project will be to add our own files to a container - something you
might want to do if you're sharing a finished analysis or just want to have
an archived copy of your entire analysis including the data. Let's assume that we've finished with our `sum.py`
script and want to add it to the container itself.

In your shell, you should still be in the `sum` folder in the `docker-intro` folder.
~~~
$ pwd
~~~
{: .language-bash}
~~~
$ /Users/yourname/Desktop/docker-intro/sum
~~~
{: .language-bash}

Take a look at the Dockerfile. It looks similar to the one we used before, but
it has an additional line with the `COPY` keyword.

~~~
COPY sum.py /home
~~~

This line will cause Docker to copy the file from your computer into the container's
file system. Let's build the container like before, but give it a different name:

~~~
$ docker build -t alice/alpine-sum .
~~~
{: .language-bash}

> ## Exercise: Did it work?
>
> Can you remember how to run a container interactively? Try that with this one.
> Once inside, try running the Python script.
>
> > ## Solution
> >
> > You can start the container interactively like so:
> > ~~~
> > $ docker run -it alice/alpine-sum sh
> > ~~~
> > {: .language-bash}
> >
> > You should be able to run the python command inside the container like this:
> > ~~~
> > /# python /home/sum.py
> > ~~~
> > {: .language-bash}
> >
> {: .solution}
{: .challenge}

This `COPY` keyword can be used to place your own scripts or own data into a container
that you want to publish or use as a record. Note that it's not necessarily a good idea
to put your scripts inside the container if you're constantly changing or editing them.
Then, referencing the scripts from outside the container is a good idea, as we
did in the previous section. You also want to think carefully about size -- if you
run `docker image ls` you'll see the size of each image all the way on the right of
the screen. The bigger your image becomes, the harder it will be to easily download.

> ## Copying alternatives
>
> Another trick for getting your own files into a container is by using the `RUN`
> keyword and downloading the files from the internet. For example, if your code
> is in a GitHub repository, you could include this statement in your Dockerfile
> to download the latest version every time you build the container:
>
> ~~~
> RUN git clone https://github.com/alice/mycode
> ~~~
>
> Similarly, the `wget` command can be used to download any file publicly available
> on the internet:
>
> ~~~
> RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.0/ncbi-blast-2.10.0+-x64-linux.tar.gz
> ~~~
>
{: callout}

## More fancy `Dockerfile` options (optional, for presentation or as exercises)

We can expand on the example above to make our container even more "automatic".
Here are some ideas:

- Make the `sum.py` script run automatically:

~~~
FROM alpine

COPY sum.py /home
RUN apk add --update python py-pip python-dev

# Run the sum.py script as the default command
CMD python /home/sum.py
# OR
# CMD ["python", "/home/sum.py"]
~~~

Build and test it:
~~~
$ docker build -t alpine-sum:v1 .
$ docker run alpine-sum:v1
~~~
{: .language-bash}

- Make the `sum.py` script run automatically with arguments from the command line:

~~~
FROM alpine

COPY sum.py /home
RUN apk add --update python py-pip python-dev

# Run the sum.py script as the default command and
# allow people to enter arguments for it
ENTRYPOINT ["python", "/home/sum.py"]
~~~

Build and test it:
~~~
$ docker build -t alpine-sum:v2 .
$ docker run alpine-sum:v2 1 2 3 4
~~~
{: .language-bash}

- Add the `sum.py` script to the `PATH` so you can run it directly:

~~~
FROM alpine

COPY sum.py /home
# set script permissions
RUN chmod +x /home/sum.py
# add /home folder to the PATH
ENV PATH /home:$PATH

RUN apk add --update python py-pip python-dev
~~~

Build and test it:
~~~
$ docker build -t alpine-sum:v3 .
$ docker run alpine-sum:v3 sum.py 1 2 3 4
~~~
{: .language-bash}

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
