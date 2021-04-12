---
title: "Introducing Containers"
teaching: 20
exercises: 0
questions:
- "What are containers, and why might they be useful to me?"
objectives:
- "Show how software depending on other software leads to configuration management problems."
- "Identify the problems that software installation can pose for research."
- "Explain the advantages virtualization has over traditional computing."
- "Give two examples of how containers can solve software configuration problems."
keypoints:
- "Almost all software depends on other software components to function, but these components have independent evolutionary paths."
- "Small environments that contain only the software that's absolutely needed for a given task are easier to replicate and maintain."
- "Critical systems that cannot be upgraded, due to cost, difficulty, etc. need to be reproduced on newer systems in a maintainable and self-documented way."
- "Virtualization was created to allow multiple environments to run on a single computer."
- "Containerization takes virtualization one step further by making even smaller environments by avoiding all but the minimum software required."
- "Containerization allows the creation of complex data pipelines that are impossible on a single system simply and reliably, without additional cost or hardware." 
- "Containers are built from 'recipes' that contain the minimum software components together and the installation instructions necessary to build them."
- "Docker is just one software platform that can create containers and the resources they use."
---
### Disclaimers

1. Docker is complex software used for many different purposes. We are unlikely to give examples that suit all of your potential ideal use-cases, but would be delighted to at least open up a discussion of what those use-cases might be.

2. Containers are a topic that requires significant amounts of technical background to understand in detail. Most of the time containers, particularly as wrapped up by Docker, do not require you to have a deep technical understanding of container technology, but when things go wrong, the diagnostic messages may turn opaque rather quickly.

### Scientific Software Challenges

> ## What's Your Experience?
> 
> Take a minute to think about challenges that you have experienced in using 
> scientific software (or software in general!) for your research. Then, 
> share with your neighbors and try to come up with a list of common gripes or 
> challenges. 
{: .challenge}

You may have come up with some of the following: 

- you want to use software that doesn't exist for the operating system (Mac, Windows, Linux) you'd prefer.
- you struggle with installing a software tool because you have to install a bunch of other things first and those installs required *other* things, and those require *more* things, etc. (.i.e combinatoric explosion).
- the software you're setting up involves many dependencies and only a subset of all possible versions of those dependencies actually works as desired.
- you're not actually sure what software you're using because the install process was so circuitous. 
- you and a colleague are using the same software but get different results because you have installed different versions and/or are using different operating systems.
- you installed everything correctly on your computer but now need to install it on a colleague's computer/campus computing cluster/etc. 
- you've written a package for other people to use but a lot of your users frequently have trouble with installation.
- you need to resurrect a research project from a former colleague and the software used was on a system you cannot recreate and won't work (or not the same!) on a modern system. 
- etc. 

A lot of these characteristics boil down to one fact: the main program you want 
to use likely depends on many, many, different other programs (including the 
operating system!), creating a very complex, and often fragile system. One change 
or missing piece may stop the whole thing from working or break something that was 
already running. It's no surprise that this situation is sometimes 
informally termed "dependency hell".

> ## Software and Science
> 
> Again, take a minute to think about how the software challenges we've discussed 
> could impact (or have impacted!) the quality of your work. 
> Share your thoughts with your neighbors. What can go wrong if our software 
> doesn't work? 
{: .challenge}

Unsurprisingly, software installation and configuration challenges can have 
negative consequences for research: 
- you can't use a specific tool at all, because it's not available or installable. 
- you can't reproduce your results because you're not sure what tools you're actually using. 
- you can't access extra/newer resources because you're not able to replicate your software set up. 
- others cannot validate and/or build upon your work because they cannot recreate your system's unicorn configuration.

Thankfully there are ways to get underneath (a lot of) this mess: containers 
to the rescue! Containers provide a way to package up software dependencies 
and access to resources such as files and communications networks in a uniform manner.

### Docker and What is a Container? 

Docker is a tool that allows you to build what are called "containers." It's 
not the only tool that can create containers, but is the one we've chosen for 
this workshop. But what *is* a container? 

To understand containers, let's first talk briefly about your computer. 

Your computer has some standard pieces that allow it to work - often what's 
called the hardware. One of these pieces is the CPU or processor; another is 
the amount of memory or RAM that your computer can use to store information 
temporarily while running programs; another is the hard drive, which can store 
information over the long-term. All these pieces work together to do the 
"computing" of a computer, but we don't see them because they're hidden from view (usually). 

