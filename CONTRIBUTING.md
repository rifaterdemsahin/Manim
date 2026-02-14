# Contributing to Manim Animation Project

Thank you for your interest in contributing! This guide will help you add new animations or improve existing ones.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Creating New Animations](#creating-new-animations)
- [Animation Guidelines](#animation-guidelines)
- [Testing Your Animation](#testing-your-animation)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Best Practices](#best-practices)

## Getting Started

### Prerequisites

1. Python 3.8 or higher
2. Manim Community Edition
3. Git for version control
4. A code editor (VS Code, PyCharm, etc.)

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/rifaterdemsahin/Manim.git
cd Manim

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test installation
manim --version
```

## Project Structure

```
Manim/
├── 1_Real_Unknown/      # Goal setting animations
├── 2_Environment/       # Environment and file operations
├── 3_Simulation/        # Simulation and modeling
├── 4_Formula/           # Mathematical formulas
├── 5_Symbols/           # Code and programming
├── 6_Semblance/         # Error handling and debugging
├── 7_Testing_known/     # Testing and validation
├── .github/workflows/   # GitHub Actions
├── media/               # Generated output (gitignored)
├── README.md            # Project overview
├── QUICKSTART.md        # Quick start guide
├── DAVINCI_RESOLVE.md   # DaVinci Resolve integration
├── requirements.txt     # Python dependencies
└── manim.cfg            # Manim configuration
```

## Creating New Animations

### 1. Choose the Right Folder

Select the folder that best matches your animation's concept:

- **1_Real_Unknown**: Goal setting, exploration, discovery
- **2_Environment**: Configuration, files, environment setup
- **3_Simulation**: Simulations, models, dynamic systems
- **4_Formula**: Mathematical equations and proofs
- **5_Symbols**: Code, algorithms, data structures
- **6_Semblance**: Errors, debugging, troubleshooting
- **7_Testing_known**: Tests, validation, quality assurance

### 2. Create Animation File

Use this template for new animations:

```python
"""
<Folder_Name>: <Animation Purpose>
This animation demonstrates <concept description>.
"""

from manim import *

class YourAnimationName(Scene):
    def construct(self):
        # Title
        title = Text("Your Animation Title", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Your animation code here
        # Use Manim objects: Circle, Square, Text, etc.
        # Use animations: Create, Write, Transform, etc.
        
        self.wait(2)  # End pause


if __name__ == "__main__":
    import os
    folder_name = "<folder_name>"  # e.g., "1_Real_Unknown"
    file_name = "<file_name>"      # e.g., "goal.py"
    scene_name = "YourAnimationName"
    os.system(f"manim -pqh --format=mp4 --media_dir ./media {folder_name}/{file_name} {scene_name}")
```

### 3. Name Your Files

Follow these naming conventions:

- **File names**: lowercase with underscores (e.g., `data_flow.py`)
- **Class names**: PascalCase with "Animation" suffix (e.g., `DataFlowAnimation`)
- **Descriptive names**: Clearly indicate what the animation shows

## Animation Guidelines

### Technical Requirements

All animations must meet these specifications for DaVinci Resolve compatibility:

- **Quality**: High (1080p60) using `-qh` flag
- **Format**: MP4 with H.264 codec
- **Duration**: 5-30 seconds (optimal for editing)
- **Frame Rate**: 60 FPS
- **No audio**: Audio added in post-production

### Content Guidelines

1. **Clear Purpose**: Each animation should have a single, clear concept
2. **Visual Clarity**: Use contrasting colors, appropriate sizing
3. **Pacing**: Allow time for viewers to understand each element
4. **Consistency**: Follow style of existing animations
5. **Documentation**: Include docstring explaining the concept

### Timing Best Practices

```python
# Good timing examples
self.wait(0.5)  # Brief pause between elements
self.play(Create(obj), run_time=1)  # 1 second animation
self.wait(2)  # End pause for viewer comprehension

# Animation speeds
self.play(Write(text), run_time=1)     # Fast
self.play(Transform(obj1, obj2), run_time=2)  # Medium
self.play(MoveAlongPath(dot, path), run_time=3)  # Slow
```

### Color Palette

Use Manim's built-in colors for consistency:

```python
# Primary colors
RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE

# Highlights
GOLD, TEAL, PINK, MAROON

# Neutral
WHITE, GRAY, BLACK
```

## Testing Your Animation

### 1. Quick Preview (Low Quality)

```bash
manim -pql <folder>/<file>.py <SceneName>
```

### 2. Check Specific Elements

Test individual components:

```python
# Debug mode: Show only specific objects
self.add(obj)  # Add without animation
self.wait(5)   # Hold to inspect
```

### 3. Production Quality Test

```bash
manim -pqh --format=mp4 <folder>/<file>.py <SceneName>
```

### 4. Verify Output

Check the rendered video:
- Resolution: 1920x1080
- Frame rate: 60 FPS
- Duration: As expected
- No visual glitches

## Submitting Changes

### 1. Create a Branch

```bash
git checkout -b add-animation-<name>
```

### 2. Make Your Changes

- Add your animation file
- Update README.md if adding new category
- Test thoroughly

### 3. Commit Changes

```bash
git add <folder>/<your_file>.py
git commit -m "Add <animation name> to <folder>"
```

### 4. Push and Create PR

```bash
git push origin add-animation-<name>
```

Then create a Pull Request on GitHub with:
- Clear title describing the animation
- Description of what it demonstrates
- Test results/screenshots if applicable

## Code Style

### Python Style

Follow PEP 8 guidelines:

```python
# Good
class MyAnimation(Scene):
    def construct(self):
        title = Text("Hello", font_size=48)
        self.play(Write(title))

# Avoid
class my_animation(Scene):
    def construct(self):
        title=Text("Hello",font_size=48)
        self.play(Write(title))
```

### Manim-Specific Style

```python
# Clear variable names
goal_circle = Circle(radius=0.5, color=YELLOW)
start_point = Dot(color=BLUE)

# Group related objects
scene_title = VGroup(title, subtitle)

# Comment complex animations
# Create recursive tree structure
for i in range(levels):
    # ... animation code
```

### Docstrings

Include helpful docstrings:

```python
"""
<Folder_Name>: <Brief Description>

This animation demonstrates <detailed explanation>.

Key concepts:
- Concept 1
- Concept 2
- Concept 3

Duration: ~<X> seconds
"""
```

## Best Practices

### 1. Start Simple

Begin with basic shapes and transitions:

```python
# Simple object creation
circle = Circle()
square = Square()

# Basic animation
self.play(Create(circle))
self.play(Transform(circle, square))
```

### 2. Build Complexity Gradually

Add details incrementally:

```python
# Step 1: Basic shape
obj = Circle()

# Step 2: Add color and size
obj = Circle(radius=1, color=BLUE, fill_opacity=0.5)

# Step 3: Position and label
obj.shift(UP * 2)
label = Text("Circle").next_to(obj, DOWN)
```

### 3. Use VGroup for Organization

```python
# Group related objects
diagram = VGroup(
    title,
    circle,
    label,
    arrow
)

# Animate as a unit
self.play(diagram.animate.shift(LEFT * 2))
```

### 4. Reuse Code Patterns

Create helper methods for repeated patterns:

```python
class MyAnimation(Scene):
    def create_labeled_circle(self, label_text, position):
        circle = Circle(radius=0.5)
        label = Text(label_text, font_size=24)
        label.next_to(circle, DOWN)
        group = VGroup(circle, label)
        group.move_to(position)
        return group
    
    def construct(self):
        obj1 = self.create_labeled_circle("A", LEFT * 2)
        obj2 = self.create_labeled_circle("B", RIGHT * 2)
```

### 5. Test on Different Systems

- Test on different screen resolutions
- Check performance on lower-end hardware
- Verify colors look good on different monitors

### 6. Optimize Performance

```python
# Good: Animate multiple objects together
self.play(*[Create(obj) for obj in objects])

# Avoid: Individual animations in loop (slower)
for obj in objects:
    self.play(Create(obj))
```

## Resources

### Official Documentation
- [Manim Community Docs](https://docs.manim.community/)
- [Manim Reference Manual](https://docs.manim.community/en/stable/reference.html)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)

### Learning Materials
- [3Blue1Brown YouTube](https://www.youtube.com/c/3blue1brown)
- [Manim Tutorial Series](https://www.youtube.com/results?search_query=manim+tutorial)
- [Manim Discord Community](https://www.manim.community/discord/)

### Tools
- [Manim Editor](https://github.com/ManimCommunity/manim_editor)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)

## Getting Help

If you need assistance:

1. **Check Documentation**: Most questions are answered in official docs
2. **Search Issues**: Look for similar issues on GitHub
3. **Ask Community**: Join Manim Discord for real-time help
4. **Open Issue**: Create detailed issue on GitHub if needed

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers learn
- Give credit where due
- Follow project guidelines

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Git commit history
- Release notes for significant contributions

---

**Thank you for contributing! 🎉**

Your animations help make technical concepts more accessible and engaging for learners worldwide.
