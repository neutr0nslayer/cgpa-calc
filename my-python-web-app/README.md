# My Python Web App

This is a simple web application built using Flask that calculates and displays the updated CGPA based on user inputs.

## Project Structure

```
my-python-web-app
├── app.py
├── templates
│   └── index.html
├── static
│   └── style.css
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-python-web-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Features

- Input current CGPA, total credits, course credits, old grade point, and new grade point.
- Calculate and display the updated CGPA.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.