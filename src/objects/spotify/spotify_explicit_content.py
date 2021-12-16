class SpotifyExplicitContent:
    """
    The user's explicit content settings.
    """

    def __init__(self, info: dict):
        """
        The user's explicit content settings.
        This field is only available when the current user has granted access to the user-read-private scope.
        :param info: The information containing the SpotifyExplicitContent information.
        """

        # When True, indicates that explicit content should not be played.
        self.filter_enabled: bool = info['filter_enabled'] if 'filter_enabled' in info else False

        # When True, indicates that the explicit content setting is locked and can't be changed by the user.
        self.filter_locked: bool = info['filter_locked'] if 'filter_locked' in info else False
