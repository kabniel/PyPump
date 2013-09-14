from pypump.newmodels.activityobject import ActivityObject

class Activity(ActivityObject):
    """ pump.io Activity object """

    # parent attributes that we dont want
    _ignore_attr = list()
    # attributes unique to this class
    _attribute_map = {
        "actor": "actor",
        "generator": "generator",
        "obj": "object",
        "verb": "verb"}

    def __init__(self, *args, **kwargs):
        # Let ActivityObject handle common things first
        super(Activity, self).__init__(*args, **kwargs)

        # Inject actor as author if not there (this sucks)
        data = kwargs.get("jsondata", dict())
        if data.get("verb") == "post":
            actor = data.get("actor", None)
            if not data["object"].get("author"):
                kwargs["jsondata"]["object"]["author"] = actor

        self._pump.newmodels.attribute.parse_map(self, self._attribute_map, *args, **kwargs)
