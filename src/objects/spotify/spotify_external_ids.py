class SpotifyExternalIDs:
    """
    Class to represent external ID's.
    """

    def __init__(self, json_response):
        """
        Construct a SpotifyExternalIDs object from a response.
        :param json_response: The information containing the SpotifyExternalIDs information.
        """

        # International Standard Recording Code
        # http://en.wikipedia.org/wiki/International_Standard_Recording_Code
        self.isrc: str = json_response['isrc'] if 'isrc' in json_response else None

        # International Article Number
        # http://en.wikipedia.org/wiki/International_Article_Number_%28EAN%29
        self.ean: str = json_response['ean'] if 'ean' in json_response else None

        # Universal Product Code
        # http://en.wikipedia.org/wiki/Universal_Product_Code
        self.upc: str = json_response['upc'] if 'upc' in json_response else None
