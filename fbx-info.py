#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: @tuxtof

import urllib2
import re
import sys

try:
    fbxinfo = urllib2.urlopen("http://mafreebox.freebox.fr/pub/fbx_info.txt")
except urllib2.HTTPError as e:
    print "Error %s" % (e.code)
    sys.exit(1)

for ligne in fbxinfo:
    if re.search(".*Version.*", ligne):
        version = ligne.split()[3]
    if re.search(".*mise en route.*", ligne):
        jour = re.search(r'(\d) jour', ligne)
        if jour is not None:
            jour = "%s*1440" % (jour.group(1))
            uptime = eval(jour)
        heure = re.search(r'(\d) heure', ligne)
        if heure is not None:
            heure = "%s*60" % (heure.group(1))
            uptime = uptime + eval(heure)
        minute = re.search(r'(\d*) minute', ligne)
        if minute is not None:
            uptime = uptime + eval(minute.group(1))

    if re.search(".*Adsl :.*", ligne):
        break



for ligne in fbxinfo:
    if re.search(".*Etat.*", ligne):
        state = ligne.split()[1]
    if re.search(".*Protocole.*", ligne):
        proto = ligne.split()[1]
    if re.search(".*Mode.*", ligne):
        mode = ligne.split()[1]
    if re.search(".*ATM.*", ligne):
        debitd = ligne.split()[2]
        debitu = ligne.split()[4]
    if re.search(".*Marge de bruit.*", ligne):
        bruitd = ligne.split()[3]
        bruitu = ligne.split()[5]
    if re.search(".*Att.*nuation.*", ligne):
        attenuationd = ligne.split()[1]
        attenuationu = ligne.split()[3]
    if re.search(".*FEC.*", ligne):
        fecd = ligne.split()[1]
        fecu = ligne.split()[2]
    if re.search(".*CRC.*", ligne):
        crcd = ligne.split()[1]
        crcu = ligne.split()[2]
    if re.search(".*HEC.*", ligne):
        hecd = ligne.split()[1]
        hecu = ligne.split()[2]
    if re.search(".*Journal de connexion adsl.*", ligne):
        break


for ligne in fbxinfo:
    if re.search(".*Connexion.*", ligne):
        debitcond = ligne.split()[4]
        debitconu = ligne.split()[6]
        break

print "freebox uptime=%i,version=\"%s\",state=\"%s\",proto=\"%s\""  % (uptime, version,state,proto)
print "freebox,type=debit down=%s,up=%s" % (debitd,debitu)
print "freebox,type=bruit down=%s,up=%s" % (bruitd, bruitu)
print "freebox,type=attenuation down=%s,up=%s" % (attenuationd, attenuationu)
print "freebox,type=FEC down=%s,up=%s" % (fecd, fecu)
print "freebox,type=CRC down=%s,up=%s" % (crcd, crcu)
print "freebox,type=HEC down=%s,up=%s" % (hecd, hecu)
print "freebox,type=journal down=%s,up=%s" % (debitcond, debitconu)
