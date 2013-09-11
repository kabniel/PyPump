##
# Copyright (C) 2013 Jessica T. (Tsyesika) <xray7224@googlemail.com>
# 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. 
# 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. 
# 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##

class ActivityObject(object):
    """ Super class for all activity objects """

    _attr_map = {
        "attachments": "attachments",
        "author": "author",
        "content": "content",
        "display_name": "displayName",
        "downstream_duplicates": "downstreamDuplicates",
        "id": "id",
        "image": "image",
        "in_reply_to": "inReplyTo",
        "likes": "likes",
        "links": "links",
        "object_type": "objectType",
        "published": "published",
        "replies": "replies",
        "shares": "shares",
        "summary": "summary",
        "updated": "updated",
        "upstream_duplicates": "upstreamDuplicates",
        "url": "url"}

    def __init__(self, *args, **kwargs):
        print('activityobject.__init__')
        self._noattr = kwargs.get("noattr", list())

        if "jsondata" in kwargs:
            for (k, v) in self._attr_map.items():
                if v in kwargs["jsondata"] and k not in self._noattr:
                    self._pump.activityobject.attr_setter.set_attr(self, k, kwargs["jsondata"][v], from_json=True)
        else:
            for (k, v) in self._attr_map.items():
                if k in kwargs and k not in self._noattr:
                    self._pump.activityobject.attr_setter.set_attr(self, k, kwargs[k])

    
class Note(ActivityObject):
    """ pump.io Note object """

    # attributes that we dont want
    _noattr = ["attachments", "display_name", "image", "summary"]

    def __init__(self, *args, **kwargs):
        print('note.__init__')
        # Let ActivityObject handle common things first
        super(Note, self).__init__(noattr=self._noattr, *args, **kwargs)

    # TODO Add Note-specific methods and stuff here


from pypump.models.feed import Inbox

class Person(ActivityObject):
    """ pump.io Person object """

    # attributes that we dont want
    _noattr = ["attachments"]

    def __init__(self, webfinger=None, *args, **kwargs):
        print('person.__init__')
        # If a webfinger is entered, grab jsondata from API and re-init with data
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
            super(Person, self).__init__(noattr=self._noattr, *args, **kwargs)

            self.username, self.server = self.id[5:].split("@")

        if self.username == self._pump.nickname and self.server == self._pump.server:
            self.inbox = Inbox(self)


    # TODO Add Person-specific methods and properties here
