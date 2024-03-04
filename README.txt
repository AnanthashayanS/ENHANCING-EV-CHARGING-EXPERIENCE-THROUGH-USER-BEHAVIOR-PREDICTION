1.py -m venv venv 
- This command creates a virtual environment named 'venv' in the current directory. Virtual environments are used to isolate project-specific dependencies from the global Python environment.

2.\Scripts\activate.bat 
- This command activates the virtual environment. Once activated, any Python packages installed will be placed in this isolated environment.

3.pip install -r requirements.txt 
- This command installs the Python packages listed in the 'requirements.txt' file. These are the dependencies required for the project to run.

4.streamlit run app.py 
- This command runs the 'app.py' file using Streamlit. Streamlit is a framework used for creating machine learning and data science web applications.
