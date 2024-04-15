import configparser

config = configparser.RawConfigParser()             # 'config' is a new object
config.read(".\\Configurations\\config.ini")        # with the 'config' object, we're reading the 'config.ini' file


class ReadConfig:               # write a class to get the needed data
    @staticmethod
    def getApplicationURL():  # need a method for each variable to retrieve, to be called from the test case
        url = config.get('common info', 'baseURL')  # extract the value of 'baseURL' from the 'common info' category
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
