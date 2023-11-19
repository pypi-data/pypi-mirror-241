# Converting STALCRAFT Files Library

Library for converting encrypted stalcraft game files, such as models and textures into well-known formats. \
You can use compiled cli utility from [Releases](https://github.com/onejeuu/sc-file/releases) page.


### Formats

`.mcsa` `->` `.obj` \
`.mic` `->` `.png` \
`.ol` `->` `.dds`


## Install

### Pip
```console
pip install sc-file -U
```

<details>
<summary>Manual</summary>

```console
git clone git@github.com:onejeuu/sc-file.git
```

```console
cd sc-file
```

```console
poetry install
```
</details>

## Usage

### Simple
```python
from scfile.utils import convert

convert.mcsa_to_obj("path/to/file.mcsa", "path/to/file.obj")
convert.mic_to_png("path/to/file.mic", "path/to/file.png")
convert.ol_to_dds("path/to/file.ol", "path/to/file.dds")
```

### Advanced
```python
from scfile import OlFile, BinaryReader

with BinaryReader("path/to/file.ol") as reader:
    dds = OlFile(reader).to_dds()

with open("path/to/file.dds", "wb") as fp:
    fp.write(dds)
```

### CLI Utility

```console
scfile path/to/file.mcsa
```

```console
scfile path/to/file.ol --output path/to/file.dds
```


## Build

```console
poetry install
```

```console
poetry run build
```
