## product name - I'm still Email From the Streets


### what is this?
a tool to alert you when there's an error with your code. complete with time stamps

### why am i making it?
i initially used a version of this code with a school project to send lecturers their daily class attendance and I decided it could be worth more so i have started to finder better ways to use it in my code to alert me of errors in live projects

![png of the working script](\email.png)
<center style=color:grey;>png of the working script</center>

### want to use it?
i one hundo support this. i also commented how you could have it send you text messages instead of emails. just find which ever one works best for your use case. setting up your google account 

* clone the project
```
git clone https://github.com/dibrinsofor/readme-template
```

* setup a ```config.py``` file like so:
```
USER= ""
PASSWORD= ""
```
* move this into your current project directory

* go to your https://myaccount.google.com/security

* enable two step verification and you will be issued an app password use that in the ```config.py``` file
* you can now go into ```emailfeedback.py``` to customise your error message and set what email or phone number you want to receive alerts on
```find the equivalent of these steps if you do not use gmail for your sending account```

### how it works
idk man,,, it just sends emails

#### technologies
this was built entirely with love on an eventful day with:

- Python
- smtplib
- ❤️

### what's coming next
i am not sure how much better you can make this, it's already pretty badass. sooooo probably nothing

### want to help make this better?
knock yourself out

[//]: # (So depending on use case, you may want to keep the documentation short. in that case you may not need to include the last two sections or you can)
