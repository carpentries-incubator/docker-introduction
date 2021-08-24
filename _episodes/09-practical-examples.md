---
title: "Practical Examples"
teaching: 20
exercises: 0
questions:
- "What are examples where docker can be applied in a research setting?"
objectives:
  - Use docker in combination with real research software
keypoints:
  - Docker can be a solution to include the legacy script into your workflow with minimum effort.
  - You can use intermediate files to let different Docker containers talk to each other.
---

> ## Python Version Conflict
>
> You are a social science researcher and are trying to establish how many people in a list are below the allowed drinking age.
> You are provided with a list of names and the corresponding birthdates.
>
> A former PhD student already did the first part and wrote a program to convert birthdates into the current age of the people. Unfortunately it was written in Python2.7 and there is no way to upgrade  it to Python3 (technically there is, but psssst).
>
> As you are one of the best and brightest you have written a script to check the current age of people against the legal drinking age and output all people who are below it. You wrote it in Python 3.6. Your professor or boss and the rest of the group use python 3.3 in the work and cannot use your useful piece of software.
> 
> Create two docker containers and provide your colleagues with a working docker workflow.
>
>### Preparation work
>
> Before you start with a solution, you need to download the files you need:
>
> - the old script [convertbirthdaytoage.py](/code/convertbirthdaytoage.py) written by the former PhD in Python 2.7;
> - the new script [checkdrinkinglimit.py](/code/checkdrinkinglimit.py) you wrote in Python 3.6;
> - the [birthday data](/data/data_birthday.csv) required for this study.
>
> To simplify our workflow, let's put them all in the same working directory:
>
> ~~~
> $ cd <your-working-directory>
> $ ls .
> ~~~
> {: .language-bash}
> 
> ~~~
> checkdrinkinglimit.py  convertbirthdaytoage.py  data_birthday.csv
> ~~~
> {: .output}
> 
> You can first try to run them inside docker containers, afterwards try creating your own containers which nicely package this workflow. (Create one container for each file. You might want to look up the `ENTRYPOINT` instruction for the second task)
> > ## Solution
> > Now let's think of our problem: we need to use the old script `convertbirthdaytoage.py` to get the age of people, and use the new script `checkdrinkinglimit.py` to find out if anyone is under the drinking age. Neither of the scripts is 100% compatible with your colleagues' Python 3.3 environment. To make sure they have a smooth workflow, we need to run the old script under Python2.7 environment, and the new script under Python 3.6.. For simplicity each script has a `-h` flag for some help. Input and output to scripts are handled via `-i` and `-o` command line parameters.
> >
> > From what we have learnt, we know `DockerHub` provides images for both environments we need. What we need to do is to pull them down:
> >
> > ~~~
> > $ docker pull python:2.7
> > $ docker pull python:3.6
> > ~~~
> > {: .language-bash}
> >
> > To verify, we can run:
> >
> > ~~~
> > $ docker image list
> > ~~~
> > {: .language-bash}
> >
> > After we have the images ready, we can run  `convertbirthdaytoage.py` to get the age of people:
> > ~~~
> > $ docker run -v $(pwd):/mnt -w /mnt python:2.7 python convertbirthdaytoage.py -i data_birthday.csv -o ages.json
> > ~~~
> >{: .language-bash}
> >
> > Here we used the `-v $(pwd):/mnt` to mount our working directory to the Docker container. `-w /mnt` is used to specify the working directory within the Docker container. Now if we check our current working directory:
> > ~~~
> > $ ls .
> > ~~~
> > {: .language-bash}
> > 
> > ~~~
> > ages.json  checkdrinkinglimit.py  convertbirthdaytoage.py  data_birthday.csv
> > ~~~
> > {: .output}
> > A new file `ages.json` has been created, which contains the ages of all people. Now we can execute `checkdrinkinglimit.py` using another Docker image:
> > ~~~
> > $ docker run -v $(pwd):/mnt -w /mnt python:3.6 python checkdrinkinglimit.py -i ages.json
> > ~~~
> > {: .language-bash}
> > ~~~
> > Daria is not allowed to drink because they are only 6 years old!
> > Sherilyn is not allowed to drink because they are only 8 years old!
> > Clint is not allowed to drink because they are only 14 years old!
> > Val is not allowed to drink because they are only 13 years old!
> > ~~~
> > {: .output}
> > Congrats! Now we find all the people who are under the drinking age!
> > 
> > Now we can make the whole thing even better, so far we only used containers to run our scripts in, but we can also create new containers our colleagues can use. It is good practice to create a folder for each dockercontainer. Copy the respective scripts to the folders
> > ~~~
> > $ mkdir convertbirthdaytoage
> > $ cp convertbirthdaytoage.py convertbirthdaytoage
> > $ mkdir checkdrinkinglimit
> > $ cp checkdrinkinglimit.py checkdrinkinglimit
> > ~~~
> > {: .language-bash}
> > The Dockerfiles for the respective folders are then
> > ~~~
> > FROM python:2.7
> > COPY convertbirthdaytoage.py /convertbirthdaytoage.py
> > ENTRYPOINT ["python2","/convertbirthdaytoage.py"]
> > ~~~
> > ~~~
> > FROM python:3.6
> > COPY checkdrinkinglimit.py /checkdrinkinglimit.py
> > ENTRYPOINT ["python3","/checkdrinkinglimit.py"]
> > ~~~
> > The `ENTRYPOINT` instruction allows you to configure a container that will run as an executable. This allows arguments to be passed to the entry point, i.e., `docker run <image> -d` will pass the `-d` argument to the entry point. You can override the `ENTRYPOINT` instruction using the `docker run --entrypoint` flag.
> > Create the two containers using `docker -build` and run them. 
> > If you want you can upload them to dockerhub as well.
> {: .solution}
{: .challenge}

## Using a dockerfile as mybinder environment
_Exercise based on example from [towardsdatascience](https://towardsdatascience.
com/animations-with-matplotlib-d96375c5442c)_
[Mybinder](https://mybinder.org/) is a website that can turn your git repository with jupyter notebooks into an 
executable environment. This makes it easy for others to reuse your code.

For many usecases, it will be enough to supply a `requirements.txt` file in your git repo to 
install the dependencies you need. However, in some more complicated cases this python environment 
will not be enough, for example if your python code calls software that has not been written in python.

Consider the following case: 

A volcanologist has recently acquired some new height data on the volcano she is studying. She 
has a notebook where she parses the data and displays it as an animated 3d density plot.

To make her research reproducible she wants to make her workflow available in mybinder. However, 
she uses some additional software that is not in the standard mybinder environment to convert 
her animation into a video file.






Example mybinder dockerfile:
```dockerfile
FROM continuumio/miniconda3

ARG NB_USER=jupyter

RUN adduser --disabled-password $NB_USER
RUN apt update -y && \
    apt install -y ffmpeg && \
    pip install jupyter

USER $NB_USER
WORKDIR /home/$NB_USER

CMD ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0"]
```

Let's break it down
- `FROM continuumio/miniconda3`: A base image that comes with a small number of Python packages 
preinstalled
- `ARG NB_USER=jupyter`: Binder requires