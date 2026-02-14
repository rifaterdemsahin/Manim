"""
4_Formula: Mathematical Formulas Visualization

This module contains 6 sample Manim animations demonstrating various mathematical concepts:

1. FormulaAnimation - Einstein's E=mc² and Pythagorean theorem
2. QuadraticFormulaAnimation - Quadratic formula with example solution
3. EulerFormulaAnimation - Euler's formula and the beautiful identity
4. DerivativeAnimation - Calculus derivative visualization with tangent line
5. IntegralAnimation - Integration as area under curve
6. TrigIdentityAnimation - Trigonometric identities with unit circle

Each animation can be rendered individually or all at once using the script at the bottom.
See README.md for detailed information about each animation.
"""

from manim import *

class FormulaAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Mathematical Formulas", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Einstein's equation
        einstein = MathTex(r"E = mc^2", font_size=72)
        self.play(Write(einstein))
        self.wait(1)
        
        # Transform to expanded form
        expanded = MathTex(
            r"E", r"=", r"m", r"c^2",
            font_size=72
        )
        self.play(TransformMatchingTex(einstein, expanded))
        self.wait(0.5)
        
        # Add labels
        energy_label = Text("Energy", font_size=24, color=YELLOW).next_to(expanded[0], DOWN)
        mass_label = Text("Mass", font_size=24, color=BLUE).next_to(expanded[2], DOWN)
        speed_label = Text("Speed of Light", font_size=24, color=GREEN).next_to(expanded[3], DOWN)
        
        self.play(
            Write(energy_label),
            Write(mass_label),
            Write(speed_label)
        )
        self.wait(1)
        
        # Move to corner
        formula_group = VGroup(expanded, energy_label, mass_label, speed_label)
        self.play(
            formula_group.animate.scale(0.5).to_corner(UL)
        )
        
        # Pythagorean theorem
        pythag = MathTex(r"a^2 + b^2 = c^2", font_size=60)
        self.play(Write(pythag))
        self.wait(1)
        
        # Create right triangle
        triangle = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [-2, 2, 0],
            color=BLUE
        )
        
        self.play(pythag.animate.scale(0.6).to_edge(DOWN))
        self.play(Create(triangle))
        
        # Label sides
        a_label = MathTex("a", font_size=36, color=RED).next_to(triangle, LEFT)
        b_label = MathTex("b", font_size=36, color=GREEN).next_to(triangle, DOWN)
        c_label = MathTex("c", font_size=36, color=YELLOW).move_to([0.5, 0.5, 0])
        
        self.play(Write(a_label), Write(b_label), Write(c_label))
        
        self.wait(2)


class QuadraticFormulaAnimation(Scene):
    """Quadratic formula visualization"""
    def construct(self):
        # Title
        title = Text("Quadratic Formula", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # The general form
        general_form = MathTex(r"ax^2 + bx + c = 0", font_size=60)
        self.play(Write(general_form))
        self.wait(1)
        
        # Move to corner
        self.play(general_form.animate.scale(0.6).to_corner(UL))
        
        # Quadratic formula
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=72
        )
        self.play(Write(formula))
        self.wait(1)
        
        # Example with numbers
        example = Text("Example: x² + 5x + 6 = 0", font_size=36, color=YELLOW)
        example.to_edge(DOWN, buff=1)
        self.play(Write(example))
        self.wait(0.5)
        
        # Solutions
        solutions = MathTex(
            r"x = -2 \text{ or } x = -3",
            font_size=48,
            color=GREEN
        )
        solutions.next_to(example, UP, buff=0.5)
        self.play(Write(solutions))
        
        self.wait(2)


