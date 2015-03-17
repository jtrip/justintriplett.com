Title: LUKS Encrypted Disk - Automounted
Date: 2015-03-16 13:49
Category: /var/log
Tags: Linux, Encryption, RHCSA


Today, I went to go take my RHCSA exam. However the kiosk shutoff while I was just getting started, so they told me I could come back in a couple of weeks....

In honor of that I figured I could make a post about one of the things I've had to study. Particularly because I found some of the documentation lacking, and a unfortunate typo in one of the most highly recomended books for the RHCSA and RHCE exams.

Here is a simple example requirment: 
Make a logical volume of 500MB, ext4, encrypted and automatically mounted on boot. Use UUID.

I love Jang's books but I have to say I found a point that might be a typo, just misleading, or just trouble due to the evolving shape of cryptsetup. In one his books he gives this example of a crypttab file:
    
    shared /dev/mapper/test none
    shared UUID=uuidnumber none
    
(use one or the other)

However from what I can tell, using the mapper is incorrect. Since I am using the UUID all over due to the vague demand, I tried to use the UUID of the mapper and that did not work, so instead I used the UUID of the encrypted device (say /dev/vda6) and that worked. This makes sense because the crypttab seems to be basically your luksOpen call and that has to refer to the encrypted device.

So here are my steps that worked:

prepare the disk and key  
  
    # dd if=/dev/urandom of=/dev/vda6
    # dd if=/dev/urandom of=/root/keyfile bs=1024 count=4
    # chmod 400 /root/keyfile
    # cryptsetup luksFormat /dev/vda6 -d /root/keyfile
    # cryptsetup luksOpen /dev/vda6 mapped-name -d /root/keyfile
    # mkfs.ext4 /dev/mapper/mapped-name

test    

    # mount /dev/mapper/mapped-name /my-mount
    # echo `date` >> /my-mount/testA
    # umount /my-mount

setup fstab    

    # dumpe2fs /dev/mapper/mapped-name | grep UUID | awk '{print $3}' >> mapperuuid
    # cp /etc/fstab ~/fstab.bak
    # echo -n UUID=`cat mapperuuid` >> /etc/fstab
    # echo -n " /my-mount    ext4    defaults    0 0" >> /etc/fstab

setup crypttab    

    # blkid /dev/vda6 | awk '{print $2}' >> /etc/crypttab
    # vi /etc/crypttab
    # sed -i 's/"//g' /etc/crypttab
    # sed -i '1s;^;mapper-name ;' /etc/crypttab
    # sed -i 's/$/ \/root\/keyfile/ luks/' /etc/crypttab
    # cat /etc/crypttab
    mapper-name UUID=LOL-OMG-WTF-BBQ /root/keyfile luks

reboot and verify    

    # init 6
    # wait
    # cat /my-mount/testA

And that's that!

Of course you don't have to use sed or awk, but I find it convenient instead of copy and paste and for listing the commands that will get the job done... and really practicing with awk and sed is great!

