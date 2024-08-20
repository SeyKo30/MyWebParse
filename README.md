# MyWebParse

MyWebParse is a Django web application for file upload, PDF conversion, and parsing. The application allows users to upload DOC and DOCX files, convert them to PDF format, and parse PDF content.

## Features

- **File Upload**: Upload DOC files for conversion.
- **PDF Conversion**: Convert uploaded DOC files to PDF format using an external API.
- **PDF Parsing**: Extract text content from PDF files.

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

git clone https://github.com/SeyKo30/MyWebParse.git
cd MyWebParse


### 2. Set Up a Virtual Environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables 
API_KEY=your_pdf_co_api_key 
Replace your_pdf_co_api_key with your actual API key on https://pdf.co 

### 5. Run Migrations
python manage.py migrate

### 6. Run the Development Server
python manage.py runserver 

Then visit http://127.0.0.1:8000 in your web browser to use the application




File Structure

mywebparse/: Main project directory
MyParser/: Contains PDF parsing and uploading functionality
MyParser/parsers/: Directory for parser functions
MyParser/views.py: Views for file handling and parsing
MyParser/urls.py: URL routing for MyParser


converter/: Directory for document conversion functionality
converter/views.py: Views for file conversion
converter/urls.py: URL routing for converter

templates/: HTML templates

static/: Static files (CSS, JavaScript)

CoreApplication:/ Directory for index page and news rss application




Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.


Contact
For any questions or issues, please contact smksergii@gmail.com.