import sys
import importlib


class Teagen(object):
    def __init__(self, api_files, python_module_name='sample', output_dir=None):
        self._python_module_name = python_module_name
        self._output_dir = output_dir
        self._api_files = api_files
        if self._output_dir is None:
            self._output_dir = os.path.join(os.path.dirname(__file__), '../output')
        module = importlib.import_module('teagen.bundler')
        bundler = getattr(module, 'Bundler')(api_files=api_files,
                                             output_dir=self._output_dir)
        bundler.bundle()
        module = importlib.import_module('teagen.generator')
        generator = getattr(module, 'Generator')(bundler.openapi_filepath,
                                                 self._python_module_name,
                                                 output_dir=self._output_dir)
        generator.generate()

    @property
    def output_dir(self):
        return self._output_dir

    @property
    def python_module_name(self):
        return self._python_module_name
