# yamlflow
Yet Another ML flow

## STATUS NOT READY

We follow `convention over configuration` (also known as coding by convention) software design paradigm.

Here are some of the features the `yamlflow` provides.


1. Build and publish your ML solution as a RESTful Web Service `with yaml`.
    
    + You don't need to write web realated code, or dockerfiles.
    
    + You don't need to benchmark which python web server or framework is best in terms of performance.
    
    + WE do it for you. All the best, packed in.


### Project structure 
```
examle-project
    ...
    ...
    yamlflow.yaml
    predictor.py
    requirements.txt
```

#### example `yamlflow.yaml`
```yaml
kind: Service  # manifest type, `Retrainig` will be added soon
meta:
  name: ml-project # name of your project
  version: 0.1.0   # version of your project
backend:
  runtime: torch # options are torch, openvino, tensorflow, tensorrt
  device: cpu    # options are cpu, gpu
frontend:
  predictor: predictor.py # path to predictor.py file
  requirements: requirements.txt # path to requirements.txt file
```

### example `predictor.py`
```py
import os
import torch
from torchvision import models


class Predictor:
    """
    """
    def __init__(self):
        """ Model object initialization.
        """
        self.model = models.resnet18(pretrained=True)


    def pre_process(self, request: dict) -> torch.Tensor:
        """ Pre_process request given from HTTP call content/type,
        best performance: python_numpy_numba.
        """
        shape = request["data"]
        return torch.randn(shape)

    
    def predict(self, model_input: torch.Tensor) -> torch.Tensor:
        """Can run native in python or using 
        inference servers where no python dependency exists.
        """
        with torch.no_grad():
            return self.model(model_input)
    

    def post_process(self, model_output: torch.Tensor) -> dict:
        """Post_process model_output given torch.
        """
        return {"data": [model_output.cpu().detach().tolist()]}
```

### User guide
```bash
pip install yamlflow
yamlflow init
yamlflow build -f flow.yaml
```

### Developer guide
```
pyenv install 3.8.6
poetry env use ~/.pyenv/versions/3.8.6/bin/python
poetry shell
poetry install
```
