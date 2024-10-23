from docx import Document
from PIL import Image
import os


def extract_from_word_with_positions(file_path):
    # Load the Word document
    doc = Document(file_path)

    # Create a folder to save images (if needed)
    image_folder = "extracted_images_v2"
    os.makedirs(image_folder, exist_ok=True)

    # Store all elements with their positions
    content_with_positions = []

    # Initialize the position counter
    position_counter = 1

    # Iterate through each element in the document
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Paragraph
            paragraph_text = element.text.strip()
            if paragraph_text:
                content_with_positions.append({
                    "type": "paragraph",
                    "position": position_counter,
                    "content": paragraph_text
                })
                position_counter += 1

        elif element.tag.endswith('tbl'):  # Table
            table_data = []
            table = doc.tables[
                len(content_with_positions) - sum(1 for c in content_with_positions if c['type'] == 'paragraph')]

            for row in table.rows:
                row_data = [cell.text.strip() for cell in row.cells]
                table_data.append(row_data)

            content_with_positions.append({
                "type": "table",
                "position": position_counter,
                "content": table_data
            })
            position_counter += 1

    # Extract images from the document
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image = rel.target_part.blob
            image_path = os.path.join(image_folder, f"image_{len(content_with_positions) + 1}.png")

            # Save the image using Pillow
            with open(image_path, "wb") as img_file:
                img_file.write(image)

            # Add image info to the content list
            content_with_positions.append({
                "type": "image",
                "position": position_counter,
                "content": image_path
            })
            position_counter += 1

    return content_with_positions


# Example usage
file_path = "example.docx"  # Replace with your file path
extracted_content = extract_from_word_with_positions(file_path)

# Display results with positions
for content in extracted_content:
    if content["type"] == "paragraph":
        print(f"Position {content['position']} - Paragraph: {content['content']}")
    elif content["type"] == "table":
        print(f"Position {content['position']} - Table:")
        for row in content['content']:
            print(row)
    elif content["type"] == "image":
        print(f"Position {content['position']} - Image saved at: {content['content']}")
