import paramiko
import getpass

# build an object that represents our ssh connection to a host

# WHERE to connect
t = paramiko.Transport("10.10.2.3", 22)

# HOW to connect
t.connect(username="bender", password=getpass.getpass())

#use that connection to build an SFTP client out of bender
sftp = paramiko.SFTPClient.from_transport(t)

sftp.put("thisisanexample.txt", "anewname.txt")
