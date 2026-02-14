# DaVinci Resolve Integration Guide

## Overview

This guide explains how to import and work with Manim animations in DaVinci Resolve for professional video production.

## Output Specifications

All Manim animations in this project are rendered with these specifications for optimal DaVinci Resolve compatibility:

- **Format:** MP4 (MPEG-4 Part 14)
- **Video Codec:** H.264 (libx264)
- **Resolution:** 1920x1080 (Full HD)
- **Frame Rate:** 60 FPS
- **Pixel Format:** YUV420P
- **Color Space:** sRGB (Rec.709)
- **Audio:** None (silent - add in post-production)

## Quick Import Guide

### 1. Render Animations

First, render all animations using the provided script:

```bash
./render_all.sh
```

Or render individually:

```bash
manim -qh --format=mp4 1_Real_Unknown/goal.py GoalAnimation
```

### 2. Locate Output Files

Rendered videos are saved in:
```
media/videos/<folder_name>/1080p60/
```

Example:
```
media/videos/goal/1080p60/GoalAnimation.mp4
media/videos/read_files/1080p60/FileReadAnimation.mp4
```

### 3. Import to DaVinci Resolve

#### Method 1: Drag and Drop
1. Open DaVinci Resolve
2. Navigate to **Media Pool** (bottom left panel)
3. Drag MP4 files directly from file explorer into Media Pool

#### Method 2: Import Media
1. In Media Pool, right-click empty space
2. Select **Import Media** or press `Ctrl+I` (Windows) / `Cmd+I` (Mac)
3. Navigate to your video files
4. Select files and click **Open**

#### Method 3: Media Storage
1. Go to **Media Storage** (top left)
2. Navigate to your project folder
3. Drag folders or files into Media Pool

## Project Setup in DaVinci Resolve

### Timeline Settings

For best results, match your timeline settings to the animation specs:

1. **File → Project Settings** or `Shift+9`
2. Navigate to **Master Settings → Timeline Format**
3. Set the following:
   - **Timeline Resolution:** 1920x1080 HD
   - **Timeline Frame Rate:** 60 fps
   - **Playback Frame Rate:** 60 fps

### Color Management

1. Go to **Project Settings → Color Management**
2. Set:
   - **Color Science:** DaVinci YRGB
   - **Input Color Space:** Rec.709 (for animations)
   - **Timeline Color Space:** Rec.709 / sRGB
   - **Output Color Space:** Rec.709 (for web) or Rec.2020 (for HDR)

## Editing Workflow

### 1. Organizing Media

Create bins for better organization:
```
📁 Media Pool
  ├── 📁 01_Goals (1_Real_Unknown)
  ├── 📁 02_Environment (2_Environment)
  ├── 📁 03_Simulation (3_Simulation)
  ├── 📁 04_Formulas (4_Formula)
  ├── 📁 05_Code (5_Symbols)
  ├── 📁 06_Errors (6_Semblance)
  └── 📁 07_Testing (7_Testing_known)
```

### 2. Timeline Assembly

1. Drag clips to timeline in desired order
2. Trim clips as needed (using `I` and `O` for in/out points)
3. Add transitions between clips:
   - **Effects Library → Video Transitions**
   - Drag transition between clips
   - Adjust duration as needed

### 3. Adding Audio

Since Manim animations are silent:

1. Import audio files (music, voiceover, sound effects)
2. Drag to audio tracks below video
3. Sync audio with visual elements
4. Adjust audio levels in **Fairlight** page

### 4. Color Grading (Optional)

1. Switch to **Color** page
2. Apply color corrections if needed:
   - Adjust exposure
   - Enhance colors
   - Add look/style
3. Animations usually need minimal grading

### 5. Effects and Enhancements

Add additional effects from Effects Library:
- **Text overlays** for titles/captions
- **Zoom effects** to highlight details
- **Speed changes** for dramatic effect
- **Lower thirds** for information

## Advanced Techniques

### Compositing Multiple Animations

Layer animations for complex compositions:

1. Use **Video 1** for background animation
2. Add more tracks (Video 2, 3, etc.) for overlays
3. Adjust opacity and blend modes
4. Use **Fusion** page for advanced compositing

### Creating Smooth Transitions

Best transition types for Manim animations:

- **Cross Dissolve**: Smooth fade between scenes
- **Dip to Color**: Fade through white/black
- **Smooth Cut**: Intelligent cut detection
- **Wipe**: Directional transition

