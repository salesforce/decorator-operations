#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGES = [
    "decoratorOperations",
    "decoratorOperations.debounce_functions",
    "decoratorOperations.throttle_functions",
]

PACKAGE_REQUIREMENTS = []

setuptools.setup(
    name="decoratorOperations",
    version="0.0.1",
    author="franck.barbedor",
    author_email="franck.barbedor@salesforce.com",
    description="Rxjs-like annotations for python functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salesforce/decorator-operations",
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=PACKAGE_REQUIREMENTS,
    test_requirements=["pytest==5.4.1"],
)
