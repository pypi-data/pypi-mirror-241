# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prepare_assignment',
 'prepare_assignment.cli',
 'prepare_assignment.core',
 'prepare_assignment.data',
 'prepare_assignment.utils']

package_data = \
{'': ['*'], 'prepare_assignment': ['schemas/*']}

install_requires = \
['gitpython>=3.1.31,<4.0.0',
 'importlib-resources>=5.12.0,<6.0.0',
 'jsonschema>=4.17.3,<5.0.0',
 'multipledispatch>=1.0.0,<2.0.0',
 'prepare-toolbox==0.3.0',
 'ruamel-yaml>=0.17.21,<0.18.0',
 'treelib>=1.7.0,<2.0.0',
 'typer[all]>=0.9.0,<0.10.0',
 'virtualenv>=20.24.5,<21.0.0']

entry_points = \
{'console_scripts': ['prepare = prepare_assignment.cli.main:app']}

setup_kwargs = {
    'name': 'prepare-assignment',
    'version': '0.1.1',
    'description': 'Prepare assignment',
    'long_description': '# Prepare assignment\n\nPrepare assignment is a GitHub Actions inspired helper tool to prepare assignments at Fontys Venlo. The goal is to define jobs inside the `prepare.yml` that indicate how to convert a solution project into a student project.\n\n## Dependencies\n\n- Git\n- Python >=3.8\n\n## Example\n\nFirst we need to have tasks available that can be executed. Take for example a look at the [remove](https://github.com/prepare-assignment/remove) task.\n\nThe tests use a [testproject](https://github.com/prepare-assignment/core/tree/tests/testproject), which contains an example of a `prepare.yml`, see below for convenience.\n\n```yaml\nname: Test project\njobs:\n  prepare:\n    - name: remove out\n      uses: remove\n      with:\n        input:\n          - "out"\n          - "out.txt"\n        force: true\n        recursive: true\n    - name: codestripper\n      id: codestripper\n      uses: codestripper\n      with:\n        include:\n          - "**/*.java"\n          - "pom.xml"\n        working-directory: "solution"\n        verbosity: 5\n    - name: Test a run command with substitution\n      run: echo \'${{ tasks.codestripper.outputs.stripped-files }}\' > out.txt\n```\n\nFor people familiar with GitHub Actions this should look very familiar. We have jobs that indicate what should happen to prepare an assignment. The tasks are defined in their own repositories, if the `uses` tag doesn\'t have a username/organization, it will default to `prepare-assignment`. So for example the `remove` task uses the following repository: [prepare-assignment/remove](https://github.com/prepare-assignment/remove)\n\n## Tasks\n\nThere are three different kind of tasks available:\n\n- Run tasks: these execute a shell command (for now only bash is supported)\n- Python tasks: these execute a python script\n- Composite tasks: these combine multiple tasks into one\n\n### Custom tasks\n\nIt is possible to create custom (python/composite) tasks.\n\n1. Create a repository\n2. Define the properties of the task in `task.yml`, these include\n    - id*: unique identifier\n    - name*: name of the task\n    - description*: short description\n    - runs*: whether it is a python or composite task\n    - inputs: the inputs for the task\n    - outputs: the outputs that get set by the task\n3. Validate that the task definition is correct against the [json schema](https://github.com/prepare-assignment/core/blob/main/prepare_assignment/schemas/task.schema.json)\n4. If python task, create a script that implements desired functionality\n\n',
    'author': 'Bonajo',
    'author_email': 'm.bonajo@fontys.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
