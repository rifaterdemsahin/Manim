"""
5_Symbols: Code and Programming Symbols
This animation demonstrates programming concepts and code symbols.
"""

from manim import *

class CodeAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Programming Symbols", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Code example
        code = Code(
            code="""def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(f"Result: {result}")""",
            language="python",
            font="Monospace",
            background="window",
            insert_line_no=True,
            style="monokai",
            font_size=20
        )
        code.scale(0.8)
        
        self.play(Create(code))
        self.wait(1)
        
        # Move code to left
        self.play(code.animate.scale(0.7).to_edge(LEFT))
        
        # Show algorithm visualization
        visualization = VGroup()
        
        # Tree structure for recursion
        circles = []
        positions = [
            [3, 2, 0],
            [2, 0.5, 0], [4, 0.5, 0],
            [1.5, -1, 0], [2.5, -1, 0], [3.5, -1, 0], [4.5, -1, 0]
        ]
        
        for i, pos in enumerate(positions):
            circle = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
            circle.move_to(pos)
            num = Text(str(i), font_size=24)
            num.move_to(circle.get_center())
            node = VGroup(circle, num)
            visualization.add(node)
            circles.append(circle)
        
        self.play(LaggedStart(*[Create(node) for node in visualization], lag_ratio=0.2))
        
        # Add arrows
        arrows = VGroup(
            Arrow(circles[0].get_bottom(), circles[1].get_top(), buff=0.1),
            Arrow(circles[0].get_bottom(), circles[2].get_top(), buff=0.1),
            Arrow(circles[1].get_bottom(), circles[3].get_top(), buff=0.1),
            Arrow(circles[1].get_bottom(), circles[4].get_top(), buff=0.1),
            Arrow(circles[2].get_bottom(), circles[5].get_top(), buff=0.1),
            Arrow(circles[2].get_bottom(), circles[6].get_top(), buff=0.1),
        )
        
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.1))
        
        self.wait(2)


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 5_Symbols/code.py CodeAnimation")
