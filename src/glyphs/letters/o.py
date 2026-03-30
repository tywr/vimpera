from config import FontConfig as fc
from shapes.superellipse_loop import draw_superellipse_loop


def draw_o(
    pen,
    stroke: int,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2 + fc.o_offset
    y1 = -fc.overshoot
    x2 = fc.width / 2 + fc.o_width / 2 + stroke / 2 + fc.o_offset
    y2 = fc.x_height + fc.overshoot
    draw_superellipse_loop(pen, stroke, x1, y1, x2, y2, fc.o_hx, fc.o_hy)
