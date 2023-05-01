import PyPDF2
import os

PDF_DIR = "pdf_files"

def main() -> None:
    
    sf = open(os.path.join(PDF_DIR, "super_pdf.pdf"), "rb")
    watermark = open(os.path.join(PDF_DIR, "wtr.pdf"), "rb")
    
    reader_sf = PyPDF2.PdfFileReader(sf)
    reader_wm = PyPDF2.PdfFileReader(watermark)
    
    writer = PyPDF2.PdfFileWriter()
    
    for i in range(reader_sf.getNumPages()):
        page = reader_sf.getPage(i)
        page.mergePage(reader_wm.getPage(0))
        writer.addPage(page)
        
        with open(os.path.join(PDF_DIR,"watermarked_super_pdf.pdf"), "wb") as wspdf:
            writer.write(wspdf)
    
    sf.close()
    watermark.close()

if __name__ == "__main__":
    main()