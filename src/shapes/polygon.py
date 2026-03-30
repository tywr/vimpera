def draw_polygon(pen, points):
    """Draw a polygon from a list of (x, y) points."""
    pen.moveTo(points[0])
    for pt in points[1:]:
        pen.lineTo(pt)
    pen.closePath()
