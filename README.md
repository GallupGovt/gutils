# Gallup Utilities
## Introduction
This repo is like the land of misfit toys. Drop things in here that are multi-purpose or useful across a broad variety of situations.

## Use
For each utility provided, create a folder that contains everything needed. This repo does not exclusively need to be the domain of one language or another. This is not West Side Story here -- everyone in the land of misfit toys can play nicely. So, Python, stop squeezing and R, tell your scoundrel pirates to back off.

An example is the following. Say there was a utility that help identify whenever the word 'puppy' was found in a Gallup deliverable. Maybe the utility itself is called puppy. Well, then it would be perfect to have a folder called `puppy` to house everything associated with the puppy utility. Petty simple, right?

## Utilities
For each utility, __please add to the README file!__ Don't leave everyone ignorant and in the dark -- sharing is caring. Provide a description of what's actually happening!

### tinyurl
In the `tinyurl` folder, there is some basic functionality within Python to create tinyurls for web addresses. Basically, [bitly](https://bitly.com) does the same thing but has some pretty specific rate limits so having another option -- one without authentication as well -- can be handy.

To use, do the following:
```
$ python3 tinyurl/tinyurl.py -d tinyurl/test_links.csv
```

The `-d` parameter is the data that's passed in. This is assumed to be an arbitrarily large CSV with one required variable: `link`. It can have any other number of variables with no issues. The program will write the tinyurls to the same CSV as the variable `tinyurl` (so best not to have a variable named that...) and then save it to the same directory, by the same name, except with `_tiny` appended to the name and before the CSV extension.

This code comes with a test worksheet (called, creatively, `test_links.csv`). That's it, have fun!
