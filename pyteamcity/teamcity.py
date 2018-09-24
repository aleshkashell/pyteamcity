import requests, os
class TeamCity:
    username = None
    password = None
    server = None
    port = None
    error_handler = None

    def __init__(self, username=None, password=None, server=None, port=None,
                 session=None, protocol=None):
        self.username = username or os.getenv('TEAMCITY_USER')
        self.password = password or os.getenv('TEAMCITY_PASSWORD')
        self.host = server or os.getenv('TEAMCITY_HOST')
        self.port = port or int(os.getenv('TEAMCITY_PORT', 0)) or 80
        self.protocol = protocol or os.getenv('TEAMCITY_PROTOCOL', 'http')
        self.base_base_url = "%s://%s:%d" % (
            self.protocol, self.host, self.port)
        self.guest_auth_base_url = "%s://%s:%d/guestAuth" % (
            self.protocol, self.host, self.port)
        if self.username and self.password:
            self.base_url = "%s://%s:%d/httpAuth/app/rest" % (
                self.protocol, self.host, self.port)
            self.auth = (self.username, self.password)
        else:
            self.base_url = "%s://%s:%d/guestAuth/app/rest" % (
                self.protocol, self.host, self.port)
            self.auth = None
        self.session = session or requests.Session()

        self._agent_cache = {}