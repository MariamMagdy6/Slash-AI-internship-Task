# Image Component Analyzer

A Streamlit app that lets users upload an image and see a list of detected components.

## Features

- **Image Upload:** Supports JPEG and PNG formats.
- **Analyze Image:** Detects and lists components in the uploaded image.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/image-component-analyzer.git
    cd image-component-analyzer
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    streamlit run image_analyzer.py
    ```

2. **Open your browser and go to:**

    ```
    http://localhost:8501
    ```

3. **Upload an image and click "Analyze Image" to see the detected components.**

## Dependencies

- streamlit
- tensorflow
- Pillow

To install dependencies, run:

```bash
pip install -r requirements.txt
License
This project is licensed under the MIT License.

perl
Copy code

### Additional Files:

1. **`requirements.txt`**:

    ```plaintext
    streamlit
    tensorflow
    Pillow
    ```

2. **`.gitignore`**:

    ```plaintext
    venv/
    __pycache__/
    .DS_Store
    ```

This streamlined `README.md` provides essential information for setting up and running your projec
