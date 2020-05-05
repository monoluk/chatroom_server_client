#pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="PASSWORD",
  database="csc651"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("USE csc651")
# mycursor.execute("SELECT * FROM users")
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


#option1 add user
def addUser(uname,pwd,iadm):
	# uname = "Kelly"
	# pwd = "1234"
	# iadm = 0
	try:
		sql = "INSERT INTO users (username, password, is_admin) VALUES (%s, %s, %s)"
		val = (uname, pwd, iadm)
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")
	except:
		print("Action failed")


#option2 change password
def changePassword(uname, newPwd):
	sql = "UPDATE USERS SET password ='"+newPwd+"' WHERE username = '"+uname+"'"
	mycursor.execute(sql)
	mydb.commit()


# #option3 delete users
def deleteUser(uname):
	sql = "DELETE FROM users WHERE username='"+uname+"'"
	mycursor.execute(sql)
	mydb.commit()
	print(mycursor.rowcount, "record(s) deleted")


#option 4, display all users
def displayAllUsers():
	mycursor.execute("SELECT * FROM users")
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)

#Login authentication
def verification(uname, pwd):
	try: 
		sql = "SELECT username, password FROM users WHERE username='"+uname+"'"
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
		  dbuname, dbpwd = x

		return(dbuname == uname and pwd == dbpwd)
	except:
		print("Action failed")

def verifyAdmin(uname):
	sql = "SELECT * FROM users WHERE username='"+uname+"'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
	  dbuname, dbpwd, is_admin = x
	return is_admin


def convertToAdmin(uname, newStatus):
	sql = "UPDATE USERS SET is_admin ='"+ str(newStatus)+ "'WHERE username='"+uname+"'"
	mycursor.execute(sql)
	mydb.commit()
	return newStatus


