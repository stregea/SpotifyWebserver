class SpotifyError:
    """
    Class that will represent an error response from the Spotify API.
    """

    def __init__(self, json_response: dict):
        """
        Construct an error.
        param json_response: The json response from the Spotify API.
        """
        self.error = json_response['error']
