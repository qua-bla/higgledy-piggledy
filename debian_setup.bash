#!/bin/bash

echo 'basics'
aptitude install vim htop etckeeper

echo 'nvidia'
aptitude install linux-headers-amd64 
aptitude install nvidia-kernel-dkms 
aptitude install nvidia-xconfig 
nvidia-xconfig 

echo 'broadcom wlan'
aptitude install broadcom-sta-dkms
modprobe -r b44 b43 b43legacy ssb brcmsmac
modprobe wl

echo 'mozilla'
echo 'deb http://mozilla.debian.net/ experimental iceweasel-esr' >> /etc/apt/sources.list
aptitude install -t experimental iceweasel iceweasel-l10n-de
aptitude install icedove icedove-l10n-de
aptitude install xul-ext-certificatepatrol xul-ext-https-everywhere xul-ext-noscript xul-ext-sieve 

echo 'others'
aptitude install pidgin pidgin-otr
aptitude install texlive-full texmaker
aptitude install gnuplot-x11
aptitude install git
aptitude install pgadmin3

echo 'media'
aptitude install vlc banshee

