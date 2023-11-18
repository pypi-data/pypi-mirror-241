from typing import Literal
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os

import sysconfig

Location = Literal["top left", "top right", "bottom left", "bottom right"]

_ANN_ANCHOR_POINTS = {
    "top left": (0, 1),
    "top right": (1, 1),
    "bottom left": (0, 0),
    "bottom right": (1, 0),
}


def _get_img_path(logo_type: str):
    BASE_DIR = None

    if os.path.isfile(sysconfig.get_path("platlib") + "/mpl_bsic"):
        BASE_DIR = sysconfig.get_path("platlib") + "/mpl_bsic"
    else:
        BASE_DIR = os.path.dirname(__file__)

    path = BASE_DIR + "/static/bsic_logo_" + logo_type + "_1x.png"

    return path


def _get_annotation_position(ax: Axes, location: Location, fr: float):
    x0, x1 = ax.get_xbound()
    y0, y1 = ax.get_ybound()

    xlen = x1 - x0
    ylen = y1 - y0

    if location == "bottom left":
        pos = (x0 + xlen / fr, y0 + ylen / fr)
    elif location == "top left":
        pos = (x0 + xlen / fr, y1 - ylen / fr)
    elif location == "top right":
        pos = (x1 - xlen / fr, y1 - ylen / fr)
    elif location == "bottom right":
        pos = (x1 - xlen / fr, y0 + ylen / fr)

    return pos


def apply_bsic_logo(
    fig: Figure,
    ax: Axes,
    scale: float = 0.03,
    location: Location = "top left",
    logo_type: Literal["formal", "square"] = "formal",
    alpha: float = 1,
    closeness_to_border: float = 50,
):
    """Apply the BSIC Logo to the Plot.

    You can specify the scale, location, type, alpha, and how close the logo is to the border.
    Since the optimal values for these parameters will value from plot to plot, the suggestion is to tweak them
    util you find the right values for your plot. Choose the location so that the plot and logo overlap as little
    as possible.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The Figure instance from matplotlib.
    ax : matplotlib.axes.Axes
        The Axes instance from matplotlib.
    scale : float, optional
        How much to scale the image, by default 0.03.
    location : Location, optional
        The location to use for the logo, by default "top left".
        Can be "top left", "top right", "bottom left", "bottom right".
    logo_type : Literal["formal", "square"], optional
        Specify the logo to use, by default "formal".
        The Formal logo is the extended one,
        the Square logo includes only the square.
    alpha : float, optional
        The alpha to use for the image (if you want transparency),
        by default 1.
    closeness_to_border : float, optional
        How close the logo should be to the border. A larger value means the logo will be closer to the border,
        by default 50.

    See Also
    --------
    TODO

    Examples
    --------
    TODO
    """

    image_path = _get_img_path(logo_type)
    logo = image.imread(image_path)

    imagebox = OffsetImage(logo, zoom=scale)
    imagebox.image.set_alpha(alpha)

    def gen_ann(ax):
        position = _get_annotation_position(ax, location, closeness_to_border)
        ab = AnnotationBbox(
            imagebox,
            position,
            box_alignment=_ANN_ANCHOR_POINTS[location],
            pad=0,
            frameon=False,
            bboxprops=dict(edgecolor="None"),
        )
        return ab

    # this is to make sure the previous logo is deleted if a new one is added
    ab = ax.add_artist(gen_ann(ax))
    prev_artists = [ab]

    def apply_logo(event):
        ab = gen_ann(ax)
        new_ab = ax.add_artist(ab)

        prev_artists[0].remove()
        prev_artists[0] = new_ab

    fig.canvas.mpl_connect("draw_event", apply_logo)
