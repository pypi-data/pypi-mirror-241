Release
-------

1. Install hatch with `pip3.11 install hatch==0.23.1`.
2. Create virtual environment with `python3.11 -m hatch env jupyter`.
3. Open virtual environment shell with `python3.11 -m hatch shell jupyter`.
4. Install dependencies with `pip install -r requirements.txt`.
5. Bump package version in `setup.py` and VERSION files.
6. Clean and build with `python setup.py clean build sdist install`.
7. Release with `twine` with `twine upload dist/*`. Username = __token__, password = API token.

