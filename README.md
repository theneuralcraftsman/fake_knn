# Custom KNN Flask Application

This project is a custom implementation of a K-Nearest Neighbors (KNN) algorithm wrapped in a Flask web application. The application allows users to interact with the KNN model via HTTP endpoints, making predictions based on the provided data.

## Setup Instructions

Follow the steps below to set up and run the application:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone [<repository-url>](https://github.com/theneuralcraftsman/fake_knn.git)
cd [<repository-directory>](https://github.com/theneuralcraftsman/fake_knn.git)
```

### 2. Create a Virtual Environment

To manage dependencies, create a virtual environment:

```bash
pip install virtualenv
virtualenv env
```

### 3. Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

- **Windows:**
  ```bash
  env\Scripts\activate
  ```
  
  - **MacOS/Linux:**
  ```bash
  source env/bin/activate
  ```

  ### 4. Install Dependencies

Install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install Dependencies

Install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
### 5. Run the Flask Application

Start the Flask application by running the following command:

```bash
python app.py
```
