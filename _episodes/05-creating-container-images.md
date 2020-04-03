---
title: "Creating your own container images"
teaching: 30
exercises: 0
questions:
- "How can I make my own Docker images?"
objectives:
- "Explain the purpose of a `Dockerfile` and show some simple examples."
- "Demonstrate how to build a Docker image from a `Dockerfile`."
- "Demonstrate how to upload ('push') your container images to the Docker Hub."
- "Explain how you can include files within Docker images when you build them."
- "Explain how you can access files on the Docker host from your Docker containers."
keypoints:
- "`Dockerfiles` specify what is within Docker images."
- "The `docker build` command is used to build an image from a `Dockerfile`"
- "You can share your Docker images through the Docker Hub so that others can create Docker containers from your images."
- You can include files from your Docker host into your Docker images by using the `COPY` instruction in your `Dockerfile`.
- Docker allows containers to read and write files from the Docker host.
---

There are lots of reasons why you might want to create your **own** Docker image.
- You can't find a container with all the tools you need on Docker Hub.
- You want to have a container to "archive" all the specific software versions you ran for a project
- You want to share your workflow with someone else.

## Interactive Installation

Before creating a reproducible installation, let's experiment with installing
software inside a container. Start the `alpine` container from before, interactively:

~~~
$ docker run -it alpine sh
~~~
{: .bash}

Because this is a basic container, there's a lot of things not installed -- for
example, `bash`!

~~~
/# bash
~~~
{: .bash}

How to install

We can also download and install Python packages.


Once we exit - these changes are not saved to a new container unless we run
another command. Instead of doing that, we are going to create a text file
with our list of changes and build the container from that text file. This is
more reproducible and creates more portable Docker images.

## Introduction to Dockerfiles

We have seen use of others' Docker container images. Now we move on to describe how you can create your own images.

The specification for how Docker should build images that you design is contained within a file named `Dockerfile`.

In a shell window:
- `cd` to your `container-playground`;
- create a new directory named `my-container-spec` within `container-playground`;
- `cd` into your `my-container-spec` directory.

Within the new `my-container-spec` directory, use your favourite editor to create a file named `Dockerfile` that contains the following:

~~~
FROM alpine
RUN /bin/echo "Greetings from my newly minted container." > /root/my_message
CMD [ "/bin/cat", "/root/my_message" ]
~~~

## Building your Docker image

Run the following command to build your Docker image, noting that the period at the end of the line is important (it means "this directory"), and has a space before it.
~~~
$ docker build -t my-container .
~~~
{: .language-bash}
~~~
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM alpine
latest: Pulling from library/alpine
6c40cc604d8e: Pull complete
Digest: sha256:b3dbf31b77fd99d9c08f780ce6f5282aba076d70a513a8be859d8d3a4d0c92b8
Status: Downloaded newer image for alpine:latest
 ---> caf27325b298
Step 2/3 : RUN /bin/echo "Greetings from my newly minted container." > /root/my_message
 ---> Running in 87417f8733c4
Removing intermediate container 87417f8733c4
 ---> bf1b7fab7caa
Step 3/3 : CMD [ "/bin/cat", "/root/my_message" ]
 ---> Running in 6c44e5e59d9b
Removing intermediate container 6c44e5e59d9b
 ---> a6a95e96d0b8
Successfully built a6a95e96d0b8
Successfully tagged my-container:latest
~~~
{: .output}

OK, now let's test that that container does what it's supposed to!

~~~
$ docker run my-container
~~~
{: .language-bash}
~~~
Greetings from my newly minted container.
~~~
{: .output}

Now use your favourite editor to make a change to the message that's contained within the `Dockerfile`. As the plan is to share your container online, it's best to ensure that your message is suitable for public viewing, and you may want to avoid including your name, credit card numbers, etc.

Rerun the `docker build -t my-container .` and `docker run my-container` commands to ensure that your image builds and that your containers function as expected.

While it may not look like you have achieved much, you have already effected the combination of a lightweight Linux operating system with your specification to run a given command that can operate reliably on macOS, Microsoft Windows, Linux and on the cloud!

### Pushing your container images to the Docker Hub

Images that you release publicly can be stored on the Docker Hub for free.

Let's "push" to your account on the Docker Hub the image that you configured to output your chosen message, in the previous section.

Note that so far, the image name `my-container` was used locally to your computer. On the Docker Hub, the name if your container must be prefixed by your user name (otherwise there would be many clashes when different users try to share images with the same name!).

You will need to run two commands that are similar to the ones included below, **except** that you need to replace the instance of "dme26" on each line with your Docker Hub username (dme26 is my Docker Hub username!). A potential source of confusion is that you typically use your email address and not your login name to access the Docker Hub, however once authenticated your user ID is shown on the Docker Hub web pages.
~~~
$ docker tag my-container:latest dme26/my-container
$ docker push dme26/my-container
~~~
{: .language-bash}
~~~
The push refers to repository [docker.io/dme26/my-container]
503e53e365f3: Mounted from library/alpine
latest: digest: sha256:1d599b3e195e282648a30719f159422165656781de420ccb6173465ac29d2b7a size: 528
~~~
{: .output}

