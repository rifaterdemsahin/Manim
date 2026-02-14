"""
1_Real_Unknown: Goal Setting Animation
This animation represents exploring unknown territories and setting goals.
"""

from manim import *

class GoalAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Goal: Exploring the Unknown", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create a target goal
        goal = Circle(radius=0.5, color=YELLOW, fill_opacity=0.5)
        goal.shift(RIGHT * 4 + UP * 1)
        goal_label = Text("Goal", font_size=24).next_to(goal, UP)
        
        # Create a starting point
        start = Dot(color=BLUE, radius=0.15)
        start.shift(LEFT * 4 + DOWN * 1)
        start_label = Text("Start", font_size=24).next_to(start, DOWN)
        
        self.play(
            Create(goal),
            Write(goal_label),
            Create(start),
            Write(start_label)
        )
        self.wait(0.5)
        
        # Create question marks representing unknowns
        unknowns = VGroup()
        for i in range(5):
            unknown = Text("?", font_size=36, color=RED)
            unknown.move_to([
                np.random.uniform(-3, 3),
                np.random.uniform(-2, 2),
                0
            ])
            unknowns.add(unknown)
        
        self.play(FadeIn(unknowns, shift=UP))
        self.wait(0.5)
        
        # Create path from start to goal
        path = Arrow(
            start.get_center(),
            goal.get_center(),
            buff=0.5,
            color=GREEN,
            stroke_width=6
        )
        
        self.play(Create(path))
        self.wait(0.5)
        
        # Move dot along path
        moving_dot = Dot(color=BLUE, radius=0.15)
        moving_dot.move_to(start.get_center())
        
        self.play(FadeOut(start))
        self.add(moving_dot)
        
        self.play(
            MoveAlongPath(moving_dot, path),
            FadeOut(unknowns),
            run_time=2
        )
        
        # Success message
        success = Text("Goal Achieved!", font_size=36, color=GREEN)
        success.next_to(goal, DOWN)
        self.play(Write(success))
        
        self.wait(2)


if __name__ == "__main__":
    # Render configuration for DaVinci Resolve compatibility
    # High quality MP4 with H.264 codec, 1920x1080, 60fps
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 1_Real_Unknown/goal.py GoalAnimation")
