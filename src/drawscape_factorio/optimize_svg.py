import os
import subprocess

# This function uses the vpype library to optimize the SVG for drawing on a pen plotter.
# vpype is a powerful tool for processing vector graphics, particularly for pen plotting.
# The optimization process includes:
#   - reloop: optimizes the drawing order of paths
#   - linemerge: combines consecutive lines and curves
#   - linesort: sorts lines to minimize pen travel
#   - linesimplify: simplifies paths by removing unnecessary points
# These operations help to reduce drawing time and improve the quality of the plot.

def optimize_svg(input_svg_path):
    print(f"Optimizing SVG file: {input_svg_path}")

    # Generate output file path
    output_dir = os.path.dirname(input_svg_path)
    output_filename = os.path.splitext(os.path.basename(input_svg_path))[0] + "_optimized.svg"
    output_path = os.path.join(output_dir, output_filename)

    # Construct the vpype command
    vpype_command = [
        "vpype",
        "read",
        input_svg_path,
        "reloop",
        "linemerge",
        "linesort",
        "linesimplify",
        "write",
        output_path
    ]

    print(vpype_command)

    # Execute the vpype command
    try:
        subprocess.run(vpype_command, check=True, capture_output=True, text=True)
        print(f"Optimized SVG saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error optimizing SVG: {e}")
        print(f"Command output: {e.output}")
        return None

    return output_path