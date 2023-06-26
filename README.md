# Primo JAG - Document Translation and Analysis Tool
Primo JAG is an interactive web-based application that leverages state-of-the-art natural language processing (NLP) technologies to translate and analyze different types of documents. Users can upload documents in image, PDF, or directly taken photos from a camera.

## Features
* Language Translation: Translates documents from English to either Spanish or English using Google's Translation API.

* Document Extraction: Extracts text from image files, camera photos, or PDF files using the Pytesseract and PyPDF2 libraries.

* Document Analysis: Analyzes the translated document and provides a summarized and easy-to-understand output using OpenAI's GPT-3.5-turbo model.

* User-friendly Interface: Provides an intuitive user interface using Streamlit where users can upload their documents, select their language, and see the translated and summarized content of their documents.

## Setup and Installation
You will need to have Python installed on your system. Once you have Python installed, you can clone this repository.

Copy code
```bash
git clone <repository-url>
```
Navigate to the directory of the project and install the necessary Python dependencies.
Copy code
```bash
cd <project-directory>
pip install -r requirements.txt
```
## Usage
To run the application, use the command:

```bash
Copy code
streamlit run <python-script-name.py>
```
This will start the web application and you can access it by navigating to localhost:8501 on your web browser.

## Troubleshooting
If you encounter any issues while running the application, please check the error logs for details on what went wrong. The error logs are configured to print error messages with timestamps. If you can't resolve the issue, feel free to open an issue on this repository or contact us at jag.solutionshub@gmail.com.

## Roadmap
Here is the future development plan for Tu Primo JAG:

- Chatbot Integration
We aim to add a chatbot feature that leverages Vector DB and Embeddings for interactive document communication.

- User Authentication
 we're planning to introduce user authentication to safeguard personal data and translations.

- Social Media Sharing


# Contributions
Your ideas are welcome! Feel free to contribute to the project or suggest any features you think would make Tu Primo JAG even better. We look forward to working with you to make Tu Primo JAG a robust document translation and analysis tool!
We welcome contributions to this project. If you have a feature request or bug report, please open an issue on this repository. If you wish to contribute code, please open a pull request. If it's a large change, please open an issue first to discuss your proposed changes.

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for the full license text.

## Contact
For any queries or suggestions, feel free to reach us at jag.solutionshub@gmail.com. We'd love to hear from you!