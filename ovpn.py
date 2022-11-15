import os, subprocess

class OVPN(object):

    def __init__(self, openvpnPath):
        self.openvpnPath = openvpnPath

        self.cdCommand = r"cd"
        self.getUsersCommand = r"./sacli UserPropGet"

    def getConsoleOutput(self, command):
        output = subprocess.check_output([command], shell=True)
        return output

    def getUsersList(self):
        command = self.cdCommand + " " + self.openvpnPath + " && " + self.getUsersCommand
        print(command)
        output = self.getConsoleOutput(command)
        return output
