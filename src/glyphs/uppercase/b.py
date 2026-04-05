from glyph import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect


class UppercaseBGlyph(Glyph):
    name = "uppercase_b"
    unicode = "0x42"
    offset = 0
    loop_ratio = 1  # Horizontal split between left stem and loops
    upper_ratio = 0.9  # Upper loop width as a fraction of the lower loop width
    hx = 200
    hy = 200

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="ascent",
            overshoot_right=True,
        )
        lower_x1 = b.x1 + (1 - self.loop_ratio) * b.width
        lower_x2 = b.x2
        lower_width = lower_x2 - lower_x1
        upper_width = self.upper_ratio * lower_width
        delta = lower_width - upper_width
        upper_x1 = lower_x1 + delta / 2
        upper_x2 = lower_x2 - delta / 2
        # gap_x = upper_x2 - dc.stroke + (lower_x2 - upper_x2) * 0.63
        gap_x = upper_x2 - dc.stroke + 2.5 * dc.gap

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke, dc.ascent)

        # Upper loop (narrower, displaced left)
        draw_superellipse_arch(
            pen,
            dc.stroke,
            upper_x1,
            b.ymid - dc.stroke / 2,
            upper_x2,
            b.y2,
            self.hx,
            self.hy,
            offset=0.75 * dc.stroke - dc.gap / 2,
            side="bottom",
            cut="left",
        )
        # Lower loop (full width)
        draw_superellipse_arch(
            pen,
            dc.stroke,
            lower_x1,
            0,
            lower_x2,
            b.ymid + dc.stroke / 2,
            self.hx,
            self.hy,
            offset=0.75 * dc.stroke - dc.gap / 2,
            side="top",
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - dc.stroke, upper_x2 - upper_width / 2, b.y2)
        draw_rect(pen, b.x1, 0, b.x2 - lower_width / 2, dc.stroke)
        draw_rect(
            pen,
            b.x1,
            b.ymid - dc.stroke / 2,
            gap_x,
            b.ymid + dc.stroke / 2,
        )
