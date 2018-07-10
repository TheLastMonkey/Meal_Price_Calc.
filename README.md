#Meal Price Calculator


The **TL:DR** is this is a meal price calculating python script. and if that's all you want you can ignore two files named [lists in list.py] & [dics in list.py].
---
For the long version.  
I had recently started a healthy diet and exercise regimen and while I was exercising it occurred to me that it would be nice to know the price of each meal. While working out I mulled over the idea and figured I could probably come up with some python code to do that. Being very new to python and having tried to learn it on more than two occasions; I went about thinking through the logic of the code. So there were some obvious things that needed to be done.

So I knew there were some simple calculations to do which should be easy enough. Gather the name of the food and the cost as well as the weight preferably in ounces. and then the amount by weight that was used and then divide the cost of the item by the number of ounces it weighs to get the price per ounce. So then the price per ounce times the amount used should be the total cost for the item. So looping through every item and adding the total to the grand total should give me the information I want.

The first barrier for me was trying to think how I was going to create new items and how I was going to store the information. I was trying to think perhaps there's a way I can create new variables. But thinking through it there's no way I can make hard-coded variables just appear out of nowhere. I thought there must be a way to do this but I really don't know what approach to use.

My first thought to try and fix this was to use a list method of doing things. Because I know that lists can be appended added to and taken away so on and so forth so maybe I could just store variables within lists and then I realize that really what we're talking about here is an object. Each item is an object and python is a object based programming language so there must be a way.

I chicken scratched out the first iteration of the program using lists within lists. And this worked although it's quite tedious and far too complicated for what I'm trying to do. It's ugly and in the first file you can see where I was at with my understanding of python and how it progresses through the next two files.

It worked! It's ugly as hell but it worked! And I thought to myself well there's got to be a better way. I tried to remember that python is great like that because there's all kinds of ways to do the same thing. It's flexible so let's see if we can figure out something better. I started watching a lot of YouTube videos and once I stumbled across and really truly understood dictionaries I absolutely fell in love with them because it feels like pulling stuff out of a database and it is nice to be able to Define and add all kinds of information about an object or in this case of food item.

In the second file I took pretty much the same approach as before but this time I made a dictionary of each item and put that dictionary inside of a list. This felt so good and felt so right. I was pulling stuff out of a data structure that made sense to me. But somehow I had a feeling that they're must be more. I had heard Whispers and rumors about these things called classes and class methods and decorators and all sorts of little goodies that I knew nothing about.After doing a little research I figured this must be what I ultimately need to make my code better.

Learning classes took forever. As soon as I thought I understood it what I was trying to do with it, was complicating it for me and I just wasn't getting it. But then the beautiful and wonderful class method appeared and I figured out how I could take input from a user and pass it through my class initializing a new instance of an item. This was beautiful because it would just simply store all the information as a single object and I could refer to it and its individual attributes as such.

It was about this time that I discovered the word pythonic. Which my understanding was basically that there may be a hundred ways to do something in Python but there is usually a pythonic way of doing it which is cleaner simpler and even easier to read. I tried to become obsessed with figuring out the pythonic way of doing things. Learning how to simplify things and learning how to ask for forgiveness and not for permission, using try instead of if, and except instead of complete and total meltdown. 

I was learning that if something seems hard or it seems like I'm taking a complicated route to get to what I want, then there must be a built-in function or something that can get me there faster and with less lines of code. So I spent a lot of time investigating some of the built-in functionality of python and came to the realization that python really does a lot of the work for you. There's a lot happening on the back end that you don't have to bother with. 

Overall I think that rewriting the same script 3 times was actually one of the most productive learning experiences I've ever had. I've tried codecademy, I've tried a few other online type things and even looking at YouTube videos. Nothing seems to stick for very long. But making a project that means something to me, seems to make stuff stick and actually make me want to pick up the language and keep running with it.

Python has made problem solving into a fun game. It seems to have a nice easy learning curve and it's opened up a world of ideas for what I could do with it. Learning the pythonic way of doing things has taught me a broader lesson about figuring out the right way to do something so that you can do it efficiently and even make it look good. Look at me fangirling about a coding language.

Okay well if you would like to take a look at some code to go right ahead. I am completely open to constructive criticism. There may be no better way to learn.