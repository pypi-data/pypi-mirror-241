# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scfile',
 'scfile.files',
 'scfile.files.output',
 'scfile.files.source',
 'scfile.reader',
 'scfile.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.7,<9.0.0', 'lz4>=4.3.2,<5.0.0']

entry_points = \
{'console_scripts': ['build = build:build']}

setup_kwargs = {
    'name': 'sc-file',
    'version': '1.5.1',
    'description': '',
    'long_description': '# Converting STALCRAFT Files Library\n\nLibrary for converting encrypted stalcraft game files, such as models and textures into well-known formats. \\\nYou can use compiled cli utility from [Releases](https://github.com/onejeuu/sc-file/releases) page.\n\n\n### Formats\n\n`.mcsa` `->` `.obj` \\\n`.mic` `->` `.png` \\\n`.ol` `->` `.dds`\n\n\n## Install\n\n### Pip\n```console\npip install sc-file -U\n```\n\n<details>\n<summary>Manual</summary>\n\n```console\ngit clone git@github.com:onejeuu/sc-file.git\n```\n\n```console\ncd sc-file\n```\n\n```console\npoetry install\n```\n</details>\n\n## Usage\n\n### Simple\n```python\nfrom scfile.utils import convert\n\nconvert.mcsa_to_obj("path/to/file.mcsa", "path/to/file.obj")\nconvert.mic_to_png("path/to/file.mic", "path/to/file.png")\nconvert.ol_to_dds("path/to/file.ol", "path/to/file.dds")\n```\n\n### Advanced\n```python\nfrom scfile import OlFile, BinaryReader\n\nwith BinaryReader("path/to/file.ol") as reader:\n    dds = OlFile(reader).to_dds()\n\nwith open("path/to/file.dds", "wb") as fp:\n    fp.write(dds)\n```\n\n### CLI Utility\n\n```console\nscfile path/to/file.mcsa\n```\n\n```console\nscfile path/to/file.ol --output path/to/file.dds\n```\n\n\n## Build\n\n```console\npoetry install\n```\n\n```console\npoetry run build\n```\n',
    'author': 'onejeuu',
    'author_email': 'bloodtrail@beber1k.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<3.13',
}


setup(**setup_kwargs)
