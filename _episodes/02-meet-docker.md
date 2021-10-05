---
title: "Introducing the Docker Command Line"
teaching: 10
exercises: 0
questions:
- "How do I know Docker is installed and running?"
- "How do I interact with Docker?"
objectives:
- "Explain how to check that Docker is installed and is ready to use."
- "Demonstrate some initial Docker command line interactions."
- "Use the built-in help for Docker commands."
keypoints:
- "A toolbar icon indicates that Docker is ready to use (on Windows and macOS)."
- "You will typically interact with Docker using the command line."
- "To learn how to run a certain Docker command, we can type the command followed by the `--help` flag."
---
### Docker command line

Start the Docker application that you installed in working through the setup instructions for this session. Note that this might not be necessary if your laptop is running Linux or if the installation added the Docker application to your startup process. 

> ## You may need to login to Docker Hub
> The Docker application will usually provide a way for you to log in to the Docker Hub using the application's menu (macOS) or systray
> icon (Windows) and it is usually convenient to do this when the application starts. This will require you to use your Docker Hub
> username and your password. We will not actually require access to the Docker Hub until later in the course but if you can login now,
> you should do so.
{: .callout}

> ## Determining your Docker Hub username
> If you no longer recall your Docker Hub username, e.g., because you have been logging into the Docker Hub using your email address,
> you can find out what it is through the steps:
> - Open <https://hub.docker.com/> in a web browser window
> - Sign-in using your email and password (don't tell us what it is)
> - In the top-right of the screen you will see your username
{: .callout}

Once your Docker application is running, open a shell (terminal) window, and run the following command to check that Docker is installed and the command line tools are working correctly. Below is the output for a Mac version, but the specific version is unlikely to matter much: it does not have to precisely match the one listed below.

~~~
$ docker --version
~~~
{: .language-bash}
~~~
Docker version 20.10.5, build 55c4c88
~~~
{: .output}

The above command has not actually relied on the part of Docker that runs containers, just that Docker
is installed and you can access it correctly from the command line.

A command that checks that Docker is working correctly is the `docker container ls` command (we cover this command in more detail later in the course).

Without explaining the details, output on a newly installed system would likely be:
~~~
$ docker container ls
~~~
{: .language-bash}
~~~
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
~~~
{: .output}
(The command `docker system info` could also be used to verify that Docker is correctly installed and operational but it produces a larger amount of output.)

However, if you instead get a message similar to the following
~~~
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
~~~
{: .output}

then you need to check that you have started the Docker Desktop, Docker Engine, or however else you worked through the setup instructions.

## Getting help
Often when working with a new command line tool, we need to get help. These tools often have some
sort of subcommand or flag (usually `help`, `-h`, or `--help`) that displays a prompt describing how to use the
tool. For Docker, it's no different. If we run `docker --help`, we see the following output (running `docker` also produces the help message):
~~~

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/vini/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/vini/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/vini/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/vini/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  app*        Docker App (Docker Inc., v0.9.1-beta3)
  builder     Manage builds
  buildx*     Build with BuildKit (Docker Inc., v0.5.1-docker)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  scan*       Docker Scan (Docker Inc., v0.6.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
~~~
{: .output}

There is a list of commands and the end of the help message says: `Run 'docker COMMAND --help' for more information on
a command.` For example, take the `docker container ls` command that we ran previously. We can see from the Docker help prompt
that `container` is a Docker command, so to get help for that command, we run:
~~~
docker container --help  # or instead 'docker container'
~~~
{: .language-bash}
~~~

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
~~~
{: .output}

There's also help for the `container ls` command:
~~~
docker container ls --help  # this one actually requires the '--help' flag
~~~
{: .language-bash}

~~~
Usage:  docker container ls [OPTIONS]

List containers

Aliases:
  ls, ps, list

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all states) (default -1)
  -l, --latest          Show the latest created container (includes all states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display container IDs
  -s, --size            Display total file sizes
~~~
{: .output}

You may notice that there are many commands that stem from the `docker` command. Instead of trying to remember
all possible commands and options, it's better to learn how to effectively get help from the command line. Although
we can always search the web, getting the built-in help from our tool is often much faster and may provide the answer
right away. This applies not only to Docker, but also to most command line-based tools.

> ## Docker Command Line Interface (CLI) syntax
>
> In this lesson we use the newest Docker CLI syntax
> [introduced with the Docker Engine version 1.13](https://www.docker.com/blog/whats-new-in-docker-1-13/).
> This new syntax combines commands into groups you will most often 
> want to interact with. In the help example above you can see `image` and `container`
> management commands, which can be used to interact with your images and 
> containers respectively. With this new syntax you issue commands using the following
> pattern `docker [command] [subcommand] [additional options]`
> 
> Comparing the output of two help commands above, you can
> see that the same thing can be achieved in multiple ways. For example to start a
> Docker container using the old syntax you would use `docker run`. To achieve the
> same with the new syntax, you use `docker container run` instead. Even though the old
> approach is shorter and still officially supported, the new syntax is more descriptive, less
> error-prone and is therefore recommended.
{: .callout}

> ## Exploring a command
> Run `docker --help` and pick a command from the list.
> Explore the help prompt for that command. Try to guess how a command would work by looking at the `Usage: `
> section of the prompt.
> 
> > ## Solution
> > Suppose we pick the `docker image build` command:
> > ~~~
> > docker image build --help
> > ~~~
> > {: .language-bash}
> > ~~~
> > Usage:  docker image build [OPTIONS] PATH | URL | -
> >
> > Build an image from a Dockerfile
> >
> > Options:
> >      --add-host list           Add a custom host-to-IP mapping (host:ip)
> >      --build-arg list          Set build-time variables
> >      --cache-from strings      Images to consider as cache sources
> >      --cgroup-parent string    Optional parent cgroup for the container
> >      --compress                Compress the build context using gzip
> >      --cpu-period int          Limit the CPU CFS (Completely Fair Scheduler) period
> >      --cpu-quota int           Limit the CPU CFS (Completely Fair Scheduler) quota
> >  -c, --cpu-shares int          CPU shares (relative weight)
> >      --cpuset-cpus string      CPUs in which to allow execution (0-3, 0,1)
> >      --cpuset-mems string      MEMs in which to allow execution (0-3, 0,1)
> >      --disable-content-trust   Skip image verification (default true)
> >  -f, --file string             Name of the Dockerfile (Default is 'PATH/Dockerfile')
> >      --force-rm                Always remove intermediate containers
> >      --iidfile string          Write the image ID to the file
> >      --isolation string        Container isolation technology
> >      --label list              Set metadata for an image
> >  -m, --memory bytes            Memory limit
> >      --memory-swap bytes       Swap limit equal to memory plus swap: '-1' to enable unlimited swap
> >      --network string          Set the networking mode for the RUN instructions during build (default "default")
> >      --no-cache                Do not use cache when building the image
> >      --pull                    Always attempt to pull a newer version of the image
> >  -q, --quiet                   Suppress the build output and print image ID on success
> >      --rm                      Remove intermediate containers after a successful build (default true)
> >      --security-opt strings    Security options
> >      --shm-size bytes          Size of /dev/shm
> >  -t, --tag list                Name and optionally a tag in the 'name:tag' format
> >      --target string           Set the target build stage to build.
> >      --ulimit ulimit           Ulimit options (default [])
> > ~~~
> > {: .output}
> > We could try to guess that the command could be run like this:
> > ~~~
> > docker image build .
> > ~~~
> > {: .language-bash}
> > or
> > ~~~
> > docker image build https://github.com/docker/rootfs.git
> > ~~~
> > {: .language-bash}
> > Where `https://github.com/docker/rootfs.git` could be any relevant URL that supports a Docker image.
> {: .solution}
{: .challenge}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment systray
 -->
{% endcomment %}
