---
title: "(extra) Using Docker with Github Actions"
teaching: 30
exercises: 0
questions:
- "How do I use Docker from Github Actions?"
objectives:
- "Generate Github.io pages using Pandoc"
- "Raise awareness of how Docker can be used in cloud services"
keypoints:
- "You can call any Docker image from a Github action"
---

> This lesson can be taught as a replacement of the chapter "Containers on the Cloud". Participants
> should have a little experience working with `git` and/or Github.
{: .callout}

# Building Github.io pages with Pandoc
Suppose you have a Github project with a README and would like to turn that into HTML for a
Github.io page. We take you through the process of creating a project on Github from scratch and
convert the README to HTML and upload it to a separate `gh-pages` branch.

Maybe it is best to first show what the end product looks like. (Instructor shows these pages live, preferably using your own repository)

We have a project ([example here](https://github.com/jhidding/readme-pages)) with a `main` branch that includes a README.

> ![](../fig/github-main-branch.png)
{: .callout}

We can use Pandoc to turn this README into a simple static website.

![](../fig/github-io-pages.png)
{: .callout}

If we switch to `gh-pages` branch in Github we can see where this page is hosted.

![](../fig/github-gh-pages-branch.png)
{: .callout}

Only a `index.html` and `.nojekyll` (that prevents Github from creating a Jekyll page). So how do we
set this up?

## Create a Github project
Create a github project with a short `README.md`, then clone it in a local shell.

~~~
git clone <your-repo-url>
cd <repo-name>
~~~

## Pandoc
Now that we have cloned the repository we can generate the HTML locally using Pandoc.

Pandoc is a universal document converter. It reads and writes between very many different file
formats, including many flavours of Markdown, HTML, LaTeX, Word, RTF, rst and many more. We use
it to generate static websites from Markdown.

~~~
docker run pandoc/core --version
~~~
{: .source}
~~~
Unable to find image 'pandoc/core:latest' locally
latest: Pulling from pandoc/core
f84cab65f19f: Pull complete
f95e84a31132: Pull complete
5d5ebbd90555: Pull complete
d084fb969d20: Pull complete
Digest: sha256:af1d118e3280ffaf6181af5a9f87ef0c010af9b5877053b750be33d0c47cc6ce
Status: Downloaded newer image for pandoc/core:latest
pandoc 2.12
Compiled with pandoc-types 1.22, texmath 0.12.1.1, skylighting 0.10.4,
citeproc 0.3.0.8, ipynb 0.1.0.1
User data directory: /root/.local/share/pandoc
Copyright (C) 2006-2021 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
~~~
{: .output}


We give Docker access to the contents of the local directory using the following command:

~~~
docker run -v $PWD:/tmp pandoc/core /tmp/README.md
~~~
{: .source}
~~~
<h1 id="readme-pages">readme-pages</h1>
<p>Example for generating Github.io pages from Readme with Pandoc.</p>
~~~
{: .output}

> Windows Powershell users should use `%cd%` in place of `$PWD` here.
> The output depends on the contents of the README.
{: .callout}

Here, `-v $PWD:/tmp` say as much as: take the directory at `$PWD` (or `%cd%` in Windows powershell)
and expose it inside the container as `/tmp`. Then `pandoc` can read the source file and convert it
to HTML. While this HTML is valid, it doesn't show the complete structure of a standalone HTML
document. For that we need to add the `--standalone` argument. Also we can redirect the output to
create a HTML file in the `build` directory.

~~~
mkdir -p build
docker run -v $PWD:/tmp pandoc/core /tmp/README.md --standalone --output=/tmp/build/index.html
~~~
~~~
[WARNING] This document format requires a nonempty <title> element.
  Defaulting to 'README' as the title.
  To specify a title, use 'title' in metadata or --metadata title="...".
~~~
{: .output}

To suppress the warning message use the suggested `--metadata title="..."` argument.
Inspect the output

~~~
cat build/index.html
~~~
{: .source}
~~~
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
... etc
~~~
{: .output}

## Github Actions
Github Actions is a cloud service for automating continuous integration and deployment. This means
we can have Github build our website and publish it on `github.io` automatically at every commit.

Go to the Github project page and click on "Actions". Because we have no active workflows yet, we
are taken immediately to a menu for creating a new one. We will skip the templates and click on
"set up a workflow yourself". The configuration format is YAML.

The first entry is the **name** of the workflow

~~~yaml
name: Deploy pages
~~~

Next we specify **when** this workflow is run. In this case: every time content is pushed to the
`main` branch

~~~yaml
on:
  push:
    branches:
      - main
~~~

Now we tell Github **what** to do.

~~~yaml
jobs:
  deploy:            # a free machine-readable name for this job
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo content
        uses: actions/checkout@v2
      - name: Prepare build environment
        run: |
          mkdir -p build
          touch build/.nojekyll
~~~

Now for the Docker bit:

~~~yaml
      - name: Run pandoc
        uses: docker://pandoc/core:2.12           # always specify a version!
        with:
          args: >-                                # multi-line argument
            --standalone
            --output=build/index.html
            --metadata title="Hello, Pandoc"
            README.md
      - name: Deploy on github pages
        uses: JamesIves/github-pages-deploy-action@4.1.0
        with:
          branch: gh-pages
          folder: build
~~~

We may recognize the command-line that we had previously. Notice that we don't need to specify the
`-v` flag. Github Actions arranges the Docker environment such that the files are in the correct
location. The last step uploads the `build` directory to the `gh-pages` branch.

Now we should enable Github Pages on this repository: go to the "Settings" tab and scroll down to
"GitHub Pages". There we select the root folder in the `gh-pages` branch. After a few (tens) of
seconds the page should be up.

# Reference material
- [Pandoc the universal document converter](https://pandoc.org)
- [Documentation on GitHub Actions](https://docs.github.com/en/actions)
- [GitHub Pages deploy action](https://github.com/marketplace/actions/deploy-to-github-pages)
- [Pandoc action example](https://github.com/pandoc/pandoc-action-example)

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment Dockerfile
 -->
{% endcomment %}
<!--  LocalWords:  bitbucket-pipelines.yml
 -->
