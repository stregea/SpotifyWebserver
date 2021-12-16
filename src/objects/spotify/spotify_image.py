class SpotifyImage:
    """
    Class that contains information relevant for an image.
    """

    def __init__(self, info: dict):
        """
        Construct a SpotifyImage object from a response.
        :param info: The information containing the SpotifyImage information.
        """

        # The source URL of the image.
        self.url: str = info['url'] if 'url' in info else None

        # The image height in pixels.
        self.height: int = info['height'] if 'height' in info else -1

        # The image width in pixels.
        self.width: int = info['width'] if 'width' in info else -1
