import numpy as np
import scipy.ndimage as ndimage
from scipy.spatial.distance import cdist
from LineageTree import lineageTree
from tifffile import imread


class SimpleTrackBuilder(lineageTree):
    """SimpleTrackBuilder is a extension of lineageTree,
    it builds lineage trees from label images

    It takes as input a list of `np.ndarray` that represent
    all the label images in temporal order.
    It can as well take a list of pathes to tiff images,
    again it has to be ordered in time.
    """

    @property
    def center_of_mass(self):
        if not hasattr(self, "_center_of_mass"):
            self.compute_centers_of_mass()
        return self._center_of_mass

    def prepare_lineage_structure(self):
        self.lT2label = {}
        self.label2lT = {}
        current_id = 0
        for t, com in self.center_of_mass.items():
            labels = sorted(com)
            lT2label = {
                id_: (t, label)
                for id_, label in zip(
                    range(current_id, current_id + len(labels)), labels
                )
            }
            current_id += len(labels)
            label2lT = {v: k for k, v in lT2label.items()}
            self.lT2label.update(lT2label)
            self.label2lT.update(label2lT)
            self.time_nodes[t] = list(lT2label)
            self.pos.update(
                (label2lT[(t, label)], np.array(com[label])) for label in labels
            )
            self.time.update((label2lT[(t, label)], t) for label in labels)
            self.nodes.update(label2lT[(t, label)] for label in labels)

    def compute_centers_of_mass(self):
        self._center_of_mass = {}
        for t, im in enumerate(self.label_image_list):
            if not isinstance(im, np.ndarray):
                im = imread(im)
            labels = np.unique(im[im != self.background])
            self._center_of_mass[t] = dict(
                zip(
                    labels,
                    ndimage.center_of_mass(np.ones_like(im), im, labels),
                )
            )

    def build_lineages(self):
        """Build the a simple lineage that assigned
        each object at time `t+dt` to its closest object
        at time `t`.

        The output is stored as an adjacency list in:
            - self.successor for the forward tree
            - self.predecessor for the backward tree
        """
        if not hasattr(self, "lT2label"):
            self.prepare_lineage_structure()
        times = sorted(self.time_nodes)
        for i, prev_time in enumerate(times[:-1]):
            next_time = times[i + 1]
            prev_labels = np.array(self.time_nodes[prev_time])
            next_labels = np.array(self.time_nodes[next_time])
            prev_pos = np.array([self.pos[c] for c in prev_labels])
            next_pos = np.array([self.pos[c] for c in next_labels])
            dist_map = cdist(prev_pos, next_pos)
            mapping = list(
                zip(prev_labels[np.argmin(dist_map, axis=0)], next_labels)
            )
            for c1, c2 in mapping:
                self.successor.setdefault(c1, []).append(c2)
                self.predecessor.setdefault(c2, []).append(c1)

    def __init__(self, label_image_list: list, background: int = 0):
        """Initialise the lineage tree builder.
        The class takes as an input a list of labeled images and optionally
        a background value (its default value is `0`)

        Args:
            label_image_list (list(str | Path) | list(np.ndarray)): list of label images.
                It can either be pathes to tiff files or np.ndarrays
            background (int): value of the background in the label images (default `0`)
        """
        super().__init__()
        self.background = background
        self.label_image_list = label_image_list


def build_tracks(
    label_image_list: list, background: int = 0, out: str = "out.lT"
):
    sp = SimpleTrackBuilder(label_image_list, background)
    sp.build_lineages()
    sp.write(out)


def script_run():
    import argparse

    parser = argparse.ArgumentParser(
        prog="build-lineage-tree",
        description=(
            "Build a lineage tree from label images."
            " !!! Either pathes or path-format has to be informed."
            " If path-format is informed then start-time AND end-time"
            " have to be informed too. !!!"
        ),
    )
    parser.add_argument(
        "--pathes",
        type=str,
        nargs="+",
        metavar="path_n.tiff",
        help="all the pathes to use",
    )
    parser.add_argument(
        "--path-format",
        type=str,
        metavar="path{t:0xd}.tiff",
        help=(
            "format of the pathes to use (with {t:0xd} for the time)"
            "for example /path/to/data/im_t{t:05d}.tiff"
        ),
    )
    parser.add_argument(
        "--start-time",
        type=int,
        metavar="t_start",
        help=("starting time if --path-format is given"),
    )
    parser.add_argument(
        "--end-time",
        type=int,
        metavar="t_end",
        help=("ending time if --path-format is given"),
    )
    parser.add_argument(
        "--output",
        type=str,
        metavar="out_path.lT",
        help="Path to the output lineage tree (default out.lT)",
        default="out.lT",
    )
    parser.add_argument(
        "--background",
        type=int,
        default=0,
        metavar="bckgrnd",
        help="value of the background",
    )

    args = parser.parse_args()
    if args.pathes is None and args.path_format is None:
        parser.print_help()
        exit()
    elif args.pathes is not None:
        pathes = args.pathes
    else:
        if args.start_time is None or args.end_time is None:
            parser.print_help()
            exit()
        pathes = [
            args.path_format.format(t=t)
            for t in range(args.start_time, args.end_time + 1)
        ]

    build_tracks(pathes, args.background, args.output)
