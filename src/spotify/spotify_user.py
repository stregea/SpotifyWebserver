class SpotifyUser:
    """
    Class that will represent a signed-in user from the Spotify API.
    """

    def __init__(self, json_response: dict):
        """
        Construct a user from a response.
        :param json_response: The json response from the Spotify API.
        """
        # Current User Information
        self.country = json_response['display_name'] if 'display_name' in json_response else None
        self.email = json_response['email'] if 'email' in json_response else None
        self.explicit_content = json_response['explicit_content'] if 'explicit_content' in json_response else None
        self.product = json_response['product'] if 'product' in json_response else None

        # General User Information
        self.display_name = json_response['display_name']
        self.external_urls = json_response['external_urls']
        self.followers = json_response['followers']
        self.href = json_response['href']
        self.id = json_response['id']
        self.images = json_response['images']  # list of images.
        self.type = json_response['type']
        self.uri = json_response['uri']

    def get_spotify_uri(self):
        pass

    def create_playlist(self):
        pass

    def get_playlists(self):
        pass

    def add_song_to_playlist(self):
        pass

    def play_song(self):
        pass
