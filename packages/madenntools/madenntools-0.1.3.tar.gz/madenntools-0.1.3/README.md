# madenntools
Our Computer Vision toolkit. Work in progress 

## Usage

Available namespaces:
- madenntools.cv
- madenntools.metric
- madenntools.plot

[Full documentation](doc/library_documentation.md)

example: 
```python
from madenntools.cv import blend

if __name__ == '__main__':
    blended_image = blend(image, mask, level=(128, 127, 0))
```

## Update pip package

- Update the code
- Update the Dependencies in requirements.txt and in pyproject.toml, if necessary. 
```bash
pipreqs --mode no-pin --force . 
```
- Update the pyproject.toml version, and metadata, if necessary.
- Build the project:
```bash
python -m build
```
- Republish: 

```bash
twine check dist/*
twine upload -r pypi dist/*
```

- Check your package at: 
https://pypi.org/project/madenntools/

- Push changes to github, including the new .whl file for the github package

## Contribution practices
- Pay attention when changing the type of the input/output data inside the function. Avoid if possible 
- scripts will be added to directories (example: cv), and linked the __init__.py file of that directory. 
- Follow the naming convention and the docstring style. Example

```python
    """   
    Blend a foreground image with a background using the binary mask as the alpha channel.

    Args:
        foreground_image (numpy.ndarray): The BGR image to be blended.
        binary_mask (numpy.ndarray): The binary mask in BGR format.
        level (tuple, optional): The BGR color of the background. Defaults to (128, 128, 128).

    Returns:
        numpy.ndarray: The blended image.
    """
    def blend(foreground_image, binary_mask, level=(128, 128, 128)):
```
