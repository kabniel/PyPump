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

from pypump.models.feed import Feed

class ActivityObject(object):
    """ Super class for all activity objects """

    _attributes = {"attachments",
                  "author",
                  "content",
                  "display_name",
                  "downstream_duplicates",
                  "id",
                  "image",
                  "in_reply_to",
                  "likes",
                  "links",
                  "object_type",
                  "published",
                  "replies",
                  "shares",
                  "summary",
                  "updated",
                  "upstream_duplicates",
                  "url"}

    def __init__(self, *args, **kwargs):
        print('activityobject.__init__')
        for i in self._attributes:
            setattr(self, i, kwargs.get(i, None))
    
    @classmethod
    def unserialize(cls, data, obj=None):
        print('activityobject.unserialize')

        obj = obj or cls()

        author = obj._pump.Person.unserialize(data.get("author", None))
        if data.get('likes', None):
            likes = Feed.unserialize(data=data.get('likes'), parent=obj)
        
        attributes = {
            'attachments': data.get("attachments", None),
            'author': author,
            'content': data.get("content", None),
            'display_name': data.get("displayName", None),
            'downstream_duplicates': data.get("downstreamDuplicates", None),
            'id': data.get("id", None),
            'image': data.get("image", None),
            'in_reply_to': data.get("inReplyTo", None),
            'likes': likes,
            'links': data.get("links", None),
            'object_type': data.get("objectType", None),
            'published': data.get("published", None),
            'replies': data.get("replies", None),
            'shares': data.get("shares", None),
            'summary': data.get("summary", None),
            'updated': data.get("updated", None),
            'upstream_duplicates': data.get("upstreamDuplicates", None),
            'url': data.get("url", None),
        }

        for k,v in attributes.items():
            setattr(obj, k, v)

        return obj

class Note(ActivityObject):
    """ pump.io Note object """

    # attributes that we should delete
    _noattr = ["attachments", "display_name", "image", "summary"]

    def __init__(self, *args, **kwargs):
        print('note.__init__')
        super(Note, self).__init__(*args, **kwargs)

        # delete unwanted attributes
        for i in self._noattr:
            delattr(self, i)

    @classmethod
    def unserialize(cls, data, obj=None):
        print('note.unserialize')
        obj = obj or cls()
        obj = super(Note, obj).unserialize(data, obj=obj)

        for i in obj._noattr:
            delattr(obj, i)

        return obj

