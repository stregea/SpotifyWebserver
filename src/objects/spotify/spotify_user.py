from objects.spotify.spotify_explicit_content import SpotifyExplicitContent
from objects.spotify.spotify_external_urls import SpotifyExternalURLs
from objects.spotify.spotify_followers import SpotifyFollowers
from objects.spotify.spotify_image import SpotifyImage


class SpotifyUser:
    """
    Class that will represent a signed-in user from the Spotify API.
    """

    def __init__(self, json_response: dict):
        """
        Construct a user from a response.
        :param json_response: The json response from the Spotify API.
        """
        # --- Current User Information ---

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

        # --- General User Information ---

        # The name displayed on the user's profile. null if not available.
        self.display_name: str = json_response['display_name'] if 'display_name' in json_response else None

        # Known external URLs for this user.
        self.external_urls: SpotifyExternalURLs = SpotifyExternalURLs(json_response['external_urls']) if 'external_urls' in json_response and json_response['external_urls'] is not None else None

        # Information about the followers of the user.
        self.followers: SpotifyFollowers = SpotifyFollowers(json_response['followers']) if 'followers' in json_response and json_response['followers'] is not None else None

        # A link to the Web API endpoint for this user.
        self.href: str = json_response['href'] if 'href' in json_response else None

        # The Spotify user ID for the user.
        self.id: str = json_response['id'] if 'id' in json_response else None

        # The user's profile image.
        self.images: [SpotifyImage] = [SpotifyImage(image) for image in json_response['images']] if 'images' in json_response and json_response['images'] is not None else []

        # The object type: "user"
        self.type: str = json_response['type'] if 'type' in json_response else None

        # The Spotify URI for the user.
        self.uri: str = json_response['uri'] if 'uri' in json_response else None
