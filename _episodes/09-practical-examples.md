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

> ## Python Workflow
>
> You are a social science researcher and are trying to establish how many people in a list are below the allowed drinking age.
> You are provided with a list of names and the corresponding birthdates.
>
> A former PhD student already did the first part and wrote a program to convert birthdates into the current age of the people. Unfortunately it was written in Python2.7 and there is no way to upgrade  it to Python3 (technically there is, but psssst).
>
> As you are on of the best and brightest you have written a script to check the current age of people against the legal drinking age and output all people who are below it. You wrote it in Python 3.6. Your professor/boss/overlord and the rest of the group use python 3.3 in the work and cannot use your critical piece of software.
> 
> Create two docker containers and provide your colleagues with a working docker workflow before they get angry!
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
>
> > ## Solution
> > Now let's think of our problem: we need to use the old script `convertbirthdaytoage.py` to get the age of people, and use the new script `checkdrinkinglimit.py` to find out if anyone is under the drinking age. Neither of the scripts is 100% compatible with your colleagues' Python 3.3 environment. To make sure they have a smooth workflow, we need to run the old script under Python2.7 environment, and the new script under Python 3.6. 
> >
> > From what we have learnt, we know `DockerHub` provides images for both environments we need. What we need to do is simply pulling them down:
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
> > $ docker run -v $(pwd):/mnt -w /mnt python:2.7 python /mnt/convertbirthdaytoage.py
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
> > $ docker run -v $(pwd):/mnt -w /mnt python:3.6 python /mnt/checkdrinkinglimit.py
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
> {: .solution}
{: .challenge}