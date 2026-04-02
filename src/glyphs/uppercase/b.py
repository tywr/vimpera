from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect


class UppercaseBGlyph(Glyph):
    name = "uppercase_b"
    unicode = "0x42"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 26
        width = 420
        overlap = stroke / 2
        hx = fc.side_hx
        hy = fc.side_hy

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = 0
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset + fc.h_overshoot
        y2 = fc.ascent
        ymid = y1 + (y2 - y1) / 2

        draw_rect(pen, x1, 0, x1 + stroke, fc.ascent)
        draw_superellipse_loop(
            pen,
            stroke,
            x1 + stroke - width,
            ymid - stroke / 2,
            x1 + stroke + width,
            y2,
            hx,
            hy,
            cut="left",
        )
        draw_superellipse_loop(
            pen,
            stroke,
            x1 + stroke - width,
            0,
            x1 + stroke + width,
            ymid + stroke / 2,
            hx,
            hy,
            cut="left",
        )
