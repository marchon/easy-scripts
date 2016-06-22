# testbench
for bench and frappe installation and erpnext initialization

Installation Steps:

1. Place test.py file inside your Home directory
2. Open terminal and go to the Home directory using shell
3. Run the test.py file by entering 'python test.py'

Logs:

Log 1: After python install.py --develop command, .bench is installed in the local directory. (i.e Home/)

Log 2: Still need to enter sudo account for this. (At the start of the terminal for security checking.)

Log 3: Changed

success = subprocess.call("bench new-site testsite")

to     

success = run_os_command(
            {'bench': 'bench new-site erpnext-test'}
        )

Log 4: ^ Requires the MYSQL Root password for this command. #We need to know the root password for the MYSQL

Log 5: Admin account is set here via Terminal.

Log 6: Changed

success = subprocess.call("bench --site testsite install-app erpnext")

to

success = run_os_command(
            {'bench': 'bench --site erpnext-test install-app erpnext'}
        )

Log 7: Successfully installed Erpnext! Yay :grin:

