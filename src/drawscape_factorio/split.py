import xml.etree.ElementTree as ET
import os

def split_svg(input_file):
    # Parse the SVG file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # A4 dimensions in mm
    a4_width = 210
    a4_height = 297

    # Get the viewBox attribute
    viewBox = root.attrib.get('viewBox', '0 0 100 100').split()
    orig_width = float(viewBox[2])
    orig_height = float(viewBox[3])

    # Print original viewBox values
    print(f"Original viewBox: {viewBox}")
    print(f"Original width: {orig_width}")
    print(f"Original height: {orig_height}")

    # Calculate scaling factor to fit within A4
    scale = min(a4_width / orig_width, a4_height / orig_height)

    # Calculate new dimensions
    new_width = orig_width * scale
    new_height = orig_height * scale

    # Print calculated values
    print(f"Scaling factor: {scale}")
    print(f"New width: {new_width}")
    print(f"New height: {new_height}")

    # Create the new SVG file (entire content centered)
    new_root = ET.Element('svg', root.attrib)
    new_root.attrib.update({
        'width': f'{a4_width}mm',
        'height': f'{a4_height}mm',
        'viewBox': f'{(a4_width - new_width) / 2} {(a4_height - new_height) / 2} {new_width} {new_height}'
    })

    # Print new viewBox
    print(f"New viewBox: {new_root.attrib['viewBox']}")

    # Copy all elements from the original SVG
    for child in root:
        new_root.append(ET.fromstring(ET.tostring(child)))

    # Write the new SVG file
    new_tree = ET.ElementTree(new_root)
    output_file = "centered_output.svg"
    output_path = os.path.join(os.path.dirname(input_file), output_file)
    new_tree.write(output_path, encoding="utf-8", xml_declaration=True)

    print(f"Created centered SVG file: {output_file}")
