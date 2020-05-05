
#pip install mysql-connector-python
import demo_mysql
import sys


AdminID = raw_input("Username for Administratior: ")
Password = raw_input("Password: ")


while not demo_mysql.verification(AdminID, Password):
    print 'Invalid login details, please try again'
    AdminID = raw_input("Username for Admin: ")
    Password = raw_input("Password: ")

while not demo_mysql.verifyAdmin(AdminID):
    print "This user is not an Administratior"
    AdminID = raw_input("Username for Admin: ")
    Password = raw_input("Password: ")


selectionPrase = '\nSelect \n 1.Add user\n 2.Change password\n 3.Delete users\n 4.Add/Remove admin role\n 5.Display all\n q.exit: \n'

choice = raw_input(selectionPrase)

while choice != 'q':
    

    if choice == '1':
        newID = raw_input("Please input new username: ")
        newPwd = raw_input("Please input password to new user: ")
        demo_mysql.addUser(newID, newPwd,0)
        print "Thanks! new User "+newID +  " was created."
     

    if choice == '2':
        newID = raw_input("Please target username: ")
        newPwd = raw_input("Please input new password user: ")
        demo_mysql.changePassword(newID, newPwd)
        print 'Thanks! password for '+ newID + ' has been changed'

    if choice == '3':
        newID = raw_input("Please enter username to delete: ")
        demo_mysql.deleteUser(newID)
        print 'Thanks! user id: '+ newID + ' has been deleted'

    if choice == '4':
        newID = raw_input("Please target username: ")
        newStatus = raw_input("Please input new admin status 0/1: ")
        # demo_mysql.convertToAdmin(newID, newStatus)
        role = "Admin" if demo_mysql.convertToAdmin(newID, newStatus)=="1" else "not Admin"
        print "Thanks! "+ newID + " is " +role

    if choice == '5':
        demo_mysql.displayAllUsers();

    choice = raw_input(selectionPrase)

print 'Bye'
sys.exit()