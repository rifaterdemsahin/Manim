# Claude Code Integration Guide

## Project Overview

This is a Manim Animation Project designed for creating professional mathematical and technical animations optimized for video production and DaVinci Resolve integration.

## Project Structure

```
Manim/
├── 1_Real_Unknown/      # Goal setting and exploration animations
├── 2_Environment/       # File operations and environment configs
├── 3_Simulation/        # Particle systems and simulations
├── 4_Formula/           # Mathematical formulas (E=mc², Pythagorean, etc.)
├── 5_Symbols/           # Code visualization and algorithms
├── 6_Semblance/         # Error handling and debugging
├── 7_Testing_known/     # Testing and validation workflows
├── .github/workflows/   # CI/CD automation
├── media/               # Generated video outputs (gitignored)
├── requirements.txt     # Python dependencies
└── manim.cfg            # Manim configuration
```

## Technology Stack

- **Manim Community Edition** (>=0.18.0) - Mathematical Animation Engine
- **Python** (3.8+) - Programming language
- **NumPy** (>=1.26.0) - Numerical computations
- **Pillow** (>=10.0.0) - Image processing
- **DaVinci Resolve** - Video editing (target platform)

## Key Configuration

### Video Output Settings (manim.cfg)
- **Resolution**: 1920x1080 (Full HD)
- **Frame Rate**: 60 FPS
- **Format**: MP4 (H.264 codec)
- **Pixel Format**: yuv420p
- **Quality**: High quality

## Animation Categories

### 1. Real Unknown (Goal Setting)
- Visualizes journey from uncertainty to achievement
- Files: goal.py

### 2. Environment (File Operations)
- Demonstrates data ingestion and configuration
- Files: read_files.py

### 3. Simulation (Dynamic Systems)
- Monte Carlo style particle simulations
- Files: simulation.py

### 4. Formula (Mathematical Concepts)
- 6 different animations covering:
  - Einstein's E=mc²
  - Pythagorean theorem
  - Quadratic formula
  - Euler's formula
  - Calculus derivatives
  - Integration visualization
  - Trigonometric identities
- Files: formula.py

### 5. Symbols (Code Visualization)
- Code structure and recursive algorithms
- Files: code.py, examples.py, goal.py

### 6. Semblance (Error Handling)
- Error detection and fixing workflows
- Files: errors.py

### 7. Testing Known (Quality Assurance)
- Test execution and validation
- Files: testing.py

## Common Commands

### Rendering Animations

```bash
# High quality render with preview
manim -pqh <folder>/<file>.py <SceneClassName>

# Examples for each category
manim -pqh 1_Real_Unknown/goal.py GoalAnimation
manim -pqh 2_Environment/read_files.py FileReadAnimation
manim -pqh 3_Simulation/simulation.py SimulationAnimation
manim -pqh 4_Formula/formula.py FormulaAnimation
manim -pqh 5_Symbols/code.py CodeAnimation
manim -pqh 6_Semblance/errors.py ErrorAnimation
manim -pqh 7_Testing_known/testing.py TestingAnimation
```

### Quality Options
- `-ql`: Low quality (480p) - for quick testing
- `-qm`: Medium quality (720p)
- `-qh`: High quality (1080p) - recommended
- `-qk`: 4K quality (2160p)

### Development Workflow

```bash
# Setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Quick test (low quality)
manim -pql <folder>/<file>.py <SceneName>

# Production render
manim -pqh --format=mp4 <folder>/<file>.py <SceneName>
```

## Development Guidelines

### Animation Creation Template

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

        self.wait(2)  # End pause
```

### Naming Conventions
- **Files**: lowercase_with_underscores.py
- **Classes**: PascalCaseAnimation
- **Variables**: descriptive_snake_case

### Best Practices
1. **Duration**: Keep animations 5-30 seconds for optimal editing
2. **Colors**: Use Manim's built-in colors (RED, BLUE, GREEN, YELLOW, etc.)
3. **Timing**: Use `wait()` strategically for pacing
4. **Documentation**: Always include docstrings
5. **Testing**: Test with `-ql` before rendering with `-qh`

## DaVinci Resolve Integration

### Export Settings
All animations are pre-configured for DaVinci Resolve:
- Format: MP4 (H.264)
- Resolution: 1920x1080
- Frame Rate: 60 FPS
- Color Space: sRGB
- Audio: Silent (add in post)

### Import Process
1. Open DaVinci Resolve
2. Navigate to Media Pool
3. Import from `media/videos/` directory
4. Drag clips to timeline
5. Edit and export

## Git Workflow

```bash
# Create feature branch
git checkout -b add-animation-<name>

# Make changes and commit
git add <folder>/<file>.py
git commit -m "Add <animation> to <category>"

# Push and create PR
git push origin add-animation-<name>
```

## Resources

### Documentation
- [Manim Community Docs](https://docs.manim.community/)
- [Manim Reference Manual](https://docs.manim.community/en/stable/reference.html)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)

### Learning
- [3Blue1Brown YouTube](https://www.youtube.com/c/3blue1brown)
- [Manim Tutorial](https://youtu.be/5qj3b7DY5oA)
- [Manim Discord Community](https://www.manim.community/discord/)

## Project Links

- **Repository**: https://github.com/rifaterdemsahin/Manim
- **Website**: https://rifaterdemsahin.github.io/Manim/
- **Inspiration**: [3Blue1Brown Animation Tutorial](https://youtu.be/5qj3b7DY5oA)

## Claude Code Tips

### Working with Animations
- When creating new animations, choose the appropriate category folder
- Follow the existing animation patterns in similar files
- Test locally with low quality before committing
- Update README.md if adding new concepts

### Common Tasks
- **Add new animation**: Copy template, customize, test, commit
- **Modify existing**: Read file, make changes, test render
- **Batch render**: Loop through categories for batch processing
- **Debug timing**: Use `self.wait()` and adjust `run_time` parameters

### File Operations
- Animation files are in numbered folders (1-7)
- Output goes to `media/` directory (gitignored)
- Configuration is in `manim.cfg`
- Dependencies listed in `requirements.txt`

## Notes for AI Assistants

- This project uses Manim Community Edition, not the original manim
- All animations target 60 FPS at 1080p for professional video production
- The 7-folder structure represents different software development concepts
- DaVinci Resolve compatibility is a key requirement
- Each animation should be self-contained and render independently
- Git workflow should follow standard branching model

---

**Last Updated**: 2026-02-14
**Manim Version**: >=0.18.0
**Python Version**: 3.8+
