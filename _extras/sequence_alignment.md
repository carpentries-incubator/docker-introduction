---
title: "sequence alignment - EMBOSS"
layout: episode
teaching: 20
exercises: 0
questions:
- "How can I align sequences without complex installation?"
- "How can I use a container from within and without?"
- "How can I share/use existing sequence files residing on my computer?"
objectives:
- "Select Docker containers from the docker hub."
- "Use a Docker container to accomplish tasks."
- "Make use of shared folder."
keypoints:
- "You can use existing container images and Docker instead of installing additional software."
- "Files can be shared with the container and used by the software within."
---

> ## EMBOSS 
> “The European Molecular Biology Open Software Suite” ([EMBOSS](http://emboss.sourceforge.net/) is a free Open Source software analysis package specially developed for the needs of the molecular biology user community. 
> EMBOSS contains a large number of sequence analysis tools, and we’ll sample a few of them via a docker method. 
{: .callout}

The purpose of this tutorial is more about learning how to use a Docker container rather than learning EMBOSS itself. 
To learn more about EMBOSS: List of applications: [emboss_apps](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/index.html) 
grouped by [function](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/groups.html), and [emboss tutorials](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)


> ## Set-up
- Macintosh: Double click on `Terminal` icon in the `/Applications/Utilities directory`.   
-  Windows: Open `PowerShell`.  
- Linux: open a new shell terminal.  
{:.prereq}

In your terminal shell window login Docker with your credentials. 
If you need to create an ID now go to the [Docker Hub](https://hub.docker.com) to register a free account.

~~~
$ docker login
~~~
{: .language-bash}
~~~
Login with your Docker ID to push and pull images from Docker Hub. 
If you don't have a Docker ID, head over to https://hub.docker.com 
to create one.
Username: YOUR_DOCKER_ID_HERE
Password: 
Login Succeeded
$ 
~~~
{: .output}

We'll use an existing container for EMBOSS version 6.6.0. The following `pull` command will make a copy of the docker image on your local computer.
Note that the lengthy tag `v6.6.0dfsg-7b1-deb_cv1` is necessary since it is not the `latest` tag.

~~~
$ docker pull biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1
~~~
{: .language-bash}
~~~
v6.6.0dfsg-7b1-deb_cv1: Pulling from biocontainers/emboss
478cd0aa93c0: Pull complete 
[...]
$ 
~~~
{: .output}

You can verify that the image now exists on your system:

~~~
$ docker image ls biocontainers/emboss
~~~
{: .language-bash}
~~~
REPOSITORY             TAG                      IMAGE ID        CREATED       SIZE
biocontainers/emboss   v6.6.0dfsg-7b1-deb_cv1   bc147a9dd825    2 years ago   638MB
~~~
{: .output}

> ## Shared directory
> We'll use the EMBOSS software on files shared from our local computer.

Download the [`docker-intro.zip`]({{ page.root }}/files/docker-intro.zip) file. _This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository][docker-introduction repository]_. Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `docker-intro`. 

These are very short peptide sequencesthe glucagon family to keep the output simple. 
*Glucagon is the principal hyperglycemic hormone, and acts as a counterbalancing hormone to insulin. 
Glucagon is a peptide hormone of 29 amino acids that shares the same precursor molecule, proglucagon, with GLP-1 and GLP-2. 
By tissue-specific posttranslational processing, glucagon is secreted from pancreatic α cells whereas GLP-1 and GLP-2 are secreted from intestinal L cells. 
All these peptides have considerable sequence similarity (Park (2015).)*   
*GIP, a related member of the glucagon peptide superfamily, also regulates nutrient disposal via stimulation of insulin secretion (Brubaker and Drucker (2002).)*

Within the `docker-intro` change to the `peptides` directory. There are 4 files in the simple "fasta" sequence format.

~~~
$ cd ~/Desktop/docker-intro/peptides
$ ls
~~~
{: .language-bash}
~~~
GIP.fa		GLP-1.fa	GLP-2.fa	glucagon.fa
~~~
{: .output}

We can quickly check the content of the files with the `cat` command.

~~~
$ cat *.fa
~~~
{: .language-bash}
~~~
>GIP
YAEGTFISDYSIAMDKIRQQDFVNWLLAQ
>GLP-1
HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG
>GLP-2
HADGSFSDEMNTILDNLAARDFINWLIQTKITD
>glucagon
HSQGTFTSDYSKYLDSRRAQDFVQWLMNT
~~~
{: .output}

We can now start a container and share the content of the current directory with the `--mount` qualifier:

~~~
$ run -it --rm --mount type=bind,source=${PWD},target=/data biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1
~~~
{: .language-bash}
~~~
biodocker@f3c591eb2b5f:/data$ 
~~~
{: .output}

The prompt tells us that now we are looking **within** the container.

> ## Exercise: Container checks
>
> What commands would you use to explore the Linux system on the container?
> What command would you use to find "who" is the default user of this container?
> Give it a try before checking the solution.
>
> > ## Solution
> >
> > To explore the Linux system the following commands are useful:
> > ~~~
> > $ uname -a
> > $ cat /etc/issue
> > $ cat /etc/os-release
> > ~~~
> > {: .language-bash}
> > Many containers by default are running as "root" *i.e.* administrator level.
> > However, it is often useful (or required) to run as a "regular" user. The
> > following commands show use the user name and the shell that is running
> > ~~~
> > $ whoami
> > $ cat /etc/issue
> > $ echo $SHELL
> > ~~~
> > {: .language-bash}
> > 
> > Therefore we are logged in as user `biodocker` running the `bash` shell and that is all good.
> {: .solution}
{: .challenge}


> ## Using EMBOSS?
> EMBOSS consists in a series of software for the analysis of protein or nucleic acid DNA and RNA sequences (but not Next Gen sequencing.)

The program `needle` is an implementation of the Needleman-Wunsch global alignment of two sequences (Needleman and Wunsch (1970).) From the EMBOSS documentation: [`needle`](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/needle.html) reads two input sequences and writes their optimal global sequence alignment to file. It uses the Needleman-Wunsch alignment algorithm to find the optimum alignment (including gaps) of two sequences along their entire length.

As an example we can align glucagon and GLP-1 using default parameters: press <kbd>return</kbd> or <kbd>enter</kbd> 3 times to keep the proposed default for the gap penalty and extension, and to use the suggested name for the output file:

~~~
$ needle glucagon.fa GLP-1.fa 
~~~
{: .language-bash}
~~~
Needleman-Wunsch global alignment of two sequences
Gap opening penalty [10.0]: 
Gap extension penalty [0.5]: 
Output alignment [glucagon.needle]: 
~~~
{: .output}

We can now visualize the output file on the screen:

~~~
$ cat glucagon.needle 
~~~
{: .language-bash}
~~~
########################################
# Program: needle
# Rundate: Tue 22 Oct 2019 16:38:08
# Commandline: needle
#    [-asequence] glucagon.fa
#    [-bsequence] GLP-1.fa
# Align_format: srspair
# Report_file: glucagon.needle
########################################

#=======================================
#
# Aligned_sequences: 2
# 1: glucagon
# 2: GLP-1
# Matrix: EBLOSUM62
# Gap_penalty: 10.0
# Extend_penalty: 0.5
#
# Length: 31
# Identity:      14/31 (45.2%)
# Similarity:    22/31 (71.0%)
# Gaps:           2/31 ( 6.5%)
# Score: 88.0
# 
#
#=======================================

glucagon           1 HSQGTFTSDYSKYLDSRRAQDFVQWLMNT--     29
                     |::||||||.|.||:.:.|::|:.||:..  
GLP-1              1 HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG     31

#---------------------------------------
#--------------------------------------- 
~~~
{: .output}

While it is nice to have an interactive interface, we can also provide all the required parameters on the comand line in order to make the alignment process non interactive. These qualifiers are detailed on the [`needle`](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/needle.html) help page.
For the above alignment example, adding the mandatory paramters the commands would be:

~~~
$ needle glucagon.fa GLP-1.fa -outfil glucagon.needle -gapopen 10 -gapextend 0.5
~~~
{: .language-bash}

This is particularly useful if we want to access and use an EMBOSS program without using an interactive shell command.

In order to do that, we'll first exit the current container. 

~~~
$ exit
~~~
{: .language-bash}

Since we added `--rm` when we started this container, it will be automatically deleted upon exit.
We are now back at the prompt of the local computer.

> ## Using EMBOSS from outside the container
> The `docker run` command used previously started an interactive container. This time, we'll provide the EMBOSS program command on the same line, and the container will start, run the EMBOSS program, and then exit after accomplishing its task.

We can accomplish this by removing the `-it` option from the `docker run` command, and adding the complete `needle` command that includes all the mandatory parameters.
Since the command has become quite long, we can add the continuation symbol ` \ ` to let the shell know that the file is written on 2 lines rather than a single, long line. This time we can align different sequences: GIP.fa and GLP-2.fa.

~~~
$ docker run --rm --mount type=bind,source=${PWD},target=/data biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1  \
needle GIP.fa GLP-2.fa -outfil gip-glp2.needle -gapopen 10 -gapextend 0.5
~~~
{: .language-bash}
~~~
 Needleman-Wunsch global alignment of two sequences 
~~~
{: .output}

We can then look just at the bottom of the resulting alignment file:

~~~
$ tail gip-glp2.needle 
~~~
{: .language-bash}
~~~
#
#=======================================

GIP                1 YAEGTFISDYSIAMDKIRQQDFVNWLLAQ----     29
                     :|:|:|..:.:..:|.:..:||:|||:..    
GLP-2              1 HADGSFSDEMNTILDNLAARDFINWLIQTKITD     33

#---------------------------------------
#---------------------------------------
~~~
{: .output}



## References

Brubaker, P. L., and D. J. Drucker. 2002. “Structure-function of the glucagon receptor family of G protein-coupled receptors: the glucagon, GIP, GLP-1, and GLP-2 receptors.” Recept. Channels 8 (3-4): 179–88. https://doi.org/10.3109/10606820213687.

Park, Min Kyun. 2015. “Subchapter 17A - Glucagon.” In Handbook of Hormones: Comparative Endocrinology for Basic and Clinical Research, 129–31. Academic Press. https://doi.org/10.1016/B978-0-12-801028-0.00138-0.

Needleman, S. B., and C. D. Wunsch. 1970. “A general method applicable to the search for similarities in the amino acid sequence of two proteins.” J. Mol. Biol. 48 (3): 443–53. https://doi.org/10.1016/0022-2836(70)90057-4.




