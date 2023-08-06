PyDocGen
--------
Automatically generate docstrings and documentation for your Python modules!

Installation
--------------
```
pip install pydocgen
```

Usage
-------
Pydocgen currently will accept a Python module file, it will support packages in the near future
```
pydocgen --help         #View all options
pydocgen -i file_name
```

Features
----------
- Easy to use, quick way to document your code
- Input module file will automatically be decorated with docstrings (under development)
    - Only need to fill in variable and function description
    - Automatic type inference!
- Documentation files will be generated automatically (current supports HTML)
