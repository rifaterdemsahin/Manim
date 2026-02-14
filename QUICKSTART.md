# Quick Start Guide

## Installation

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Verify Installation
```bash
python -c "import manim; print(manim.__version__)"
```

## Running Animations

### Basic Syntax
```bash
manim [options] <script_file> <SceneClass>
```

### Quality Options
- `-ql` - Low quality (480p, 15fps) - Fast preview
- `-qm` - Medium quality (720p, 30fps) - Good for testing
- `-qh` - High quality (1080p, 60fps) - Production ready
- `-qk` - 4K quality (2160p, 60fps) - Ultra HD

### Common Options
- `-p` - Play video after rendering
- `-s` - Save last frame as image
- `-a` - Render all scenes in file
- `--format=mp4` - Output as MP4 (default)

## Examples

### 1. Goal Animation (Quick Preview)
```bash
manim -pql 1_Real_Unknown/goal.py GoalAnimation
```

### 2. File Reading (Production Quality)
```bash
manim -pqh 2_Environment/read_files.py FileReadAnimation
```

### 3. Render All Animations
```bash
# Render all scenes from all files
for file in */*.py; do
    manim -qh --format=mp4 "$file"
done
```

### 4. Custom Output Directory
```bash
manim -qh --media_dir ./my_output 1_Real_Unknown/goal.py GoalAnimation
```

## DaVinci Resolve Import

### Step 1: Locate Rendered Videos
After rendering, find your videos in:
```
media/videos/<folder_name>/<quality>/
```

### Step 2: Import to DaVinci Resolve
1. Open DaVinci Resolve
2. Create new project or open existing
3. Navigate to **Media Pool** (bottom left)
4. Right-click → **Import Media**
5. Select your MP4 files
6. Drag to timeline for editing

### Step 3: Project Settings (if needed)
- Timeline Format: 1920x1080 HD
- Frame Rate: 60 fps
- Color Space: Rec.709 / sRGB

## Troubleshooting

### Problem: "Command not found: manim"
**Solution:** Ensure Manim is installed:
```bash
pip install manim
```

### Problem: LaTeX errors
**Solution:** Install LaTeX (for mathematical formulas):
```bash
# Ubuntu/Debian
sudo apt-get install texlive texlive-latex-extra

# macOS
brew install --cask mactex
```

### Problem: Slow rendering
**Solution:** Use lower quality for previews:
```bash
manim -ql script.py SceneName  # Fast preview
```

### Problem: Import issues in Python
**Solution:** Check Python path:
```bash
python -c "import sys; print(sys.path)"
pip list | grep manim
```

## Customization Tips

### Change Colors
```python
# Use built-in colors
circle = Circle(color=RED)

# Or use hex colors
circle = Circle(color="#FF5733")
```

### Adjust Timing
```python
# Wait between animations
self.wait(2)  # Wait 2 seconds

# Control animation speed
self.play(Create(circle), run_time=3)  # 3 seconds
```

### Position Objects
```python
# Absolute positioning
obj.move_to([x, y, z])

# Relative positioning
obj.to_edge(UP)
obj.shift(RIGHT * 2)
obj.next_to(other_obj, DOWN)
```

## Tips for Video Production

1. **Consistent Quality**: Use `-qh` for all production renders
2. **Test First**: Use `-ql` for quick previews
3. **Silent Audio**: Add audio in DaVinci Resolve
4. **Multiple Takes**: Render variations for editing options
5. **Naming Convention**: Use descriptive scene names
6. **Batch Rendering**: Script multiple renders for efficiency

## Next Steps

1. Review the sample animations in each folder
2. Modify existing animations to understand the code
3. Create your own scenes based on your needs
4. Check out [Manim documentation](https://docs.manim.community/)
5. Watch [3Blue1Brown tutorials](https://www.youtube.com/c/3blue1brown)

## Support

- GitHub Issues: Report problems
- Manim Community: Join Discord server
- Documentation: https://docs.manim.community/
- Examples: Check the 7 sample animations
