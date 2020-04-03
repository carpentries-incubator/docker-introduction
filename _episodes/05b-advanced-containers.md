---
title: "Creating More Complex Container Images"
teaching: 20
exercises: 20
questions:
- "How can I make more complex container images? "
objectives:
- "TODO: learning objectives about software installation"
- "Explain how you can include files within Docker images when you build them."
- "Explain how you can access files on the Docker host from your Docker containers."
keypoints:
- You can include files from your Docker host into your Docker images by using the `COPY` instruction in your `Dockerfile`.
- Docker allows containers to read and write files from the Docker host.
---


## Boring but important notes about installation

There are a lot of choices when it comes to installing software - sometimes too many!
Here are some things to consider when creating your own container:

- **Start Smart**, or, don't install everything from scratch! If you're using Python
as your main tool, start with a [Python container](https://hub.docker.com/_/python). Same with [R](https://hub.docker.com/r/rocker/r-ver/). We've used Alpine Linux as an example
in this lesson, but it's generally not a good container to start with because it is
a less common version of Linux; using [Ubunutu](), [Debian]() and [CentOS]() are all
good options for scientific software installations. The program you're using might
recommend a particular version of Linux; if this happens, find a container with that
version of Linux at the base.
- **Know (or Google) your Linux**. Each version of Linux has a special set of tools specifically for installing software. The `apk` command we used above is the installer for Alpine Linux. The installers for various common Linux versions are listed below:
    - Ubuntu: `apt` or `apt-get`
    - Debian: `deb`
    - CentOS: `yum`
  Most common software installations are available to be installed via these tools.
  Searching for "install X on Y Linux" is always a good start for common software
  installations; if something isn't available via the Linux distributions installation
  tools, try the options below.
- **Use what you know**. You've probably used commands like `pip` or `install.packages()`
before -- these will also work to install things in containers (if the basic scripting
language is installed).
- **README**. Many scientific software tools have a README or installation instructions
that lay out how to install software. You want to look for instructions for Linux. If
the install instructions include options like those suggested above, try those first.


In general
- Interactive first
- Group commands together

> ## TODO
>
> Have a set of "choose your own adventure" software installation examples
{: callout}

## Additional `Dockerfile` options and tips

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
