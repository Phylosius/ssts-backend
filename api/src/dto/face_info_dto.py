from api.src.dto.ltbr_rectangle import LTBRRectangle
from api.src.model.face_id import FaceId


class FaceInfoDto:
    def __init__(self, image_source_url: str, encodings: list[float], bounding_box: LTBRRectangle):
        self.image_source_url = image_source_url
        self.encodings = encodings
        self.bounding_box = bounding_box

    @classmethod
    def from_model(cls, model: FaceId):
        # TODO: get image source url
        # TODO: get bounding box
        return cls('', list(model.face_encodings), None)

    def to_dict(self):
        return {
            "encodings": self.encodings,
            "boundingBox": self.bounding_box.to_dict(),
            "imageSourceUrl": self.image_source_url
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            image_source_url=data.get('imageSourceUrl'),
            encodings=data.get('encodings'),
            bounding_box=LTBRRectangle(
                left=data.get('boundingBox').get('left'),
                top=data.get('boundingBox').get('top'),
                bottom=data.get('boundingBox').get('bottom'),
                right=data.get('boundingBox').get('right')
            )
        )