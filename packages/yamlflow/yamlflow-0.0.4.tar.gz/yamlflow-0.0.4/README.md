# yamlflow
Yet Another ML flow

## STATUS NOT READY

This is only the skeleton of an example project.
The actual code of the `example-project` will be added soon!

```
examle-project
    ...
    ...
    flow.yaml
    predictor.py
    requirements.txt
```

#### example `flow.yaml`
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
poetry env use <path/to/python3.8.6/executable>
poetry shell
poetry install
```