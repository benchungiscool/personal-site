# I <3 htmx

I've started to use htmx to render posts. I'm doing this by rendering a markdown post into html using python, which I directly inject into htmx with an Ajax event on page-load. 

This has been something that I didn't realise I wanted since I started hosting my own website. Not that I'm against using React or other JS frameworks, but wrapping megabytes of dependencies for a site like this, which I always wanted to be lean and load quickly seemed like a huge waste. This method only involves importing an 18kb dependency that enables exactly what I want to do.

Now to support all the markdown features in CSS!