In a web browser, open <https://hub.docker.com>, and on your user page you should now see your container listed, for anyone to use or build on.

### Copying files into your containers at build time

Let's rework our container to run some code written in the Python programming language.

You will need two shell windows. You can continue using the shell you've used so far in this lesson, let's call that the "image building shell". Let's refer to the new shell window that you open as the "testing shell".

Open the `Dockerfile` you created above with your favourite editor, and change its contents to match the following:
~~~
FROM python:3-slim

WORKDIR /usr/src/app

COPY test.py .

CMD [ "python", "./test.py" ]
~~~

In your image building shell run the command to try to build your image (this will fail!):
~~~
$ docker build -t another-greeting .
~~~
{: .language-bash}
~~~
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM python:3-slim
3-slim: Pulling from library/python
743f2d6c1f65: Pull complete
977e13fc7449: Pull complete
de5f9e5af26b: Pull complete
0d27ddbe8383: Pull complete
228d55eb5a23: Pull complete
Digest: sha256:589527a734f2a9e48b23cc4687848cb9503d0f8569fad68c3ad8b2ee9d1c50ff
Status: Downloaded newer image for python:3-slim
 ---> ca7f9e245002
Step 2/4 : WORKDIR /usr/src/app
 ---> Running in 59d26b86423b
Removing intermediate container 59d26b86423b
 ---> c0d009871ab7
Step 3/4 : COPY test.py .
COPY failed: stat /var/lib/docker/tmp/docker-builder728731527/test.py: no such file or directory
~~~
{: .output}

Our `Dockerfile` made reference to a file on the host `test.py` that should have been in the directory that contained our `Dockerfile`. It was not present, so the building of the image failed. It is the `COPY test.py .` command in the `Dockerfile` that is trying to copy the file `test.py` into the working directory of the current image building operation.

Using your favourite editor, create the file "test.py" in the same directory as your Dockerfile, with the following contents:
~~~
print("Hello world from Python")
~~~
{: .language-python}

Now re-run the command to build your image.

~~~
$ docker build -t another-greeting .
~~~
{: .language-bash}
~~~
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM python:3-slim
 ---> ca7f9e245002
Step 2/4 : WORKDIR /usr/src/app
 ---> Using cache
 ---> c0d009871ab7
Step 3/4 : COPY test.py .
 ---> 23b27e9f57a9
Step 4/4 : CMD [ "python", "./test.py" ]
 ---> Running in 0d48c16b40c1
Removing intermediate container 0d48c16b40c1
 ---> bede6575d987
Successfully built bede6575d987
Successfully tagged another-greeting:latest
~~~
{: .output}

In your testing shell, within your `container-playground` directory, create a directory `test` and `cd` into it.

Test your container using the following command, which should produce the output shown below.
~~~
$ docker run another-greeting
~~~
{: .language-bash}
~~~
Hello world from Python
~~~
{: .output}

### Sharing files with your containers at run time

Having shown how to include files of your choice into your image as it was built, we now move to another important form of sharing: allowing your container instances to read and write files on the host computer.

Being able to share files between the host and the container allows you to build images that process input data sitting in files on the host, and write results back to files on the host.

Let's create an image for a container that uses Python to read in a CSV file from the Docker host, and write results back as a file on the Docker host. (As usual, the container itself, will be cleaned away when it finishes.)

In the same directory as your Dockerfile, use your favourite editor to create a file named `csv-to-scatter-plot.py` containing the following Python code:
~~~
# Libraries to include
import matplotlib.pyplot as the_plot
import numpy as np

# Read a CSV file "data.csv" shared to the Docker container from the Docker host.
# The header line is skipped, and typically contains a description of the columns:
# [ x-coordinate, y-coordinate, colour, size ]
# Each row of the CSV file (other than the header) defines one point to plot.
the_data = np.genfromtxt('/data/data.csv',delimiter=',',skip_header=1)
transposed_data = the_data.transpose()

points_x = transposed_data[0]
points_y = transposed_data[1]
points_colour = transposed_data[2]
points_size = transposed_data[3]

# This code is not at all robust, but skipping error handling makes it more brief.

# Define the scatter plot
the_plot.style.use('seaborn-whitegrid')
f = the_plot.figure()
the_plot.scatter(points_x, points_y, c=points_colour, s=points_size, alpha=0.4, cmap='viridis')
the_plot.colorbar()

# Save the scatter plot to two output files (on the Docker host).
f.savefig("/data/output.pdf", bbox_inches='tight')
f.savefig("/data/output.png", bbox_inches='tight')
~~~
{: .language-python}

Your Dockerfile will need to be changed to refer to this new script, as follows:
~~~
FROM python:3-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir numpy matplotlib

