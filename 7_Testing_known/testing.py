"""
7_Testing_known: Test Scenarios and Validation
This animation demonstrates testing and validation processes.
"""

from manim import *

class TestingAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Testing & Validation", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create test cases
        test_cases = VGroup()
        test_labels = [
            "Test 1: Input Validation",
            "Test 2: Edge Cases",
            "Test 3: Performance",
            "Test 4: Integration"
        ]
        
        for i, label in enumerate(test_labels):
            # Test box
            box = Rectangle(height=0.6, width=5, color=BLUE, fill_opacity=0.2)
            text = Text(label, font_size=20)
            text.move_to(box.get_center())
            
            test_group = VGroup(box, text)
            test_group.shift(UP * (1.5 - i))
            test_cases.add(test_group)
        
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT) for t in test_cases], lag_ratio=0.3))
        self.wait(0.5)
        
        # Run tests with status indicators
        for i, test in enumerate(test_cases):
            # Running indicator
            running = Text("⟳", font_size=36, color=YELLOW)
            running.next_to(test, RIGHT)
            self.play(FadeIn(running))
            self.wait(0.3)
            
            # Result (all pass for this demo)
            if i < 3:
                result = Text("✓", font_size=36, color=GREEN)
            else:
                result = Text("✓", font_size=36, color=GREEN)
            
            result.next_to(test, RIGHT)
            self.play(Transform(running, result))
            self.wait(0.2)
        
        # Summary
        summary_box = Rectangle(height=1.5, width=6, color=GREEN, fill_opacity=0.3)
        summary_box.to_edge(DOWN, buff=0.5)
        
        summary_text = Text(
            "All Tests Passed ✓\n4/4 Successful\n0 Failures",
            font_size=28,
            color=GREEN
        )
        summary_text.move_to(summary_box.get_center())
        
        summary = VGroup(summary_box, summary_text)
        self.play(FadeIn(summary, shift=UP))
        
        # Celebration
        confetti = VGroup()
        for _ in range(20):
            dot = Dot(
                color=random.choice([RED, BLUE, GREEN, YELLOW, PURPLE]),
                radius=0.1
            )
            dot.move_to([
                np.random.uniform(-6, 6),
                4,
                0
            ])
            confetti.add(dot)
        
        self.play(
            *[dot.animate.shift(DOWN * 8).set_opacity(0) for dot in confetti],
            run_time=1.5
        )
        
        self.wait(2)


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 7_Testing_known/testing.py TestingAnimation")