Instead, what we see is our desktop, program windows, different folders, and 
files. These all live in what's called the file system. Everything on your computer - programs, 
pictures, documents - lives somewhere in the file system. One way to think of 
the file system is the layer of stuff that uses the CPU, memory and hard 
drive of your computer on your behalf.

NOW, imagine you wanted to install some new software but don't want to take the chance of making a mess of your existing system by installing a bunch of additional stuff (libraries/dependencies/etc.).  You could buy a second computer but you're a cheapskate and don't want to buy a whole new computer just for this.  Plus bringing two laptops to a meeting is a weird flex. 😉 What if, instead, you could have another filesystem that you could store and access from your main computer, but was inside your existing computer?

Or, imagine you have two tools you want to use in your groundbreaking research on cat memes: PurrLOLing, a tool that does AMAZING at predicting the best text for a meme based on the cat species and WhiskerSpot, the only tool available for identifying cat species from images.  You want to send cat pictures to WhiskerSpot, and then send the species output to PurrLOLing.  But there's a problem: PurrLOLing only works on Ubuntu and WhiskerSpot is only supported for OpenSUSE so you can't have them on the same system!  Again, we really want another filesystem (or two) on our computer that we could use to chain together WhiskerSpot and PurrLOLing in a "pipeline"... 

Container systems like Docker are special programs on your computer that make it possible!
The term "container" can be usefully considered with reference to shipping 
containers. Before shipping containers were developed, packing and unpacking 
cargo ships was time consuming and error prone, with high potential for 
different clients' goods to become mixed up. Just like shipping containers keep things 
together that should stay together, software containers standardize the description and 
creation of a complete software system: you can drop a container into any computer with 
the container software installed (the 'container host'), and it should "just work".

> ## Virtualization
> 
> Containers are an example of what's called **virtualization** -- having a 
> second "virtual" computer running and accessible from a main or **host**
> computer. Another example of virtualization are **virtual machines** or 
> VMs. A virtual machine typically contains a whole copy of an operating system in 
> addition to its own file system and has to get booted up in the same way 
> a computer would. 
> A container is considered a lightweight version of a virtual machine; 
> underneath, the container is using the Linux kernel and simply has some 
> flavor of Linux + the file system inside. 
{: .callout}

One final term: while the **container** is an alternative file system layer that you 
can access and run from your computer, the **container image** is the 'recipe' or template
for a container. The container image has all the needed information to start 
up a running copy of the container. A running container tends to be transient 
and can be started and shut down. The image is more long-lived: as a source file 
for the container, it can also serve as documentation for what is inside the container, 
like the list of ingredients in a cookie recipe. The container image can be used to 
create batches of the same cookie (.i.e multiple containers) and is relatively unchanging, 
whereas the individual cookies come and go. If you want a different type of container 
(cookie), then you need a different image (recipe).


### Putting the Pieces Together

Think back to some of the challenges we described at the beginning. The many layers 
of scientific software installations make it hard to install and re-install 
scientific software -- which ultimately, hinders reliability and reproducibility. 

But now, think about what a container is - a self-contained, complete, separate 
computer file system. What advantages are there if you put your scientific software
tools into containers? 

This solves several of our problems: 

- documentation: there is a clear record of what software and software dependencies were used, from bottom to top. 
- portability: the container can be used on any computer that has Docker installed -- it doesn't matter whether the computer is Mac, Windows or Linux-based. 
- reproducibility: you can use the exact same software and environment on your computer and on other resources (like a large-scale computing cluster). 
- configurability: containers can be sized to take advantage of more resources (memory, CPU, etc.) on large systems (clusters) or less, depending on the circumstances.

The rest of this workshop will show you how to download and run pre-existing containers 
on your own computer, and how to create and share your own containers.

### Use cases for containers

Now that we have discussed a little bit about containers - what they do and the
issues they attempt to address - you may be able to think of a few potential use
cases in your area of work. Some examples of common use cases for containers in 
a research context include:

- Using containers solely on your own computer to use a specific software tool 
  or to test out a tool (possibly to avoid a difficult and complex installation
  process, to save your time or to avoid dependency hell).
- Setting up software in a container and then sharing it with your collaborators
  for use on their computers or a remote computing resource (e.g. cloud-based or HPC
  system).
- Archiving the container(s) so you can repeat analysis/modelling using the 
  same software and configuration in the future - capturing your workflow.
- Imagine 

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
