import pathops
from fontTools.pens.recordingPen import RecordingPen

from config import FontConfig
from characters.o import draw_o


def draw_e(pen, font_config: FontConfig, stroke: int):
    """Draw an 'e' from the 'o' shape: add a horizontal crossbar, then cut the bottom-right quarter."""
    # Record the full 'o' shape
    rec = RecordingPen()
    draw_o(rec, font_config=font_config, stroke=stroke)

    o_path = pathops.Path()
    rec.replay(o_path.getPen())

    # Horizontal crossbar at mid-height, spanning the full inner counter
    mid_y = FontConfig.X_HEIGHT / 2
    outer_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2

    bar = pathops.Path()
    bp = bar.getPen()
    bp.moveTo((outer_left, mid_y - stroke / 2))
    bp.lineTo((outer_left, mid_y + stroke / 2))
    bp.lineTo((outer_right, mid_y + stroke / 2))
    bp.lineTo((outer_right, mid_y - stroke / 2))
    bp.closePath()

    result = pathops.op(o_path, bar, pathops.PathOp.UNION, fix_winding=True)

    # Cut the bottom-right quarter: below the crossbar, right half
    cut = pathops.Path()
    cp = cut.getPen()
    cp.moveTo((FontConfig.WIDTH / 2, -50))
    cp.lineTo((FontConfig.WIDTH / 2, mid_y - stroke / 2))
    cp.lineTo((FontConfig.WIDTH + 50, mid_y - stroke / 2))
    cp.lineTo((FontConfig.WIDTH + 50, -50))
    cp.closePath()

    result = pathops.op(result, cut, pathops.PathOp.DIFFERENCE, fix_winding=True)

    # Extend the bottom tail to E_TAIL_RATIO * WIDTH
    tail_x = FontConfig.WIDTH / 2 + (FontConfig.E_TAIL_RATIO * FontConfig.X_WIDTH) / 2
    tail = pathops.Path()
    tp = tail.getPen()
    tp.moveTo((FontConfig.WIDTH / 2, 0))
    tp.lineTo((FontConfig.WIDTH / 2, stroke))
    tp.lineTo((tail_x, stroke))
    tp.lineTo((tail_x, 0))
    tp.closePath()

    result = pathops.op(result, tail, pathops.PathOp.UNION, fix_winding=True)

    result.draw(pen)
