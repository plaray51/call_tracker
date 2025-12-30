# Call Tracker

A simple desktop app for tracking paid calls.

Each call  
Pays 3.67 dollars  
Counts as 10 minutes of work  

The app tracks  
Total calls  
Money earned  
Time worked shown as hours and minutes  

It also supports automatic call tracking using an on screen image.

## Features

Manual add and remove calls  
Manual edit of total calls  
Automatic saving and loading  
Time shown as hours and minutes  
Optional auto increment when a recording indicator disappears  
Visual flash when a call is auto counted  

## How auto tracking works

Place an image named recording.png in the same folder.  
When that image is visible on screen the app treats it as an active call.  
When the image disappears the app automatically adds one call.  

You can turn this on or off using the checkbox in the app.

## Important warning about short calls

If a call ends before 2 minutes it will still be counted automatically.  
If a call drops or ends early you should manually remove that call using the Remove Call button.  

The app does not currently check call duration.  
Always review your total calls if a call ends very quickly.

## Requirements

Python 3  
The libraries listed in requirements.txt  

## Install dependencies

Run this in the project folder

```bash
py -m pip install -r requirements.txt
