import PyPDF2
import sys
import os

PDF_DIR = "pdf_files"

def main() -> None:
    
    clargs = sys.argv[1:]
    pdf_combine(clargs)

def pdf_combine(pdf_list):
    
    merger = PyPDF2.PdfFileMerger()
    
    # Merge all pages to the merger object
    for pdf in pdf_list:
        merger.append(pdf)
        
    # Create super PDF file with all pages of previous PDFs
    merger.write(os.path.join(PDF_DIR, "super_pdf.pdf"))    
    
    

if __name__ == "__main__":
    main()