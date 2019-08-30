---
title: "Introducing containers"
teaching: 20
exercises: 0
questions:
- "What are containers, and why might they be useful to me?"
objectives:
- "Show how software depending on other software leads to configuration management problems."
- "Explain the notion of virtualisation in computing."
- "Explain the ways in which virtualisation may be useful."
- "Explain how containers streamline virtualisation."
keypoints:
- "Almost all software depends on other software components to function, but these components have independent evolutionary paths."
- "Projects involving many software components can rapidly run into a combinatoric explosion in the number of software version configurations available, yet only a subset of possible configurations actually works as desired."
- "Containers collect software components together and can help avoid software dependency problems."
- "Virtualisation is an old technology that container technology makes more practical."
- "Docker is just one software platform that can create containers and the resources they use."
---
### Disclaimers / apologies

This lesson comes with a whole set of disclaimers; my apologies for needing them!

1. You are the first learners to have engaged with this material. Various wheels are likely to fall off during parts of the session. Thankfully we have excellent helpers on hand. There are also separate episodes that do not depend on each other, so if you have to give up on one episode, you should be able to return later in the session.

2. This looks like the Carpentries' formatting of lessons because it is using their stylesheet (which is openly available for such purposes). However the similarity is visual-only: so far I have developed this lesson myself, which means that it does not have the quality-assurance or quality of the official Carpentries' lessons.

3. Docker is complex software used for many different purposes. We are unlikely to give examples that suit all of your potential ideal use-cases, but would be delighted to at least open up discussion of what those use-cases might be.

4. Containers are a topic that requires significant amounts of technical background to understand in detail. Most of the time containers, particularly as wrapped up by Docker, do not require you to have a deep technical understanding of container technology, but when things go wrong, the diagnostic messages may turn opaque rather quickly.

### The fundamental problem: software has dependencies that are difficult to manage

Consider Microsoft Excel: a typical workplace productivity tool. Most Excel users probably give little thought to the underlying software dependencies allowing them to open a given XLSX file on their computer. Indeed, in an ideal world none of us would need to think about fixing software dependencies, but we are far from that world. For example:
- Excel isn't directly available for computers running Linux at all. So clearly Linux, as operating system software, is different from the Windows and macOS operating systems that do have Excel versions.
- Although XLSX is notionally standardised, Excel on macOS and Excel on Windows can interpret files differently. Clearly, despite looking similar, these two "Excel"s are clearly not precisely the same software.
  - Note that this macOS/Windows Excel situation is *much*  better now than a few years ago: Microsoft had previously chosen to separately develop both of macOS Excel and Windows Excel, however when they also started releasing Office for iOS and Android, and providing web-based versions through Office 365, there was too much potential for divergence and compatibility chaos, so my understanding is that the core "engine" was standardised better across all the Office platforms. There still needs to be different software on each operating system that Excel supports to get that core "engine" up and running.
  - It is extremely unlikely that a current-day version of Excel would run on the Windows 2000 operating system. (A separate point is that it is also highly unlikely that it is a good idea to run Windows 2000 at all, given Microsoft has long stopped fixing its critical security flaws!) There are many other versions of Excel that either will or won't run on all the other versions of Windows... and all of them may read and write XLS(X) files slightly differently, and potentially, incompatibly.

All of the above discussion is *just* about one piece of software: Microsoft Excel. Excel mostly just depends on the version of the operating system you're running. However the situation gets far worse when building software in programming environments like R or Python. Those languages change over time, and depend on an enormous set of software libraries written by unrelated software development teams.

What if you wanted to distribute a software tool that automated interaction between R and Python. *Both* of these language environments have independent version and software dependency lineages. As the number of software components such as R and Python increases, this can rapidly lead to a combinatoric explosion in the number of possible configurations, only some of which will work as intended. This situation is sometimes informally termed "dependency hell".

