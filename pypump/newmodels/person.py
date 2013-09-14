from pypump.newmodels.activityobject import ActivityObject
from pypump.models.feed import Inbox

class Person(ActivityObject):
    """ pump.io Person object """

    # parent attributes that we dont want
    _ignore_attr = ["attachments",]
    # attributes unique to this class
    _attribute_map = {"preferred_username": "preferredUsername"}

    def __init__(self, webfinger=None, *args, **kwargs):
        print('person init')
        # If a webfinger is entered, grab json from API and re-init
        if webfinger:
            self.username, self.server = webfinger.split("@")

            data = self._pump.request("{proto}://{server}/api/user/{username}/profile".format(
                proto=self._pump.protocol,
                server=self.server,
                username=self.username
            ))

            self.__init__(jsondata=data)

        else:
            # Let ActivityObject handle common things first
            super(Person, self).__init__(*args, **kwargs)

            self.username, self.server = self.id[5:].split("@")

        if self.username == self._pump.nickname and self.server == self._pump.server:
            self.inbox = Inbox(self)

        self._pump.newmodels.attribute.parse_map(self, self._attribute_map, *args, **kwargs)


    # TODO Add Person-specific methods and properties here
    # lists
    # followers
    # following
    # outbox
