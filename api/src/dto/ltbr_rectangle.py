class LTBRRectangle:
    def __init__(self, left: int, top: int, bottom: int, right: int):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def to_dict(self):
        return {
            "left": self.left,
            "top": self.top,
            "bottom": self.bottom,
            "right": self.right
        }
