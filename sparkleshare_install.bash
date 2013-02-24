#!/bin/bash -e

aptitude install gtk-sharp2 mono-runtime mono-devel monodevelop libndesk-dbus1.0-cil-dev  nant libnotify-cil-dev libgtk2.0-cil-dev mono-mcs mono-gmcs libwebkit-cil-dev intltool libtool libndesk-dbus-glib1.0-cil-dev desktop-file-utils

tar xvf sparkleshare-linux-1.0.0.tar.gz
cd sparkleshare-1.0.0/
./configure
make
make install
