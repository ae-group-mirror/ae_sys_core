""" mock of connector_module with connector classes/funcs """


class SystemConnectionSuccessMock:
    """ test connection mock """
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


def connector_success_mock(_system):
    """ connector class for successful connections """
    return SystemConnectionSuccessMock()


# noinspection PyUnusedLocal
def connector_failure_mock(_system):
    """ connector class for failing connect """
    return SystemConnectionFailureMock()


# noinspection PyUnusedLocal
def disconnect_failure_mock(_system):
    """ connector class for failing disconnect/close """
    return SystemDisconnectionFailureMock()
