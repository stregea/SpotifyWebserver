class SpotifyExplicitContent:
    """
    The user's explicit content settings.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyExplicitContent object.
        :param info: The information containing the SpotifyExplicitContent information.
        """
        self.filter_enabled = info['filter_enabled']
        self.filter_locked = info['filter_locked']
