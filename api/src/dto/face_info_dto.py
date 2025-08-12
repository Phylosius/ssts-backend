from api.src.dto.ltbr_rectangle import LTBRRectangle

class FaceInfoDto:
    def __init__(self, image_source_url: str, encodings: list[float], bounding_box: LTBRRectangle):
        self.image_source_url = image_source_url
        self.encodings = encodings
        self.bounding_box = bounding_box

    def to_dict(self):
        return {
            "encodings": self.encodings,
            "boundingBox": self.bounding_box.to_dict(),
            "imageSourceUrl": self.image_source_url
        }