class EulerFormulaAnimation(Scene):
    """Euler's formula and identity visualization"""
    def construct(self):
        # Title
        title = Text("Euler's Formula", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Euler's formula
        euler = MathTex(r"e^{i\theta} = \cos(\theta) + i\sin(\theta)", font_size=60)
        self.play(Write(euler))
        self.wait(1)
        
        # Transform to Euler's identity
        self.play(euler.animate.scale(0.7).to_edge(LEFT))
        
        # Euler's identity (when theta = pi)
        identity_label = Text("When θ = π:", font_size=32, color=YELLOW)
        identity_label.move_to(RIGHT * 3 + UP * 1.5)
        
        identity = MathTex(
            r"e^{i\pi} + 1 = 0",
            font_size=64,
            color=GREEN
        )
        identity.move_to(RIGHT * 3 + DOWN * 0.5)
        
        self.play(Write(identity_label))
        self.play(Write(identity))
        self.wait(1)
        
        # Add description
        desc = Text("The most beautiful equation", font_size=28, color=BLUE)
        desc.next_to(identity, DOWN, buff=0.5)
        self.play(Write(desc))
        
        self.wait(2)


class DerivativeAnimation(Scene):
    """Derivative visualization"""
    def construct(self):
        # Title
        title = Text("Derivative: Rate of Change", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Derivative definition
        derivative_def = MathTex(
            r"\frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=52
        )
        self.play(Write(derivative_def))
        self.wait(1)
        
        # Move to corner
        self.play(derivative_def.animate.scale(0.5).to_corner(UL))
        
        # Create axes
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            x_length=6,
            y_length=4,
            tips=False
        )
        
        # Function f(x) = x^2
        graph = ax.plot(lambda x: x**2, color=BLUE, x_range=[-2.5, 2.5])
        graph_label = MathTex("f(x) = x^2", font_size=36, color=BLUE)
        graph_label.next_to(ax, UP, buff=0.3)
        
        self.play(Create(ax), Create(graph), Write(graph_label))
        self.wait(0.5)
        
        # Show tangent line at x = 1
        x_val = 1
        dot = Dot(ax.c2p(x_val, x_val**2), color=RED)
        
        # Tangent line (derivative of x^2 is 2x, so at x=1, slope is 2)
        tangent = ax.plot(lambda x: 2*(x-1) + 1, color=RED, x_range=[0, 2])
        tangent_label = MathTex("f'(1) = 2", font_size=32, color=RED)
        tangent_label.next_to(dot, UP + RIGHT, buff=0.3)
        
        self.play(Create(dot), Create(tangent), Write(tangent_label))
        
        self.wait(2)


class IntegralAnimation(Scene):
    """Integral visualization"""
    def construct(self):
        # Title
        title = Text("Integral: Area Under Curve", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Integral symbol
        integral = MathTex(
            r"\int_{a}^{b} f(x) \, dx",
            font_size=72
        )
        self.play(Write(integral))
        self.wait(1)
        
        # Move to corner
        self.play(integral.animate.scale(0.5).to_corner(UL))
        
        # Create axes
        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            tips=False
        )
        
        # Function
        graph = ax.plot(lambda x: x**2 / 2 + 0.5, color=BLUE, x_range=[0.5, 3.5])
        
        self.play(Create(ax), Create(graph))
        self.wait(0.5)
        
        # Create area under curve
        area = ax.get_area(
            graph,
            x_range=[1, 3],
            color=[BLUE, GREEN],
            opacity=0.5
        )
        
        # Labels
        a_label = MathTex("a", font_size=32).next_to(ax.c2p(1, 0), DOWN)
        b_label = MathTex("b", font_size=32).next_to(ax.c2p(3, 0), DOWN)
        
        self.play(FadeIn(area), Write(a_label), Write(b_label))
        self.wait(0.5)
        
        # Area value
        area_text = Text("Area = ∫f(x)dx", font_size=36, color=GREEN)
        area_text.to_edge(DOWN)
        self.play(Write(area_text))
        
        self.wait(2)


class TrigIdentityAnimation(Scene):
    """Trigonometric identities visualization"""
    def construct(self):
        # Title
        title = Text("Trigonometric Identities", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Pythagorean identity
        identity1 = MathTex(r"\sin^2(\theta) + \cos^2(\theta) = 1", font_size=56)
        self.play(Write(identity1))
        self.wait(1)
        
        # Transform to show more identities
        self.play(identity1.animate.scale(0.6).shift(UP * 2))
        
        # Double angle formulas
        identity2 = MathTex(r"\sin(2\theta) = 2\sin(\theta)\cos(\theta)", font_size=44)
        identity2.shift(UP * 0.5)
        
        identity3 = MathTex(r"\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)", font_size=44)
        identity3.shift(DOWN * 0.8)
        
        self.play(Write(identity2))
        self.wait(0.5)
        self.play(Write(identity3))
        self.wait(0.5)
        
        # Unit circle visualization
        circle = Circle(radius=1.5, color=WHITE)
        circle.to_edge(DOWN, buff=0.5)
        
        # Angle line
        angle_line = Line(circle.get_center(), circle.get_center() + RIGHT * 1.5, color=YELLOW)
        
        # sin and cos projections
        sin_line = DashedLine(
            circle.get_center() + RIGHT * 1.5,
            circle.get_center() + RIGHT * 1.5 + UP * 0,
            color=RED
        )
        
        circle_group = VGroup(circle, angle_line, sin_line)
        circle_label = Text("Unit Circle", font_size=24).next_to(circle, DOWN, buff=0.3)
        
        self.play(Create(circle), Create(angle_line), Write(circle_label))
        
        self.wait(2)


if __name__ == "__main__":
    import os
    # You can render any of these animations:
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py FormulaAnimation")
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py QuadraticFormulaAnimation")
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py EulerFormulaAnimation")
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py DerivativeAnimation")
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py IntegralAnimation")
    # os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py TrigIdentityAnimation")
    
    # Render all animations
    animations = [
        "FormulaAnimation",
        "QuadraticFormulaAnimation", 
        "EulerFormulaAnimation",
        "DerivativeAnimation",
        "IntegralAnimation",
        "TrigIdentityAnimation"
    ]
    
    for anim in animations:
        print(f"\nRendering {anim}...")
        os.system(f"manim -pql --format=mp4 --media_dir ./media 4_Formula/formula.py {anim}")
