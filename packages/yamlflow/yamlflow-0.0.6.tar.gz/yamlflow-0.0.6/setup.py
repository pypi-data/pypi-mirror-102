# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yamlflow',
 'yamlflow.cli',
 'yamlflow.cli.commands',
 'yamlflow.dockerfiles',
 'yamlflow.dockerfiles.core.base']

package_data = \
{'': ['*'], 'yamlflow.dockerfiles': ['app/*', 'core/torch-cpu/*']}

install_requires = \
['click>=7.0.0,<8.0.0', 'docker>=5.0.0,<6.0.0', 'pyyaml>=5.4.1,<6.0.0']

entry_points = \
{'console_scripts': ['yamlflow = yamlflow.cli:main']}

setup_kwargs = {
    'name': 'yamlflow',
    'version': '0.0.6',
    'description': 'Yet Another ML flow',
    'long_description': '# yamlflow\nYet Another ML flow\n\n## STATUS NOT READY\n\nWe follow `convention over configuration` (also known as coding by convention) software design paradigm.\n\nHere are some of the features the `yamlflow` provides.\n\n\n1. Build and publish your ML solution as a RESTful Web Service `with yaml`.\n    \n    + You don\'t need to write web realated code, or dockerfiles.\n    \n    + You don\'t need to benchmark which python web server or framework is best in terms of performance.\n    \n    + WE do it for you. All the best, packed in.\n\n\n### Project structure \n```\nexamle-project\n    ...\n    ...\n    yamlflow.yaml\n    predictor.py\n    requirements.txt\n```\n\n#### example `yamlflow.yaml`\n```yaml\nkind: Service  # manifest type, `Retrainig` will be added soon\nmeta:\n  name: ml-project # name of your project\n  version: 0.1.0   # version of your project\nbackend:\n  runtime: torch # options are torch, openvino, tensorflow, tensorrt\n  device: cpu    # options are cpu, gpu\nfrontend:\n  predictor: predictor.py # path to predictor.py file\n  requirements: requirements.txt # path to requirements.txt file\n```\n\n### example `predictor.py`\n```py\nimport os\nimport torch\nfrom torchvision import models\n\n\nclass Predictor:\n    """\n    """\n    def __init__(self):\n        """ Model object initialization.\n        """\n        self.model = models.resnet18(pretrained=True)\n\n\n    def pre_process(self, request: dict) -> torch.Tensor:\n        """ Pre_process request given from HTTP call content/type,\n        best performance: python_numpy_numba.\n        """\n        shape = request["data"]\n        return torch.randn(shape)\n\n    \n    def predict(self, model_input: torch.Tensor) -> torch.Tensor:\n        """Can run native in python or using \n        inference servers where no python dependency exists.\n        """\n        with torch.no_grad():\n            return self.model(model_input)\n    \n\n    def post_process(self, model_output: torch.Tensor) -> dict:\n        """Post_process model_output given torch.\n        """\n        return {"data": [model_output.cpu().detach().tolist()]}\n```\n\n### User guide\n```bash\npip install yamlflow\nyamlflow init\nyamlflow build -f flow.yaml\n```\n\n### Developer guide\n```\npyenv install 3.8.6\npoetry env use ~/.pyenv/versions/3.8.6/bin/python\npoetry shell\npoetry install\n```\n',
    'author': 'Sevak Harutyunyan',
    'author_email': 'sevak.g.harutyunyan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sevakharutyunyan/aida',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
