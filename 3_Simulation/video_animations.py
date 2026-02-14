"""
3_Simulation: Video Production Animations
This module contains animations created from the storyboard, graphics, and shot list inputs.
All animations are optimized for video production and DaVinci Resolve integration.
"""

from manim import *
import numpy as np

class StaticVsDynamicAnimation(Scene):
    """
    Scene 3: Static vs. Dynamic (00:00:35 - 00:00:48)
    Visualizes the transformation from static rules to dynamic AI.
    """
    def construct(self):
        # Title
        title = Text("Breaking the Iron Chains", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Split screen labels
        left_label = Text("Static Rules", font_size=32, color=GRAY).to_edge(LEFT).shift(UP * 2.5)
        right_label = Text("Dynamic AI", font_size=32, color=BLUE).to_edge(RIGHT).shift(UP * 2.5)

        # Static side - Stone statue (represented by rigid squares)
        static_blocks = VGroup(*[
            Square(side_length=0.4, color=GRAY, fill_opacity=0.8).shift(
                LEFT * 3.5 + UP * (1.5 - i * 0.5) + RIGHT * (j * 0.5)
            )
            for i in range(6) for j in range(3)
        ])

        # Dynamic side - Fluid mercury (represented by flowing particles)
        dynamic_particles = VGroup(*[
            Dot(color=BLUE, radius=0.08).shift(
                RIGHT * 3.5 + UP * np.random.uniform(-2, 2) + LEFT * np.random.uniform(0, 1)
            )
            for _ in range(50)
        ])

        # Show labels and elements
        self.play(Write(left_label), Write(right_label), run_time=0.8)
        self.play(FadeIn(static_blocks), run_time=1)
        self.play(LaggedStart(*[FadeIn(p) for p in dynamic_particles], lag_ratio=0.02), run_time=1.5)
        self.wait(0.5)

        # Breaking chains animation
        chains = VGroup(*[
            Line(
                LEFT * 5 + UP * (2 - i),
                LEFT * 5 + DOWN * (2 - i),
                color=GRAY,
                stroke_width=8
            )
            for i in range(3)
        ])

        self.play(Create(chains), run_time=0.5)

        # Chains breaking
        for chain in chains:
            self.play(
                chain.animate.scale(0.1).set_opacity(0),
                run_time=0.3
            )

        # Transformation - static blocks dissolve into dynamic particles
        self.play(
            *[block.animate.scale(0.1).set_opacity(0) for block in static_blocks],
            *[p.animate.shift(LEFT * 7 + np.random.randn(3) * 0.3) for p in dynamic_particles],
            run_time=2
        )

        self.wait(1)


class GitCloneAnimation(Scene):
    """
    Scene 4: Repository Cloning Animation (00:00:48 - 00:03:52)
    Visualizes the git clone process.
    """
    def construct(self):
        # Title
        title = Text("Git Clone: Copying the Blueprint", font_size=44)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Source repository (cloud)
        cloud = Circle(radius=1.2, color=BLUE, fill_opacity=0.3)
        cloud.shift(UP * 1.5 + LEFT * 4)
        cloud_label = Text("GitHub\nRepository", font_size=24, color=BLUE)
        cloud_label.next_to(cloud, UP)

        # Repository files inside cloud
        files = VGroup(*[
            Rectangle(height=0.15, width=0.6, color=WHITE, fill_opacity=0.5).shift(
                cloud.get_center() + UP * (0.4 - i * 0.2)
            )
            for i in range(4)
        ])

        self.play(Create(cloud), Write(cloud_label), run_time=1)
        self.play(LaggedStart(*[FadeIn(f) for f in files], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        # Local machine
        computer = Rectangle(height=2, width=2.5, color=GREEN, fill_opacity=0.2)
        computer.shift(DOWN * 1 + RIGHT * 4)
        computer_label = Text("Local\nMachine", font_size=24, color=GREEN)
        computer_label.next_to(computer, DOWN)

        self.play(Create(computer), Write(computer_label), run_time=1)
        self.wait(0.5)

        # Connection arrow
        arrow = Arrow(
            cloud.get_bottom(),
            computer.get_top(),
            buff=0.2,
            color=YELLOW,
            stroke_width=6
        )

        self.play(Create(arrow), run_time=1)

        # Clone command text
        command = Text("$ git clone https://github.com/...", font_size=28, color=YELLOW)
        command.next_to(arrow, RIGHT, buff=0.3)
        self.play(Write(command), run_time=1.5)
        self.wait(0.5)

        # Files copying animation
        for i, file in enumerate(files):
            file_copy = file.copy().set_color(YELLOW)
            self.play(
                file_copy.animate.move_to(computer.get_center() + UP * (0.5 - i * 0.3)),
                run_time=0.4
            )
            self.play(file_copy.animate.set_color(GREEN), run_time=0.2)

        # Success indicator
        checkmark = Text("✓", font_size=72, color=GREEN)
        checkmark.move_to(computer.get_center())
        self.play(FadeIn(checkmark, scale=2), run_time=0.6)

        self.wait(1.5)


class SpeedMultiplierAnimation(Scene):
    """
    Scene 8: The Engine Room - Speed Multiplier (00:08:26 - 00:09:01)
    Shows 1000x speed improvement visualization.
    """
    def construct(self):
        # Title
        title = Text("1000x Faster Deployment", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Clock visual
        clock_circle = Circle(radius=1.5, color=WHITE, stroke_width=4)
        clock_center = Dot(color=WHITE, radius=0.1)
        clock = VGroup(clock_circle, clock_center)
        clock.shift(LEFT * 3.5)

        # Clock hands
        hour_hand = Line(ORIGIN, UP * 0.8, color=WHITE, stroke_width=6)
        minute_hand = Line(ORIGIN, UP * 1.2, color=YELLOW, stroke_width=4)
        clock_hands = VGroup(hour_hand, minute_hand)
        clock_hands.move_to(clock.get_center())

        self.play(Create(clock), run_time=0.8)
        self.play(Create(clock_hands), run_time=0.5)

        # Spinning animation
        self.play(
            Rotate(clock_hands, angle=20 * PI, run_time=2),
        )

        # Speed comparison bars
        traditional_bar = Rectangle(height=0.5, width=2, color=RED, fill_opacity=0.7)
        traditional_bar.shift(RIGHT * 2 + UP * 1)
        traditional_label = Text("Traditional: 1000 hours", font_size=22, color=RED)
        traditional_label.next_to(traditional_bar, LEFT)

        ai_bar = Rectangle(height=0.5, width=8, color=GREEN, fill_opacity=0.7)
        ai_bar.shift(RIGHT * 2 + DOWN * 1)
        ai_label = Text("AI-Powered: 1 hour", font_size=22, color=GREEN)
        ai_label.next_to(ai_bar, LEFT)

        # Animate bars
        self.play(
            Write(traditional_label),
            traditional_bar.animate.set_width(2),
            run_time=0.8
        )

        self.play(
            Write(ai_label),
            ai_bar.animate.set_width(8),
            run_time=1.2
        )

        # 1000x text
        multiplier = Text("1000x", font_size=96, color=YELLOW, weight=BOLD)
        multiplier.shift(DOWN * 0)
        self.play(FadeIn(multiplier, scale=2), run_time=1)

        self.wait(1.5)


class CICDPipelineAnimation(Scene):
    """
    Scene 11: CI/CD Pipeline Flow (00:13:15 - 00:17:24)
    Visualizes the continuous integration and deployment pipeline.
    """
    def construct(self):
        # Title
        title = Text("CI/CD Pipeline: Automated Deployment", font_size=42)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Pipeline stages
        stages = [
            {"name": "Code", "color": BLUE, "icon": "{ }"},
            {"name": "Test", "color": PURPLE, "icon": "✓"},
            {"name": "Build", "color": ORANGE, "icon": "⚙"},
            {"name": "Deploy", "color": YELLOW, "icon": "↑"},
            {"name": "Live", "color": GREEN, "icon": "★"}
        ]

        stage_objects = VGroup()
        stage_labels = VGroup()

        start_x = -5
        spacing = 2.5

        for i, stage in enumerate(stages):
            # Stage box
            box = RoundedRectangle(
                height=1.2,
                width=1.8,
                corner_radius=0.2,
                color=stage["color"],
                fill_opacity=0.3,
                stroke_width=3
            )
            box.shift(RIGHT * (start_x + i * spacing))

            # Icon
            icon = Text(stage["icon"], font_size=36, color=stage["color"])
            icon.move_to(box.get_center() + UP * 0.2)

            # Label
            label = Text(stage["name"], font_size=24, color=WHITE)
            label.move_to(box.get_center() + DOWN * 0.3)

            stage_group = VGroup(box, icon, label)
            stage_objects.add(stage_group)

            # Create stage with animation
            self.play(FadeIn(stage_group, shift=DOWN * 0.3), run_time=0.5)

            # Arrow between stages (except for last stage)
            if i < len(stages) - 1:
                arrow = Arrow(
                    box.get_right(),
                    box.get_right() + RIGHT * (spacing - 1.8),
                    buff=0,
                    color=WHITE,
                    stroke_width=3
                )
                self.play(Create(arrow), run_time=0.4)

        self.wait(0.8)

        # Data flow animation (dot traveling through pipeline)
        flow_dot = Dot(color=YELLOW, radius=0.15)
        flow_dot.move_to(stage_objects[0].get_center())

        self.play(FadeIn(flow_dot, scale=2), run_time=0.3)

        for i in range(len(stages) - 1):
            # Highlight current stage
            self.play(
                stage_objects[i][0].animate.set_fill(opacity=0.6),
                run_time=0.3
            )

            # Move dot to next stage
            self.play(
                flow_dot.animate.move_to(stage_objects[i + 1].get_center()),
                run_time=0.6
            )

            # Add checkmark
            check = Text("✓", font_size=32, color=GREEN)
            check.next_to(stage_objects[i], UP, buff=0.2)
            self.play(FadeIn(check, scale=1.5), run_time=0.3)

        # Final stage highlight
        self.play(
            stage_objects[-1][0].animate.set_fill(opacity=0.6),
            run_time=0.3
        )

        # Success message
        success = Text("✓ Deployment Successful!", font_size=36, color=GREEN)
        success.to_edge(DOWN, buff=0.5)
        self.play(Write(success), run_time=1)

        self.wait(2)


class LLMFeatureCardsAnimation(Scene):
    """
    Scene 9: The Digital Feast - LLM Feature Cards (00:09:01 - 00:11:45)
    Shows comparison of different LLM options.
    """
    def construct(self):
        # Title
        title = Text("Choose Your AI Assistant", font_size=48)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # LLM data
        llms = [
            {
                "name": "Claude",
                "tagline": "The Reasoning Layer",
                "features": ["Sonnet 3.5, 4.5, 4.6", "Complex Problems", "Code Analysis"],
                "color": ORANGE
            },
            {
                "name": "ChatGPT",
                "tagline": "The Versatile Leader",
                "features": ["Search & Browse", "Plugins", "General Purpose"],
                "color": GREEN
            },
            {
                "name": "DeepSeek",
                "tagline": "The Coding Disruptor",
                "features": ["Free & Powerful", "Development Focus", "Open Source"],
                "color": BLUE
            },
            {
                "name": "Gemini",
                "tagline": "The Versatile Platform",
                "features": ["Multi-modal", "Images & Code", "Google Integration"],
                "color": PURPLE
            }
        ]

        # Create and display cards one by one
        for i, llm in enumerate(llms):
            # Card container
            card = RoundedRectangle(
                height=3.5,
                width=3,
                corner_radius=0.3,
                color=llm["color"],
                fill_opacity=0.2,
                stroke_width=4
            )
            card.shift(LEFT * 4.5 + RIGHT * (i * 3.3))

            # Name
            name = Text(llm["name"], font_size=32, color=llm["color"], weight=BOLD)
            name.move_to(card.get_top() + DOWN * 0.5)

            # Tagline
            tagline = Text(llm["tagline"], font_size=18, color=WHITE)
            tagline.move_to(card.get_center() + UP * 0.5)

            # Features
            features_group = VGroup()
            for j, feature in enumerate(llm["features"]):
                feature_text = Text(f"• {feature}", font_size=16, color=GRAY)
                feature_text.move_to(card.get_center() + DOWN * (0.2 + j * 0.4))
                features_group.add(feature_text)

            # Logo placeholder (circle with initial)
            logo = Circle(radius=0.4, color=llm["color"], fill_opacity=0.5)
            logo.move_to(card.get_center() + UP * 1.2)
            logo_text = Text(llm["name"][0], font_size=36, color=WHITE)
            logo_text.move_to(logo.get_center())

            card_group = VGroup(card, logo, logo_text, name, tagline, features_group)

            # Animate card entrance
            self.play(
                FadeIn(card_group, shift=UP * 0.5),
                run_time=0.8
            )
            self.wait(0.3)

        # "100+ Options" text
        options_text = Text("100+ AI Models Available", font_size=32, color=GOLD)
        options_text.to_edge(DOWN, buff=0.5)
        self.play(Write(options_text), run_time=1)

        self.wait(2)


class NumberCounterAnimation(Scene):
    """
    Animated number counter for statistics (37+ commits, 240 workflows, etc.)
    """
    def construct(self):
        # Title
        title = Text("Project Evolution", font_size=48)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Statistics
        stats = [
            {"label": "Workflows Built", "value": 240, "color": BLUE},
            {"label": "Commits Made", "value": 37, "color": GREEN},
            {"label": "Days Active", "value": 90, "color": PURPLE},
            {"label": "Accuracy %", "value": 98, "color": GOLD}
        ]

        stat_objects = VGroup()

        for i, stat in enumerate(stats):
            # Container
            box = RoundedRectangle(
                height=1.5,
                width=3,
                corner_radius=0.2,
                color=stat["color"],
                fill_opacity=0.2,
                stroke_width=3
            )

            # Position in 2x2 grid
            row = i // 2
            col = i % 2
            box.shift(
                LEFT * 2 + RIGHT * (col * 4.5) +
                UP * 1.5 + DOWN * (row * 2.5)
            )

            # Number (will be animated)
            number = Integer(0, font_size=48, color=stat["color"])
            number.move_to(box.get_center() + UP * 0.3)

            # Label
            label = Text(stat["label"], font_size=22, color=WHITE)
            label.move_to(box.get_center() + DOWN * 0.4)

            stat_group = VGroup(box, number, label)
            stat_objects.add(stat_group)

            # Show box and label
            self.play(
                FadeIn(box),
                Write(label),
                run_time=0.5
            )

            # Animate counter
            self.play(
                ChangeDecimalToValue(number, stat["value"]),
                run_time=1.5,
                rate_func=linear
            )

            # Add "+" if applicable
            if stat["label"] in ["Workflows Built", "Commits Made"]:
                plus = Text("+", font_size=36, color=stat["color"])
                plus.next_to(number, RIGHT, buff=0.1)
                self.play(FadeIn(plus), run_time=0.2)

        self.wait(2)


# Render script
if __name__ == "__main__":
    import os

    # Output directory
    output_dir = "/Users/rifaterdemsahin/projects/Manim/3_Simulation/output"
    os.makedirs(output_dir, exist_ok=True)

    scenes = [
        "StaticVsDynamicAnimation",
        "GitCloneAnimation",
        "SpeedMultiplierAnimation",
        "CICDPipelineAnimation",
        "LLMFeatureCardsAnimation",
        "NumberCounterAnimation"
    ]

    print("Rendering animations for video production...")
    for scene in scenes:
        print(f"\n{'='*50}")
        print(f"Rendering: {scene}")
        print(f"{'='*50}\n")

        cmd = f'manim -pqh --format=mp4 --media_dir "{output_dir}" 3_Simulation/video_animations.py {scene}'
        os.system(cmd)

    print("\n" + "="*50)
    print("All animations rendered successfully!")
    print(f"Output location: {output_dir}")
    print("="*50)
