# How to release

## version bump
change version in pyproject.toml

## build
- install build: `python -m pip install --upgrade build`
- run `python -m build`

## upload
- install twine: `python -m pip install twine`
- `python -m twine upload dist/*`



