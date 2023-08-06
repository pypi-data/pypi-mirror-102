# Distribution package

This package was developed as lesson from Machine Learning Engineering Udacity Nanodegree.
Here you will find all necessary data to upload a package to [PyPI](pypi.org).

# Requirements

The project requires some dependencies. You can install them by executing the following code.

```
pip install -r requirements.txt
```

# Tests

To run the tests execute the following code.

```
python distributions_mf/test.py
```

# Installing the package locally

To install the package locally run the commando below. Make sure you are on the same path as the setup.py file.

```
pip install .
```

# Uploading the package to PyPI

## Generate distribution files

To generate the distribution (dist) files run the command below.

```
python setup.py sdist
```

After that two directories will be created: **dist** and **[package-name].egg-info**. 

## Upload package to PyPI

To do so you will need the twine package. It is already included on the requirements.txt file.
Beforehand make sure to create an account on PyPY.

It is important to mention that PyPI also has a [test repository](https://test.pypi.org).

To upload you package to the test repository run the following command.

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

And to upload you package to the official PyPI repository run the command below.


```
twine upload dist/*
```
