from simple_track_builder import SimpleTrackBuilder
import numpy as np


def test_module():
    im1 = np.array(
        [
            [0, 1, 0],
            [0, 0, 2],
            [0, 0, 0],
        ]
    )
    im2 = np.array(
        [
            [0, 2, 0],
            [0, 0, 0],
            [0, 3, 1],
        ]
    )

    sp = SimpleTrackBuilder([im1, im2])
    sp.build_lineages()

    assert sorted(sp[sp.label2lT[0, 1]]) == sorted([sp.label2lT[1, 2]])
    assert sorted(sp[sp.label2lT[0, 2]]) == sorted([sp.label2lT[1, 1], sp.label2lT[1, 3]])