---
title: Setup
---
### Website accounts to create
Please seek help at the start of the lesson if you have not been able to establish a website account on:
- The [Docker Hub](http://hub.docker.com). We will use the Docker Hub to download pre-built container images, and for you to upload and download container images that you create, as explained in the relevant lesson episodes.

### Files to download

Download the [`docker-intro.zip`]({{ page.root }}/files/docker-intro.zip) file. _This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository][docker-introduction repository]_.

Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `docker-intro`. 

### Software to install
Docker's installation experience has steadily improved, however situations will arise in which installing Docker on your computer may not be straightforward unless you have a large amount of technical experience.
Workshops try to have helpers on hand that have worked their way through the install process, but do be prepared for some troubleshooting.

In most cases, you will need to have administrator rights on the computer in order to install the Docker software. If you are using a computer managed by your organisation and do not have administrator rights, you *may* be able to get your organisation's IT staff to install Docker for you. Alternatively your IT support staff *may* be able to give you remote access to a server that can run Docker commands.

Please try to install the appropriate software from the list below depending on the operating system that your computer is running. Do let the workshop organisers know as early as possible if you are unable to install Docker using these instructions, as there may be other options available.

#### Microsoft Windows

**You must have admin rights to run Docker!** Some parts of the lesson will work without running as admin but if you are unable to `Run as administrator` on your machine some elements of this workshop might not work as described.

Ideally, you will be able to install the Docker Desktop software, following the [Docker website's documentation](https://docs.docker.com/docker-for-windows/install/). Note that the instructions for installing Docker Desktop on Windows 10 Home Edition are different from other versions of Windows 10.

Note that the above installation instructions highlight a minimum version or "build" that is required to be able to install Docker on your Windows 10 system. See [Which version of Windows operating system am I running?](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808) for details of how to find out which version/build of Windows 10 you have.

If you are unable to follow the above instructions to install Docker Desktop on your Windows system, the final release of the deprecated Docker Toolbox version of Docker for Windows can be downloaded from the [releases page of the Docker Toolbox GitHub repository](https://github.com/docker/toolbox/releases). (Download the `.exe` file for the Windows installer). _Please note that this final release of Docker Toolbox includes an old version of Docker and you are strongly advised not to attempt to use this for any production use. It will, however, enable you to follow along with the lesson material._

#### Apple macOS

Ideally, you will be able to install the Docker Desktop software, following the
[Docker website's documentation](https://docs.docker.com/docker-for-mac/install/).
The current version of the Docker Desktop software requires macOS version 10.14 (Mojave) or later.

If you already use Homebrew or MacPorts to manage your software, and would prefer to use those
tools rather than Docker's installer, you can do so. For Homebrew, you can run the command
`brew install --cask docker`. Note that you still need to run the Docker graphical user interface
once to complete the initial setup, after which time the command line functionality of Docker will
become available. The homebrew install of Docker also requires a minimum macOS version of 10.14.
The MacPorts Docker port should support older, as well as the most recent, operating system
versions (see the [port details](https://ports.macports.org/port/docker/details/)), but note that
we have not recently tested the Docker installation process via MacPorts.

#### Linux

There are too many varieties of Linux to give precise instructions here, but hopefully you can locate documentation for getting Docker installed on your Linux distribution. It may already be installed. If it is not already installed on your system, the [Install Docker Engine](https://docs.docker.com/engine/install/) page provides an overview of supported Linux distributions and pointers to relevant installation information. Alternatively, see:

 - [Docker Engine on CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
 - [Docker Engine on Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
 - [Docker Engine on Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
 - [Docker Engine on Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

### A quick tutorial on copy/pasting file contents from episodes of the lesson
Let's say you want to copy text off the lesson website and paste it into a file named `myfile` in the current working directory of a shell window. This can be achieved in many ways, depending on your computer's operating system, but routes I have found work for me:
- macOS and Linux: you are likely to have the `nano` editor installed, which provides you with a very straightforward way to create such a file, just run `nano myfile`, then paste text into the shell window, and press <kbd>control</kbd>+<kbd>x</kbd> to exit: you will be prompted whether you want to save changes to the file, and you can type <kbd>y</kbd> to say "yes".
- Microsoft Windows running `cmd.exe` shells:
  - `del myfile` to remove `myfile` if it already existed;
  - `copy con myfile` to mean what's typed in your shell window is copied into `myfile`;
  - paste the text you want within `myfile` into the shell window;
  - type <kbd>control</kbd>+<kbd>z</kbd> and then press <kbd>enter</kbd> to finish copying content into `myfile` and return to your shell;
  - you can run the command `type myfile` to check the content of that file, as a double-check.
- Microsoft Windows running PowerShell:
  - The `cmd.exe` method probably works, but another is to paste your file contents into a so-called "here-string" between `@'` and `'@` as in this example that follows (the ">" is the prompt indicator):

        > @'
        Some hypothetical
        file content that is

        split over many

        lines.
        '@ | Set-Content myfile -encoding ascii

{% include links.md %}

{% comment %}
<!--  LocalWords:  myfile kbd links.md md endcomment
-->
{% endcomment %}
