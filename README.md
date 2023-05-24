# LIdata_processing

## File Processing Application

This is a Python application built using the tkinter library to process text files within a selected folder. The application reads the text files, performs data cleaning operations, and saves the processed data to an Excel file.

## Prerequisites

- Python (3.x) - You can download Python from the official website: https://www.python.org/downloads/
- Required Libraries: pandas, tkinter

## Installation

1. Clone the repository or download the source code.

2. Open a terminal or command prompt and navigate to the project directory.

3. Set up a virtual environment (optional but recommended):
   - Create a virtual environment:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```
       venv\Scripts\activate
       ```
     - For macOS and Linux:
       ```
       source venv/bin/activate
       ```

4. Install the required libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Activate the virtual environment (if created):
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

3. Run the following command to start the application:
  ```
  python3 program.py
  ```

4. The application window will appear with two buttons and an entry field.

5. Click the "Select folder" button to choose a folder containing the text files you want to process.

6. The selected folder path will be displayed in the entry field.

7. Click the "Process data" button to start processing the files. The application will read the text files, concatenate them into a pandas DataFrame, perform data cleaning operations, and save the processed data to an Excel file named "output.xlsx" in the "../1_test/" directory.

8. The status label will display messages about the progress and completion of the processing.

9. After the processing is complete, a message box will appear displaying the path to the generated Excel file.


