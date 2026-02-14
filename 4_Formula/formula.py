"""
4_Formula: Mathematical Formulas Visualization
This animation demonstrates mathematical formulas and equations.
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


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py FormulaAnimation")
