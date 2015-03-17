Title: Re: Pelican
Date: 2014-11-21 13:49
Category: /var/log
Tags: Python, Pelican, website, #ItsATrap, Static Site Generators


If you happen to have seen this site sometime durring the first 3 quarters of 2014 you would have noticed a change. Specifically from a CherryPy-BootstrappedSlate-website devoid of any content, to the content rich (hah) flat bootstrapped site which is being produced with Pelican now. Maybe you didn't notice these things, and maybe that is for the better. :)

I've been trying to practice my python foo and thought it would be good to post things to a website, partially for motivation and also for sharring. However I found my self in a 'Chicken or the Egg' problem I ended up using as a procrastination excuse. So I thought I would explain so you don't fall into the same trap.

It basically went like this:  
A) I want to get better at python.  
B) I should have a website for this.  
C) My website should use python.  
D) I do not currently have the specific python skills to make the website I want, from scratch.  

I looked into all the popular frameworks for making websites in python and actually learned a lot about them and when they would be used best. It took a lot of digging before I realized I didn't need something big and complex, and the simple features were more important to me. CherryPy looks like a very fun framework to build with, but I didn't want to build a system to just make posts, at least not yet. I wanted to write articles in markdown. I wanted tags on posts and pages, also different categories for posts. Of course I wanted Bootstrap or Foundation to makes things wonderfull, but I could add that to plain html... There was brief period where I considered going back to the stone age. I remember writting plain html by hand, it was fine... but then I wanted to dedupe my navigation code so I would use php includes... cough php? oh goodness no, I'm not going back to that.

So then I took a look at Static Site Generators, there a few great projects for that in Python, Ruby or whatever probably even erlang. I took a look at Hyde (Python, but inspired? by Jekyll in Ruby) and it looked pretty good, but I heard documentation was lacking, and I saw a post about how awesome Pelican is so I decided to investigate that further.

Basically, (and to prevent this post from getting much longer) Pelican is as amazing as they say it is. There is a very good amount of documentation, the configuratiuon is sane, and there are a lot of other people using it and keeping their themes in github. It has everything I needed and still uses python so extending it in some way will be a fun project one of these days.

Static site generation was right under my nose the whole time. I have a bad habbit of looking past the obvious and chasing after other things. When I get tired of the chase, I can't even remember why I didn't just go with the easy route right in front of me. It is all a learning experience and I certainly don't regret it. I'm just glad for those times when I get tired, take a step back, and re-evaluate.
