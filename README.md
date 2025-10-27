Sometimes you need to screenshot stuff. A lot of stuff. In order to save lots money.
coordstool.py is just to help me find locations on the screen. Yes this could've been added into the main program and automated, but this would lead to slowing down the time it takes to get the program started and just was not worth implementing at the time. 

The main program does as follows:
- Opens an initial link for sign in purposes
- Once logged in, automatically redirects to the actual site
- where the main loop begins
- Find the element that holds the page number and extract the value
- Wait until the content is fully loaded
- Screenshot the content
- Turn page
- Catch any errors and return if errors
- Otherwise add every screenshot to a pdf file


Additional notes:
It's unlikely I continue this project until next semester, but until then here are some things I would need to work on:

known issues:
- It should really wait for the page to load first before trying to find page number. I don't know why I put it the other way around
- Lacking in portability
  - Too many hard coded values
- Setup needs to be more automated, it still requires a little bit of human intervention
- It would be nice to be able to input a list of links and all of them get processed
- Add the ability to edit a few pages
- Some pages will repeat

