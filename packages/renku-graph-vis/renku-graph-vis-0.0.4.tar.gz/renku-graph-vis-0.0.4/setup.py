# -*- coding: utf-8 -*-
#
# Gabriele Barni [UniGe], Volodymyr Savchenko [EPFL]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

install_requires = [
    'deepdiff',
    'pydotplus',
    'rdflib',
    'bs4',
    'renku>=2.7,<3',
    'pyvis==0.3.0',
    'pydotplus',
    'lockfile'
]

packages = find_packages()
version_file = open('VERSION')

setup(
    name='renku-graph-vis',
    description='Renku Graph Vis plugin',
    keywords='Renku Graph Vis',
    license='Apache License 2.0',
    author='Gabriele Barni, Volodymyr Savchenko',
    author_email='',
    install_requires=install_requires,
    python_requires='>=3.9,<3.12',
    packages=packages,
    entry_points={
        "renku.cli_plugins": ["graphvis = renkugraphvis.plugin:graphvis"],
        "jupyter_serverproxy_servers": ["interactive_graph = renkugraphvis:setup_graph_visualizer"]
    },
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    version = version_file.read().strip(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 4 - Beta',
    ],
)
