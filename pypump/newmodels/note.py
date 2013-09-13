from pypump.newmodels.activityobject import ActivityObject

class Note(ActivityObject):
    """ pump.io Note object """

    # attributes that we dont want
    _noattr = ["attachments", "display_name", "image", "summary"]

    def __init__(self, *args, **kwargs):
        print('note.__init__')
        # Let ActivityObject handle common things first
        super(Note, self).__init__(noattr=self._noattr, *args, **kwargs)

    # TODO Add Note-specific methods and stuff here
