import pickle

allowedUsers = {'ye':'1234','ke': '1234','justin':'1234','hayley':'1234','admin':'password'}

filename = "users.txt"
file = open(filename, 'wb')
pickle.dump(allowedUsers, file)
file.close()


file1 = open(filename, 'rb')
new_users = pickle.load(file1)

for user in new_users:
    print user