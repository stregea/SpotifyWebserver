class SpotifyImage:

    def __init__(self, info: dict):
        self.url = info['url']
        self.height = info['height']
        self.width = info['width']
