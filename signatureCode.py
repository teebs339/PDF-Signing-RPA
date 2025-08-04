from PyPDF2 import PdfWriter, PdfReader
import io
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def main():
    # Get arguments (now 7 parameters with client name)
    if len(sys.argv) != 7:
        print("Usage: python signatureCode.py <input_pdf> <output_pdf> <signature_path> <client_name> <email_date_left> <email_date_right>")
        sys.exit(1)

    pdfPath = sys.argv[1]
    resultPath = sys.argv[2]
    signaturePath = sys.argv[3]
    clientName = sys.argv[4]
    emailDateLeft = sys.argv[5]
    emailDateRight = sys.argv[6]

    # Create overlay PDF
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 8)

    # Add all elements
    # Client name at original position
    can.drawString(120, 100, clientName)
    can.drawString(120, 80, emailDateLeft)     # Left date position
    can.drawString(450, 80, emailDateRight)    # Right date position
    can.drawImage(signaturePath, 415, 95, width=150, height=40, mask='auto')
    can.save()

    # Move to beginning of buffer
    packet.seek(0)

    # Create new PDF with Reportlab
    new_pdf = PdfReader(packet)

    # Read existing PDF
    existing_pdf = PdfReader(pdfPath)
    output = PdfWriter()

    # Add watermark only to last page
    total_pages = len(existing_pdf.pages)
    for i in range(total_pages):
        page = existing_pdf.pages[i]
        if i == (total_pages - 1):
            page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    # Write output file
    with open(resultPath, "wb") as outputStream:
        output.write(outputStream)


if __name__ == "__main__":
    main()
