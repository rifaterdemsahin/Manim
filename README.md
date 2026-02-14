# Manim Animation Project for Video Production

This project contains sample Manim animations optimized for video production and DaVinci Resolve compatibility. The animations are organized into seven conceptual categories representing different aspects of software development and problem-solving.

## 🎯 Project Overview

This project demonstrates how to create professional animations for technical content, educational videos, and software development concepts using Manim (Mathematical Animation Engine). All outputs are configured for seamless import into DaVinci Resolve for further video editing.

**Inspired by:** [3Blue1Brown Animation Tutorial](https://youtu.be/5qj3b7DY5oA)

## 📁 Project Structure

The project is organized into 7 thematic folders, each representing a different concept:

### 1. **1_Real_Unknown** - Goal Setting
- **Purpose:** Represents exploring unknown territories and setting achievable goals
- **Animation:** `goal.py` - Visualizes the journey from uncertainty to goal achievement
- **Concept:** Starting from the unknown, navigating obstacles, and reaching defined objectives

### 2. **2_Environment** - Reading Files
- **Purpose:** Demonstrates data ingestion and environment configuration
- **Animation:** `read_files.py` - Shows file reading and data processing workflows
- **Concept:** How systems read configuration files, data inputs, and environment variables

### 3. **3_Simulation** - Particle Systems
- **Purpose:** Illustrates simulation and modeling concepts
- **Animation:** `simulation.py` - Monte Carlo style particle simulation
- **Concept:** Running simulations to understand complex system behaviors

### 4. **4_Formula** - Mathematical Formulas
- **Purpose:** Visualizes mathematical concepts and equations
- **Animation:** `formula.py` - Famous equations like E=mc² and Pythagorean theorem
- **Concept:** Making abstract mathematical ideas concrete and understandable

### 5. **5_Symbols** - Code Visualization
- **Purpose:** Represents programming concepts and algorithms
- **Animation:** `code.py` - Shows code structure and recursive algorithms
- **Concept:** Visualizing how code works internally

### 6. **6_Semblance** - Error Handling
- **Purpose:** Demonstrates debugging and error management
- **Animation:** `errors.py` - Error detection and fixing workflow
- **Concept:** How to identify, handle, and resolve errors in code

### 7. **7_Testing_known** - Validation
- **Purpose:** Shows testing and quality assurance processes
- **Animation:** `testing.py` - Test execution and validation workflows
- **Concept:** Ensuring code quality through systematic testing

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8 or higher
python3 --version

# Install dependencies
pip install -r requirements.txt
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rifaterdemsahin/Manim.git
cd Manim
```

2. Install Manim and dependencies:
```bash
pip install -r requirements.txt
```

### Running Animations

Each folder contains a Python script that can be run independently:

```bash
# General syntax
manim -pqh <script_path> <SceneClassName>

# Examples:
manim -pqh 1_Real_Unknown/goal.py GoalAnimation
manim -pqh 2_Environment/read_files.py FileReadAnimation
manim -pqh 3_Simulation/simulation.py SimulationAnimation
manim -pqh 4_Formula/formula.py FormulaAnimation
manim -pqh 5_Symbols/code.py CodeAnimation
manim -pqh 6_Semblance/errors.py ErrorAnimation
manim -pqh 7_Testing_known/testing.py TestingAnimation
```

### Render Options

- `-p` : Preview the animation after rendering
- `-q` : Quality setting
  - `-ql` : Low quality (480p)
  - `-qm` : Medium quality (720p)
  - `-qh` : High quality (1080p)
  - `-qk` : 4K quality (2160p)
- `--format=mp4` : Output format (MP4 is best for DaVinci Resolve)

## 🎬 DaVinci Resolve Compatibility

All animations are rendered with settings optimized for DaVinci Resolve:

- **Format:** MP4 (H.264 codec)
- **Resolution:** 1920x1080 (Full HD)
- **Frame Rate:** 60 FPS
- **Color Space:** sRGB
- **Audio:** Silent (can be added in post-production)

### Importing into DaVinci Resolve

1. Open DaVinci Resolve
2. Create a new project or open existing
3. Go to Media Pool
4. Import the rendered videos from `media/videos/` folder
5. Drag and drop to timeline for editing

## 💡 Prompt Examples

### Creating New Animations

Here are example prompts to create your own animations:

1. **Data Flow Animation:**
   ```
   "Create a Manim animation showing data flowing through a pipeline 
   with three stages: input, processing, and output. Use arrows and 
   color-coded boxes."
   ```

2. **Algorithm Visualization:**
   ```
   "Animate a sorting algorithm (bubble sort) with colored bars that 
   swap positions. Show the comparison and swap operations clearly."
   ```

3. **Network Topology:**
   ```
   "Create an animation showing nodes connecting in a network topology. 
   Start with isolated nodes, then connect them with edges one by one."
   ```

4. **State Machine:**
   ```
   "Visualize a state machine with 4 states (Idle, Running, Paused, Stopped). 
   Show transitions between states with labeled arrows."
   ```

5. **Data Structure:**
   ```
   "Animate how a binary search tree works. Show insertion of nodes 
   with values: 50, 30, 70, 20, 40, 60, 80."
   ```

### Customization Tips

- **Colors:** Use Manim's built-in colors (RED, BLUE, GREEN, etc.) or hex codes
- **Timing:** Adjust `wait()` and `run_time` parameters for pacing
- **Transitions:** Experiment with FadeIn, FadeOut, Transform, MoveAlongPath
- **Text:** Use `Text()` for regular text and `MathTex()` for equations
- **Layouts:** Use `.to_edge()`, `.shift()`, `.next_to()` for positioning

## 📚 Learning Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [3Blue1Brown Channel](https://www.youtube.com/c/3blue1brown)
- [Manim Tutorial Video](https://youtu.be/5qj3b7DY5oA)
- [Manim GitHub Repository](https://github.com/ManimCommunity/manim)

## 🛠️ Development Workflow

1. **Create Animation:** Write your Manim scene in Python
2. **Test Locally:** Run with `-ql` for quick preview
3. **Refine:** Adjust timing, colors, and positioning
4. **Final Render:** Use `-qh` or `-qk` for production quality
5. **Import to DaVinci:** Load MP4 files for further editing
6. **Export:** Render final video from DaVinci Resolve

## 🤝 Contributing

Contributions are welcome! To add new animations:

1. Choose appropriate folder based on concept
2. Follow the naming convention
3. Include docstring explaining the animation
4. Test render before committing
5. Update README if adding new concepts

## 📄 License

This project is open source and available for educational purposes.

## 🎨 Output Gallery

Visit the [project website](https://rifaterdemsahin.github.io/Manim/) to see rendered examples of all animations.

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check Manim community documentation
- Review the example animations for reference

---

**Made with ❤️ using Manim**
