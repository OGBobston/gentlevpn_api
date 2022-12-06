import os, subprocess

class OVPN(object):

    def __init__(self, openvpnPath):
        self.openvpnPath = openvpnPath

        self.cdCommand = r"cd"
        self.getUsersCommand = r"./sacli UserPropGet"

        self.userCommand =  r"./sacli --user"
        self.typeUserConnectCommand = r'--key "type" --value "user_connect" UserPropPut'
        self.propAutologinCommand = r'--key "prop_autologin" --value "true" UserPropPut'

    def getConsoleOutput(self, command):
        output = subprocess.check_output([command], shell=True)
        return output

    def getUsersList(self):
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.getUsersCommand
        output = self.getConsoleOutput(command)
        return output

    def register(self, username):
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + self.typeUserConnectCommand
        output = output = self.getConsoleOutput(command)
        print(output)
        
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.userCommand + " " + self.propAutologinCommand
        output = output = self.getConsoleOutput(command)
        print(output)
