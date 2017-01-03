#!/usr/bin/python

import os


#######################################################################
#defs

def yum_install ( pkg ):
   "function_docstring"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def play_book ( pb ):
   "function_docstring"
   book = "ansible-playbook ./" + pb
   os.system(book)
   return;

def install_galaxy ( galaxy ):
   "function_docstring"
   ig = "ansible-galaxy install " + galaxy
   os.system(ig)
   return;

########################################################################

yum_install( "epel-release" )
yum_install( "ansible" )
install_galaxy( "jmbarros.common")
install_galaxy( "jmbarros.etcd")
play_book ("install.yml")


