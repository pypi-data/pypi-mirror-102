import pytest
import sys
import os
import importlib


@pytest.fixture(scope='session')
def teagen():
    api_files = [
        os.path.join(os.path.dirname(__file__), './api/info.yaml'),
        os.path.join(os.path.dirname(__file__), './api/api.yaml')
    ]
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..')))
    module = importlib.import_module('teagen.teagen')
    teagen = getattr(module, 'Teagen')(api_files=api_files)
    return teagen


@pytest.fixture
def api(teagen):
    sys.path.append(teagen.output_dir)
    module = importlib.import_module(teagen.python_module_name)
    api = getattr(module, 'api')()
    return api
