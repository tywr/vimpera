from math import atan, cos
from glyph import Glyph
from shapes.rect import draw_rect

# from shapes.polygon import draw_polygon
from shapes.parallelogramm import draw_parallelogramm


class LowercaseZGlyph(Glyph):
    name = "lowercase_z"
    unicode = "0x7A"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)

        # Top and bottom bars
        draw_rect(pen, b.x1, dc.x_height - dc.stroke, b.x2, dc.x_height)
        draw_rect(pen, b.x1, 0, b.x2, dc.stroke)
        # Diagonal stroke
        draw_parallelogramm(
            pen, dc.stroke, b.x1, b.y1 + dc.stroke, b.x2, b.y2 - dc.stroke
        )
