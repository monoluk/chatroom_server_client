# With UserName Validation

# Server Run 
python2 server.py <internal ip address> 8088
use $ ifconfig | grep inet to check if necessary

# Client Run
python2 client.py <server's ip address> 8088
#then enter username and password

# admin Run
python2 admin.py
#then enter "Admin" and "password"
#need to quit admin.py program for the change to take effect. But Server doesn't have to stop.

# run pickleData.py
#to quickly restore uses.txt to default


