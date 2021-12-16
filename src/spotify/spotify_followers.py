class SpotifyFollowers:
    """
    This class contains information about the followers of the artist.
    """
    def __init__(self, info: dict):
        """
        Construct a SpotifyFollowers object.
        :param info: The information containing the follower information.
        """
        self.href = info['href']
        self.total = info['total']
