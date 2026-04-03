from math import atan, cos, sin, sqrt, asin, atan2
from glyph import Glyph
from shapes.rect import draw_rect
from shapes.polygon import draw_polygon


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    offset = 10
    bowl_width = 320
    neck_len = 100
    width_ratio = 1
    neck_ratio = 0.35

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        x_neck = b.x1 + self.neck_ratio * b.width

        # Angle of each diagonal branch
        w = b.x2 - x_neck
        h = dc.x_height / 2 - dc.stroke / 2
        s = dc.stroke
        delta = (s * (h * sqrt(w**2 + h**2 - s**2) - s * w)) / (h**2 - s**2)
        theta = atan2(h, w - delta)
        # delta = s / cos(theta)

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke, dc.ascent)
        # Middle junction connecting stem to branches
        draw_rect(
            pen,
            b.x1 + dc.stroke,
            b.ymid - dc.stroke / 2,
            x_neck,
            b.ymid + dc.stroke / 2,
        )
        # Upper branch (stem to top-right)
        draw_polygon(
            pen,
            points=[
                (x_neck, dc.x_height / 2 + dc.stroke / 2),
                (b.x2 - delta, dc.x_height),
                (b.x2, dc.x_height),
                (x_neck + delta, dc.x_height / 2 + dc.stroke / 2),
                (
                    x_neck + delta - dc.stroke * cos(theta),
                    dc.x_height / 2 + dc.stroke / 2 - dc.stroke * sin(theta),
                ),
                (x_neck, dc.x_height / 2 - dc.stroke / 2),
            ],
        )
        # Lower branch (stem to bottom-right)
        draw_polygon(
            pen,
            points=[
                (x_neck, dc.x_height / 2 + dc.stroke / 2),
                (
                    x_neck + delta - dc.stroke * cos(theta),
                    dc.x_height / 2 - dc.stroke / 2 + dc.stroke * sin(theta),
                ),
                (x_neck + delta, dc.x_height / 2 - dc.stroke / 2),
                (b.x2, 0),
                (b.x2 - delta, 0),
                (x_neck, dc.x_height / 2 - dc.stroke / 2),
            ],
        )
