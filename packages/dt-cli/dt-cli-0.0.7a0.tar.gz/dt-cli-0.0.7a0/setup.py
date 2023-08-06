# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dtcli', 'dtcli.scripts']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'asn1crypto>=1.4.0,<2.0.0',
 'click-aliases>=1.0.1,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'cryptography>=3.4.7,<4.0.0']

entry_points = \
{'console_scripts': ['dt = dtcli.scripts.dt:main']}

setup_kwargs = {
    'name': 'dt-cli',
    'version': '0.0.7a0',
    'description': 'Dynatrace CLI',
    'long_description': '# dt-cli — Dynatrace developer\'s toolbox\n\nDynatrace CLI is a command line utility that assists in developing, signing,\nand building extensions for Dynatrace Extension Framework 2.0.\n\n<p>\n  <a href="https://pypi.org/project/dt-cli/"><img alt="PyPI" src="https://img.shields.io/pypi/v/dt-cli?color=blue"></a>\n  <a href="https://github.com/dynatrace-oss/dt-cli/actions/workflows/built-test-release.yml"><img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/dynatrace-oss/dt-cli/build-test-release/main"></a>\n</p>\n\n\n`dt-cli` is currently in **ALPHA**. But it\'s evolving quickly with new\nfeatures for extension development and cluster management to be added soon.\n\n### Features\n\n* Build and sign extensions from source\n* Generate development certificates for extension signing\n* Generate CA certificates for development\n\n## Installation\n\n```shell\npip install dt-cli\n```\n\n## Usage\n\nCurrently there are three basic commands available for working with extensions.\nExtension subcommand has two aliases for convenience: `dt ext` or `dt extensions`.\n\n* `dt extension genca`\n\n  generates CA root certificate and key, required to generate developer certificates\n  and for extension validation. The file containing the certificate (`ca.cert` is\n  the deafult name) needs to be placed on ActiveGates and monitored hosts that will\n  be executing extensions.\n\n  ```shell\n  Usage: dt extension genca [OPTIONS]\n\n    creates CA key and certificate, needed to create developer certificate\n    used for extension signing\n\n    Options:\n    --ca-cert TEXT  CA certificate. Default: ./ca.crt\n    --ca-key TEXT   CA key. Default: ./ca.key\n    -h, --help      Show this message and exit.\n  ```\n\n* `dt extension gendevcert`\n\n  generates a developer certificate used for signing extensions. Please note that\n  there may be multiple developer certificates coming from a single root\n  certificate. It\'s up to your organization to manage them.\n\n  ```shell\n  Usage: dt extension gendevcert [OPTIONS]\n\n    creates developer key and certificate used for extension signing\n\n    Options:\n    --ca-cert TEXT   CA certificate. Default: ./ca.crt\n    --ca-key TEXT    CA key. Default: ./ca.key\n    --dev-cert TEXT  Developer certificate. Default: ./developer.crt\n    --dev-key TEXT   Developer key. Default: ./developer.key\n    -h, --help       Show this message and exit.\n  ```\n\n* `dt extension build`\n  builds distributable extension file from a given directory containing extension files\n  (`./extension` by default). The extension will be signed with a developer certificate and key.\n\n  ```shell\n  Usage: dt extension build [OPTIONS]\n\n    builds extension file from the given extension directory (extension in\n    current dir. is the default)\n\n    Options:\n    --extension-directory TEXT  Directory where extension files are. Default:\n                                ./extension\n\n    --target-directory TEXT     Directory where extension package should be\n                                written. Default: .\n\n    --certificate TEXT          Certificate used for signing. Default:\n                                ./developer.crt\n\n    --private-key TEXT          Private key used for signing. Default:\n                                ./developer.key\n\n    --keep-intermediate-files   Do not delete the signature and `extension.zip\'\n                                files after building extension archive\n\n    -h, --help                  Show this message and exit.\n  ```\n\n## Development\n\nThis tool requires Python 3.8+ and is build with [poetry](https://python-poetry.org/).\nBefore starting, make sure you have a dedicated [virtual environment](https://docs.python.org/3/library/venv.html)\nfor working with this project. Create your virtual environment in project directory:\n\n```shell\npython -m venv env\n````\n\nActivate it before proceeding:\n\n```shell\nsource ./env/bin/activate\n```\n\nInstall `poetry`:\n\n```shell\n$ pip install poetry\n```\n\nNow you can build the project and get the wheel file:\n\n```shell\n$(env) poetry build\n```\n\nThe resulting wheel file can be found in the `dist` folder, e.g. `./dist/dtcli-0.0.1-py3-none-any.whl`\n\nIf you have a separate environment where `dtcli` should be available, you should install the  wheel file there. Simply run the following command:\n\n```shell\n$ pip install dt_cli-0.0.1-py3-none-any.whl\n```\n\nIf you want to start using it in the environment where it was built, you just use this `poetry` command:\n\n```shell\n$ poetry install\n```\n\nFrom this moment you can start using the command line tool directly (or from your code, see a dedicated section below):\n\n```shell\n$ dt --help\n```\n\nEach command contains its own help description, see:\n\n```shell\n$ dt ext build --help\n```\n\n## Testing\n\nRun `pytest` tests\n\n```shell\npoetry run pytest --flake8\n```\n\nRun `mypy` tests\n\n```shell\npoetry run pytest --mypy dtcli --strict\n```\n\nRun test coverage report\n\n```shell\npoetry run pytest --cov . --cov-report html\n```\n\n## Using dt-cli from your Python code\n\nYou may want to use some commands implemented by `dt-cli` directly in your Python code, e.g. to automatically sign your extension in a CI environment.\nHere\'s an example of building an extension programatically, it assumes `dtcli` package is already installed and available in your working environment.\n\n\n```python\nfrom dtcli import building\n\n\nbuilding.build_extension(\n    extension_dir_path = \'./extension\',\n    extension_zip_path = \'./extension.zip\',\n    extension_zip_sig_path = \'./extension.zip.sig\',\n    target_dir_path = \'./dist\',\n    certificate_file_path = \'./developer.crt\',\n    private_key_file_path = \'./developer.key\',\n    keep_intermediate_files=False,\n)\n```\n\n## Contributions\n\nYou are welcome to contribute using Pull Requests to the respective\nrepository. Before contributing, please read our\n[Code of Conduct](https://github.com/dynatrace-oss/dt-cli/blob/main/CODE_OF_CONDUCT.md).\n\n## License\n\n`dt-cli` is an Open Source Project. Please see\n[LICENSE](https://github.com/dynatrace-oss/dt-cli/blob/main/LICENSE) for more information.',
    'author': 'Wiktor Bachnik',
    'author_email': 'wiktor.bachnik@dynatrace.com',
    'maintainer': 'Wiktor Bachnik',
    'maintainer_email': 'wiktor.bachnik@dynatrace.com',
    'url': 'https://github.com/dynatrace-oss/dt-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
