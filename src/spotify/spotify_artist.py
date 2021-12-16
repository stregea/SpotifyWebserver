class SpotifyArtist:

    def __init__(self, json_response: dict):
        """
        Construct an Artist object from a response.

        Response Example:
            {
              "external_urls": {
                "spotify": "string"
              },
              "followers": {
                "href": "string",
                "total": 0
              },
              "genres": [
                "Prog rock",
                "Grunge"
              ],
              "href": "string",
              "id": "string",
              "images": [
                {
                  "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228\n",
                  "height": 300,
                  "width": 300
                }
              ],
              "name": "string",
              "popularity": 0,
              "type": "artist",
              "uri": "string"
            }
        :param json_response: The response from the Sport
        """
        self.external_urls = json_response['external_urls']
        self.followers = json_response['followers']
        self.genres = json_response['genres']
        self.href = json_response['href']
        self.id = json_response['id']
        self.images = json_response['images'] # list of images
        self.name = json_response['name']
        self.popularity = json_response['popularity']
        self.type = json_response['type']
        self.uri = json_response['uri']
