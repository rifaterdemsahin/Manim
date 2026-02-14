"""
Simple Manim Examples
These are minimal examples to help you understand the basics.
"""

from manim import *

# Example 1: Hello World
class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)


# Example 2: Basic Shapes
class BasicShapes(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        square = Square(color=RED, fill_opacity=0.5)
        triangle = Triangle(color=GREEN, fill_opacity=0.5)
        
        circle.shift(LEFT * 2)
        triangle.shift(RIGHT * 2)
        
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(2)


# Example 3: Transformations
class TransformExample(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        
        self.play(Create(circle))
        self.wait(0.5)
        self.play(Transform(circle, square))
        self.wait(2)


# Example 4: Movement
class MovementExample(Scene):
    def construct(self):
        dot = Dot(color=YELLOW, radius=0.2)
        dot.shift(LEFT * 4)
        
        self.play(Create(dot))
        self.play(dot.animate.shift(RIGHT * 8))
        self.wait(2)


# Example 5: Multiple Objects
class MultipleObjects(Scene):
    def construct(self):
        title = Text("Three Objects", font_size=36)
        title.to_edge(UP)
        
        obj1 = Circle(radius=0.5, color=RED)
        obj2 = Square(side_length=1, color=BLUE)
        obj3 = Triangle(color=GREEN)
        
        obj1.shift(LEFT * 3)
        obj3.shift(RIGHT * 3)
        
        self.play(Write(title))
        self.play(
            Create(obj1),
            Create(obj2),
            Create(obj3)
        )
        self.wait(2)


# Example 6: Math Equation
class MathExample(Scene):
    def construct(self):
        equation = MathTex(r"e^{i\pi} + 1 = 0")
        equation.scale(2)
        
        self.play(Write(equation))
        self.wait(2)


# Example 7: Arrow and Labels
class ArrowExample(Scene):
    def construct(self):
        start = Dot(color=GREEN)
        end = Dot(color=RED)
        
        start.shift(LEFT * 3)
        end.shift(RIGHT * 3)
        
        arrow = Arrow(start.get_center(), end.get_center(), buff=0.1)
        
        start_label = Text("Start", font_size=24).next_to(start, DOWN)
        end_label = Text("End", font_size=24).next_to(end, DOWN)
        
        self.play(Create(start), Create(end))
        self.play(Write(start_label), Write(end_label))
        self.play(Create(arrow))
        self.wait(2)


# Example 8: Color Gradient
class ColorGradient(Scene):
    def construct(self):
        circles = VGroup(*[
            Circle(radius=0.3, fill_opacity=0.8)
            for _ in range(7)
        ])
        
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        for circle, color in zip(circles, colors):
            circle.set_fill(color)
        
        circles.arrange(RIGHT, buff=0.3)
        
        self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.2))
        self.wait(2)


# Example 9: Animation Groups
class AnimationGroups(Scene):
    def construct(self):
        title = Text("Sequential vs Simultaneous", font_size=32)
        title.to_edge(UP)
        
        # Sequential
        seq_label = Text("Sequential", font_size=24).shift(LEFT * 3 + UP)
        seq_objects = VGroup(*[
            Square(side_length=0.5, color=BLUE).shift(LEFT * 3 + DOWN * i)
            for i in range(3)
        ])
        
        # Simultaneous
        sim_label = Text("Simultaneous", font_size=24).shift(RIGHT * 3 + UP)
        sim_objects = VGroup(*[
            Circle(radius=0.3, color=RED, fill_opacity=0.5).shift(RIGHT * 3 + DOWN * i)
            for i in range(3)
        ])
        
        self.play(Write(title))
        self.play(Write(seq_label), Write(sim_label))
        self.wait(0.5)
        
        # Show sequential
        for obj in seq_objects:
            self.play(Create(obj))
        
        # Show simultaneous
        self.play(*[Create(obj) for obj in sim_objects])
        
        self.wait(2)


# Example 10: Graph
class SimpleGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=6,
            tips=False
        )
        
        graph = ax.plot(lambda x: x**2 / 10, color=BLUE)
        
        title = Text("y = x²/10", font_size=36)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.play(Create(ax))
        self.play(Create(graph), run_time=2)
        self.wait(2)


# How to run these examples:
# manim -pql examples.py HelloWorld
# manim -pql examples.py BasicShapes
# manim -pql examples.py TransformExample
# etc.
