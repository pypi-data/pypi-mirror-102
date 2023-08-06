# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpleicons', 'simpleicons.icons']

package_data = \
{'': ['*'], 'simpleicons': ['_data/*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0', 'reportlab>=3.5.67,<4.0.0', 'svglib>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['generate = scripts.build_package:build']}

setup_kwargs = {
    'name': 'simpleicons',
    'version': '4.20.1',
    'description': 'Use a wide-range of icons derived from the simple-icons/simple-icons repo in python.',
    'long_description': '# simpleicons\nUse a wide-range of icons derived from the [simple-icons](https://github.com/simple-icons/simple-icons) repo in python. Go to [their website](https://simpleicons.org/) for a full list of icons. The slug version (all lowercase and no spaces with some exceptions) must be used for the `icon_name`. The icons folder that accompanies the package has all the files. The package searches for icons by filename.\n\n## Installation\nInstall with `pip install simpleicons`. Keep in mind that this is a fairly large package due to all the icons (a couple of megabytes).\n\n## Usage\n### General Usage\nThe API can then be used as follows, where [ICON SLUG] is replaced by a slug:\n```py\nfrom simpleicons.all import icons\n\n# Get a specific icon by its slug as:\nicons.get(\'[ICON SLUG]\')\n\n# For example:\nicon = icons.get(\'simpleicons\')\n\nprint(icon.__dict__)\n\n"""\n{\n    \'title\': \'Simple Icons\',\n    \'slug\': \'simpleicons\',\n    \'hex\': \'111111\',\n    \'source\': \'https://simpleicons.org/\',\n    \'svg\': \'<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">...</svg>\',\n    \'path\': \'M12 12v-1.5c-2.484 ...\',\n    \'guidelines\': \'https://simpleicons.org/styleguide\',\n    \'license\': {\n        type: \'...\',\n        url: \'https://example.com/\'\n    }\n}\n"""\n```\nNOTE: The `guidelines` entry will be `None` if we do not yet have guidelines data for the icon.\n\nNOTE: The `license` entry will be `None` if we do not yet have license data for the icon.\n\nAlternatively you can import the needed icons individually, where [ICON SLUG] is replaced by a slug:\n```py\n# Import a specific icon by its slug as:\nfrom simpleicons.icons.[ICON SLUG] import icon\n\n# For example:\nfrom simpleicons.icons.simpleicons import icon\n\nprint(icon)\n```\nNOTE: If the icon\'s slug is not compatible with python imports (e.g. it has a dash) you must use importlib to import it:\n```py\nimport importlib\n\nimportlib.import_module(\'simpleicons.icons.[ICON SLUG]\').icon\n\n# For example:\nimportlib.import_module(\'simpleicons.icons.dot-net\').icon\n```\n\nLastly, the `icons` object is also enumerable. This is useful if you want to do a computation on every icon:\n```py\nfrom simpleicons.all import icons\n\nfor (key, icon in icons) {\n    # do stuff\n}\n```\n\n### XML\nThe XML for each icon can be easily manipulated with either of two functions:\n\n`get_xml(icon_name: str, **attrs) -> ElementTree`\n\n```py\nfrom simpleicons.icon_xml import get_xml\n\n# blue logo (simply adds <svg fill="blue"></svg>)\nget_xml("github", fill="blue")\n```\n\n`get_xml_bytes(icon_name: str, **attrs) -> bytes`\n\n```py\nfrom simpleicons.icon_xml import get_xml_bytes\n\nget_xml_bytes("github", fill="blue")\n```\n\nTo simply get the unparsed XML string for each icon, use `get_str(icon_name: str) -> str`:\n\n```py\nfrom simpleicons.icon_xml import get_str\n\nget_str("github")\n```\n\nThis string representation will allow for quick implementation in web pages, however it cannot be manipulated. Use `get_xml_bytes` for easy web page implementation alongside manipulation.\n\n### Image\nIcons can be converted to PIL Images with `icon_to_image(icon_xml: bytes, bg: int=0xffffff, scale: Tuple[int, int]=(1, 1)) -> Image`:\n\n```py\nfrom simpleicons.icon_xml import get_xml_bytes\nfrom simpleicons.image import icon_to_image\n\nxml_bytes = get_xml_bytes("github", fill="blue")\n\n# black background and x5 scale\nimg = icon_to_image(xml_bytes, bg=0x000000, scale=(5, 5))\n\n# manipulate PIL Image\nimg.putalpha(32)\nimg.save("github.png")\n```\n',
    'author': 'Sachin Raja',
    'author_email': 'sachinraja2349@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
