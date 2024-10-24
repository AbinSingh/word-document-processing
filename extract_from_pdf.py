import pdfplumber


def extract_pdf_content(pdf_path):
    # Store all content in a list to preserve order
    extracted_content = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # Extract text from the page
            text = page.extract_text()
            if text:
                extracted_content.append(f"Page {page_num + 1} - Text Section:\n\n{text}\n\n")

            # Extract tables from the page, if any
            tables = page.extract_tables()
            for table_num, table in enumerate(tables):
                if table:
                    table_content = f"Page {page_num + 1} - Table {table_num + 1}:\n"
                    # Format the table content
                    for row in table:
                        table_content += " | ".join(str(cell) if cell else '' for cell in row) + "\n"
                    extracted_content.append(table_content + "\n\n")

    # Join all extracted content to a single output
    full_content = "\n".join(extracted_content)

    return full_content


# Replace filename with the path
pdf_path = "policy_wording.pdf"
extracted_content = extract_pdf_content(pdf_path)

# Save the extracted content to a text file if needed
with open('extracted_content.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_content)

# Output the result
print(extracted_content)
