from objects.spotify.spotify_explicit_content import SpotifyExplicitContent
from objects.spotify.spotify_user import SpotifyUser


class SpotifyCurrentUser(SpotifyUser):
    """
    Class that will represent the current user.
    """

    def __init__(self, json_response: dict):
        """
        Construct the current user from a response.
        :param json_response: The json response from the Spotify API.
        """
        super().__init__(json_response)

        # The country of the user, as set in the user's account profile. An ISO 3166-1 alpha-2 country code.
        # This field is only available when the current user has granted access to the user-read-private scope.
        self.country: str = json_response['display_name'] if 'display_name' in json_response else None

        # The user's email address, as entered by the user when creating their account.
        # Important! This email address is unverified; there is no proof that it actually belongs to the user.
        # This field is only available when the current user has granted access to the user-read-email scope.
        self.email: str = json_response['email'] if 'email' in json_response else None

        # The user's explicit content settings.
        # This field is only available when the current user has granted access to the user-read-private scope.
        self.explicit_content: SpotifyExplicitContent = SpotifyExplicitContent(json_response['explicit_content']) if 'explicit_content' in json_response and json_response['explicit_content'] is not None else None

        # The user's Spotify subscription level: "premium", "free", etc.
        # (The subscription level "open" can be considered the same as "free".)
        # This field is only available when the current user has granted access to the user-read-private scope.
        self.product: str = json_response['product'] if 'product' in json_response else None
