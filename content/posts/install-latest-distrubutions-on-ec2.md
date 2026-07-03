---
title: 'Install latest distrubutions on EC2'
date: 2013-07-04T14:55:00.000+08:00
draft: false
url: /2013/07/install-latest-distrubutions-on-ec2.html
---

EC2 typically has slightly older version of software (Amazon AMI, i use that most often. Other linux distributions are likely to be similar but the repos folder is likely to be different). I like to be cutting edge, (but not so much bleeding edge).

  

Here is how you can use external repos to install the latest distributions. Most of the LAMP stack stuff is available in this repo.

\-- 

cd /etc/yum.repos.d

sudo wget [http://rpms.famillecollet.com/enterprise/remi.repo](http://rpms.famillecollet.com/enterprise/remi.repo)

sudo vim remi.repo 

\- change all occurrences of '$releasesever' to '6' 

        - $releasever contains the string 'latest' but that doesnt seem to work, so we manually put the latest server available

        - this is where it gets the repos from, so you can figure out the latest server version available : [http://rpms.famillecollet.com/enterprise/6/remi/mirror](http://rpms.famillecollet.com/enterprise/6/remi/mirror)

  

Then go here: [http://rpms.famillecollet.com/enterprise/6/remi/x86\_64/](http://rpms.famillecollet.com/enterprise/6/remi/x86_64/)

  

wget <path to repo you want>

sudo yum --enablerepo=remi install <path to downloaded repo>

  

So much easier than building from source.. which is the other altearnative.