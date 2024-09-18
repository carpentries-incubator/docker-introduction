---
title: Learner profiles
---

Here we provide some example profiles of people who represent the target
audience for this lesson. These example scenarios are designed to give you an
idea of the different reasons people might want to learn Docker and the types
of roles that they might hold.

The profiles provided here and the individuals described are fictional but they
represent the lesson developers' experiences of teaching members of the
research community about Docker and other container technologies over a period
of several years. They also incorporate feedback from instructors involved in
pilot runs of this course.

Note that containers are applicable across a wide range of use cases within the
research and High Performance Computing communities. These profiles are not
intended to cover all areas but rather to offer some examples of the types of
roles people learning this material might hold and their reasons for learning
about containers.

## Individual learner profiles

***Nelson is a graduate student in microbiology.*** They have experience in running Unix shell
commands and using libraries in R for the bioinformatics workflows they have developed.
They are expanding their analysis to run on 3000 genomes in 200 samples and they have
started to use the local cluster to run their workflows. The local research computing
facilitator has advised them that Docker could be useful for running their workflows on
the cluster. They'd like to make use of existing containers that other bioinformaticians
have made so they want to learn how to use Docker. They would also be interested in
creating their own Docker images for other lab members and collaborators to re-use their
workflows.

***Caitlin is a second year undergraduate in computer science examining Docker for the first
time.*** She has heard about Docker but does not really know what it achieves or why it is
useful. She is reasonably confident in using the Unix shell, having used it briefly in
her first year modules. She is keen to find jump-off points to learn more about technical
details and alternative technologies that are also popular, having heard that container
technologies are widely used within industry.

***Xu, a materials science researcher, wants to package her software for release with
a paper to help ensure reproducibility.*** She has written some code that makes use of a
series of Python libraries to undertake analysis of a compound. She wants to (or is
required to) make her software available as part of the paper submission. She
understands why Docker is important in helping to ensure reproducibility but not the
process and low-level detail of preparing a container and archiving it to obtain a DOI
for inclusion with the paper submission.

***Bronwyn is a PhD student running Python/R scripts on her local laptop/workstation.***
She is having difficulty getting all the tools she needs to work because of conflicting
dependencies and little experience with package managers. She is also keen to reduce
the overhead of managing software so she can get on with her thesis research. She has
heard that Docker might be able to help out but is not confident to start exploring
this on her own and does not have access to any expertise in this within her local
research group. She currently wants to know how to use preexisting Docker containers
but may need to create her own containers in the future.

***Virat is a grad student who is running an obscure bioinformatics tool (from a GitHub
repo) that depends on a number of other tools that need to be pre-installed .*** He wants to be able to
run on multiple resources and have his undergrad assistant use the same tools. Virat
has command line experience and has struggled his way through complex installations
but he has no formal CS background - he only knows to use containers because a departmental
IT person suggested it. He is usually working from a Windows computer. He needs to
understand how to create his own container, use it locally, and train his student
to use it as well.

## Group profiles

In addition to our individual learner profiles above, we also look at three
more general groups who may want to learn about containers. This is intended to
help you get a perspective of the different types of skills and expertise that
learners engaging with this material may have:

- **Researchers:** For researchers, even those based in non-computational domains, software
  is an increasingly important element of their day-to-day work. Whether they are writing
  code or installing, configuring and/or running software to support their research, they
  will eventually need to deal with the complexities of running software on different
  platforms, handling complex software dependencies and potentially submitting their code and data to
  repositories to support the reproduction of research outputs by other researchers, or to
  meet the requirements of publishers or funders. Software container technologies are valuable
  to help researchers address these challenges.

- **RSEs:** RSEs -- Research Software Engineers -- provide software development, training
  and technical guidance to support the development of reliable, maintainable, sustainable
  research software. They will generally have extensive technical skills but they may not
  have experience of working with or managing software containers. In addition to working with
  researchers to help build and package software, they are likely to be interested in how
  containers can help to support best practices for the development of research software
  and aspects such as software deployment.

- **Systems professionals:** Systems professionals represent the more technical end of
  our spectrum of learners. They may be based within a central IT services environment
  within a research institution or within individual departments or research groups.
  Their work is likely to encompass supporting researchers with effective use of
  infrastructure and they are likely to need to know about managing and orchestrating
  multiple containers in more complex environments. For example, they may need to provide
  database servers, web application servers and other services that can be deployed
  in containerized environments to support more straightforward management, maintenance
  and upgradeability.
