# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adaptgym',
 'adaptgym.envs',
 'adaptgym.envs.cdmc',
 'adaptgym.envs.cdmc.rl',
 'adaptgym.envs.cdmc.suite',
 'adaptgym.envs.cdmc.suite.common',
 'adaptgym.envs.crafter',
 'adaptgym.envs.distracting_control',
 'adaptgym.envs.distracting_control.data',
 'adaptgym.envs.playground',
 'adaptgym.envs.playground.arenas',
 'adaptgym.envs.playground.arenas.assets',
 'adaptgym.envs.playground.labmaze',
 'adaptgym.envs.playground.labmaze.assets',
 'adaptgym.envs.playground.policies',
 'adaptgym.envs.playground.suite',
 'adaptgym.envs.playground.tasks',
 'adaptgym.envs.playground.walkers']

package_data = \
{'': ['*'],
 'adaptgym.envs.distracting_control.data': ['bmx-bumps/*',
                                            'boat/*',
                                            'flamingo/*'],
 'adaptgym.envs.playground.arenas.assets': ['outdoor_natural/*', 'pitch/*'],
 'adaptgym.envs.playground.labmaze.assets': ['sky_01/*',
                                             'sky_02/*',
                                             'sky_03/*',
                                             'style_01/*',
                                             'style_02/*',
                                             'style_03/*',
                                             'style_04/*',
                                             'style_05/*',
                                             'style_black/*',
                                             'style_gray/*',
                                             'style_white/*'],
 'adaptgym.envs.playground.walkers': ['assets/*', 'assets/jumping_ball/*']}

install_requires = \
['Pillow==8.2.0',
 'bidict==0.22.1',
 'dm-control==1.0.7',
 'dm-env==1.5',
 'dm-tree==0.1.7',
 'gym==0.18.3',
 'matplotlib>=3.4.2',
 'numpy>=1.22',
 'opencv-python>=4.0.0',
 'pandas>=1.2,<1.4',
 'protobuf==3.20.3',
 'pytest>=5.2,<6.0',
 'scipy>=1.7.0']

setup_kwargs = {
    'name': 'adaptgym',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Isaac Kauvar',
    'author_email': 'ikauvar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
