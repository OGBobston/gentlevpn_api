import os, subprocess

class OVPN(object):

    def __init__(self, openvpnPath):
        self.openvpnPath = openvpnPath

        self.cdCommand = r"cd"
        self.getUsersCommand = r"./sacli UserPropGet"

        self.userCommand =  r"./sacli --user"
        self.typeUserConnectCommand = r'--key "type" --value "user_connect" UserPropPut'
        self.propAutologinCommand = r'--key "prop_autologin" --value "true" UserPropPut'
        self.getAutologinCommand = r"GetAutoLogin >/home/profiles/"
        self.deleteUserCommand = r' UserPropDelAll'
        self.refreshServerCommand =  r"./sacli start"
        self.newPassCommand =  r"--new_pass"
        self.setPassCommand =  r"SetLocalPassword"



    def getConsoleOutput(self, command):
        output = subprocess.check_output([command], shell=True)
        return output

    def getUsersList(self):
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.getUsersCommand
        output = self.getConsoleOutput(command)
        return output

    def register(self, username):
        username = str(username)
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + username + " " + self.typeUserConnectCommand
        output = self.getConsoleOutput(command)
        print(output)

        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + username + " " + self.propAutologinCommand
        output = self.getConsoleOutput(command)
        print(output)

        self.updateServer()

    def getCertificate(self, username):
        username = str(username)
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + username + " " + self.getAutologinCommand + " " + username + ".ovpn"
        output = self.getConsoleOutput(command)
        file = open(r'/home/profiles/' + username + r'.ovpn', 'rb')
        return file

    def deleteUser(self, username):
        username = str(username)
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + username + " " + self.deleteUserCommand
        output = self.getConsoleOutput(command)
        print(output)
        return output

    def updateServer(self):
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.refreshServerCommand
        output = self.getConsoleOutput(command)
        print(output)
