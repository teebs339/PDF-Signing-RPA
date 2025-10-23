# PDF-Signing-RPA

 UiPath RPA to sign PDF invoices with signature PNG

PDF-Signing-RPA is an automation project built with UiPath to digitally sign PDF invoices using a PNG signature image. It streamlines the process of getting unread invoice & signature emails from Outlook Desktop (Classic), applying signatures to multiple invoices, saving time and reducing manual effort.

## Features

- Reads all the unread emails from Outlook Desktop (Classic)
- Filters out emails based on if both the invoice & signature email arrived
- Saves attachment from both emails. (Invoice PDF file & Singature PNG)
- Uses Python to apply the digital signature to PDF invoices
- Finally, uploads the signed invoice PDF to Sharepoint using UiPath built in outlook activities

## Technologies Used

- UiPath Studio
- Python (for signature handling)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/teebs339/PDF-Signing-RPA.git
   cd PDF-Signing-RPA
   
2. Install Python 3.11 or higher
   
   ```bash
   pip install:
   - PyPDF2
   - reportlab
   
4. Make sure Outlook Desktop is signed in & open during the RPA run.
5. Make sure Sharepoint is connected (Comment out/disable the sharepoint sequence if not needed)
   
