Title: Key based login for ssh 
Date: 2015-03-22 17:49
Category: /var/log
Tags: Linux, Encryption, remote, ssh, Mac OS X
  
If you use ssh to connect to different hosts a lot you may find yourself wanting to either A) make it easier/faster or B) make it more secure. I am going to presume you jsut have the basic ssh familiarity and can perform your typical login no problem:
  
    $ ssh remoteuser@server.domain.tld 
  
When you do this (without any prior configuration) you will be asked for the user's password and then logged in after that is entered successfully.Presuming that this is a local server or otherwise has a very low security concern you might want to make it so you don't have to enter a password everytime. Not only is this just nice and easy, but it will also be conveneient it you want to be able to script an ssh command and not deal with needing the password. 
  
Of course the solution is not to disable the need for the password! Instead what you want to do is replace the password with a Key. By that I mean a Keyfile, you can basically think of it as a big password stored in a file. If 'ease of use' is not your concern and you are thinking more about making your server more secure then you can do the same thing using an encrypted Keyfile which will require a password to unlock!
  
So, the... KEY, to all of this is generating a Key. The ssh utility comes with a nice way to do this:

    $ ssh-keygen

Without any arguments this command will prompt you for the necessary info
    
    Enter file in which to save the key (/home/localuser/.ssh/id_rsa): 
    
First, it will ask where you want to store it. For using it with ssh for loging in purposes the default location (/home/localuser/.ssh/id_rsa) is perfect, So you can just press return.

    Enter passphrase (empty for no passphrase): 
Here you make the 'big' choice, do you want to make things easier or more secure. The choice is yours. For this example I am making things easier, and just pressing return again.
  
After that it will give you some output like this... (of course I am not using this key)

    Your identification has been saved in /home/localuser/.ssh/id_rsa.
    Your public key has been saved in /home/localuser/.ssh/id_rsa.pub.
    The key fingerprint is:
    5:25:2d:a7:ec:x6:a4:49:c8:c6:74:ee:f3:98:f9:a0 localuser@localhost
    The key's randomart image is:
    +--[ RSA 2048]----+
    |O+.   . o.. .    |
    |OO.. . +   o     |
    |E=. . o   o      |
    |o    o   . .     |
    |      o S=-.     |
    |     .           |
    |                 |
    +-----------------+

Notice that you have both a 'identification' and a 'public key', and of course remember where they are stored... Otherwise you do not event need to look at this other than to verify that it succeeded in creating a key. But I _really_ do like the randomart image... I think I might make something out of those just for fun.

Anyway, now you have your keys the only thing left to do is to tell your server about them. To do this you actually want to give your server your public key. We keep the private key 'identification' right where it is and you don't ever have to touch it really.

Now to give your server your public key there is a super easy way, using a utility that should be on an linux system:

    $ ssh-copy-id remoteuser@server.domain.tld

This command will automatically take your public key (id_rsa.pub) and append it to the .ssh/authorized_keys file on the remote server. This is super great, you can then immediately test it and you should be logged in without the server asking for the user password. If you chose to encrypt the key with a password then this is when ssh would ask for that new password to decrypt your private key.

One thing I've ran into, is that Mac OS X of course comes with ssh and the ssh-keygen utility, however it does not come with the ssh-copy-id utility and you may run into a few other systems that don't have this utility. You might be able to install it (on Mac OS X I would recomend: $ brew install ssh-copy-id), but sometimes that is not an option. So then what do you do? Manually add your public key to the authorized_keys file on the remote server!

    $ cat .ssh/id_rsa.pub | ssh remoteuser@server.domain.tld 'cat >> .ssh/authorized_keys'

And Voila! You should now be able to login to the remote server using your key file instead of the remoteuser password! You should be able to see that this redirects the output of your public key to ssh which then redirects it to the authorized_keys file. :)

One thing to note here is that the manual method does assume there already is a .ssh folder on the remote server. This may not be the case, and you would get an error returned indicating this. You can do some similar single command to make this directory first, like:

    # ssh remoteuser@server.domain.tld 'mkdir .ssh'

However I will warn you ssh is very picky about the persmissions of the .ssh folder and the authorized_keys file, of course this is a very good thing. :P Make sure the .ssh folder is set to 700 and the authorized_keys file should be set to 600. Because you may end up logging in to check this and fix it, there is not much of a good reason to use ssh to create the directory with one command. If these permissions are not set correctly, you will be asked for the remote user's password. To verify this issue check sshd log...

    # sudo grep authorized_keys /var/log/secure

If this is the issue you would see:

    sshd[14832]: Authentication refused: bad ownership or modes for file /home/remoteuser/.ssh/authorized_keys

Otherwise, if everything is working right, you will see:

    sshd[1422]: Accepted publickey for remoteuser from 123.456.789.01 port 4038 ssh2
