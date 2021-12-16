class SpotifyExternalURLs:
    """
    This class contains known external URLs for an album.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyExternalURLs object.
        :param info: The information containing the SpotifyExternalURLs information.
        """
        self.spotify = info['spotify']
