import requests

class Nemiling(object):
    def __init__(self):
        self.url = r"https://nemilin.pro/API"
        self.id = "489812576:e351329634e5a9"
        self.checkMemberUrl = r"/v1/checkmember/2pqr/"

    def checkMember(self, id):
        headers = { 'Authorization' : self.id }
        response = requests.get(self.url + self.checkMemberUrl + str(id), headers=headers)
        return response.text
