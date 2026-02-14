#!/bin/bash
# Render all Manim animations for DaVinci Resolve

echo "🎬 Manim Animation Renderer"
echo "============================"
echo ""
echo "This script will render all animations in high quality"
echo "Output format: MP4 (H.264) - DaVinci Resolve compatible"
echo "Resolution: 1920x1080 (Full HD)"
echo "Frame Rate: 60 FPS"
echo ""

# Check if manim is installed
if ! command -v manim &> /dev/null; then
    echo "❌ Error: Manim is not installed"
    echo "Please install with: pip install -r requirements.txt"
    exit 1
fi

echo "✅ Manim is installed"
echo ""

# Array of animations to render
declare -a animations=(
    "1_Real_Unknown/goal.py:GoalAnimation"
    "2_Environment/read_files.py:FileReadAnimation"
    "3_Simulation/simulation.py:SimulationAnimation"
    "4_Formula/formula.py:FormulaAnimation"
    "5_Symbols/code.py:CodeAnimation"
    "6_Semblance/errors.py:ErrorAnimation"
    "7_Testing_known/testing.py:TestingAnimation"
)

# Create output directory
mkdir -p media/videos

echo "Starting rendering process..."
echo ""

# Counter
total=${#animations[@]}
current=0

# Render each animation
for animation in "${animations[@]}"; do
    current=$((current + 1))
    IFS=':' read -r file scene <<< "$animation"
    
    echo "[$current/$total] Rendering: $scene from $file"
    echo "----------------------------------------"
    
    # Render with high quality settings
    manim -qh --format=mp4 --media_dir ./media "$file" "$scene"
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully rendered: $scene"
    else
        echo "❌ Failed to render: $scene"
    fi
    
    echo ""
done

echo "============================"
echo "✨ Rendering complete!"
echo ""
echo "📁 Output location: ./media/videos/"
echo ""
echo "📋 Next steps:"
echo "1. Open DaVinci Resolve"
echo "2. Import videos from ./media/videos/ folders"
echo "3. Edit and enhance your animations"
echo "4. Export your final video"
echo ""
echo "For more information, see DAVINCI_RESOLVE.md"
