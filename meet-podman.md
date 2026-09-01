---
title: Introducing the Podman Command Line
teaching: 10
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain how to check that Podman is installed and is ready to use.
- Demonstrate some initial Podman command line interactions.
- Use the built-in help for Podman commands.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I know Podman is installed and running?
- How do I interact with Podman?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Podman command line

Start the Podman application that you installed in working through the setup instructions for this session. Note that this might not be necessary if your laptop is running Linux or if the installation added the Podman application to your startup process.

:::::::::::::::::::::::::::::::::::::::::  callout

## You may need to login to Docker Hub

The Podman Desktop application will usually provide a way for you to log in to
the Docker Hub via the 'Settings' menu followed by 'Registries' and then
'Configure' under the Docker Hub entry. It is usually convenient to do this when
the application starts. This will require you to use your Docker Hub username
and your password. We will not actually require access to the Docker Hub until
later in the course but if you can login now, you should do so.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Determining your Docker Hub username

If you no longer recall your Docker Hub username, e.g., because you have been logging into the Docker Hub using your email address,
you can find out what it is through the steps:

- Open [https://hub.docker.com/](https://hub.docker.com/) in a web browser window
- Sign-in using your email and password (don't tell us what it is)
- In the top-right of the screen you will see your username
  

::::::::::::::::::::::::::::::::::::::::::::::::::

Once your Podman application is running, open a shell (terminal) window, and run the following command to check that Podman is installed and the command line tools are working correctly. Below is the output for a Mac version, but the specific version is unlikely to matter much: it does not have to precisely match the one listed below.

```bash
$ podman --version
```

```output
podman version 5.4.2
```

The above command has not actually relied on the part of Podman that runs containers, just that Podman
is installed and you can access it correctly from the command line.

A command that checks that Podman is working correctly is the `podman container ls` command (we cover this command in more detail later in the course).

Without explaining the details, output on a newly installed system would likely be:

```bash
$ podman container ls
```

```output
CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES
```

(The command `podman system info` could also be used to verify that Podman is correctly installed and operational but it produces a larger amount of output.)

However, if you instead get a message similar to the following

```output
Cannot connect to Podman. Please verify your connection to the Linux system using `podman system connection list`, or try `podman machine init` and `podman machine start` to manage a new Linux VM
Error: unable to connect to Podman socket: failed to connect: dial tcp 127.0.0.1:63249: connect: connection refused
```

then you need to check that you have started the Podman Desktop application or Podman Machine or however else you worked through the setup instructions.

## Getting help

Often when working with a new command line tool, we need to get help. These tools often have some
sort of subcommand or flag (usually `help`, `-h`, or `--help`) that displays a prompt describing how to use the
tool. For Podman, it's no different. If we run `podman --help`, we see the following output (running `podman` also produces the help message):

```output
Manage pods, containers and images

Usage:
  podman [options] [command]

Available Commands:
  attach      Attach to a running container
  build       Build an image using instructions from Containerfiles
  commit      Create new image based on the changed container
  compose     Run compose workloads via an external provider such as docker-compose or podman-compose
  container   Manage containers
  cp          Copy files/folders between a container and the local filesystem
  create      Create but do not start a container
  diff        Display the changes to the object's file system
  events      Show podman system events
  exec        Run a process in a running container
  export      Export container's filesystem contents as a tar archive
  farm        Farm out builds to remote machines
  generate    Generate structured data based on containers, pods or volumes
  healthcheck Manage health checks on containers
  help        Help about any command
  history     Show history of a specified image
  image       Manage images
  images      List images in local storage
  import      Import a tarball to create a filesystem image
  info        Display podman system information
  init        Initialize one or more containers
  inspect     Display the configuration of object denoted by ID
  kill        Kill one or more running containers with a specific signal
  kube        Play containers, pods or volumes from a structured file
  load        Load image(s) from a tar archive
  login       Log in to a container registry
  logout      Log out of a container registry
  logs        Fetch the logs of one or more containers
  machine     Manage a virtual machine
  manifest    Manipulate manifest lists and image indexes
  network     Manage networks
  pause       Pause all the processes in one or more containers
  pod         Manage pods
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image from a registry
  push        Push an image to a specified destination
  rename      Rename an existing container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images from local storage
  run         Run a command in a new container
  save        Save image(s) to an archive
  search      Search registry for image
  secret      Manage secrets
  start       Start one or more containers
  stats       Display a live stream of container resource usage statistics
  stop        Stop one or more containers
  system      Manage podman
  tag         Add an additional name to a local image
  top         Display the running processes of a container
  unpause     Unpause the processes in one or more containers
  untag       Remove a name from a local image
  update      Update an existing container
  version     Display the Podman version information
  volume      Manage volumes
  wait        Block on one or more containers

Options:
      --config string             Location of authentication config file
  -c, --connection string         Connection to use for remote Podman service (CONTAINER_CONNECTION) (default "podman-machine-default-root")
      --help                      Help for podman
      --identity string           path to SSH identity file, (CONTAINER_SSHKEY) (default "/Users/william/.local/share/containers/podman/machine/machine")
      --log-level string          Log messages above specified level (trace, debug, info, warn, warning, error, fatal, panic) (default "warn")
      --out string                Send output (stdout) from podman to a file
      --ssh string                define the ssh mode (default "golang")
      --storage-opt stringArray   Used to pass an option to the storage driver
      --url string                URL to access Podman service (CONTAINER_HOST) (default "ssh://root@127.0.0.1:63249/run/podman/podman.sock")
  -v, --version                   version for podman
```

We can view further help on the individual Podman commands by adding `--help` to that command. For example, take the `podman container ls` command that we ran previously. We can see from the Podman help prompt that `container` is a Podman command, so to get help for that command, we run:

```bash
podman container --help  # or instead 'podman container'
```

```output
Manage containers

Description:
  Manage containers

Usage:
  podman container [command]

Available Commands:
  attach      Attach to a running container
  checkpoint  Checkpoint one or more containers
  clone       Clone an existing container
  commit      Create new image based on the changed container
  cp          Copy files/folders between a container and the local filesystem
  create      Create but do not start a container
  diff        Inspect changes to the container's file systems
  exec        Run a process in a running container
  exists      Check if a container exists in local storage
  export      Export container's filesystem contents as a tar archive
  init        Initialize one or more containers
  inspect     Display the configuration of a container
  kill        Kill one or more running containers with a specific signal
  list        List containers
  logs        Fetch the logs of one or more containers
  pause       Pause all the processes in one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all non running containers
  ps          List containers
  rename      Rename an existing container
  restart     Restart one or more containers
  restore     Restore one or more containers from a checkpoint
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more containers
  stats       Display a live stream of container resource usage statistics
  stop        Stop one or more containers
  top         Display the running processes of a container
  unpause     Unpause the processes in one or more containers
  update      Update an existing container
  wait        Block on one or more containers
```

There's also help for the `container ls` command:

```bash
podman container ls --help  # this one actually requires the '--help' flag
```

```output
List containers

Description:
  Prints out information about the containers

Usage:
  podman container list [options]

Aliases:
  list, ls

Examples:
  podman container list -a
  podman container list -a --format "{{.ID}}  {{.Image}}  {{.Labels}}  {{.Mounts}}"
  podman container list --size --sort names

Options:
  -a, --all                  Show all the containers, default is only running containers
      --external             Show containers in storage not controlled by Podman
  -f, --filter stringArray   Filter output based on conditions given
      --format string        Pretty-print containers to JSON or using a Go template
  -n, --last int             Print the n last created containers (all states) (default -1)
      --no-trunc             Display the extended information
      --noheading            Do not print headers
      --ns                   Display namespace information
  -p, --pod                  Print the ID and name of the pod the containers are associated with
  -q, --quiet                Print the numeric IDs of the containers only
  -s, --size                 Display the total file sizes
      --sort choice          Sort output by: command, created, id, image, names, runningfor, size, status
      --sync                 Sync container state with OCI runtime
  -w, --watch uint           Watch the ps output on an interval in seconds
```

You may notice that there are many commands that stem from the `podman` command. Instead of trying to remember
all possible commands and options, it's better to learn how to effectively get help from the command line. Although
we can always search the web, getting the built-in help from our tool is often much faster and may provide the answer
right away. This applies not only to Podman, but also to most command line-based tools.

:::::::::::::::::::::::::::::::::::::::::  callout

## Podman Command Line Interface (CLI) syntax

In this lesson we use the CLI syntax
[introduced with the Docker Engine version 1.13](https://www.docker.com/blog/whats-new-in-docker-1-13/).
This new syntax combines commands into groups you will most often
want to interact with. In the help example above you can see `image` and `container`
management commands, which can be used to interact with your images and
containers respectively. With this new syntax you issue commands using the following
pattern `podman [command] [subcommand] [additional options]`

Comparing the output of two help commands above, you can
see that the same thing can be achieved in multiple ways. For example to start a
container using the old syntax you would use `podman run`. To achieve the
same with the new syntax, you use `podman container run` instead. Even though the old
approach is shorter and still officially supported, the new syntax is more descriptive, less
error-prone and is therefore recommended.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Exploring a command

Run `podman --help` and pick a command from the list.
Explore the help prompt for that command. Try to guess how a command would work by looking at the `Usage: `
section of the prompt.

:::::::::::::::  solution

## Solution

Suppose we pick the `podman image build` command:

```bash
podman image build --help
```

```output
Build an image using instructions from Containerfiles

Description:
  Builds an OCI or Docker image using instructions from one or more Containerfiles and a specified build context directory.

Usage:
  podman image build [options] [CONTEXT]

Examples:
  podman image build .
  podman image build --creds=username:password -t imageName -f Containerfile.simple .
  podman image build --layers --force-rm --tag imageName .

Options:
      --add-host host:ip                             add a custom host-to-IP mapping (host:ip) (default [])
      --all-platforms                                attempt to build for all base image platforms
      --annotation stringArray                       set metadata for an image (default [])
      --arch string                                  set the ARCH of the image to the provided value instead of the architecture of the host (default "arm64")
      --authfile string                              path of the authentication file.
      --build-arg argument=value                     argument=value to supply to the builder
      --build-arg-file argfile.conf                  argfile.conf containing lines of argument=value to supply to the builder
      --build-context argument=value                 argument=value to supply additional build context to the builder
      --cache-from stringArray                       remote repository list to utilise as potential cache source.
      --cache-to stringArray                         remote repository list to utilise as potential cache destination.
      --cache-ttl string                             only consider cache images under specified duration.
      --cap-add strings                              add the specified capability when running (default [])
      --cap-drop strings                             drop the specified capability when running (default [])
      --cert-dir string                              use certificates at the specified path to access the registry
      --cgroup-parent string                         optional parent cgroup for the container
      --cgroupns string                              'private', or 'host'
      --compat-volumes                               preserve the contents of VOLUMEs during RUN instructions
      --cpp-flag stringArray                         set additional flag to pass to C preprocessor (cpp)
      --cpu-period uint                              limit the CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                                limit the CPU CFS (Completely Fair Scheduler) quota
  -c, --cpu-shares uint                              CPU shares (relative weight)
      --cpuset-cpus string                           CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string                           memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems.
      --created-annotation                           set an "org.opencontainers.image.created" annotation in the image (default true)
      --creds [username[:password]]                  use [username[:password]] for accessing the registry
      --decryption-key strings                       key needed to decrypt the image
      --device stringArray                           additional devices to provide
  -D, --disable-compression                          don't compress layers by default (default true)
      --dns /etc/resolv.conf                         set custom DNS servers or disable it completely by setting it to 'none', which prevents the automatic creation of /etc/resolv.conf.
      --dns-option strings                           set custom DNS options
      --dns-search strings                           set custom DNS search domains
      --env stringArray                              set environment variable for the image
  -f, --file pathname or URL                         pathname or URL of a Dockerfile
      --force-rm                                     always remove intermediate containers after a build, even if the build is unsuccessful. (default true)
      --format format                                format of the built image's manifest and metadata. Use BUILDAH_FORMAT environment variable to override. (default "oci")
      --from string                                  image name used to replace the value in the first FROM instruction in the Containerfile
      --group-add strings                            add additional groups to the primary container process. 'keep-groups' allows container processes to use supplementary groups.
      --hooks-dir stringArray                        set the OCI hooks directory path (may be set multiple times)
      --http-proxy                                   pass through HTTP Proxy environment variables (default true)
      --identity-label                               add default identity label (default true)
      --ignorefile string                            path to an alternate .dockerignore file
      --iidfile file                                 file to write the image ID to
      --inherit-annotations                          inherit the annotations from the base image or base stages. (default true)
      --inherit-labels                               inherit the labels from the base image or base stages. (default true)
      --ipc path                                     'private', path of IPC namespace to join, or 'host'
      --isolation type                               type of process isolation to use. Use BUILDAH_ISOLATION environment variable to override. (default "rootless")
      --jobs int                                     how many stages to run in parallel (default 1)
      --label stringArray                            set metadata for an image (default [])
      --layer-label stringArray                      set metadata for an intermediate image (default [])
      --layers                                       use intermediate layers during build. Use BUILDAH_LAYERS environment variable to override. (default true)
      --logfile file                                 log to file instead of stdout/stderr
      --manifest string                              add the image to the specified manifest list. Creates manifest list if it does not exist
  -m, --memory string                                memory limit (format: <number>[<unit>], where unit = b, k, m or g)
      --memory-swap string                           swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --network string                               'private', 'none', 'ns:path' of network namespace to join, or 'host'
      --no-cache                                     do not use existing cached images for the container build. Build from the start with a new set of cached layers.
      --no-hostname                                  do not create new /etc/hostname file for RUN instructions, use the one from the base image.
      --no-hosts                                     do not create new /etc/hosts file for RUN instructions, use the one from the base image.
      --omit-history                                 omit build history information from built image
      --os string                                    set the OS to the provided value instead of the current operating system of the host (default "darwin")
      --os-feature feature                           set required OS feature for the target image in addition to values from the base image
      --os-version version                           set required OS version for the target image instead of the value from the base image
      --pid path                                     private, path of PID namespace to join, or 'host'
      --platform OS/ARCH[/VARIANT]                   set the OS/ARCH[/VARIANT] of the image to the provided value instead of the current operating system and architecture of the host (for example "linux/arm") (default [darwin/arm64/v8])
      --pull string[="always"]                       Pull image policy ("always"|"missing"|"never"|"newer") (default "missing")
  -q, --quiet                                        refrain from announcing build instructions and image read/write progress
      --retry int                                    number of times to retry in case of failure when performing push/pull (default 3)
      --retry-delay string                           delay between retries in case of push/pull failures
      --rewrite-timestamp                            set timestamps in layers to no later than the value for --source-date-epoch
      --rm                                           remove intermediate containers after a successful build (default true)
      --runtime-flag strings                         add global flags for the container runtime
      --sbom preset                                  scan working container using preset configuration
      --sbom-image-output path                       add scan results to image as path
      --sbom-image-purl-output path                  add scan results to image as path
      --sbom-merge-strategy strategy                 merge scan results using strategy
      --sbom-output file                             save scan results to file
      --sbom-purl-output file                        save scan results to file`
      --sbom-scanner-command command                 scan working container using command in scanner image
      --sbom-scanner-image image                     scan working container using scanner command from image
      --secret stringArray                           secret file to expose to the build
      --security-opt stringArray                     security options (default [])
      --shm-size <number><unit>                      size of '/dev/shm'. The format is <number><unit>. (default "65536k")
      --skip-unused-stages                           skips stages in multi-stage builds which do not affect the final target (default true)
      --source-date-epoch seconds                    set new timestamps in image info to seconds after the epoch, defaults to current time
      --squash                                       squash all image layers into a single layer
      --squash-all                                   Squash all layers into a single layer
      --ssh stringArray                              SSH agent socket or keys to expose to the build. (format: default|<id>[=<socket>|<key>[,<key>]])
      --stdin                                        pass stdin into containers
  -t, --tag name                                     tagged name to apply to the built image
      --target string                                set the target build stage to build
      --timestamp seconds                            set new timestamps in image info and layer to seconds after the epoch, defaults to current times
      --ulimit strings                               ulimit options
      --unsetannotation strings                      unset annotation when inheriting annotations from base image
      --unsetenv strings                             unset environment variable from final image
      --unsetlabel strings                           unset label when inheriting labels from base image
      --userns path                                  'container', path of user namespace to join, or 'host'
      --userns-gid-map containerGID:hostGID:length   containerGID:hostGID:length GID mapping to use in user namespace
      --userns-gid-map-group name                    name of entries from /etc/subgid to use to set user namespace GID mapping
      --userns-uid-map containerUID:hostUID:length   containerUID:hostUID:length UID mapping to use in user namespace
      --userns-uid-map-user name                     name of entries from /etc/subuid to use to set user namespace UID mapping
      --uts path                                     private, :path of UTS namespace to join, or 'host'
      --variant variant                              override the variant of the specified image
  -v, --volume stringArray                           bind mount a volume into the container
```

We could try to guess that the command could be run like this:

```bash
podman image build .
```

or

```bash
podman image build https://github.com/docker/rootfs.git
```

where `https://github.com/docker/rootfs.git` could be any relevant URL that supports a Docker-style image.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::




:::::::::::::::::::::::::::::::::::::::: keypoints

- You will typically interact with Podman using the command line.
- To learn how to run a certain Podman command, we can type the command followed by the `--help` flag.

::::::::::::::::::::::::::::::::::::::::::::::::::
