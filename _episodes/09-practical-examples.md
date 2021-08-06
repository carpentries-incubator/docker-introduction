---
title: "Practical Examples"
teaching: 20
exercises: 0
questions:
- "What are examples where docker can be applied in a research setting?"
objectives:
  - Use docker in combination with real research software
keypoints:
-  
---

You are a social science researcher and are trying to establish how many people in a list are below the allowed drinking age.
You are provided with a list of names and the corresponding birthdates.

A former PhD student already did the first part and wrote a program to convert birthdates into the current age of the people. Unfortunately it was written in Python2.7 and 
there is no way to upgrade it to Python3 (technically there is,but psssst). 

As you are on of the best and brightest you have written a code to check the current age of people against the legal drinking age and output all people who are below it. You wrote it in Python 3.6. Your professor/boss/overlord and the rest of the group use python 3.3 in the work and cannot use your critical piece of software. 

Create two docker containers and provide your colleagues with a working docker workflow before they get angry!
