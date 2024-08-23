import os
import subprocess

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