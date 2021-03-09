---
title: "Introducing Containers"
teaching: 20
exercises: 0
questions:
- "What are containers, and why might they be useful to me?"
objectives:
- "Show how software depending on other software leads to configuration management problems."
- "Identify the problems that software installation problems can pose for research."
- "Give two examples of how containers can solve software configuration problems." 
keypoints:
- "Almost all software depends on other software components to function, but these components have independent evolutionary paths."
- "Projects involving many software components can rapidly run into a combinatoric explosion in the number of software version configurations available, yet only a subset of possible configurations actually works as desired."
- "Containers collect software components together and can help avoid software dependency problems."
- "Virtualisation is an old technology that container technology makes more practical."
- "Docker is just one software platform that can create containers and the resources they use."
---
### Disclaimers

1. Docker is complex software used for many different purposes. We are unlikely to give examples that suit all of your potential ideal use-cases, but would be delighted to at least open up discussion of what those use-cases might be.

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
- software that doesn't exist for the operating system (Mac, Windows, Linux) you use or want to use. 
- software that is hard to install because you have to install a bunch of other things first 
(and those installations required *other* installations...). 
- you're not actually sure what software you're using because the install process was 
so circuitous. 
- you and a colleague are using the "same" software but have installed different versions. 
- you installed everything correctly on your computer, once, but now need to 
install it on your colleague's computer, or on the campus computing cluster. 
- you're writing a package for other people to use, but you get a lot of emails 
from people who can't install it. 

Etc. 

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
- you can't access extra resources because you're not able to replicate your software set up. 

Thankfully there are ways to get underneath (a lot of) this mess: containers 
to the rescue! Containers provide a way to package up software dependencies 
and access to resources such as files and communications networks in a uniform manner.

### What is a Container? 

Docker is a tool that allows you to build what are called "containers." It's 
not the only tool that can create containers, but is the one we've chosen for 
this workshop. But what *is* a container? 

To understand containers, let's first talk briefly about your computer. 

Your computer has some standard pieces that allow it to work - often what's 
called the hardware. One of these pieces is the CPU or processor; another is 
the amount of memory or RAM that your computer can use to store information 
temporarily while running programs; another is the hard drive, which can store 
information over the long-term. All these pieces work together to do the 
"computing" of a computer, but we don't see them, because they're hidden away. 

Instead, what we see is our desktop, program windows, different folders, and 
files. These all 
live in what's called the file system. Everything on your computer - programs, 
pictures, documents - lives somewhere in the file system. One way to think of 
the file system is the layer of stuff that can be activated to use use the CPU, memory and hard 
drive of your computer. 

NOW, imagine you wanted to have a second computer. You don't want to buy a 
whole new computer because it's too expensive. What if, instead, you could have 
another filesystem that you could store and access from your main computer, 
but that is self-contained? 

 A container system (like Docker) is a special program 
on your computer that does this. 
The term "container" can be usefully considered with reference to shipping 
containers. Before shipping containers were developed, packing and unpacking 
cargo ships was time consuming, and error prone, with high potential for 
different clients' goods to become mixed up. Software containers standardise 
the packaging of a complete software system:
 you can drop a container into a computer with the container software installed
 (also called a container host), and it should "just work".

> ## Virtualization
> 
> Containers are an example of what's called **virtualization** -- having a 
> second "virtual" computer running and accessible from a main or **host**
> computer. Another example of virtualization are **virtual machines** or 
> VMs. A virtual machine typically contains a whole copy of an operating system in 
> addition to its own file system and has to get booted up in the same way 
> a computer would. 
> A container is considered a lightweight version of a virtual machine; 
> underneath, the container is using the Linux 
> kernel and simply has some flavor of Linux + the file system inside. 
{: .callout}

One final term: if the container is an alternative file system layer that you 
can access and run from your computer, the **container image** is like a template 
for that container. The container image has all the needed information to start 
up a running copy of the container. A running container tends to be transient 
and can be started and shut down. The image is more long-lived, as a source file for the container. 
You could think of the container image like a cookie cutter -- it 
can be used to create multiple copies of the same shape (or container) 
and is relatively unchanging, where cookies come and go. If you want a 
different type of container (cookie) you need a different image (cookie cutter).


### Putting the Pieces Together

Think back to some of the challenges we described at the beginning. The many layers 
of scientific software installations make it hard to install and re-install 
scientific software -- which ultimately, hinders reliability and reproducibility. 

But now, think about what a container is - a self-contained, complete, separate 
computer file system. What if you put your scientific software tools into a 
container? 

This solves several of our problems: 
- There is a clear record of what software and software dependencies were used, 
from bottom to top. 
- The container can be used on any computer that has Docker installed -- it 
doesn't matter whether the computer is Mac, Windows or Linux-based. 
- The container ensures that you can use the exact same software and environment 
on your computer and on other resources (like a large-scale computing cluster). 

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
- Setting up software and then sharing it with your collaborators for use on
  their computers or a remote computing resource (e.g. cloud-based or HPC
  system).
- Archiving the container(s) so you can repeat analysis/modelling using the 
  same software and configuration in the future - capturing your workflow.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
