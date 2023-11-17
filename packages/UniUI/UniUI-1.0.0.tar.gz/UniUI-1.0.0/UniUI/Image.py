import pygame
import Console

def init():
    global Funcs
    from . import Funcs

DEFAULT_IMAGE_WIDTH = 128
DEFAULT_IMAGE_HEIGHT = 128
DEFAULT_IMAGE_COLOR = (255, 255, 255)

class ScreenResolution:
    AUTO = 0

class RenderType:
    SMOOTHED = 0
    PIXELATED = 1

class Anchor:
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3
    CENTER = 4

    X_ANCHORS = [LEFT, RIGHT, CENTER]
    Y_ANCHORS = [TOP, BOTTOM, CENTER]

class Image:
    def __init__(self, window: pygame.Surface, x: int = 0, y: int = 0,
                 width: int = None, height: int = None, color: tuple = DEFAULT_IMAGE_COLOR,
                 image: pygame.Surface = None, fill_size: int = 0,
                 border_radius: int = -1, anchor = [Anchor.CENTER, Anchor.CENTER],
                 render: bool = True, scale: pygame.Vector2 = pygame.Vector2(1, 1), screen_resolution: (int, int) = ScreenResolution.AUTO,
                 render_type: RenderType = RenderType.SMOOTHED) -> None:
        
        self._render = render
        self._render_type = render_type

        self._window = window
        self._screen_resolution = screen_resolution

        self._surface = None

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._scale = scale

        self._color = color
        self._image = image
        self._fill_size = fill_size
        self._border_radius = border_radius

        self._anchor = anchor

        self.INITIALIZED = False
        all_vars = vars(self).copy()

        for var in all_vars:
            if var.startswith("_"):
                setattr(self, var[1:], all_vars[var])
                
        self.INITIALIZED = True
        self.hash()
    
    @property
    def surface(self):
        return self._surface
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def color(self):
        return self._color
    @property
    def image(self):
        return self._image
    @property
    def fill_size(self):
        return self._fill_size
    @property
    def border_radius(self):
        return self._border_radius
    @property
    def scale(self):
        return self._scale
    @property
    def screen_resolution(self):
        return self._screen_resolution
    @property
    def window(self):
        return self._window
    @property
    def anchor(self):
        return self._anchor
    @property
    def render(self):
        return self._render
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def render_type(self):
        return self._render_type
    
    @surface.setter
    def surface(self, value):
        if self.INITIALIZED: Console.Warning("It is not recommended to change the surface.")
        self._surface = self.surface
    @width.setter
    def width(self, value):
        if type(value) != int and type(value) != float:
            Console.Warning("Width : value is not a number.")
            self._width = self.width if type(self.width) == int else 0
        else:
            self._width = max(0, value)
            if self.INITIALIZED: self.hash()
    @height.setter
    def height(self, value):
        if type(value) != int and type(value) != float:
            Console.Warning("Height : value is not a number.")
            self._height = self.height if type(self.height) == int else 0
        else:
            self._height = max(0, value)
            if self.INITIALIZED: self.hash()
    @color.setter
    def color(self, value):
        isRGB, error = Funcs.IsRGBColor(value)
        if not isRGB:
            Console.Warning(error)
            self._color = self.color if isRGB(self.color)[0] else DEFAULT_IMAGE_COLOR
        else:
            self._color = value
            if self.INITIALIZED: self.hash()
    @image.setter
    def image(self, value):
        if type(value) != pygame.Surface and value != None:
            Console.Warning("image is not a pygame.Surface.")
            self._image = self.image if type(self.image) == pygame.Surface else None
        else:
            self._image = value
            if self.INITIALIZED: self.hash()
        
    @fill_size.setter
    def fill_size(self, value):
        if type(value) != int:
            Console.Warning("Fill Size : value is not int.")
            self._fill_size = self.fill_size if type(self.fill_size) == int else 0
        else:
            self._fill_size = value
            if self.INITIALIZED: self.hash()

    @border_radius.setter
    def border_radius(self, value):
        if type(value) != int:
            Console.Warning("Border Radius : value is not int.")
            self._border_radius = self.border_radius if type(self.border_radius) == int else -1
        else:
            self._border_radius = value
            if self.INITIALIZED: self.hash()

    @scale.setter
    def scale(self, value):
        if type(value) != pygame.Vector2:
            Console.Warning("Scale : value is not pygame.Vector2.")
            self._scale = self.scale if type(self.scale) == pygame.Vector2 else pygame.Vector2(1, 1)
        else:
            self._scale = value
            if self.INITIALIZED: self.hash()
    
    @screen_resolution.setter
    def screen_resolution(self, value):
        if value == ScreenResolution.AUTO:
            self._screen_resolution = self.window.get_size()
        else:
            isCorrect, error = Funcs.isCorrectSize(value, 2, int, True)
            if isCorrect:
                self._screen_resolution = value
                if self.INITIALIZED: self.hash()
            else:
                Console.Error(f"Screen Resolution : {error}")
                self._screen_resolution = self.screen_resolution
    
    @window.setter
    def window(self, value):
        if type(value) != pygame.Surface:
            Console.Error("Window : value is not a pygame.Surface.")
            self._window = self.window if type(self.window) == pygame.Surface else pygame.Surface((0, 0))
        else:
            self._window = value
    
    @anchor.setter
    def anchor(self, value):
        isCorrect, error = Funcs.isCorrectAnchor(value)
        
        if not isCorrect:
            Console.Error(f"Anchor : {error}")
            self._anchor = self.anchor if Funcs.isCorrectAnchor(self.anchor) else [Anchor.CENTER, Anchor.CENTER]
        else:
            self._anchor = list(value)
    
    @render.setter
    def render(self, value):
        if type(value) != bool:
            Console.Error("Render : value is not bool.")
            self._render = self.render if type(self.render) == bool else True
        else:
            self._render = value
    
    @x.setter
    def x(self, value):
        if type(value) != int and type(value) != float:
            Console.Error("X : value is not a number.")
            self._x = self.x if type(self.x) == int or type(self.x) == float else 0
        else:
            self._x = value
    
    @y.setter
    def y(self, value):
        if type(value) != int and type(value) != float:
            Console.Error("Y : value is not a number.")
            self._y = self.y if type(self.y) == int or type(self.y) == float else 0
        else:
            self._y = value
    
    @render_type.setter
    def render_type(self, value):
        types = (RenderType.PIXELATED, RenderType.SMOOTHED)
        if value not in types:
            Console.Error("Render Type : value is not correct type.")
            self._render_type = self.render_type if self.render_type in types else RenderType.SMOOTHED
        else:
            self._render_type = value
            if self.INITIALIZED: self.hash()
    
    def GET_SCALED_SURFACE(self, surface: pygame.Surface, new_width: int, new_height: int) -> pygame.Surface:
        if self.render_type == RenderType.PIXELATED:
            return pygame.transform.scale(surface, (new_width, new_height))
        if self.render_type == RenderType.SMOOTHED:
            return pygame.transform.smoothscale(surface, (new_width, new_height))
    
    def GET_ADAPTED_SIZE(self, width: int, height: int):
        current_window_size = self.window.get_size()
        if current_window_size == self.screen_resolution:
            return width, height

        scale_factor = min(current_window_size[0] / self.screen_resolution[0],
                     current_window_size[1] / self.screen_resolution[1]) if current_window_size[0] > self.screen_resolution[0] and current_window_size[1] > self.screen_resolution[1] else min(current_window_size[0] / self.screen_resolution[0], current_window_size[1] / self.screen_resolution[1])
        
        return width * scale_factor, height * scale_factor

    def GET_ADAPTED_POSITION(self, x: int, y: int):
        current_window_size = self.window.get_size()
        if current_window_size == self.screen_resolution:
            return x, y

        scale_factor = min(current_window_size[0] / self.screen_resolution[0],
                    current_window_size[1] / self.screen_resolution[1]) if current_window_size[0] > self.screen_resolution[0] and current_window_size[1] > self.screen_resolution[1] else min(current_window_size[0] / self.screen_resolution[0], current_window_size[1] / self.screen_resolution[1])
        
        return x * scale_factor, y * scale_factor

    def hash(self) -> None:
        end_width, end_height = self.width, self.height

        if type(self.image) == pygame.Surface:
            if end_width == None: end_width = self.image.get_width()
            if end_height == None: end_height = self.image.get_height()

            end_width, end_height = self.GET_ADAPTED_SIZE(end_width, end_height)

            self._surface = self.GET_SCALED_SURFACE(self.image, end_width, end_height)
        else:
            if end_width == None: end_width = DEFAULT_IMAGE_WIDTH
            if end_height == None: end_height = DEFAULT_IMAGE_HEIGHT

            end_width, end_height = self.GET_ADAPTED_SIZE(end_width, end_height)

            self._surface = pygame.Surface((end_width, end_height))
            self._surface.fill((255, 255, 255))
            self._surface = self.GET_SCALED_SURFACE(self.surface, end_width, end_height)
        
        size = self.surface.get_size()
        rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(rect_image, (255, 255, 255), (0, 0, *size), self.fill_size, self.border_radius)
        self._surface.blit(rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)
        color_surface = pygame.Surface(self.surface.get_size()).convert_alpha()
        color_surface.fill(self.color)
        self.surface.blit(color_surface, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

        if len(self.color) == 4:
            self.surface.set_alpha(self.color[-1])
    
    def GET_RENDER_POSITION(self) -> (int, int):
        x, y = self.GET_ADAPTED_POSITION(self.x, self.y)

        anchor_positions = {
            "x": {
                Anchor.LEFT: 0,
                Anchor.RIGHT: self.window.get_width() - self.surface.get_width() * self.scale.x,
                Anchor.CENTER: self.window.get_width() // 2 - (self.surface.get_width() * self.scale.x) // 2,
            },
            "y": {
                Anchor.TOP: 0,
                Anchor.BOTTOM: self.window.get_height() - self.surface.get_height() * self.scale.y,
                Anchor.CENTER: self.window.get_height() // 2 - (self.surface.get_height() * self.scale.y) // 2
            }
        }
               
        return anchor_positions["x"][self.anchor[0]] + x, anchor_positions["y"][self.anchor[1]] + y
    
    def update(self):
        if self.render:
            end_position = self.GET_RENDER_POSITION()
            self.window.blit(pygame.transform.smoothscale(self.surface, (self.surface.get_width() * self.scale.x,
                                                                         self.surface.get_height() * self.scale.y)), end_position)