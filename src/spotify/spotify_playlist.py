from spotify.spotify_image import SpotifyImage
from spotify.spotify_user import SpotifyUser


class SpotifyPlaylist:
    """
    Class to represent a spotify playlist.
    """

    def __init__(self, json_response: dict):
        self.collaborative = json_response['collaborative']
        self.description = json_response['description']
        self.external_urls = json_response['external_urls']
        self.followers = json_response['external_urls']
        self.href = json_response['href']
        self.id = json_response['id']
        self.images = [SpotifyImage(image) for image in json_response['images']]
        self.name = json_response['name']
        self.owner = SpotifyUser(json_response['owner'])
        self.public = json_response['public']
        self.snapshot_id = json_response['snapshot_id']
        self.tracks = json_response['tracks']  # todo: build this object
        self.type = json_response['type']
        self.uri = json_response['uri']

    # get, create, modify etc.
