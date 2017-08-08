Title:Blogging with GitHub Pages + Pelican (2)
Date: 2015-07-11 15:40
Modified: 2015-07-13 9:50
Tags: tech-iT 
Category: Blog/English
Slug: How_to_setup_blog_with_GitHub_Pages_Pelican(2)
Author: JIN Lin
[TOC]

This guide is to give you some pointers so that you can customise the blog to your personal taste and add necessary functions.

#### Change Theme 

Go to Github Repo and clone the theme or all [Pelican-Themes](Pelican-Themes)  down to your desktop:

Following the instructions as described in the README file. asically two steps,first `clone`:

	git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes    

then add the line to the `pelicanconf.py` file:

	THEME = "/home/user/pelican-themes/theme-name"
`theme-name` is the the theme you want to use, for example, my blog is using `elegant`.	


#### Add 'About' Page
The About page or CV page is the one page where you can share who you are and what you do. It is generally quite constant but you can update it from time to time. Pelican by default can convert the `pages` you create and copy to `output`. 

- create a `pages` folder under `content`

![static_paths](https://dl.dropboxusercontent.com/u/18094167/blogimages/staticpath.png)

- add the lines to `pelicanconf.py`

![pagesonmenu](https://dl.dropboxusercontent.com/u/18094167/blogimages/pageonmenue.png)

Now create an About file in Markdown format and put it under the `pages` folder. You will be able to generate the page. The same applies to `images`, pictures in which will be copied directly to the `output` folder with an associated link. To save space and reduce the load when committing to the repo, I store my pictures in `Dropbox` which provides a `Public` folder. It locates each item a unique public identifier (URL):

![dropbox public](https://dl.dropboxusercontent.com/u/18094167/blogimages/dropboxpublic.png)


#### Relate to Custom Domain 
Assume you have already bought a domain from somewhere, e.g. GoDaddy for my domain.

Now create a CNAME file and put under `content/extra` in your local blog directory. It should contain your domain address only. 

![cnmae](https://dl.dropboxusercontent.com/u/18094167/blogimages/cname.png)

And then add the following lines to your `pelicanconf.py`

![cname path](https://dl.dropboxusercontent.com/u/18094167/blogimages/cnamepath.png)

Then configure the DNS settings on your DNS provider.

Point to IP of server for Github Pages 

![ipdns](https://dl.dropboxusercontent.com/u/18094167/blogimages/CNAMEDNS.png)


Related to the page address provided by GitHub. 


![ipdns](https://dl.dropboxusercontent.com/u/18094167/blogimages/IPDNS.png)


After commit CNAME files to the remote repo, you should see this: 
![settingssite](https://dl.dropboxusercontent.com/u/18094167/blogimages/settingssite.png)

GitHub has provide a [guide](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/) for setting your custom domain as well. 

#### Add 'Comments'
Pelican does not provide the function for comments, the most popular third party tool is `Disqus`. If you need this function, register an account with them and do the following settings. 

At Disqus follow the instructions and get a `website shortname`
![disques](https://dl.dropboxusercontent.com/u/18094167/blogimages/disqus.png)

In local configure file, add the following line: 

	DISQUS_SITENAME = 'linnus'
	 

#### Add 'Google Analytics'

Google Analytics is simply powerful. You use it, you know it. You can get every bit of information about your website's performance. It is good for SEO. I haven't gone into that step yet. Take a look first.
![](https://dl.dropboxusercontent.com/u/18094167/blogimages/google%20analytics.png =712x400)

Create an account with Google Analytics, get an `tracking id` and add it to configure file:

	GOOGLE_ANALYTICS = 'your tracking id'
	
You can also use other services provided by Google such as [Webmaster](http://www.google.com.sg/webmasters/) or [Custom search engin](https://cse.google.com/cse/). The theme I am using actually provides a great search using `tupe_search` plugin. I found `Categories` `Tags` are pretty enough to navigate around so I disabled the search function.  


#### More

Subjected to your specific needs and your skills in HTML/CSS/JS, you can probably make a lot more enhancement. I want to keep my blog full functioned yet clean and simple. It requires a lot more learning. Stay hungry. 
