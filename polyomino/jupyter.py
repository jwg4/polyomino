import io

from pretty_poly.image import make_colored_blocks
from pretty_poly.png import _make_png_writer

def solution_to_png(solution):
    data, palette = make_colored_blocks(solution.tiling)
    writer = _make_png_writer(data, palette)
    f = io.BytesIO()
    writer.write(f, data)
    return f.getvalue()
