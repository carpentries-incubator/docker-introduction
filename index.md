---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---
This session aims to introduce the use of Docker containers with the goal of using them to effect reproducible computational environments. Such environments are useful for ensuring reproducible research outputs, for example.

After completing this session you should:
- Have an understanding of what Docker containers are, why they are useful
  and the common terminology used
- Have a working Docker installation on your local system to allow you to
  use containers
- Understand how to use existing Docker containers for common tasks
- Be able to build your own Docker containers by understanding both the role
  of a `Dockerfile` in building containers, and the syntax used in `Dockerfile`s
- Understand how to manage Docker containers on your local system
- Appreciate issues around reproducibility in software, understand how 
  containers can address some of these issues and what the limits to
  reproducibility using containers are

The practical work in this lesson is primarily aimed at using Docker on your own laptop. Beyond your laptop, software container technologies such as Docker can also be used in the cloud and on high performance computing (HPC) systems. Some of the material in this lesson will be applicable to those environments too.

> ## Containers on HPC systems
> On HPC systems it is more likely that *Singularity* rather than Docker will be the available container technology.
> If you are looking for a lesson on using Singularity containers (instead of Docker), see this lesson:
> * [Reproducible Computational Environments Using Containers: Introduction to Singularity](https://carpentries-incubator.github.io/singularity-introduction/)
{: .callout}

> ## Prerequisites
>
> - You should have basic familiarity with using a command shell, and the lesson text will at times request that you "open a shell window", with an assumption that you know what this means.
>   - Under Linux or macOS it is assumed that you will access a `bash` shell (usually the default), using your Terminal application.
>   - Under Windows, Powershell and Git Bash should allow you to use the Unix instructions. We will also try to give command variants for Windows `cmd.exe`.
> - The lessons will sometimes request that you use a text editor to create or edit files in particular directories. It is assumed that you either have an editor that you know how to use that runs within the working directory of your shell window (e.g. `nano`), or that if you use a graphical editor, that you can use it to read and write files into the working directory of your shell.
{: .prereq}

> ## A note about Docker
>
> Docker is a mature, robust and very widely used application. Nonetheless,
> it is still under extensive development. New versions are released regularly
> often containing a range of updates and new features.
>
> While we do our best to ensure that this lesson remains up to date and the
> descriptions and outputs shown match what you will see on your own computer,
> inconsistencies can occur.
> 
> If you spot inconsistencies or encounter any problems, please do report them
> by [opening an issue][open a lesson issue] in the [GitHub repository][docker-introduction repository] 
> for this lesson.
{: .callout}

## Learner profiles

To help give an idea of the target audience for this lesson we have included 
some example learner profiles.

*Nelson is a graduate student in microbiology.* They have experience in running Unix shell
commands and using libraries in R for the bioinformatics workflows they have developed.
They are expanding their analysis to run on 3000 genomes in 200 samples and they have
started to use the local cluster to run their workflows. The local research computing
facilitator has advised them that Docker could be useful for running their workflows on
the cluster. They'd like to make use of existing containers that other bioinformaticians
have made so they want to learn how to use Docker. They would also be interested in
creating their own Docker images for other lab members and collaborators to re-use their
workflows.

*Caitlin is a second year undergraduate in computer science examining Docker for the first
time.* She has heard about Docker but does not really know what it achieves or why it is
useful. She is reasonably confident in using the Unix shell, having used it briefly in
her first year modules. She is keen to find jump-off points to learn more about technical
details and alternative technologies that are also popular, having heard that container
technologies are widely used within industry.

*Xu, a materials science researcher, wants to package her software for release with
a paper to help ensure reproducibility.* She has written some code that makes use of a
series of Python libraries to undertake analysis of a compound. She wants to (or is
required to) make her software available as part of the paper submission. She
understands why Docker is important in helping to ensure reproducibility but not the
process and low-level detail of preparing a container and archiving it to obtain a DOI
for inclusion with the paper submission.

*Bronwyn is a PhD student running Python/R scripts on her local laptop/workstation.*
She is having difficulty getting all the tools she needs to work because of conflicting
dependencies and little experience with package managers. She is also keen to reduce
the overhead of managing software so she can get on with her thesis research. She has
heard that Docker might be able to help out but is not confident to start exploring
this on her own and does not have access to any expertise in this within her local
research group. She currently wants to know how to use preexisting Docker containers
but may need to create her own containers in the future.

*Virat is a grad student who is running an obscure bioinformatics tool (from a GitHub
repo) that depends on a number of other tools that need to be pre-installed .* He wants to be able to
run on multiple resources and have his undergrad assistant use the same tools. Virat
has command line experience and has struggled his way through complex installations
but he has no formal CS background - he only knows to use containers because a departmental
IT person suggested it. He is usually working from a Windows computer. He needs to
understand how to create his own container, use it locally, and train his student
to use it as well. 

{% include links.md %}

{% comment %}

TODO: systematically check for Windows-isms

<!--  LocalWords:  prereq links.md endcomment
 -->
{% endcomment %}
