---
title: "sequence alignment - EMBOSS, clustalomega"
layout: episode
teaching: 10
exercises: 20
questions:
- "How can I align sequences without complex installation?"
- "How can I use a container from within and without?"
- "How can I share/use existing sequence files residing on my computer?"
objectives:
- "Select Docker containers from the docker hub."
- "Use a Docker container to accomplish tasks."
- "Make use of shared folder."
keypoints:
- "You can use existing Docker images instead of installing additional software."
- "Files can be shared with the container and used by the installed software."
-  "Software installed within a container can be accessed from outside the container."
---

> ## EMBOSS 
> “The European Molecular Biology Open Software Suite” ([EMBOSS](http://emboss.sourceforge.net/) is a free Open Source software analysis package specially developed for the needs of the molecular biology user community. 
> EMBOSS contains a large number of sequence analysis tools, and we’ll use one of them using a docker method. 
{: .callout}

The purpose of this tutorial is more about learning how to use a Docker container rather than learning EMBOSS itself. 
To learn more about EMBOSS: 
* List of applications: [emboss_apps](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/index.html) 
* grouped by [function](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/groups.html), and 
* [emboss tutorials](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)


> ## Set-up
- **Macintosh**: Double click on `Terminal` icon in the `/Applications/Utilities directory`.   
-  **Windows**: Open `PowerShell`.  
- **Linux**: open a new shell terminal.  
- If you need to create a Docker ID: go to the [Docker Hub](https://hub.docker.com) to register a free account.
{:.prereq}

In your terminal shell window login Docker with your Docker credentials.

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

We'll use an existing container for EMBOSS version 6.6.0. 

The following `pull` command will make a copy of the docker image on your local computer.
Note that the lengthy tag `v6.6.0dfsg-7b1-deb_cv1` is necessary since it is not the `latest` tag.

~~~
$ docker image pull biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1
~~~
{: .language-bash}
~~~
v6.6.0dfsg-7b1-deb_cv1: Pulling from biocontainers/emboss
478cd0aa93c0: Pull complete 
[...]
$ 
~~~
{: .output}

You can verify that the image has been copied onto your computer with a listing command:

~~~
$ docker image ls biocontainers/emboss
~~~
{: .language-bash}
~~~
REPOSITORY             TAG                      IMAGE ID        CREATED       SIZE
biocontainers/emboss   v6.6.0dfsg-7b1-deb_cv1   bc147a9dd825    2 years ago   638MB
~~~
{: .output}

> ## Challenge: make your own updated EMBOSS image.
>
> During the early part of the lesson we explored creating our own Docker images thanks to a list of instruction within a `Dockerfile` document.
> The file for a different but similar EMBOSS Docker image is available: [Dockerfile](https://hub.docker.com/r/pegi3s/emboss/dockerfile) (also shown within "Solution" below.)  
> This information would allow you to create your own image from a newer version of Ubuntu.   
> How would you use this information to make your own image?   
> Could you use another Linux distributions?  
> Find help on an earlier section of the workshop if you need, or skip this exercise for now.   
> 
> > ## Solution
> > The [Dockerfile](https://hub.docker.com/r/pegi3s/emboss/dockerfile) from a similar image is shown below:
> > ~~~
> > FROM ubuntu:18.04
> > LABEL emboss.version="6.6.0" \
> >    emboss.web="http://emboss.sourceforge.net"
> > RUN apt-get -qq update && apt-get -y upgrade && \
>	> apt-get install -y emboss=6.6.0+dfsg-6build1
> > ~~~
> > {: .output}
> > 
> > Here are some steps that would accomplish this task:
> > * create a copy of the Dockerfile document to be modified (for example use `nano` as a text editor.)
> > * Check the latest version available for ubuntu, using the [official image](https://hub.docker.com/_/ubuntu) hub page
> > * replace this new version name and tag on the Dockerfile
> > * Run the `docker build -t ...` command
> > * Test your image with a `docker run ...` command
> > * Push the image to your own hub account for future retrieval
> > 
> > This solution uses Ubuntu, but other Linux distributions could be used. However, this would also require changing the `apt-get` command to that specific to the chosen distribution such as `yum` for CentOS.
> {: .solution}
{: .challenge}

> ## Shared directory
> We'll use the EMBOSS software on files shared from our local computer.
{: .callout}

Download the [`docker-intro.zip`]({{ page.root }}/files/docker-intro.zip) file. _This file can alternatively be downloaded from the `files` directory in the [docker-introduction GitHub repository][docker-introduction repository]_. Move the downloaded file to your Desktop and unzip it. It should unzip to a folder called `docker-intro`. 


> ## Sequences used: glucagon family peptides
> These are very short peptide sequences of the glucagon family to keep the input and output simple.   
> > ## Information on physiological role of sequences:
> > *Glucagon is the principal hyperglycemic hormone, and acts as a counterbalancing hormone to insulin. 
> > Glucagon is a peptide hormone of 29 amino acids that shares the same precursor molecule, proglucagon, with GLP-1 and GLP-2. 
> > By tissue-specific posttranslational processing, glucagon is secreted from pancreatic α cells whereas GLP-1 and GLP-2 are secreted from intestinal L cells. 
> > All these peptides have considerable sequence similarity (Park (2015).)*   
> > *GIP, a related member of the glucagon peptide superfamily, also regulates nutrient disposal via stimulation of insulin secretion (Brubaker and Drucker (2002).)*
> {: .solution}
{: .challenge}

Within the `docker-intro` downloaded previously change to the `peptides` directory. There are 4 files in the simple ["fasta"](https://en.wikipedia.org/wiki/FASTA_format) sequence format.

~~~
$ cd ~/Desktop/docker-intro/peptides
$ ls
~~~
{: .language-bash}
~~~
GIP.fa		GLP-1.fa	GLP-2.fa	glucagon.fa
~~~
{: .output}

Since they are very short, we can quickly check the content of all the files at the same time with the
following `cat` command:

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

We can now start a new container and share the content of the current directory with the container by using the `--mount` qualifier. 
This will create the `/data` directory within the container, sharing the content of the current directory which is invoqued by `${PWD}`.

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
{: .callout}

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
> The `docker run` command used previously started an interactive container. 
> This time, we'll provide the EMBOSS program command on the same line, and the container will start, run the EMBOSS program, 
> and then exit after accomplishing its task.
{: .callout}

We can accomplish this by removing the `-it` option from the `docker run` command, and adding the complete `needle` command that includes all the mandatory parameters.
Since the command has become quite long, we can add the continuation symbol `\` to let the shell know that the file is written on 2 lines rather than a single, long line. This time we can align different sequences: GIP.fa and GLP-2.fa.

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

This can easily be turned into a loop, for example aligning all sequences to that of glucagon.
The filename extension `.fa` is removed with the `bash` method using `basename` so that the resulting file name only has `.needle` as an extension.
However, due to the loop nature of the command, it is not possible to use the continuation symbol as we just did previously.

~~~
$ for f in G*.fa; do  b=`basename $f .fa`; docker run --rm --mount type=bind,source=${PWD},target=/data biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1  needle glucagon.fa $f -outfil gluc_$b.needle  -gapopen 10 -gapextend 0.5; done
~~~
{: .language-bash}
~~~
Needleman-Wunsch global alignment of two sequences
Needleman-Wunsch global alignment of two sequences
Needleman-Wunsch global alignment of two sequences
~~~
{: .output}

The output shows that the program ran 3 times, as expected. The resulting files can be found within the current directory that you can explore using the `cat` or `tail` shell commands for example.

> ## Multiple sequence alignment
> EMBOSS only provides a "wrapper" ([emma](http://emboss.sourceforge.net/apps/release/6.6/emboss/apps/emma.html)) calling an external multiple sequence 
> alignment named `clustalw` which is an older algorithm. For protein sequences one of the recommended algorithm is a similar, newer algorithm named `clustalomega` 
> that we will use within a different docker image.   
> From web [clustalomega documentation](https://www.ebi.ac.uk/seqdb/confluence/display/THD/Clustal+Omega): 
> *Clustal Omega is a multiple sequence alignment program for aligning three or more sequences together in a computationally efficient and accurate manner. 
> It produces biologically meaningful multiple sequence alignments of divergent sequences.*
> (See Sievers and Higgins (2018).)
> 
{: .callout}

One of the great advantages of Docker is the modularity that it can bring to using software that is not even installed on your own computer.

We can pull the image in advance. Since the `latest` tag exists the command does not requires one. It may still be informative to explore the ["Tags"](https://hub.docker.com/r/pegi3s/clustalomega/tags) page on the hub.

~~~
$ docker image pull pegi3s/clustalomega
~~~
{: .language-bash}
~~~
Using default tag: latest
latest: Pulling from pegi3s/clustalomega
6abc03819f3e: Pull complete 
[...]
$ 
~~~
{: .output}

This image  was constructed with an "entrypoint" statement as indicated by its [Dockerfile](https://hub.docker.com/r/pegi3s/clustalomega/dockerfile): `ENTRYPOINT ["clustalo"]`. This means that as the container is started the `clustalo` software is immediately engaged *i.e.* expecting sequence input. 
However, we can check if the container works and at the same time request help on `clustalo` by simply adding `-h` to request the help information. (The rather long output is also online: [README](http://www.clustal.org/omega/README).)

~~~
$ docker run --rm  pegi3s/clustalomega -h
~~~
{: .language-bash}
~~~
Clustal Omega - 1.2.4 (AndreaGiacomo)
[...]
  --long-version            Print long version information and exit
  --force                   Force file overwriting
$ 
~~~
{: .output}

We can now proceed to align sequences. 
We should still be set within the `~/Desktop/docker-intro/peptides` directory as before, and we will share the current directory with the container.
As a first attempt we'll use the multiple sequence file `peptides.fasta` located in the same directory. 
The file contains all 4 sequences we just used previously. 
You can check its content with the  `cat` command.

Since the container uses  `ENTRYPOINT` at this time we can only use it from outside the container *i.e.* adding `-it` 
to make the container interactive would have no effect. We can provide the minimal mandatory input required 
as the input and output file names with `-i` and `-o` which will pass directly to the `clustalo` program.
For now, we also need to accept that `clustalo` expects data to be found in the `/data` directory on the container.

~~~
$ docker run --rm --mount type=bind,source=${PWD},target=/data pegi3s/clustalomega -i /data/peptides.fasta -o /data/peptides_aligned.fasta
$ cat peptides_aligned.fasta
~~~
{: .language-bash}
~~~
>GIP
YAEGTFISDYSIAMDKIRQQDFVNWLLAQ----
>GLP-1
HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG--
>GLP-2
HADGSFSDEMNTILDNLAARDFINWLIQTKITD
>glucagon
HSQGTFTSDYSKYLDSRRAQDFVQWLMNT----
~~~
{: .output}

The `-` symbols represent the gaps. Therefore it worked. 

Note: running the same command will provide an error as `clustalo` will refuse to overwrite the existing `peptides_aligned.fasta` file. 
This is a good thing! However, it is possible to override this safety by adding `--force` to the command. `clustalo` can also output
the alignment in other formats as detailed in the help under the optional modifier `--outfmt`. We can try the `clustal` format for a more visual output:

~~~
$ docker run --rm --mount type=bind,source=${PWD},target=/data pegi3s/clustalomega --outfmt=clu -i /data/peptides.fasta -o /data/peptides_aligned.clu
$ cat peptides_aligned.clu
~~~
{: .language-bash}
~~~
CLUSTAL O(1.2.4) multiple sequence alignment


GIP           YAEGTFISDYSIAMDKIRQQDFVNWLLAQ----
GLP-1         HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG--
GLP-2         HADGSFSDEMNTILDNLAARDFINWLIQTKITD
glucagon      HSQGTFTSDYSKYLDSRRAQDFVQWLMNT----
              :::*:* .: .  ::    ::*: **:      
~~~
{: .output}

> ## Challenge: align more sequences.
> How would you proceed to align the hemogloin and globin sequences contained within the file `hglob.fasta`? located in the `~/Desktop/docker-intro/peptides` you copied?
> 
> Would anything be different to align the 32 spike protein sequence found in file `spike_32.fa` within the `~/Desktop/docker-intro/covid` directory?
> > ## Solution
> >
> > Since we cannot run (for now) the container interactively we need to provide names for the input file and output result files. We can also select an alternate output format.
> > ~~~
> > $ docker run --rm --mount type=bind,source=${PWD},target=/data pegi3s/clustalomega --outfmt=clu -i /data/hglob.fasta -o /data/hglob_aligned.clu
> > ~~~
> > {: .language-bash}
> > For the larger set in `spike_32.fa` we could add `-v` (verbose) to obtain more information from `clustalo` as the software is computing the alignment. 
> > Nothing else needs to be fundamentally different. Just remember to add `--force` to run the same command again.
> >  ~~~
> > $ docker run --rm --mount type=bind,source=${PWD},target=/data pegi3s/clustalomega -v --outfmt=clu -i /data/spike_32.fa -o /data/spike_32_aln.clu
> > ~~~
> > {: .language-bash}
> > ~~~
> > Using 4 threads
> > Read 32 sequences (type: Protein) from /data/spike_32.fa
> > not more sequences (32) than cluster-size (100), turn off mBed
> > Calculating pairwise ktuple-distances...
> > Ktuple-distance calculation progress done. CPU time: 0.37u 0.01s 00:00:00.38 Elapsed: 00:00:00
> > Guide-tree computation done.
> > Progressive alignment progress: 64 % (20 out of 31
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Challenge: bypassing the entry point.
> How would you proceed to run this container interactively
> since adding `-it` has no effect due to the built-in entry point command?
> This aspect was explored within an earlier lesson chapter. 
> > ## Solution
> > We can bypass this issue if we add `-it` and `--entrypoint` followed by a suitable command.
> > To simply enter to container the command could be "/bin/sh" or even better with "/bin/bash". For example:
> > ~~~
> > $ docker run --rm -it --entrypoint "/bin/bash"  pegi3s/clustalomega
> > ~~~
> > {: .language-bash}
> > ~~~
> > root@1971dd7cc161:/#
> > ~~~
> > {: .output} 
> > From this point it is possible to explore the content of the container. For example the command `which clustalo` will provide the location of the program.
> > There is no `/data` directory as it was created "on the fly" in previous commands when 
> {: .solution}
{: .challenge}



## References

Brubaker, P. L., and D. J. Drucker. 2002. “Structure-function of the glucagon receptor family of G protein-coupled receptors: the glucagon, GIP, GLP-1, and GLP-2 receptors.” Recept. Channels 8 (3-4): 179–88. https://doi.org/10.3109/10606820213687.

Needleman, S. B., and C. D. Wunsch. 1970. “A general method applicable to the search for similarities in the amino acid sequence of two proteins.” J. Mol. Biol. 48 (3): 443–53. https://doi.org/10.1016/0022-2836(70)90057-4.

Park, Min Kyun. 2015. “Subchapter 17A - Glucagon.” In Handbook of Hormones: Comparative Endocrinology for Basic and Clinical Research, 129–31. Academic Press. https://doi.org/10.1016/B978-0-12-801028-0.00138-0.

Sievers, F., and D. G. Higgins. 2018. “Clustal Omega for making accurate alignments of many protein sequences.” Protein Sci. 27 (1): 135–45.

