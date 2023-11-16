# Simple-Track-Builder

[![License MIT](https://img.shields.io/pypi/l/Simple-Track-Builder.svg?color=green)](https://github.com/GuignardLab/Simple-Track-Builder/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/Simple-Track-Builder.svg?color=green)](https://pypi.org/project/Simple-Track-Builder)
[![Python Version](https://img.shields.io/pypi/pyversions/Simple-Track-Builder.svg?color=green)](https://python.org)
[![tests](https://github.com/GuignardLab/Simple-Track-Builder/workflows/tests/badge.svg)](https://github.com/GuignardLab/Simple-Track-Builder/actions)
[![codecov](https://codecov.io/gh/GuignardLab/Simple-Track-Builder/branch/main/graph/badge.svg)](https://codecov.io/gh/GuignardLab/Simple-Track-Builder)

A very simple cell tracker from labeled images

----------------------------------

## Installation

You can install `Simple-Track-Builder` via [pip]:

```shell
pip install Simple-Track-Builder
```

To install latest development version :

```shell
pip install git+https://github.com/GuignardLab/Simple-Track-Builder.git
```

## Usage

Once installed, Simple-Track-Builder can be used multiple ways.

### Command line call

Simple-Track-Builder can be called in the terminal the following way:

```shell
simple-track-builder --pathes p1.tiff p2.tiff [...] --output out_test.lT
```

where `p1.tiff`, `p2.tiff`, ... are the pathes to all the images to use in temporal order, from start to finish.

Instead of informing all the pathes manually, one can inform the path format, the starting and ending times:

```shell
simple-track-builder --path-format p{t:d}.tiff --start-time 0 --end-time 10 --output out_test.lT
```

If necessary, the background can be informed using the `--background` parameter.

Finally, a help for `simple-track-builder` can be called the following way:

```shell
simple-track-builder --help
```

### Python

Simple-Track-Builder can be called in Python 2 different ways:

#### Direct function

```python
from simple_track_builder import build_tracks

pathes = ["p1.tiff", "p2.tiff", ...]
out = "test.lT"
build_track(label_image_list=pathes, background=0, out=out)
```

`label_image_list` can also take `np.ndarray`s:

```python
from simple_track_builder import build_tracks
from tifffile import imread
pathes = [imread("p1.tiff"), imread("p2.tiff"), ...]
out = "test.lT"
build_track(label_image_list=pathes, background=0, out=out)
```

That can be usefull when you are running tests and do not want to reload the images each time.

#### Class

For the most modularity, one can use the class itself:

```python
from simple_track_builder import SimpleTrackBuilder
pathes = ["p1.tiff", "p2.tiff", ...]

lT = SimpleTrackBuilder(pathes, background=0)
lT.build_lineages()

lT.write("out.lT")
```

`lT` is a `LineageTree` instance that has all their properties (see [there](https://github.com/leoguignard/LineageTree))

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"Simple-Track-Builder" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

----------------------------------

This library was generated using [Cookiecutter] and a custom made template based on [@napari]'s [cookiecutter-napari-plugin] template.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[pip]: https://pypi.org/project/pip/
[tox]: https://tox.readthedocs.io/en/latest/

[file an issue]: https://github.com/GuignardLab/Simple-Track-Builder/issues