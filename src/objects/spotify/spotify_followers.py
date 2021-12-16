class SpotifyFollowers:
    """
    This class contains information about the followers of the artist, user, etc.
    """

    def __init__(self, info: dict):
        """
        Information about the followers of an artist.
        :param info: The information containing the follower information.
        """

        # This will always be set to null, as the Web API does not support it at the moment.
        self.href: str = info['href'] if 'href' in info else None

        # The total number of followers.
        self.total: int = info['total'] if 'total' in info else -1
