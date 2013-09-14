from pypump.models.feed import Feed

class Likeable(object):
    """
        Provides the model with the like and unlike methods as well as
        the property likes which will look up who's liked the model instance
        and return you back a list of user objects
    
    """

    @property
    def likes(self):
        """ Gets who's liked this object """
        endpoint = self._feed_url["likes"]
        return Feed(self, endpoint)

    favorites = likes

    def like(self, verb="like"):
        """ Likes the model """
        activity = {
            "verb": verb,
            "object": {
                "id": self.id,
                "objectType": self.object_type,
            }
        }

        self._post_activity(activity)

    def unlike(self, verb="unlike"):
        """ Unlikes the model """
        activity = {
            "verb": verb,
            "object": {
                "id": self.id,
                "objectType": self.object_type,
            }
        }

        self._post_activity(activity)

    def favorite(self):
        """ Favourite model """
        return self.like(verb="favorite")

    def unfavorite(self):
        """ Unfavourite model """
        return self.unlike(verb="unfavorite")


class Commentable(object):
    """
        Provides the model with the comment method allowing you to post
        a comment to on the model. It also provides an ability to read
        comments.

    """

    @property
    def comments(self):
        """ Fetches the comment objects for the models """
        endpoint = self._feed_url["replies"]
        return Feed(self, endpoint)

    def comment(self, comment):
        """ Posts a comment object on model """
        comment.inReplyTo = self
        comment.send()


class Shareable(object):
    """
        Provides the model with the share and unshare methods and shares
        property allowing you to see who's shared the model.

    """

    @property
    def shares(self):
        """ Fetches the people who've shared the model """
        endpoint = self._feed_url["shares"]
        return Feed(self, endpoint)

    def share(self):
        """ Shares the model """
        activity = {
            "verb": "share",
            "object": {
                "id": self.id,
                "objectType": self.object_type,
            },
        }

        self._post_activity(activity)

    def unshare(self):
        """ Unshares a previously shared model """
        activity = {
            "verb": "unshare",
            "object": {
                "id": self.id,
                "objectType": self.object_type,
            },
        }

        self._post_activity(activity)

class Deleteable(object):
    """ Provides the model with the ability to be deleted """

    def delete(self):
        """ Delete's a model """
        activity = {
            "verb": "delete",
            "object": {
                "id": self.id,
                "objectType": self.object_type,
            }
        }

        self._post_activity(activity)

