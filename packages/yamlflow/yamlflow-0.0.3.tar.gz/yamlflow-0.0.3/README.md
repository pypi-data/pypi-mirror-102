# yamlflow
Yet Another ML flow

## STATUS NOT READY

```
examle-project
    ...
    ...
    .yamlflow
        flow.yaml
        predictor.py
        requirements.txt
```

### User guide
```bash
pip install yamlflow
yamlflow apply -f flow.yaml
```

### Developer guide
```
poetry env use <path/to/python3.8.6/executable>
poetry shell
poetry install
```