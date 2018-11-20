#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

sys.path.append('/home/cvrsg/Others/YfMao/pva-faster-rcnn/ContainerRecognition/serialconverter/build')

import ipmodule as ip

#cpu_id=''  #'F2060300-FFFBEBBF-00000000-0000'
#jphu: cpu_id=E9060900-FFFBEBBF-FEFBEBBF-0000
id_impl  = ip.pc_id()
if id_impl.calc_cpu_id_by_asm()==True:
    cpu_id=id_impl.get_cpu_id()
    print "cpu_id_by_asm: ", cpu_id
else:
    print "can not get cpu id"

if id_impl.calc_mac_address_by_ioctl()==True:
    mac_id=id_impl.get_mac_address()
    print "mac_address: ",mac_id
else:
    print "can not get mac id"

if id_impl.calc_disk_serial_number()==True:
    disk_serial_number=id_impl.get_disk_serial_number()
    print "disk_serial_number: ",disk_serial_number
else:
    print "can not get disk_serial_number"
