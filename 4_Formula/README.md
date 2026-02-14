# 4_Formula: Mathematical Formulas Visualization

This folder contains Manim animations that visualize various mathematical formulas and concepts. Each animation demonstrates a different mathematical principle with clear visualizations and examples.

## Available Animations

### 1. FormulaAnimation
**Description:** Demonstrates famous mathematical formulas including Einstein's equation and the Pythagorean theorem.

**Featured Concepts:**
- Einstein's mass-energy equivalence: E = mc²
- Pythagorean theorem: a² + b² = c²
- Visual representation with right triangle

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py FormulaAnimation
```

---

### 2. QuadraticFormulaAnimation
**Description:** Visualizes the quadratic formula and shows how to solve quadratic equations.

**Featured Concepts:**
- General quadratic form: ax² + bx + c = 0
- Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a
- Example solution: x² + 5x + 6 = 0

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py QuadraticFormulaAnimation
```

---

### 3. EulerFormulaAnimation
**Description:** Shows Euler's formula and its special case, Euler's identity - often called "the most beautiful equation."

**Featured Concepts:**
- Euler's formula: e^(iθ) = cos(θ) + i·sin(θ)
- Euler's identity: e^(iπ) + 1 = 0
- Connection between exponential and trigonometric functions

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py EulerFormulaAnimation
```

---

### 4. DerivativeAnimation
**Description:** Visualizes the concept of derivatives as the rate of change, with a graph showing the tangent line.

**Featured Concepts:**
- Derivative definition: df/dx = lim(h→0) [f(x+h) - f(x)] / h
- Example function: f(x) = x²
- Tangent line visualization at x = 1
- Slope interpretation: f'(1) = 2

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py DerivativeAnimation
```

---

### 5. IntegralAnimation
**Description:** Demonstrates integration as the area under a curve.

**Featured Concepts:**
- Integral notation: ∫ₐᵇ f(x) dx
- Visual representation of area under curve
- Definite integral bounds

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py IntegralAnimation
```

---

### 6. TrigIdentityAnimation
**Description:** Shows fundamental trigonometric identities with unit circle visualization.

**Featured Concepts:**
- Pythagorean identity: sin²(θ) + cos²(θ) = 1
- Double angle formulas:
  - sin(2θ) = 2sin(θ)cos(θ)
  - cos(2θ) = cos²(θ) - sin²(θ)
- Unit circle representation

**How to render:**
```bash
manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py TrigIdentityAnimation
```

---

## Rendering All Animations at Once

You can render all formula animations at once using the included script in `formula.py`:

```bash
python 4_Formula/formula.py
```

Or render them all with high quality:
```bash
for anim in FormulaAnimation QuadraticFormulaAnimation EulerFormulaAnimation DerivativeAnimation IntegralAnimation TrigIdentityAnimation; do
    manim -pqh --format=mp4 --media_dir ./media 4_Formula/formula.py $anim
done
```

## Quality Settings

- **Low Quality (480p):** `-ql` - Fast rendering for testing
- **Medium Quality (720p):** `-qm` - Good for previews
- **High Quality (1080p):** `-qh` - Production ready
- **4K Quality (2160p):** `-qk` - Ultra high definition

## Output Location

Rendered videos are saved to:
```
media/videos/formula/<quality>/
```

For example:
- Low quality: `media/videos/formula/480p15/`
- High quality: `media/videos/formula/1080p60/`

## DaVinci Resolve Compatibility

All animations are rendered in MP4 format with H.264 codec, making them fully compatible with DaVinci Resolve for further video editing and post-production.

## Educational Use

These animations are perfect for:
- Mathematics education videos
- STEM content creation
- Tutorial videos
- Educational presentations
- Online courses
- Math visualization projects

## Customization

Feel free to modify any animation by:
1. Editing the corresponding class in `formula.py`
2. Adjusting colors, timing, or positions
3. Adding new mathematical concepts
4. Creating variations of existing animations

## Requirements

- Python 3.8+
- Manim Community Edition (v0.18.0+)
- LaTeX (for rendering mathematical expressions)
- ffmpeg (for video encoding)

See the main repository README for installation instructions.
