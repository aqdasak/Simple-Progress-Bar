# Simple Progress Bar

The ProgressBar class is a simple implementation of a progress bar that can be used to display progress in command-line interfaces.

## Usage

To use the ProgressBar class, copy the progress_bar.py in the working directory, then import it from the progressbar module:

```python
from progressbar import ProgressBar
```

Then create an instance of the ProgressBar class with the desired bar_length:

```python
bar = ProgressBar(bar_length=50)
```

Next, set the total number of iterations using the total property:

```python
bar.total = 100
```

Finally, update the progress bar with the current iteration count using the update method:

```python
for i in range(1, 101):
    bar.update(i, msg='Processing...')
    time.sleep(0.1)
```

The msg parameter is optional and can be used to display a message after the progress bar. The update method automatically calculates the length of the progress bar based on the total and bar_length properties.

## License

The ProgressBar class is released under the MIT License. See [LICENSE](LICENSE.md) for details.
