class SpotifyRestrictions:
    """
    Included in the response when a content restriction is applied.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyRestrictions object.
        :param info: The information containing the SpotifyRestrictions information.
        """

        # The reason for the restriction. Albums may be restricted if the content is not available in a given market,
        # to the user's subscription type, or when the user's account is set to not play explicit content.
        # Additional reasons may be added in the future.
        self.reason: str = info['reason'] if 'reason' in info else None
