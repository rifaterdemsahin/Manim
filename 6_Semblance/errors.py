"""
6_Semblance: Error Handling and Debugging
This animation demonstrates error detection and handling processes.
"""

from manim import *

class ErrorAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Error Handling & Debugging", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Code with error
        error_code = Code(
            code="""def divide(a, b):
    result = a / b  # Error: Division by zero
    return result

answer = divide(10, 0)""",
            language="python",
            font="Monospace",
            background="window",
            insert_line_no=True,
            style="monokai",
            font_size=24
        )
        error_code.scale(0.7)
        
        self.play(Create(error_code))
        self.wait(1)
        
        # Show error indicator
        error_icon = Text("⚠️", font_size=72, color=RED)
        error_icon.next_to(error_code, RIGHT, buff=1)
        
        error_text = Text("ZeroDivisionError", font_size=28, color=RED)
        error_text.next_to(error_icon, DOWN)
        
        self.play(
            Write(error_icon),
            Write(error_text),
            error_code.animate.set_color(RED)
        )
        self.wait(1)
        
        # Transform to fixed code
        fixed_code = Code(
            code="""def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    result = a / b
    return result

answer = divide(10, 0)  # Returns error message""",
            language="python",
            font="Monospace",
            background="window",
            insert_line_no=True,
            style="monokai",
            font_size=24
        )
        fixed_code.scale(0.7)
        
        self.play(
            FadeOut(error_icon),
            FadeOut(error_text),
            Transform(error_code, fixed_code)
        )
        
        # Success indicator
        success_icon = Text("✓", font_size=72, color=GREEN)
        success_icon.next_to(error_code, RIGHT, buff=1)
        
        success_text = Text("Error Handled", font_size=28, color=GREEN)
        success_text.next_to(success_icon, DOWN)
        
        self.play(
            Write(success_icon),
            Write(success_text)
        )
        
        self.wait(2)


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 6_Semblance/errors.py ErrorAnimation")
