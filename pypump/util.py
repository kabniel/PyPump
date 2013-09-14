class Attribute(object):

    _strings = ["content", "display_name", "id", "object_type",
                "summary", "url", "preferred_username"]

    _dates = ["updated", "published"]

    def __init__(self, pypump=None):
        self._pump = pypump

    def parse_map(self, obj, attr_map, *args, **kwargs):
        if "jsondata" in kwargs:
            for (k, v) in attr_map.items():
                if v in kwargs["jsondata"] and k not in obj._ignore_attr:
                    self.add(obj, k, kwargs["jsondata"][v], from_json=True)
        else:
            for (k, v) in attr_map.items():
                if k in kwargs and k not in obj._ignore_attr:
                    self.add(obj, k, kwargs[k]) 

    def add(self, obj, key, data, from_json=False):

        if key in self._strings:
            # set string attributes
            self.set_string(obj, key, data, from_json)

        elif key in self._dates:
            # set date attributes
            self.set_date(obj, key, data, from_json)

        elif key == "author":
            self.set_person(obj, key, data, from_json)
        elif key == "downstream_duplicates":
            self.set_downstream_duplicates(obj, key, data, from_json)
        elif key == "image":
            self.set_image(obj, key, data, from_json)
        elif key == "in_reply_to":
            self.set_in_reply_to(obj, key, data, from_json)
        elif key == "likes":
            self.set_likes(obj, key, data, from_json)
        elif key == "links":
            self.set_links(obj, key, data, from_json)
        elif key == "replies":
            self.set_replies(obj, key, data, from_json)
        elif key == "shares":
            self.set_shares(obj, key, data, from_json)
        elif key == "upstream_duplicates":
            self.set_upstream_duplicates(obj, key, data, from_json)


    def set_attachment(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_person(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, self.get_object(data))

    def set_string(self, obj, key, data, from_json):
        setattr(obj, key, data)

    def set_downstream_duplicates(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_upstream_duplicates(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_image(self, obj, key, data, from_json):
        #TODO not finished
        #need to handle different types, for profiles objectType is not set
        if from_json:
            setattr(obj, key, data)

    def set_in_reply_to(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, self.get_object(data))

    def get_object(self, data):
        try:
            print data
            print data['objectType'].capitalize()
            objekt = getattr(self._pump.newmodels, data["objectType"].capitalize())
            print('found')
            return objekt(jsondata=data)
        except:
            print('except')
            # fall back to base activity object
            return self._pump.newmodels.ActivityObject(jsondata=data)

    def set_likes(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_links(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_date(self, obj, key, data, from_json):
        #TODO not finished, we should convert to datetime object
        if from_json:
            setattr(obj, key, data)

    def set_replies(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)

    def set_shares(self, obj, key, data, from_json):
        #TODO not finished
        if from_json:
            setattr(obj, key, data)
