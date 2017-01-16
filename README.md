# twitLarge
Script for downloading the large version of twitter pictures if they exist.  
  
When a tweet has multiple images, usually only the normal size image is available. This script allows you to download the large version of every image in that tweet.  
  
### How to use:
Change the pictureDir to the directory you want the files to be downloaded.  

Call twitLarge.py with the link to the tweet with images you want to download as the second argument.
#### Example:
    $ ./twitLarge.py https://twitter.com/UserName/status/801849397843611648
Calling twitLarge.py alone will use whatever is currently in your clipboard as the address for download.
