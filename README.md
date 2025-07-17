# Manim Learning Project

This repository contains my learning journey with the Manim library, following the [Manim Community Tutorial Playlist](https://youtube.com/playlist?list=PL3Q3QFVgazl1qr948EOpix__PrVxjg4RO&si=gtMFEuvxtvGGbyhE) by Yola Montalvan.

## 🎯 Project Overview

This project documents various Manim concepts and techniques through practical examples. Each scene demonstrates different aspects of mathematical animation creation.

## 📋 Prerequisites

- Python 3.8+
- Manim Community
- LaTeX (optional, for MathTex rendering)

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
# Install Manim Community
pip install manim

# Install LaTeX (optional, for mathematical expressions)
# Download and install MiKTeX from https://miktex.org/download
```

### 2. Code Formatting
This project uses Black for Python code formatting:
```bash
# Install Black
pip install black

# Format code
black .

# Check formatting
black --check .
```

## 🎬 Scenes Overview

### 1. **Pith** - Basic Shape Creation
- **File**: `ManimCourse.py` (lines 4-11)
- **Concept**: Creating and animating basic geometric shapes
- **Features**: 
  - Square with custom colors and opacity
  - Basic animation with `Create()`

### 2. **Testing** - Text and Shape Manipulation
- **File**: `ManimCourse.py` (lines 14-30)
- **Concept**: Working with text, shapes, and animations
- **Features**:
  - Text positioning with `to_edge()`
  - Multiple shape creation (Square, Triangle)
  - Complex animations with `animate`

### 3. **Errors** - Error Handling Example
- **File**: `ManimCourse.py` (lines 33-39)
- **Concept**: Understanding common Manim errors
- **Features**:
  - Basic Circle creation
  - Error demonstration and debugging

### 4. **Library** - Mathematical Objects
- **File**: `ManimCourse.py` (lines 42-47)
- **Concept**: Using Manim's mathematical object library
- **Features**:
  - Axes creation and animation

### 5. **Getters** - Dynamic Positioning
- **File**: `ManimCourse.py` (lines 50-65)
- **Concept**: Using getter methods for dynamic positioning
- **Features**:
  - `get_bottom()`, `get_top()` methods
  - `always_redraw()` for dynamic arrows
  - Real-time position updates

### 6. **Updaters** - Real-time Updates
- **File**: `ManimCourse.py` (lines 68-79)
- **Concept**: Using updaters for dynamic animations
- **Features**:
  - `always_redraw()` with lambda functions
  - Dynamic rectangle and text positioning
  - Real-time updates during animations

## 🎥 Rendering Commands

### Basic Rendering
```bash
# Render a specific scene
manim .\ManimCourse.py SceneName -pqm

# Examples:
manim .\ManimCourse.py Pith -pqm
manim .\ManimCourse.py Testing -pqm
manim .\ManimCourse.py Updaters -pqm
```

### Quality Options
- `-p`: Preview the video after rendering
- `-q`: Quality (l=low, m=medium, h=high, k=4k)
- `-m`: Medium quality (default)

### Other Useful Flags
```bash
# Render all scenes
manim .\ManimCourse.py -pqm

# Save last frame as image
manim .\ManimCourse.py SceneName -s

# Show progress
manim .\ManimCourse.py SceneName -pqm --progress_bar True
```

## 📁 Project Structure

```
Manim/
├── ManimCourse.py          # Main file with all scenes
├── pyproject.toml          # Black formatting configuration
├── .vscode/
│   └── settings.json       # VS Code settings for Black
├── media/                  # Generated output files
│   ├── images/
│   ├── texts/
│   └── videos/
└── venv/                   # Virtual environment
```

## 🔧 Development Setup

### VS Code/Cursor Configuration
The project includes `.vscode/settings.json` with:
- Black as the default Python formatter
- Format on save enabled
- Import organization on save

### Code Quality
- **Black**: Code formatting (line length: 88)
- **Type hints**: Python type checking enabled
- **Consistent style**: 4-space indentation, single quotes

## 📚 Learning Resources

- **Primary Tutorial**: [Manim Community Playlist](https://youtube.com/playlist?list=PL3Q3QFVgazl1qr948EOpix__PrVxjg4RO&si=gtMFEuvxtvGGbyhE)
- **Documentation**: [Manim Community Docs](https://docs.manim.community/)
- **Examples**: [Manim Examples](https://docs.manim.community/en/stable/examples.html)

## 🎨 Key Concepts Learned

1. **Basic Shapes**: Square, Circle, Triangle, Rectangle
2. **Text Objects**: Creating and positioning text
3. **Animations**: Create, Write, DrawBorderThenFill
4. **Positioning**: to_edge(), shift(), next_to()
5. **Dynamic Updates**: always_redraw(), getter methods
6. **Mathematical Objects**: Axes, MathTex (with LaTeX)
7. **Grouping**: VGroup for multiple objects

## 🐛 Common Issues & Solutions

### LaTeX Not Found Error
**Problem**: `FileNotFoundError: [WinError 2] The system cannot find the file specified`
**Solution**: Install MiKTeX or use `Text()` instead of `MathTex()`

### Import Errors
**Problem**: Module not found errors
**Solution**: Ensure you're in the virtual environment: `venv\Scripts\activate`

### Rendering Issues
**Problem**: Videos not generating
**Solution**: Check file paths and ensure all dependencies are installed

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome!

## 📄 License

This project is for educational purposes. Follow the original Manim Community license for the library itself.

---

**Happy Animating! 🎬✨** 