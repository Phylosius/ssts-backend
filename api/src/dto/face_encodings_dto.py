
class EncodingsMatchInfoDTO:
    def __init__(self, encodings: list, is_matches: bool, distance: float):
        self.encodings = encodings
        self.is_matches = is_matches
        self.distance = distance

    def to_dict(self):
        return {
            "encodings": self.encodings,
            "isMatches": self.is_matches,
            "distance": self.distance
        }