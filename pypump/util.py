class AttrSetter(object):
    def __init__(self, pypump=None):
        self._pump = pypump

    def set_attr(self, obj, key, data, from_json=False):
        if key == "attachment":
            self.set_attachment(obj, key, data, from_json)
        elif key == "author":
            self.set_person(obj, key, data, from_json)
        elif key == "content":
            self.set_string(obj, key, data, from_json)
        elif key == "display_name":
            self.set_string(obj, key, data, from_json)
        elif key == "downstream_duplicates":
            self.set_downstream_duplicates(obj, key, data, from_json)
        elif key == "id":
            self.set_string(obj, key, data, from_json)
        elif key == "image":
            self.set_image(obj, key, data, from_json)
        elif key == "in_reply_to":
            self.set_in_reply_to(obj, key, data, from_json)
        elif key == "likes":
            self.set_likes(obj, key, data, from_json)
        elif key == "links":
            self.set_links(obj, key, data, from_json)
        elif key == "object_type":
            self.set_string(obj, key, data, from_json)
        elif key == "published":
            self.set_date(obj, key, data, from_json)
        elif key == "replies":
            self.set_replies(obj, key, data, from_json)
        elif key == "shares":
            self.set_shares(obj, key, data, from_json)
        elif key == "summary":
            self.set_string(obj, key, data, from_json)
        elif key == "updated":
            self.set_date(obj, key, data, from_json)
        elif key == "upstream_duplicates":
            self.set_upstream_duplicates(obj, key, data, from_json)
        elif key == "url":
            self.set_string(obj, key, data, from_json)


    def set_attachment(self, obj, key, data, from_json):
        # TODO
        pass

    def set_person(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, self.get_object(data))

    def set_string(self, obj, key, data, from_json):
        setattr(obj, key, data)

    def set_downstream_duplicates(self, obj, key, data, from_json):
        # TODO
        pass

    def set_upstream_duplicates(self, obj, key, data, from_json):
        # TODO
        pass

    def set_image(self, obj, key, data, from_json):
        # TODO
        pass

    def set_in_reply_to(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, self.get_object(data))

    def get_object(self, data):
        try:
            objekt = getattr(self._pump.activityobject, data["objectType"].capitalize())
            return objekt(jsondata=data)
        except:
            return self._pump.activityobject.ActivityObject(jsondata=data)

    def set_likes(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, "likes goes here")

    def set_links(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, "links goes here")

    def set_date(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, "date goes here")

    def set_replies(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, "replies goes here")

    def set_shares(self, obj, key, data, from_json):
        if from_json:
            setattr(obj, key, "shares goes here")

