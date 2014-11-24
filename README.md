CSE-360
=======
Operating System:
    This document assumes you are operating on a clean install of Ubuntu Server 14.04 LTS, and has not been tested on any other versions or distributions.  The software may function, but deviations from the instructions below will likely be required and functionality cannot be guaranteed.  Complete the base install of the OS.  No special selections are required at this stage.

    Packages:
    Before we can run the server software, we must install supporting software as follows.  Become root and execute the following commands.  First, we install the GUI for Ubuntu on top of the server install.  Then, we reboot to make sure that the GUI is fully functioning.  Note that these package installs may take a while, and that this is a perfect opportunity to grab a coffee (or alternative beverage).

# apt-get install ubuntu-desktop
# reboot
# apt-get install build-essential python-pip sqlite

Once the package installs are complete, we download the repository from the git.  Once the download is complete, return to the terminal, and change to the repository directory.  Note that your path will differ from the example below.  We then use pip to install some dependencies and move the static directory alongside CSE-360.

# cd /home/nash/CSE-360
# pip install -r /image_space/requirements.pip
# mv static ..

Now that our dependencies are in order, we sync the database to prepare the server to run.  When prompted, create the root user with the password “testing”.
# python manage.py syncdb
# python manage.py runserver

Note:  In order for the site navigation menu as well as event listings to be populated, they must be configured from the Django admin webpage.
    Admin Page Configuration:

    Browser Navigation:
        If an audio-visual explanation of these instructions is preferred, please go to http://youtu.be/y25mUueq22k.  The same steps will be covered below in a written format.
    Open the browser of your choice, and enter the IP Address of the server, followed by a colon, followed by the port number into the address bar.  In the example covered by this document, you would enter the following.

127.0.0.1:8000

Unless credentials have already been procured, click the underlined “here” to create a new account.  The user will now be prompted for a username, password, optional picture, and a valid email address.  Populate each field as appropriate.  Note that the username must consist of letters and numbers, and must be unique.  Similarly, the password must be alphanumeric and must match in both password fields.  The profile picture is optional, but if desired, select an image from your machine to upload.  The server will check to make sure that the file is an image, so do not try to upload anything else, such as a PDF.  It simply will not work.  Now, enter a valid email address in the format shown below, then click submit.

<NAME>@<DOMAIN>.<EXTENSION>

If all fields have been populated correctly, the user will be created and you may now login.  When attempting to log in, the user will be redirected to the homepage if credentials are valid, or to an alternative page if either the username or password is incorrect.

Once the user has reached the homepage, a listing of available tickets is shown.  Once the user has finished their business, they may log out or simply close the browser.

    Unit Testing:

    Functional Testing:
