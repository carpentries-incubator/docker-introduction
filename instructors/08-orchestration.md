---
title: Container Orchestration
teaching: 10
exercises: 0
questions: How can I deploy multiple containers?
objectives: Become aware of container orchestration services.
keypoints: Docker Compose, Kubernetes, and Docker Swarm are tools that can deploy
  multiple containers.
---

## Container Orchestration

Although you can certainly manage research workflows that use multiple containers manually, there are a number of
container orchestration tools that you may find useful when managing workflows that use multiple containers.
We won't go in depth on using these tools in this lesson but instead briefly describe
a few options and point to useful resources on using these tools to allow you to explore them yourself.

- Docker Compose
- Kubernetes
- Docker Swarm

:::::::::::::::::::::::::::::::::::::::::  callout

## The Wild West

Use of container orchestration tools for research workflows is a relatively new concept and so there
is not a huge amount of documentation and experience out there at the moment. You may need to search
around for useful information or, better still, contact your
[friendly neighbourhood RSE](https://society-rse.org/community/rse-groups/) to discuss what you want to do.


::::::::::::::::::::::::::::::::::::::::::::::::::

**Docker Compose** provides a way of constructing a unified workflow (or service) made up of multiple
individual Docker containers. In addition to the individual Dockerfiles for each container, you provide
a higher-level configuration file which describes the different containers and how they link together
along with shared storage definitions between the containers. Once this high-level configuration has been
defined, you can use single commands to start and stop the orchestrated set of containers.

- [Using Docker Compose for the Simple Deployment of an Integrated Drug Target Screening Platform](https://www.degruyter.com/view/journals/jib/14/2/article-20170016.xml)
- [Docker Compose Overview](https://docs.docker.com/compose/)

**Kubernetes** is an open source framework that provides similar functionality to Docker Compose. Its
particular strengths are that is platform independent and can be used with many different container
technologies and that it is widely available on cloud platforms so once you have implemented your workflow
in Kubernetes it can be deployed in different locations as required. It has become the de facto standard
for container orchestration.

- [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

**Docker Swarm** provides a way to scale out to multiple copies of similar containers. This potentially
allows you to parallelise and scale out your research workflow so that you can run multiple copies and
increase throughput. This would allow you, for example, to take advantage of multiple cores on a local
system or run your workflow in the cloud to access more resources. Docker Swarm uses the concept of
a manager container and worker containers to implement this distribution.

- [Docker Swarm Overview](https://docs.docker.com/engine/swarm/)