### Adding Motion Graphics

Enhance animations with:

1. **Titles** - Create text overlays
2. **Lower Thirds** - Add information bars
3. **Callouts** - Highlight specific elements
4. **Progress Bars** - Show video progress

### Timing and Pacing

- Watch for natural pause points in animations
- Allow viewers time to absorb information
- Use `J-K-L` keys for playback control
- Mark important points with `M` (markers)

## Exporting from DaVinci Resolve

### For YouTube/Web (Recommended)

1. Go to **Deliver** page
2. Select **YouTube** preset or custom:
   - **Format:** MP4
   - **Codec:** H.264
   - **Resolution:** 1920x1080
   - **Frame Rate:** 60 fps
   - **Quality:** Automatic (or 30-50 Mbps)
3. Click **Add to Render Queue**
4. Click **Render All**

### For High Quality Archive

Use these settings for maximum quality:

- **Format:** MP4 or QuickTime
- **Codec:** H.265 (HEVC) for smaller files
- **Bitrate:** 80-100 Mbps (VBR)
- **Audio:** AAC 320 kbps

### For Social Media

Different platforms have specific requirements:

**Instagram:**
- Resolution: 1080x1080 (square) or 1080x1920 (story)
- Frame Rate: 30 fps
- Duration: Max 60 seconds (feed), 15 seconds (story)

**Twitter:**
- Resolution: 1920x1080 or 1280x720
- Frame Rate: 30 or 60 fps
- File Size: Max 512 MB

**TikTok:**
- Resolution: 1080x1920 (vertical)
- Frame Rate: 30 fps
- Duration: 15-60 seconds

## Tips for Best Results

### 1. Planning
- Plan your video structure before importing
- Create a shot list or storyboard
- Know which animations connect thematically

### 2. Consistency
- Use consistent transitions between similar content
- Maintain timing patterns
- Apply uniform color grading

### 3. Audio
- Add background music for engagement
- Use sound effects at key moments
- Add voiceover to explain concepts
- Keep audio levels balanced

### 4. Performance
- Generate optimized media for smooth playback
- Use proxy mode for 4K content
- Close unnecessary applications
- Save project frequently

### 5. Review
- Watch full video before final export
- Check audio sync
- Verify all edits are intentional
- Get feedback from others

## Troubleshooting

### Issue: Choppy Playback

**Solutions:**
1. Generate **Optimized Media** (right-click clip)
2. Lower playback resolution (Timeline → Playback → Timeline Proxy Mode)
3. Enable **Smart Cache** in preferences

### Issue: Color Looks Different

**Solutions:**
1. Check Input Color Space is set to Rec.709
2. Verify Timeline Color Space matches
3. Calibrate monitor if possible

### Issue: Audio Sync Problems

**Solutions:**
1. Check Timeline Frame Rate matches media
2. Use **Auto Sync** feature if available
3. Manually adjust with ripple edit

### Issue: Export Takes Too Long

**Solutions:**
1. Use hardware acceleration (NVIDIA/AMD)
2. Lower export resolution for testing
3. Render in sections if needed
4. Close other applications

## Resources

- [DaVinci Resolve Training](https://www.blackmagicdesign.com/products/davinciresolve/training)
- [Official Documentation](https://documents.blackmagicdesign.com/)
- [YouTube Tutorials](https://www.youtube.com/results?search_query=davinci+resolve+tutorial)
- [Community Forums](https://forum.blackmagicdesign.com/)

## Example Workflow

Here's a complete workflow example:

1. **Render animations** using `./render_all.sh`
2. **Import** all MP4s to DaVinci Resolve
3. **Create timeline** at 1920x1080, 60fps
4. **Arrange clips** in logical order:
   - Intro: Goal Animation
   - Section 1: Environment + Formula
   - Section 2: Simulation + Code
   - Section 3: Error Handling + Testing
   - Outro: Custom title card
5. **Add transitions** (Cross Dissolve, 1 second)
6. **Import audio** (background music + voiceover)
7. **Add text** overlays for key points
8. **Color grade** (minimal, adjust if needed)
9. **Export** for YouTube at 1080p60
10. **Upload** with optimized metadata

## Next Steps

1. Practice with sample animations
2. Experiment with different effects
3. Learn keyboard shortcuts for efficiency
4. Explore Fusion page for advanced compositing
5. Study color grading techniques

---

**Happy Editing! 🎬**
