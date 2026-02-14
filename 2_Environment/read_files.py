"""
2_Environment: File Reading Animation
This animation demonstrates reading and processing files from the environment.
"""

from manim import *

class FileReadAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Environment: Reading Files", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create file icons
        files = VGroup()
        file_names = ["config.txt", "data.json", "settings.xml", "input.csv"]
        
        for i, name in enumerate(file_names):
            # File rectangle
            file_rect = Rectangle(height=1, width=1.5, color=BLUE, fill_opacity=0.3)
            file_label = Text(name, font_size=18)
            file_label.move_to(file_rect.get_center())
            
            file_group = VGroup(file_rect, file_label)
            file_group.shift(LEFT * 4 + DOWN * (i * 0.8 - 1.5))
            files.add(file_group)
        
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT) for f in files], lag_ratio=0.3))
        self.wait(0.5)
        
        # Create processor
        processor = Circle(radius=0.8, color=GREEN, fill_opacity=0.3)
        processor_label = Text("Processor", font_size=20)
        processor_label.move_to(processor.get_center())
        processor_group = VGroup(processor, processor_label)
        
        self.play(Create(processor_group))
        self.wait(0.5)
        
        # Create data stream
        for file in files:
            data_stream = Arrow(
                file.get_right(),
                processor.get_left(),
                buff=0.2,
                color=YELLOW
            )
            
            self.play(Create(data_stream), run_time=0.5)
            self.play(FadeOut(data_stream), run_time=0.3)
        
        # Output
        output = Rectangle(height=2, width=2, color=PURPLE, fill_opacity=0.3)
        output.shift(RIGHT * 4)
        output_label = Text("Output\nData", font_size=24)
        output_label.move_to(output.get_center())
        output_group = VGroup(output, output_label)
        
        self.play(FadeIn(output_group, shift=LEFT))
        
        # Final arrow
        final_arrow = Arrow(
            processor.get_right(),
            output.get_left(),
            buff=0.2,
            color=GREEN,
            stroke_width=6
        )
        self.play(Create(final_arrow))
        
        self.wait(2)


if __name__ == "__main__":
    import os
    os.system("manim -pqh --format=mp4 --media_dir ./media 2_Environment/read_files.py FileReadAnimation")
