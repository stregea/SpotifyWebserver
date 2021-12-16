class SpotifyImage:
    """
    Object that contains information relevant for an image.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyImage object.
        :param info: The information containing the SpotifyImage information.
        """
        self.url = info['url']
        self.height = info['height']
        self.width = info['width']
