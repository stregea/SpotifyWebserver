class SpotifyRestrictions:
    """
    Included in the response when a content restriction is applied.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyRestrictions object.
        :param info: The information containing the SpotifyRestrictions information.
        """
        self.reason = info['reason']
