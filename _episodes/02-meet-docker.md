---
title: "Introducing the Docker command line"
teaching: 10
exercises: 0
questions:
- "How do I interact with Docker?"
objectives:
- "Explain how to check that Docker is installed and is ready to use."
- "Demonstrate some initial Docker command line interactions."
keypoints:
- "A toolbar icon indicates that Docker is ready to use containers."
- "You will typically interact with Docker using the command line."
---
### Docker command line

Start the Docker application that you installed in working through the setup instructions for this session. Note that this might not be necessary if your laptop is running Linux. 

The Docker application will usually provide a way for you to log in using the application's menu (macOS) or systray icon (Windows). This will require you to use your Docker Hub username and your password.

> ## Determining your Docker Hub username
> If you no longer recall your Docker Hub username, e.g., because you have been logging into the Docker Hub using your email address, you can find out what it is through the steps:
> - Open <http://hub.docker.com/> in a web browser window
> - Sign-in using your email and password (don't tell us what it is)
> - In the top-right of the screen you will see your username. Mine's `dme26`.
{: .callout}

Now open a shell window, and run the following command in your shell to check that Docker is installed. I have appended the output that I see on my Mac, but the specific version is unlikely to matter much: it certainly does not have to precisely match mine.
~~~
$ docker --version
~~~
{: .language-bash}
~~~
Docker version 18.09.1, build 4c52b90
~~~
{: .output}

Ensure that your command line `docker` commands are able to reach the Docker Hub by running the following command:
~~~
$ docker login
~~~
{: .language-bash}
~~~
Authenticating with existing credentials...
Login Succeeded
~~~
{: .output}
(I wasn't prompted for authentication details, if you are, then you need to use your Docker Hub username and password.)

The `Login Succeeded` message means that your `docker` command line tool is ready to access the Docker Hub. We will return to discussion of the Docker Hub soon...

> ## A note about security
>
> On most systems `docker login` stores your credentials in plain-text in a text file in your computer.
> If you use a shared computer or you'd rather not store your credentials in plain-text, you might want to consider using a [docker credential helper](https://github.com/docker/docker-credential-helpersworry).
> These will connect docker with password or keychain managers that will allow you to store your credentials securely.
{: .callout}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment systray
 -->
{% endcomment %}
