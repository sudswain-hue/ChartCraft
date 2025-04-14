# ChartCraft: Language Agnostic Visualization Web Application

## Overview

ChartCraft is a web application that allows users to generate and view data visualizations by submitting custom scripts written in Python or R. The application executes these scripts on the backend and renders the resulting visualizations in the frontend.

## Features

- Support for both Python and R scripting languages
- Generation of multiple types of visualizations:
  - Static visualizations
  - Interactive visualizations
  - 3D visualizations
- Built-in script templates for common visualization types
- Real-time visualization rendering in the web interface

## Technology Stack

### Frontend
- React.js
- Bootstrap for styling

### Backend
- Flask (Python)
- Support for executing Python and R scripts in isolated environments

### Visualization Libraries Supported
- **Python**: Matplotlib, Plotly, seaborn
- **R**: ggplot2, plotly, rgl, htmlwidgets

## Installation and Setup

### Prerequisites
- Node.js and npm for the frontend
- Python 3.10+ for the backend (Development version: 3.12.6)
- R for R-language support (Development version: 4.4.1)
- Pandoc (for interactive R visualizations) 

### Backend Setup

1. Clone the repository
   ```
   git clone https://github.com/sudswain-hue/ChartCraft.git
   cd ChartCraft/backend
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies
   ```
   pip install -r Requirements/pthon_requirements.txt
   ```

4. Install R packages (if using R support)
   ```
   # Launch R and run Requirements/r_requirements.R
   ```

5. Install Pandoc (required for interactive R visualizations)
   - Windows: Download and install from [pandoc.org](https://pandoc.org/installing.html)
   - MacOS: `brew install pandoc`
   - Linux: `sudo apt-get install pandoc`

6. Start the Flask server
   ```
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory
   ```
   cd ../frontend
   ```

2. Install dependencies
   ```
   npm install
   ```

3. Start the development server
   ```
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Select the scripting language (Python or R) from the dropdown menu
2. Write or paste your visualization code in the text area
3. Click "Generate Visualization" to render the chart
4. The generated visualization will appear in a modal window
5. You can use the provided sample templates as starting points
6. You can view the genrated visualization in a different window
7. You can download the code used for the visualization
8. Switching between dark/light mode is available

## Troubleshooting

### Common Issues:

1. **"Error connecting to the server"**
   - Ensure the backend Flask server is running
   - Check that the frontend is correctly configured to connect to the backend URL

2. **R visualization errors**
   - Make sure Pandoc is installed if using interactive R visualizations
   - Check that required R packages are installed

3. **Python visualization errors**
   - Ensure all required Python packages are installed
   - Check your Python code for syntax errors

## Project Structure

```
chartcraft/
├── backend/
│   ├── Requirements/                    # Python & R Package requirements
│   │   ├── python_requirements.txt
│   │   └── r_requirements.R
│   ├── app.py                           # Flask application
│   ├── .env                             
│   ├── python_wrapper.py                # Python execution wrapper
│   ├── r_wrapper.R                      # R execution wrapper
│   └── visualizations/                  # Generated visualizations directory
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js                       # Main React component
│   │   ├── App.css                      # Styles
│   │   └── ...
│   ├── package.json
│   └── ...
└── README.md
```

## Development Notes

This project was developed to demonstrate the integration of multiple programming language environments in a web application. It shows how to:

1. Execute code in isolated environments securely
2. Handle different visualization types and formats
3. Create a user-friendly interface for code submission and visualization
4. Integrate Python and R graphics libraries in a web context

## Future Improvements

- Support for more visualization libraries and languages
- User authentication and saved visualizations
- Data upload functionality for visualization
- Export options for generated visualizations
- Code syntax highlighting and autocompletion

## Acknowledgements

- This project was created as part of a programming assessment
- Libraries used: Flask, React, Matplotlib,Pandas, Numpy, Seaborn, Plotly, ggplot2, rgl and more