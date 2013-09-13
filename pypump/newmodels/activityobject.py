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

    _attribute_map = {
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

    def __repr__(self):
        return "<{type}: {id}>".format(type=self.object_type, id=self.id)

    def __init__(self, *args, **kwargs):
        attr_map = ActivityObject._attribute_map
        self._pump.newmodels.attribute.parse_map(self, attr_map, *args, **kwargs)
