## Project title
Google fails us on the regular.  It's time to start scraping valuable content and keeping local repositories of useful information. 

## Motivation
I was writing a doc comparing stateful and stateless firewall capabilities.    **Scraping** a structured page where they had various DoS attacks enumerated in H2 headers was a better use of my time than copy paste.


## Code style
[Hijacked & tweaked from a Stack Overflow post.](https://stackoverflow.com/questions/69496293/how-to-extract-multiple-h2-tags-using-beautifulsoup)

## Features
Nothing about this is particularly complicated.  I'm building a hammer for scraping when I need it.

## Code Example
python3 ScrapeH2fromSite.py

## Installation
Make sure you have python3.10 or greater installed.  Don't forget to update pip
python3 -m venv venv #You venv, don't you bro?
source venv/bin/activate #You venv, don't you bro?
pip3 update 
pip3 install bs4
pip3 install requests
pip3 install requests
pip3 install bs4
pip3 install pandas
pip3 install lxml
python3 ScrapeH2fromSite.py
deactivate #You stopped the venv, bro!  Run "source venv/bin/activate" to bro down in your venv again!


## How to use?
Put the script in a directory you're going to work in.
create your venv.
install the dependencies.
run the script.
deactivate the venv.

In the future, just source venv/bin/activate and then run the script. 



## Credits
[a Stack Overflow post.](https://stackoverflow.com/questions/69496293/how-to-extract-multiple-h2-tags-using-beautifulsoup)

#### Anything else that seems useful

## License
A short snippet describing the license (MIT, Apache etc)

[CaptainMcCrank]
