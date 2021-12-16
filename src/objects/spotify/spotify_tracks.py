class SpotifyTracks:
    """
    The tracks of an album or playlist.
    """

    def __init__(self, json_response):
        """
        Construct a SpotifyPlaylistTracks object from a response.
        :param json_response: The response from the Spotify API.
        """

        # A link to the Web API endpoint returning the full result of the request.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # The requested content. Todo: find out structure of objects - may be a list of 'Track'
        self.items: [object] = [item for item in json_response['items']] if 'items' in json_response else []

        # The maximum number of items in the response (as set in the query or by default).
        self.limit: int = json_response['limit'] if 'limit' in json_response else -1

        # URL to the next page of items. ( null if none)
        self.next: str = json_response['next'] if 'next' in json_response else None

        # The offset of the items returned (as set in the query or by default)
        self.offset: int = json_response['offset'] if 'offset' in json_response else -1

        # URL to the previous page of items. ( null if none)
        self.previous: str = json_response['previous'] if 'previous' in json_response else None

        # The total number of items available to return.
        self.total: int = json_response['total'] if 'total' in json_response else -1