The situation is often mitigated in part by factors such as:
- an acceptance of inherent software and hardware obsolesce (let's destroy the planet faster) so it's not expected that *all* versions of software need to be supported forever;
- some inherent synchronisation in the reasons for making software changes (e.g., the shift from 32-bit to 64-bit software), so not all versions will be expected to interact with all other versions.

It's not very practical to have every version of every piece of software installed on any computer that might need to resolve dependencies, as the mostly-redundant space used by the different versions will continue to mount.

Thankfully there are ways to get underneath (a lot of) this mess: containers to the rescue! Containers provide a way to package up software dependencies and access to resources such as files and communications networks in a uniform manner.

### Background: virtualisation in computing

Some uses of computers and the software they run should be deterministic, particularly when building reproducible computational environments. The meaning of "deterministic" is: if you feed in the same input, to the same computer, then the same output will appear.

However a computer running deterministic software, let's call it the "guest", should *itself* be able to be simulated as a deterministic computational process running on a computer we will call the "host". The guest computer can be said to have been virtualised: it is no longer a physical computer. Note that "virtual machine" is frequently referred to using the abbreviation "VM".

We have avoided the software dependency issue by looking for the lowest common factor across all software systems, which is the computer itself, beneath even the operating system software.

> ## Omitting details and avoiding complexities...
> Note that this description omits many details and avoids discussing complexities that are not particularly relevant to this introduction session, for example:
> - Thinking with analogy to movies such as Inception, The Matrix, etc., can the guest computer figure out that it's not actually a physical computer, and that it's running as software inside a host physical computer? Yes, it probably can... but let's not go there within this episode: we can talk later.
> - Can you run a host as a guest itself within another host? Sometimes... but let's not go there, either, and again, we can talk later if you are interested in further details.
{: .callout}

### Motivation for virtualisation

What features does virtualisation offer?
- Isolation: the VM is self-contained, so you can create and destroy it without affecting the host computer.
- Reproducibility: the VM can be "wound-back" to a known-good situation, much as you might revert a document you are editing to the last saved state.
- Manageability: the VM is software, so can be saved and restored as you might a document file (albeit a *much* larger file than a typical XLSX document!).
- Migration: the VM is just data, so can be transmitted to another physical host and run in the same way from there.

Downsides of "full" virtualisation:
- The file describing a VM has to contain its entire simulated hard-disk, so this leads to very large files.
- The guest computer wastes a lot of time managing "hardware" that's not actually real, e.g., VMs need to boot up in the same way that your laptop does.
- A host needs *lots* of RAM to run large numbers of virtual machines, as the strong isolation means that the VMs do not share any resources.

### Containers are a type of lightweight virtualisation

Containers are cut-down virtual machines. Containers sacrifice the strong isolation that full virtualisation provides in order to vastly reduce the resource requirements on the virtualisation host.

The term "container" can be usefully considered with reference to shipping containers. Before shipping containers were developed, packing and unpacking cargo ships was time consuming, and error prone, with high potential for different clients' goods to become mixed up. Software containers standardise the packaging of a complete software system (the lightweight virtual machine): you can drop a container into a container host, and it should "just work".

Hopefully this lesson will demonstrate the portability aspect of containers, showing the *same* containers running on:
- macOS;
- Microsoft Windows;
- (any Linux users out there?); and
- in the cloud.

### Docker is a popular container platform

Docker is software that manages containers and the resources that containers need. While Docker is a clear leader in the container space, there are many similar technologies available... we just need to pick one to use for this workshop.

### Docker's terminology

- **Image**: this is the term that Docker uses to describe the template from which live instances of containers will be created. The term "container image" may sometimes be used to emphasise that the "image" relates to software containers and not, say, the sense of an "image" when discussing cute kitten pictures (without loss of generality).
- **Container**: this is an instance of a lightweight virtual machine created by Docker from a (container) image.
- **Hub**: the Docker hub is a storage resource and associated website where a vast collection of preexisting container images are documented, and are made available for your use.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment
 -->
{% endcomment %}
