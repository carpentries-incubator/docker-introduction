---
title: "Creating containers in the cloud"
teaching: 20
exercises: 0
questions:
- "How can I create Docker containers in the cloud?"
objectives:
- "Demonstrate how to effect creation of a container from the Docker image in the cloud."
- "Gain an initial experience of the container functionality provided by the Bitbucket repository storage service."
keypoints:
- "You can create Docker containers on cloud computing resources just using a web browser."
- "Bitbucket is an online repository storage service that can create Docker containers to perform computation in response to files changing in your repositories."
---
### Containers can be created on cloud computing platforms
There are lots of ways containers can be created on cloud computing platforms (a.k.a., "in the cloud"). Most commercial cloud providers now offer a container hosting service that will connect to the Docker Hub in order to fetch the container images that you specify, and charge for the time and resources that the containers use. The container hosting will usually be significantly cheaper than full virtualisation services that might be on offer.

Note also that most cloud providers will give you sign-up credit that you can use for free after you first create your account.

For this lesson, though, we instead use an excellent software project repository platform, Bitbucket, that allows users a monthly quota of minutes for which containers of your choice can be run. Bitbucket allows containers to be created in response to the modification of files within your software project.

> ## There are many excellent sites for storing public software repositories
> - Note that Bitbucket, GitHub and GitLab all achieve similar functions.
> - Bitbucket offers container-based features that are easier to get at than the equivalent functions in GitHub, although GitHub will soon catch up when they release their GitHub Actions functionality publicly.
{: .callout}

### Running a container in the cloud, using your Bitbucket account

Because the ability to use the `git` version management tool is not a prerequisite of this session, we will use Bitbucket in an atypical manner. However we should still be able to clearly see Bitbucket's cloud servers running a container of your choice, under your control.

- Open a web browser window and visit <https://bitbucket.org/>.
- Log into your Bitbucket account.
- Click the "create" (or just "+", if the menu is not expanded) button near the top-left of the page.
- In the Create menu that appears, choose "Repository".
- You will need to fill in the "Create new repository" form:
    - You need to choose a Repository name: I am going to choose "use-my-container", and you are welcome to do the same.
    - I unchecked the "This is a private repository" button, to make my repository public
    - All of the other defaults should be OK, including the advanced settings
- Activate the "Create repository" button
- A page with heading "Let's put some bits in your bucket" appears, since the aim of Bitbucket is to host repositories of code and data... but we will ignore this workflow, and instead, you should click "Pipelines" in the second menu in from the left.
- A page that promotes Bitbucket Pipelines should appear. This page also notes that you have 500 free minutes per month (for a free account): this is minutes of time that your containers are allowed to run, on Bitbucket's cloud servers. You just need to click the "Start using Pipelines" link in the bottom-centre.
- Under the "Choose a language template" heading that appears, choose the "Other" pull-down menu, and select "Other" from the bottom of that list.
- If an example "bitbucket-pipelines.yml" file appears, then all is well, and you can continue with the next section.

### Edit your repository's `bitbucket-pipelines.yml` file through the web

You should be looking at a web-based text editor that is headed "bitbucket-pipelines.yml". The one that I see has 13 lines, all of which are numbered on the left of the text editor.

Bitbucket Pipelines allow you to specify software tools to run, for example, in response to files being changed in your Bitbucket projects. The Bitbucket servers run your software tools within Docker containers, and thus Bitbucket Pipelines can specify Docker images to fetch from the Docker Hub.

Change your repository's `bitbucket-pipelines.yml` file to be similar to the following example, but note that you need to replace the Docker Hub user ID (alice in example) with yours. Also, ensure that your indentation steps in line-by-line, the language being used (YAML) gives significance to the indentation of the lines.
~~~
image: alice/my-container

pipelines:
  default:
    - step:
        script:
          - /bin/cat /root/my_message
~~~

Click the "commit file" button. After you commit your `bitbucket-pipelines.yml` file, the Bitbucket Pipeline will download the Docker image you specified from the Docker Hub, and display the progress of the computations it runs.

When using the `docker run` command (as you have done previously), the container takes some default actions after being created, which are specified in your Dockerfile (e.g., the `CMD` line). Bitbucket Pipelines disable these default actions, instead using the commands listed under the "script:" section in your `bitbucket-pipelines.yml`. Note that hyphens at the same indentation level are treated as an itemised list. There is only one item in our `script:` list, namely the command `/bin/cat /root/my_message`.

If the pipeline runs successfully, a green heading containing a tick icon will be shown near the top of the page. On the right-hand-side of the page, you should see the following headings:
- Build step
- `/bin/cat /root/my_message`
- Build teardown

Click on the `/bin/cat /root/my_message` heading, and you should see that your custom message was shown.

While it is difficult to argue that this container achieves important computational work, you have, nonetheless, demonstrated that Docker images that you create can be run on the cloud. Moreover, many cloud organisations that are willing to create containers from your images will offer generous allowances to you to do so, even if you only have a free account.

{% comment %}
Going further section
### Digital Ocean hosting

Cloud providers such as Digital Ocean
{% endcomment %}

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints links.md endcomment Dockerfile
 -->
{% endcomment %}
<!--  LocalWords:  bitbucket-pipelines.yml
 -->
