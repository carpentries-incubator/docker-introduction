---
title: "Examples of Using Container Images in Practice"
teaching: 20
exercises: 0
questions:
- "How can I use Docker for my own work?"
objectives:
- "Use existing container images and Docker in a research project."
keypoints:
- "There are many ways you might use Docker and existing container images in your research project."
---

Now that we have learned the basics of working with docker images and containers,
let's apply what we learned to an example workflow.

You may choose one or more of the following examples to practice using containers.

## Jekyll Website Example

In this [Jekyll Website example](../_extras/e02-jekyll-lesson-example), you can practice
rendering this lesson website on your computer using Jekyll in a Docker container.
Rendering the website in a container avoids a complicated software installation; instead of installing Jekyll and all the other tools needed to create the final website, all the work can be done in the container.
Additionally, when you no longer need to render the website, you can easily and cleanly remove the software from your computer.

## GitHub Actions Example

In this [GitHub Actions example](../_extras/e01-github-actions), you can learn more about
continuous integration in the cloud and how you can use container images with GitHub to
automate repetitive tasks like testing code or deploying websites.

<!--- Placeholder for 
## Geospatial Example

Ask @mkuzak to make a PR to add extra for <https://github.com/escience-academy/docker-gdal-demo>

-->

Do you have another example of using Docker in a workflow related to your field?  Please [open a lesson issue] or [submit a pull request] to add it to this episode and the extras section of the lesson.


{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints _episodes_rmd CODE_OF_CONDUCT.md aio.md
 -->
<!--  LocalWords:  CONTRIBUTING.md LICENSE.md index.md reference.md
 -->
<!--  LocalWords:  README.md setup.md _config.yml webserver srv
 -->
<!--  LocalWords:  jekyll x86_64-linux-musl favicons github.io
 -->
<!--  LocalWords:  links.md _episodes_rmd _config.yml endcomment
 -->
{% endcomment %}


[submit a pull request]: https://github.com/carpentries-incubator/docker-introduction/pulls
