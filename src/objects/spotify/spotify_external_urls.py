class SpotifyExternalURLs:
    """
    This class contains known external URLs for an album.
    """

    def __init__(self, info: dict):
        """
        Known external URLs for an artist, playlist, etc.
        :param info: The information containing the SpotifyExternalURLs information.
        """

        # The Spotify URL for the object.
        self.spotify: str = info['spotify'] if 'spotify' in info else None
