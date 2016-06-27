#!/bin/bash
import os, sys, subprocess, getpass, json, multiprocessing, shutil
from distutils.spawn import find_executable

pw = ""

def run_os_command(command_map):
	'''command_map is a dictionary of {'executable': command}. For ex. {'apt-get': 'sudo apt-get install -y python2.7'} '''
	success = True
	for executable, commands in command_map.items():
		print command_map.items()
		if find_executable(executable):
			if isinstance(commands, basestring):
				commands = [commands]

			for command in commands:
				returncode = subprocess.check_call(command, shell=True)
				success = success and ( returncode == 0 )

			break

	return success

def prompt_pass():

	sys.stderr.write("Enter for MySQL password: ");
	global pw
	pw =raw_input("")
	print "You entered: " + pw


def setup_bench():
	print "Downloading install.py...................."
	subprocess.call("wget https://raw.githubusercontent.com/flomente96/bench/master/playbooks/install.py", shell=True)

	print "Running playbook...................."
	subprocess.call("python install.py --develop", shell=True)
	# subprocess.call("echo 'peregrine11\r'")


def get_erpnext(): #gets frappe-bench and erpnext
	print os.getcwd()
	os.chdir('frappe-bench/')
	success = subprocess.call("bench get-app erpnext https://github.com/flomente96/erpnext.git", shell=True)
	os.chdir(sys.path[0])
	return success


def change_pass():
	print "Desired password: "+ pw
	print os.getcwd()
	# subprocess.call("xterm -hold -geometry 70x20 -T check_mySQLRoot -e sudo /etc/init.d/mysql restart", shell=True)
	# subprocess.call("xterm -e 'try.sh'; bash")
	# os.system("gnome-terminal -e 'bash -c \"sudo add-apt-repository ppa:x2go/ppa && sudo apt-get update ; exec bash\"'")

	# subprocess.call("sudo /etc/init.d/mysql stop", shell=True)
	# subprocess.call("sudo mysqld --skip-grant-tables &", shell=True)
	# subprocess.call("mysql -u root mysql", shell=True)
	# success = subprocess.call("UPDATE user SET Password=PASSWORD("+pw+") WHERE User='root'; FLUSH PRIVILEGES; exit;", shell=True)
	# subprocess.call("sudo /etc/init.d/mysql restart", shell = True)
	#  mysql -u root mysql


def create_new_site():
	os.chdir('frappe-bench/')
	success = run_os_command(
		{'bench': 'bench new-site erpnext'}
	)
	os.chdir(sys.path[0])
	return success

def install_app():
	os.chdir('frappe-bench/')
	subprocess.call("bench --site erpnext install-app erpnext", shell=True)
	os.chdir(sys.path[0])

def bench_start():
	print os.getcwd()
	os.chdir('frappe-bench/')
	print os.getcwd()
	subprocess.call("bench start", shell=True)


# prompt_pass()
# change_pass()
setup_bench()
get_erpnext()
create_new_site()
install_app()
bench_start()
