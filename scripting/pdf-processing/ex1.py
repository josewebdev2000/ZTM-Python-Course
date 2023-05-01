# Working with PDF files example
import PyPDF2
import os

PDF_DIR = "pdf_files"

def main() -> None:
    
    read_pdf()

def read_pdf() -> None:
    
    with open(os.path.join(PDF_DIR, "dummy.pdf"), "rb") as pdf_file:
        
        # Get file reader to read content from the file
        reader = PyPDF2.PdfFileReader(pdf_file)
    
        # Print number of pages
        print(f"Number of pages: {reader.getNumPages()}")
        
        # Get first page (The only page of this pdf)
        first_page = reader.getPage(0)
        
        # Rotate that page counter clockwise
        first_page = first_page.rotateCounterClockwise(90)
        
        # Create writer object to write rotated page to another file
        writer = PyPDF2.PdfFileWriter()
        
        # Remember to add rotated page to writer
        writer.addPage(first_page)
        
        # Write new PDF file that has the rotated page
        with open(os.path.join(PDF_DIR, "crooked_dummy.pdf"), "wb") as cpdf:
            writer.write(cpdf)      

if __name__ == "__main__":
    main()