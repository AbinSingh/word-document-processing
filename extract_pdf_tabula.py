import tabula

pdf_path = "policy_wording.pdf"
# Extract tables from PDF
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

for table in tables:
    print(table)
