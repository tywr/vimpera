from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class UppercaseAGlyph(Glyph):
    name = "uppercase_a"
    unicode = "0x41"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = fc.body_width + fc.h_overshoot
        loop_ratio = fc.a_ratio
        hx = fc.a_hx
        hy = fc.a_hy
        cap_hx = 200
        cap_hy = 200
        len_cap = 235

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = 0
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset
        y2 = fc.ascent
        xmid = x1 + (x2 - x1) / 2