COPY csv-to-scatter-plot.py .

CMD [ "python", "./csv-to-scatter-plot.py" ]
~~~

Now build an image named "csv-to-scatter-plot" using the following command, which is followed by the output that that command produces for me.

~~~
$ docker build -t csv-to-scatter-plot .
~~~
{: .language-bash}
~~~
Sending build context to Docker daemon   5.12kB
Step 1/5 : FROM python:3-slim
 ---> ca7f9e245002
Step 2/5 : WORKDIR /usr/src/app
 ---> Using cache
 ---> c0d009871ab7
Step 3/5 : RUN pip install --no-cache-dir numpy matplotlib
 ---> Running in a6c85255c679
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/bb/76/24e9f32c78e6f6fb26cf2596b428f393bf015b63459468119f282f70a7fd/numpy-1.16.3-cp37-cp37m-manylinux1_x86_64.whl (17.3MB)
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/dc/cb/a34046e75c9a4ecaf426ae0d0eada97078c8ce4bbe3250940b1a312a1385/matplotlib-3.1.0-cp37-cp37m-manylinux1_x86_64.whl (13.1MB)
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/93/f8/518fb0bb89860eea6ff1b96483fbd9236d5ee991485d0f3eceff1770f654/kiwisolver-1.1.0-cp37-cp37m-manylinux1_x86_64.whl (90kB)
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/dd/d9/3ec19e966301a6e25769976999bd7bbe552016f0d32b577dc9d63d2e0c49/pyparsing-2.4.0-py2.py3-none-any.whl (62kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from matplotlib)
  Downloading https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl (226kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (41.0.1)
Collecting six (from cycler>=0.10->matplotlib)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Installing collected packages: numpy, kiwisolver, pyparsing, six, cycler, python-dateutil, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.1.0 matplotlib-3.1.0 numpy-1.16.3 pyparsing-2.4.0 python-dateutil-2.8.0 six-1.12.0
Removing intermediate container a6c85255c679
 ---> 57816a2108b7
Step 4/5 : COPY csv-to-scatter-plot.py .
 ---> 96bef9863250
Step 5/5 : CMD [ "python", "./csv-to-scatter-plot.py" ]
 ---> Running in 2fb116f99da3
Removing intermediate container 2fb116f99da3
 ---> c2eba3ad398a
Successfully built c2eba3ad398a
Successfully tagged csv-to-scatter-plot:latest
~~~
{: .output}

Now in your *testing shell*, use your favourite editor to create a file named `data.csv` that contains, for example:
~~~
x-coordinate,y-coordinate,colour,size
1.76405235,1.8831507,0.96193638,392.67567700
0.40015721,-1.34775906,0.29214753,956.40572300
0.97873798,-1.270485,0.2408288,187.13089200
2.2408932,0.96939671,0.10029394,903.98395500
1.86755799,-1.17312341,0.01642963,543.8059500
-0.9772779,1.94362119,0.92952932,456.91142200
0.95008842,-0.41361898,0.66991655,882.0414100
-0.15135721,-0.74745481,0.78515291,458.60396200
-0.10321885,1.92294203,0.28173011,724.16763700
0.41059850,1.48051479,0.58641017,399.02532200
0.14404357,1.86755896,0.06395527,904.04439300
1.45427351,0.90604466,0.48562760,690.0250200
0.76103773,-0.86122569,0.9774951,699.62205400
0.12167502,1.91006495,0.87650525,327.72040200
0.44386323,-0.26800337,0.33815895,756.77864300
0.33367433,0.80245640,0.96157016,636.06105500
1.49407907,0.94725197,0.23170163,240.02027300
-0.20515826,-0.15501009,0.94931882,160.53882200
0.31306770,0.6140794,0.94137771,796.39147500
-0.85409574,0.92220667,0.79920259,959.16660300
-2.55298982,0.37642553,0.63044794,458.13882700
~~~

The `-v` switch to the `docker run` command allows us to specify a mapping between a directory on the host, followed by a colon, then the place that directory should be mapped to within any container that is created. Note that the default if for the container to both be able to read from and write to the mapped directory on the host. (This is a potential security risk: you should only run containers from images for which you trust the provenance.)

In your testing shell, create an instance of your "csv-to-scatter-plot" container.

For macOS, Linux or PowerShell:
~~~
$ docker run -v ${PWD}:/data csv-to-scatter-plot
~~~
{: .language-bash}

For `cmd.exe` shells on Microsoft Windows:
~~~
> docker run -v "%CD%":/data csv-to-scatter-plot
~~~

If all goes well, you should now see, within the working directory of your testing shell, a PNG and a PDF file that plot the data from `data.csv`.

Change your `data.csv` file, and rerun the appropriate preceding `docker run` invocation.

You should see the PDF and PNG file update appropriately.

You have now successfully implemented an image that creates containers that transform input data through a stable, reproducible computational environment into output, in the form of plot images.

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
