import pickle
import sys

filename = "users.txt"
file1 = open(filename, 'rb')
allowedUsers = pickle.load(file1)


AdminID = raw_input("Username for Admin: ")
Password = raw_input("Password: ")


while Password != allowedUsers['admin']:
    print 'Invalid login details, please try again'
    AdminID = raw_input("Username for Admin: ")
    Password = raw_input("Password: ")

# for user in allowedUsers:
#     print user  + '\t ' + allowedUsers[user]
selectionPrase = '\nSelect \n 1.Add user\n 2.Change password\n 3.Delete users\n 4.Display all\n q.exit: \n'

choice = raw_input(selectionPrase)

while choice != 'q':
    

    if choice == '1':
        newID = raw_input("Please input new username: ")
        newPwd = raw_input("Please input password to new user: ")


        allowedUsers[newID] = newPwd
        print 'Thanks! new User was created.'
        # for user in userInfo.allowedUsers:
        #     print user

    if choice == '2':
        newID = raw_input("Please target username: ")
        newPwd = raw_input("Please input new password user: ")
        allowedUsers[newID] = newPwd
        print 'Thanks! password for '+ newID + ' has been changed'

    if choice == '3':
        newID = raw_input("Please enter username to delete: ")
        del allowedUsers[newID]
        print 'Thanks! user id: '+ newID + ' has been deleted'

    if choice == '4':
        print '\n'
        for user in allowedUsers:
            print user + '\t\t ' + allowedUsers[user]

    choice = raw_input(selectionPrase)

file1.close()
file1 = open(filename, 'wb')
pickle.dump(allowedUsers,file1)
file1.close()
print 'Bye'
sys.exit()