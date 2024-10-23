from docx import Document
from PIL import Image
from io import BytesIO
import os


def extract_from_word(file_path):
    # Load the Word document
    doc = Document(file_path)

    # Create a folder to save images (if needed)
    image_folder = "extracted_images"
    os.makedirs(image_folder, exist_ok=True)

    # Extract content
    content = {
        "paragraphs": [],
        "tables": [],
        "images": []
    }

    # Iterate through each element in the document
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Paragraph
            paragraph = element.text.strip()
            if paragraph:
                content["paragraphs"].append(paragraph)

        elif element.tag.endswith('tbl'):  # Table
            table_data = []
            table = doc.tables[len(content["tables"])]
            for row in table.rows:
                row_data = [cell.text.strip() for cell in row.cells]
                table_data.append(row_data)
            content["tables"].append(table_data)

    # Extract images from the document
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image = rel.target_part.blob
            image_path = os.path.join(image_folder, f"image_{len(content['images']) + 1}.png")
            content["images"].append(image_path)

            # Save the image using Pillow
            with open(image_path, "wb") as img_file:
                img_file.write(image)

    return content


# Example usage
file_path = "example.docx"  # Replace with your file path
extracted_content = extract_from_word(file_path)

# Display results
print("Paragraphs:")
for para in extracted_content["paragraphs"]:
    print(para)

print("\nTables:")
for table in extracted_content["tables"]:
    for row in table:
        print(row)

print("\nImages saved at:")
for img_path in extracted_content["images"]:
    print(img_path)
