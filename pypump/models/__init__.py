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

import json

class AbstractModel(object):

    @property
    def TYPE(self):
        return self.__class__.__name__

    @property
    def objectType(self):
        return self.TYPE.lower()

    _mapping = {
        "objectType":"TYPE",
    }

    _pump = None

    def __init__(self, pypump=None, *args, **kwargs):
        """ Sets up pump instance """
        if pypump:
            self._pump = pypump

    def _post_activity(self, activity, unserialize=True):
        """ Posts a activity to feed """
        # I think we always want to post to feed
        feed_url = "{proto}://{server}/api/user/{username}/feed".format(
            proto=self._pump.protocol,
            server=self._pump.server,
            username=self._pump.nickname
        )

        data = self._pump.request(feed_url, method="POST", data=activity)

        if not data:
            return False

        if "error" in data:
            raise PumpException(data["error"])

        if unserialize:
            if "target" in data:
                # we probably want to unserialize target if it's there
                # true for collection.{add,remove}
                self.unserialize(data["target"], obj=self)
            else:
                self.unserialize(data["object"], obj=self)

        return True

    def serialize(self, *args, **kwargs):
        """ Changes it from obj -> JSON """
        data = {}
        for item in dir(self):
            if item.startswith("_"):
                continue # we don't want
            
            value =  getattr(self, item)
            
            # we need to double check we're not in mapper
            item = self.remap(item)
            data[item] = value

        return json.dumps(data, *args, **kwargs)

    @staticmethod
    def unserialize(self, data, *args, **kwargs):
        """ Changes it from JSON -> obj """
        data = json.loads(data)

        klass = self(pypump=self._pump)

        for key, value in data.items():
            key = self.remap(key)
            if key is None:
                continue

            setattr(klass, key, value)            

        return klass

    def remap(self, data):
        """ Remaps """
        if data in self._mapping.keys():
            return self._mappping[data]
        elif data in self.__mapping.values():
            for k, v in self._mapping.items():
                if data == v:
                    return k

        return data

