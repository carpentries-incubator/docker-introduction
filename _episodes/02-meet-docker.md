---
title: "Introducing the Docker command line"
teaching: 10
exercises: 5
questions:
- "How do I interact with Docker?"
objectives:
- "Explain how to check that Docker is installed and is ready to use."
- "Demonstrate some initial Docker command line interactions."
keypoints:
- "A toolbar icon indicates that Docker is ready to use."
- "You will typically interact with Docker using the command line."
---
### Docker command line

Start the Docker application that you installed in working through the setup instructions for this session. Note that this might not be necessary if your laptop is running Linux or if the installation added the Docker application to your startup process. 

> ## You may need to login to Dockerhub
> The Docker application will usually provide a way for you to log in to the Dockerhub using the application's menu (macOS) or systray
> icon (Windows) and it is usually convenient to do this when the application starts. This will require you to use your Docker Hub
> username and your password. We will not actually require access to Dockerhub until later in the course but if you can login now,
> you should do so.
{: .callout}

> ## Determining your Docker Hub username
> If you no longer recall your Docker Hub username, e.g., because you have been logging into the Docker Hub using your email address,
> you can find out what it is through the steps:
> - Open <http://hub.docker.com/> in a web browser window
> - Sign-in using your email and password (don't tell us what it is)
> - In the top-right of the screen you will see your username
{: .callout}

Once your Docker application is running, open a shell (terminal) window, and run the following command to check that Docker is
installed and the command line tools are working correctly. I have appended the output that I see on my Mac, but the specific
version is unlikely to matter much: it certainly does not have to precisely match mine.
~~~
$ docker --version
~~~
{: .language-bash}
~~~
Docker version 19.03.5, build 633a0ea
~~~
{: .output}

The above command has not actually relied on the part of Docker that runs lightweight virtual machines being operational. Somewhat stretching a physical analogy, you can think of the above Docker command having been instructions to the cranes on a hypothetical shipping dock, but we haven't actually checked if the container ship we want to interact with is present yet. A command that checks that the virtual machine host is running is the Docker container list command (we cover this command in more detail later in the course).

Without explaining the details, output on a newly installed system would likely be:
~~~
$ docker container ls
~~~
{: .language-bash}
~~~
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
~~~
{: .output}
(The command `docker info` will achieve a similar end. but produces potentially daunting volumes of output.)

However, if you instead get a message similar to the following
~~~
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
~~~
{: .output}

then you need to check that you have started the Docker Desktop, Docker Engine, or however else you worked through the setup instructions.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment systray
 -->
{% endcomment %}
