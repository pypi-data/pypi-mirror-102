import os
import sys
from dataclasses import dataclass, asdict

import yaml

from yamlflow.dockerfiles import APP

@dataclass(frozen=True, order=True)
class _meta:
    name: str
    version: str

    def __repr__(self):
        return f"{self.name}:{self.version}"


@dataclass(frozen=True, order=True)
class _backend:
    runtime: str
    device: str
    
    def __repr__(self):
        return f"{self.runtime}-{self.device}"


@dataclass(frozen=True, order=True)
class _frontend:
    predictor: str
    requirements: str
    

class Manifest:

    def __init__(self, mainfest_path: str):
        super().__init__()
        self._yf = mainfest_path
        self._read()
    
    def _read(self) -> None:
        with open(self._yf, 'r') as fp:
            try:
                self.data = yaml.safe_load(fp)
            except yaml.YAMLError as err:
                print(err)
                sys.exit(1)


    @property
    def meta(self):
        return repr(_meta(**self.data["meta"]))


    @property
    def backend(self):
        return repr(_backend(**self.data["backend"]))

    @property
    def frontend(self):
        return _frontend(**self.data["frontend"])


    def build_info(self):
        return {
            "path": ".yamlflow",
            "tag": self.meta,
            "buildargs": {"BACKEND": self.backend}
        }
