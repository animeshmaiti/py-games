# Py games
Dependencies:
- pygame
install with:
```bash
pip install pygame
```
## Pygame display surface
```python
surface=pygame.display.set_mode((400,300),0,32)
```
Explanation:
- `400`: width
- `300`: height
- `0`: flags
    - Flags: Display flags are parameters that you can pass to the `pygame.display.set_mode()` function to control various settings and behaviors related to the display surface and window.
    1. `pygame.FULLSCREEN`: Creates a fullscreen window.
    1. `pygame.RESIZABLE`: Allows the window to be resized by the user.
    1. `pygame.NOFRAME`: Creates a borderless window without decorations.
    1. `pygame.HWSURFACE`: Specifies that the display surface should be created in video memory for faster rendering.
    1. `pygame.DOUBLEBUF`: Uses double buffering for smoother animations by swapping between two display surfaces.
    1. `pygame.OPENGL`: Creates an OpenGL rendering context in the window.
    1. `pygame.SCALED`: Enables automatic window scaling (high-DPI displays).
    1. `pygame.SWSURFACE`: Creates the display surface in system memory (slower but more compatible).
    - Ex.
    ```python
    surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF)
    ```
- `32` : This parameter specifies the bit depth of the display surface. It determines the number of bits used to represent each pixel's color. A bit depth of 32 indicates that each pixel's color can be represented using 8 bits for red, 8 bits for green, 8 bits for blue, and 8 bits for alpha (transparency)

## pygame.event.get()
### Retrieve a list of all the events that have occurred since the last time this function was called.
- Mouse clicks
- Keyboard inputs
- Mouse pointer co-ordinate
- Window resizing 
- Quit button .etc

