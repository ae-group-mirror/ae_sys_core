""" mock of connector_module with connector classes/funcs """


class SystemConnectionSuccessMock:
    """ test connection mock """
    def __init__(self, credentials, features, app_name, debug_level):
        self.credentials = credentials
        self.features = features
        self.app_name = app_name
        self.debug_level = debug_level

    def connect(self):
        """ helper method """
        return not self or ''

    def close(self):
        """ helper method """
        return not self or ''

    def disconnect(self):
        """ helper method """
        return not self or ''


class SystemConnectionFailureMock:
    """ test connection mock """
    def connect(self):
        """ helper method """
        return 'ConnectError' or self


class SystemDisconnectionFailureMock:
    """ test connection mock """
    def connect(self):
        """ helper method """
        return not self or ''

    def close(self):
        """ helper method """
        return 'CloseError' or self

    def disconnect(self):
        """ helper method """
        return 'DisconnectError' or self


def connector_success_mock(credentials, features, app_name, debug_level):
    """ connector class for successful connections """
    return SystemConnectionSuccessMock(credentials, features, app_name, debug_level)


# noinspection PyUnusedLocal
def connector_failure_mock(credentials, features, app_name, debug_level):
    """ connector class for failing connect """
    return SystemConnectionFailureMock()


# noinspection PyUnusedLocal
def disconnect_failure_mock(credentials, features, app_name, debug_level):
    """ connector class for failing disconnect/close """
    return SystemDisconnectionFailureMock()
