class SpotifyError:
    """
    Class that will represent an error response from the Spotify API.
    """

    def __init__(self, json_response: dict):
        """
        Construct an error.

        Response Example:
            {
              "error": {
                "status": 400,
                "message": "string"
              }
            }
        :param json_response: The json response from the Spotify API.
        """

        # The error response status. Default of 400.
        self.status: int = json_response['status'] if 'status' in json_response else 400

        # The error response message.
        self.error: str = json_response['error'] if 'error' in json_response else None
