#from flask import Flask, render_template
import os
import uuid
import subprocess
import shutil
import tempfile
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
# Directory to store visualizations
VISUALIZATIONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualizations')
os.makedirs(VISUALIZATIONS_DIR, exist_ok=True)

@app.route('/api/visualize', methods=['POST'])
def visualize():
    try:
        # Get the code and language from the request
        data = request.json
        if not data or 'code' not in data or 'language' not in data:
            return jsonify({'error': 'Code and language are required'}), 400
        
        code = data['code']
        language = data['language']
        
        if language not in ['python', 'r']:
            return jsonify({'error': 'Language must be either "python" or "r"'}), 400
        
        # Generate a unique ID for this visualization
        viz_id = str(uuid.uuid4())
        output_dir = os.path.join(VISUALIZATIONS_DIR, viz_id)
        os.makedirs(output_dir, exist_ok=True)
        
        # Determine file type based on code content (basic detection)
        file_type = 'static'
        file_name = 'visualization.png'
        
        if language == 'python':
            if 'plotly' in code:
                file_type = 'interactive'
                file_name = 'visualization.html'
            elif 'matplotlib' in code:
                file_type = 'static'
                file_name = 'visualization.png'
        else:  # R
            if 'plotly' in code:
                file_type = 'interactive'
                file_name = 'visualization.html'
            elif 'rgl' in code:
                file_type = '3d'
                file_name = 'visualization.html'
        
        # Execute the visualization code
        result = generate_visualization(code, language, output_dir, file_name)
        
        if result['success']:
            return jsonify({
                'success': True,
                'vizId': viz_id,
                'visualizationUrl': f'/visualizations/{viz_id}/{file_name}',
                'type': file_type
            })
        else:
            return jsonify({'error': result['error']}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_visualization(code, language, output_dir, file_name):
    """Generate visualization by executing code in the specified language."""
    try:
        # Create temporary script file
        script_ext = '.py' if language == 'python' else '.R'
        script_path = os.path.join(output_dir, f'script{script_ext}')
        
        # Write code to script file
        with open(script_path, 'w') as script_file:
            script_file.write(code)
        
        # Execute the script based on language
        if language == 'python':
            # Add wrapper code for saving the visualization
            wrapper_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'python_wrapper.py')
            cmd = ['python', wrapper_path, script_path, output_dir, file_name]
        else:  # R
            wrapper_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r_wrapper.R')
            cmd = ['Rscript', wrapper_path, script_path, output_dir, file_name]
        
        # Execute the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check if visualization was created
        output_file_path = os.path.join(output_dir, file_name)
        if os.path.exists(output_file_path):
            return {'success': True}
        else:
            error_message = f"Execution output: {result.stdout}\nError: {result.stderr}"
            return {'success': False, 'error': error_message}
    
    except Exception as e:
        return {'success': False, 'error': str(e)}
    
@app.route('/visualizations/<viz_id>/<path:filename>')
def get_visualization(viz_id, filename):
    """Serve the visualization file."""
    return send_from_directory(os.path.join(VISUALIZATIONS_DIR, viz_id), filename)
  
if __name__ == "__main__":
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    app.run(debug=True,port=port)
