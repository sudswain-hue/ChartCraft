#!/usr/bin/env python
import sys
import os
import traceback
import matplotlib

def run_script(script_path, output_dir, output_file):
    """
    Execute the user's Python script in a controlled environment
    and save the visualization to the specified output directory.
    """
    try:
        # Create a namespace for the script execution
        script_globals = {
            "__file__": script_path,
            "output_dir": output_dir,
            "output_file": output_file,
        }
        
        # Read the script content
        with open(script_path, 'r') as f:
            script_content = f.read()
        
        # Add code to save the visualization at the end
        if '.html' in output_file:
            # For interactive visualizations (Plotly, Bokeh, etc.)
            additional_code = f"""
# Save the visualization
import os
import sys
if 'fig' in locals() or 'fig' in globals():
    if 'plotly' in sys.modules:
        import plotly.io as pio
        pio.write_html(fig, os.path.join(output_dir, output_file))
    elif 'bokeh' in sys.modules:
        from bokeh.io import save
        save(fig, os.path.join(output_dir, output_file))
"""
        else:
            # For static visualizations (Matplotlib, Seaborn, etc.)
            additional_code = f"""
# Save the visualization
import os
import matplotlib.pyplot as plt
if 'plt' in locals() or 'plt' in globals():
    plt.savefig(os.path.join(output_dir, output_file), bbox_inches='tight')
    plt.close()
elif 'fig' in locals() or 'fig' in globals():
    try:
        fig.savefig(os.path.join(output_dir, output_file), bbox_inches='tight')
    except:
        pass
"""
        
        # Execute the script with additional save code
        exec(script_content + additional_code, script_globals)
        
        # Check if the output file was created
        output_path = os.path.join(output_dir, output_file)
        if os.path.exists(output_path):
            print(f"Visualization successfully saved to {output_path}")
            return True
        else:
            print(f"Warning: Output file {output_path} was not created")
            return False
    
    except Exception as e:
        print(f"Error executing script: {str(e)}")
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python_wrapper.py <script_path> <output_dir> <output_file>")
        sys.exit(1)
    
    script_path = sys.argv[1]
    output_dir = sys.argv[2]
    output_file = sys.argv[3]
    
    # Ensure we have matplotlib, plotly, and other libraries
    try:
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt # type: ignore
    except ImportError:
        print("Warning: matplotlib not available")
    
    try:

        import plotly
    except ImportError:
        print("Warning: plotly not available")
    
    try:
        import seaborn
    except ImportError:
        print("Warning: seaborn not available")
    
    # Run the script
    success = run_script(script_path, output_dir, output_file)
    sys.exit(0 if success else 1)