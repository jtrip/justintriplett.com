Title: Make your own service script for autostart and management
Date: 2015-04-14 13:49
Category: /var/log
Tags: Linux, Debian, init.d, bash,

Unit recently most linux distributions used init.d for managing the various services that are installed and configured appropriately. Understanding how these services are setup is essential for general server maintenance as well as creating custom solutions with capabilities like autostart, and status reporting.

    /etc/init.d

This path contains the scripts used for services. There is also usually a helpfull example skeleton file,
which can be used as a template. These scripts can be called in one of two ways:

    # /etc/init.d/AwesomeServiceName start|status|stop|restart
or
    # service AwesomeServiceNameName start|status|stop|restart

These are just bash scripts with a standard comment header for init.d to know specific things about the service. Here is an example of the header:

    ### BEGIN INIT INFO
    # Provides:          AwesomeServiceName
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: Example initscript
    # Description:       This file should be used to construct scripts to be
    #                    placed in /etc/init.d.
    ### END INIT INFO

The 'Provides' keyword is the name that the service uses to identify itself so that scripts that require it can be started subsequently. You should probably just use the name of the script without any extension. The Require-Start and Required stop ensure any requirements are met before starting and that it will stop before any other services to avoid conflicts.

The next two fields require understanding the run level system. This system is used to configure linux to be bootable into different modes with generally more or less services enabled. If you take a look at the inittab file you will see the default runlevel setting and a layout/example.

    # The default runlevel.
    id:2:initdefault: 

    # /etc/init.d executes the S and K scripts upon change
    # of runlevel.
    #
    # Runlevel 0 is halt.                                                                                    # Runlevel 1 is single-user.
    # Runlevels 2-5 are multi-user.
    # Runlevel 6 is reboot.

    l0:0:wait:/etc/init.d/rc 0
    l1:1:wait:/etc/init.d/rc 1
    l2:2:wait:/etc/init.d/rc 2
    l3:3:wait:/etc/init.d/rc 3
    l4:4:wait:/etc/init.d/rc 4
    l5:5:wait:/etc/init.d/rc 5
    l6:6:wait:/etc/init.d/rc 6 

This will vary by system, but usually 2 or 3 is used for a generally booting 'completely'




