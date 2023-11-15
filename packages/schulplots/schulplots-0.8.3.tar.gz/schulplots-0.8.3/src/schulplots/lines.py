from dataclasses import dataclass, field
from typing import Optional, Any, ClassVar
import numpy as np

from .converter import register_model, register_impl
from .utils.math_expression import MathExpression

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .saxes import SAxes
    
@register_model  
@dataclass
class VLineModel:
    class_id: ClassVar[str] = "VLine"    
    x: MathExpression = 0
    y_min: float = 0
    y_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.5))
@register_impl
class VLine(VLineModel):
    _saxes: SAxes
    def __init__(self, saxes: SAxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_saxes(saxes)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        x = self.x.evaluate(self._saxes.axes_variables)
        self._saxes.axes.axvline(x=x,ymin=self.y_min, ymax=self.y_max, 
                                 **self.plot_args)
@register_model  
@dataclass
class HLineModel:
    class_id: ClassVar[str] = "HLine"    
    y: MathExpression = 0
    x_min: float = 0
    x_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.5))
@register_impl
class HLine(HLineModel):
    _saxes: SAxes
    def __init__(self, saxes: SAxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_saxes(saxes)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        y = self.y.evaluate(self._saxes.axes_variables)
        self._saxes.axes.axhline(y=y,xmin=self.x_min, xmax=self.x_max, 
                                 **self.plot_args)
@register_model  
@dataclass
class VSpanModel:
    class_id: ClassVar[str] = "VSpan"    
    x0: MathExpression = MathExpression(0)
    x1: MathExpression = MathExpression(0)
    y_min: float = 0
    y_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.3, lw=0))

@register_impl
class VSpan(VSpanModel):
    _saxes: Optional[SAxes]
    def __init__(self, saxes: SAxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_saxes(saxes)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        x0 = self.x0.evaluate(self._saxes.axes_variables)
        x1 = self.x1.evaluate(self._saxes.axes_variables)
        self._saxes.axes.axvspan(xmin=x0, xmax=x1,ymin=self.y_min, 
                                 ymax=self.y_max, **self.plot_args)
        
@register_model  
@dataclass
class HSpanModel:
    class_id: ClassVar[str] = "HSpan"    
    y0: MathExpression = 0
    y1: MathExpression = 0
    x_min: float = 0
    x_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.3, lw=0))

@register_impl
class HSpan(HSpanModel):
    _saxes: Optional[SAxes]
    def __init__(self, saxes: SAxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_saxes(saxes)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        y0 = self.y0.evaluate(self._saxes.axes_variables)
        y1 = self.y1.evaluate(self._saxes.axes_variables)
        self._saxes.axes.axhspan(ymin=y0, ymax=y1,xmin=self.x_min, 
                                 xmax=self.x_max, **self.plot_args)
        
@register_model  
@dataclass
class ArrowModel:
    class_id: ClassVar[str] = "Arrow" 
    x: MathExpression = 0
    y: MathExpression = 0
    dx: MathExpression = 1
    dy: MathExpression = -1
    width: float = 0.08
    length_includes_head: bool = True
    
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(linewidth=0))

@register_impl
class Arrow(ArrowModel):
    def __init__(self, saxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saxes = saxes
        self.setup_saxes(self._saxes)
    def setup_saxes(self, saxes: SAxes):
        self._saxes = saxes
        x = self.x.evaluate(self._saxes.axes_variables)
        y = self.y.evaluate(self._saxes.axes_variables)
        dx = self.dx.evaluate(self._saxes.axes_variables)
        dy = self.dy.evaluate(self._saxes.axes_variables)
        self._saxes.axes.arrow(x,y, dx, dy, 
                               length_includes_head=self.length_includes_head,
                               width=self.width, **self.plot_args)
        