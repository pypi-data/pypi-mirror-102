## Requirements

- Python 3.8+
- Flit to put Python packages and modules on PyPI
- Pydantic for the data parts.

## Installation
```
pip install flit
pip install pyimporters-dummy
```

## Publish the Python Package to PyPI
- Increment the version of your package in the `__init__.py` file:
```
"""An amazing package!"""

__version__ = 'x.y.z'
```
- Publish
```
flit publish
```

## Write your own pyimporters plugin
- Git clone the pyimporters_dummy project
```
git clone git@bitbucket.org:kairntech/pyimporters_dummy.git
```
- Rename the project with your own format name <new_format>
```
mv pyimporters_dummy pyimporters_<new_format>
```
- Delete the .git directory
```
rm -r -f pyimporters_<new_format>/.git
```
- Change to the new pyimporters_<new_format> directory
```
cd pyimporters_<new_format>
```
- Rename the package directory project
```
mv pyimporters_dummy pyimporters_<new_format>
```
- Rename the python file implementation
```
mv pyimporters_<new_format>/dummy.py pyimporters_<new_format>/<new_format>.py
```
- Rename the python tests file implementation
```
mv tests/test_dummy.py tests/test_<new_format>.py
```
- Edit the pyproject.toml file to change a few lines and add your additional requirements
```
[tool.flit.metadata]
module = "pyimporters_<new_format>"
...
requires = [
    "pyimporters_plugins>=0.1.61",
    "additional_requirement1",
    "additional_requirement2",
    ...
    "additional_requirementN",
]
dist-name = "pyimporters-<new_format>"
...
[tool.flit.entrypoints."pyimporters.plugins"]
<new_format> = "pyimporters_<new_format>.<new_format>:NewFormatKnowledgeParser"
```
- Write the implementation and test of your new format in python using your favorite IDE
```
@dataclass
class NewFormatOptions(KnowledgeParserOptions):
    """
    Options for the new format knowledge import
    """
    foo : str = Query("bar", description="Dummy parameter")

NewFormatOptionsModel = NewFormatOptions.__pydantic_model__

class NewFormatKnowledgeParser(KnowledgeParserBase):
    def parse(self, source : Path, options: Union[KnowledgeParserOptions, Dict[str, Any]], bar : Bar) -> Generator[Term, None, None]:
        options = NewFormatOptions(**options) if isinstance(options, dict) else options
        # Initialize the progress indicator number of terms to read so that the progress indicator can send feedback to the end user
        bar.max = 100 
        bar.start()
        # yield as many terms as you want, advancing the progress indicator each time
        bar.next()
        yield Term(identifier=options.foo, preferredForm=options.foo)
        # Terminate the progress indicator
        bar.finish()

    @classmethod
    def get_schema(cls) -> KnowledgeParserOptions:
        return NewFormatOptions

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return NewFormatOptionsModel
```

