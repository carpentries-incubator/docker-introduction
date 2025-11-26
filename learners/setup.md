---
title: Setup
---

### Website accounts to create

Please seek help at the start of the lesson if you have not been able to establish a website account on:

- The [Docker Hub](https://hub.docker.com). We will use the Docker Hub to download pre-built container images, and for you to upload and download container images that you create, as explained in the relevant lesson episodes.

### Files to download

Download the [`podman-intro.zip`](files/podman-intro.zip) file. *This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository](https://github.com/carpentries-incubator/docker-introduction/blob/gh-pages/files/podman-intro.zip)*.

Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `podman-intro`.

### Software to install

Podman's installation experience has steadily improved, however situations will arise in which installing Podman on your computer may not be straightforward unless you have a large amount of technical experience.
Workshops try to have helpers on hand that have worked their way through the install process, but do be prepared for some troubleshooting.

In most cases, you will need to have administrator rights on the computer in order to install the Podman software. If you are using a computer managed by your organisation and do not have administrator rights, you *may* be able to get your organisation's IT staff to install Podman for you. Alternatively your IT support staff *may* be able to give you remote access to a server that can run Podman commands.

Please try to install the appropriate software from the list below depending on the operating system that your computer is running. Do let the workshop organisers know as early as possible if you are unable to install Podman using these instructions, as there may be other options available.

#### Microsoft Windows

**You must have admin rights to run Podman!** Some parts of the lesson will work without running as admin but if you are unable to `Run as administrator` on your machine some elements of this workshop might not work as described.

Ideally, you will be able to install the Podman Desktop, following the [Podman website's documentation](https://podman-desktop.io/docs/installation/windows-install).
Note that Podman for Windows relies upon installing the Windows Subsystem for Linux (WSL).

Note that the above installation instructions highlight a minimum version or "build" that is required to be able to install Podman on your Windows 10 system. See [Which version of Windows operating system am I running?](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808) for details of how to find out which version/build of Windows 10 you have.

If you are unable to follow the above instructions to install Podman on your Windows system, the final release of the deprecated Docker Toolbox version of Docker for Windows can be downloaded from the [releases page of the Docker Toolbox GitHub repository](https://github.com/docker/toolbox/releases). (Download the `.exe` file for the Windows installer). *Please note that this final release of Docker Toolbox includes an old version of Docker and you are strongly advised not to attempt to use this for any production use. It will, however, enable you to follow along with the lesson material.*

:::::::::::::::::::::::::::::::::::::::::  callout

## Warning: Git Bash

If you are using Git Bash as your terminal on Windows then you should be aware that you may run
into issues running some of the commands in this lesson as Git Bash will automatically re-write
any paths you specify at the command line into Windows versions of the paths and this will confuse
the Docker container you are trying to use. For example, if you enter the command:

```
docker run alpine cat /etc/os-release
```

Git Bash will change the `/etc/os-release` path to `C:\etc\os-release\` before passing the command
to the Docker container and the container will report an error. If you want to use Git Bash then you
can request that this path translation does not take place by adding an extra `/` to the start of the
path. i.e. the command would become:

```
docker run alpine cat //etc/os-release
```

This should suppress the path translation functionality in Git Bash.


::::::::::::::::::::::::::::::::::::::::::::::::::

#### Apple macOS

Ideally, you will be able to install the Podman software, from the
[Podman Github Releases website](https://github.com/containers/podman/releases/).
The current version of the Podman software appears to require macOS version 13 (Ventura) or later, but we have not tested this.

If you already use Homebrew or MacPorts to manage your software, and would prefer to use those
tools rather than Podman's installer, you can do so. For Homebrew, you can run the command
`brew install podman`.

#### Linux

If it is not already installed on your system, the [Podman Installation instructions](https://podman.io/docs/installation#linux-distributions) page provides an overview of supported Linux distributions and pointers to relevant installation information. 

### Verify Installation

To quickly check if the Docker and client and server are working run the following command in a new terminal or ssh session:

```bash
$ podman version
```

```output
Version:      3.4.4
API Version:  3.4.4
Go Version:   go1.18.1
Built:        Thu Jan  1 01:00:00 1970
OS/Arch:      linux/amd64
```

The above output shows a successful installation and will vary based on your system.

### A quick tutorial on copy/pasting file contents from episodes of the lesson

Let's say you want to copy text off the lesson website and paste it into a file named `myfile` in the current working directory of a shell window. This can be achieved in many ways, depending on your computer's operating system, but routes I have found work for me:

- macOS and Linux: you are likely to have the `nano` editor installed, which provides you with a very straightforward way to create such a file, just run `nano myfile`, then paste text into the shell window, and press <kbd>control</kbd>\+<kbd>x</kbd> to exit: you will be prompted whether you want to save changes to the file, and you can type <kbd>y</kbd> to say "yes".
- Microsoft Windows running `cmd.exe` shells:
  - `del myfile` to remove `myfile` if it already existed;
  - `copy con myfile` to mean what's typed in your shell window is copied into `myfile`;
  - paste the text you want within `myfile` into the shell window;
  - type <kbd>control</kbd>\+<kbd>z</kbd> and then press <kbd>enter</kbd> to finish copying content into `myfile` and return to your shell;
  - you can run the command `type myfile` to check the content of that file, as a double-check.
- Microsoft Windows running PowerShell:
  - The `cmd.exe` method probably works, but another is to paste your file contents into a so-called "here-string" between `@'` and `'@` as in this example that follows (the ">" is the prompt indicator):
    
    ```
    > @'
    Some hypothetical
    file content that is
    
    split over many
    
    lines.
    '@ | Set-Content myfile -encoding ascii
    ```

