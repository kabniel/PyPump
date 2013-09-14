from pypump.newmodels.activityobject import ActivityObject

class Application(ActivityObject):
    """ pump.io Application object """

    # parent attributes that we dont want
    _ignore_attr = ["likes", "replies", "shares"]
    # attributes unique to this class
    _attribute_map = dict()

    def __init__(self, *args, **kwargs):
        # Let ActivityObject handle common things first
        super(Application, self).__init__(*args, **kwargs)

        self._pump.newmodels.attribute.parse_map(self, self._attribute_map, *args, **kwargs)
