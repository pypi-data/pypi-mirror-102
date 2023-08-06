https://www.youtube.com/watch?v=GIF3LaRqgXo
https://www.youtube.com/watch?v=U-aIPTS580s



$ python setup.py bdist_wheel
$ pip install -e . 

# -e : instead of installing or copying the file, it links and you can continue to work on it . test it 
# . : install this package from local directory 

from helloworld import say_hello

say_hello()


Documentation

- Add gitignore gitignore.io  https://www.toptal.com/developers/gitignore
- License : https://choosealicense.com   : human way for Non-legal people 
- Classifiers : https://pypi.org/classifiers  : PEP301
- Documentation 
   - Restructured Text : Pythonic , Powerful, Can use Sphinx
   - Markdown : More widespread, Simpler, Can use MkDocs
   

   - Add read documentation to PyPI 
- Add dependencies install_requires 

Run pip install -e . to check the dependecies


Installs vs Extras

Install_requires 
- is for production dependcies (Flas, Click, Numpy, Pandas)
- versions should be as relaxed as possible (>3.0, <4.0)

Extras_require 
- is for optional requirements (PyTest, Mock, Coverage.py)
- Versions should be as specific as possible ( as it is for devlopers)



Now Add Tests 
- Test with PyTest
- Add Dev dependecies 

Update README 
Running tests

```python
pytest
```

Source Distribution 

Python setup.py sdist 
Add url, author, author_email 
Test it 
$ tar tzf dist/helloworld-0.0.1.tar.gz

it doesn't contain License.txt, Test_helloworld.py 


Check Manifest
pip install check-manifest
check-manifest --create
git add MANIFEST.in 
Python setup.py sdist 


Publish Earlier 
python setup.py bdist_wheel sdist

## Push to PyPI

# Stick this in `extras_require`

$ pip install twine
$ twine upload --repository pytpi dist/*
make sure you have the PyPI project


NOw productionize it 
## Tox.ini 

```
pip install tox
tox
```
## Travis

## Extra Credit
Badges
- Code Coverage (coversalls, codecov.io)
- Quality Metrics ( Code climate, landscape.io)

Manage versioning with bumpversion
Test on OSX and Windows
More documentation
- Add contributors section
- 

Use CookieCutter
- move metadat from setup.py to setup.cfg
- 