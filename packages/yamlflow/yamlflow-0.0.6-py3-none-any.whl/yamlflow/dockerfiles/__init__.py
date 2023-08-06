import os

here = os.path.abspath(os.path.dirname(__file__))

CORE = os.path.join(here, "core")
APP = os.path.join(here, "app")

base = f"{CORE}/base"
torch_cpu = f"{CORE}/torch-cpu"