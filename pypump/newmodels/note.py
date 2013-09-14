from pypump.newmodels.activityobject import ActivityObject

class Note(ActivityObject):
    """ pump.io Note object """

    # parent attributes that we dont want
    _ignore_attr = ["attachments", "display_name", "image", "summary"]
    # attributes unique to this class
    _attribute_map = dict()

    def __init__(self, *args, **kwargs):
        # Let ActivityObject handle common things first
        super(Note, self).__init__(*args, **kwargs)

    # TODO Add Note-specific methods and stuff here
