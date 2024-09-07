from setuptools import setup, find_packages

setup(
    name="textimate",
    version="0.1",
    description="A Python library for automating tasks like text extraction, speech recognition, and language translation.",
    author="Madhu Mohan Reddy Y",
    packages=find_packages(),  # Finds the textimate folder and treats it as a package
    install_requires=[
        "pytesseract",
        "Pillow",
        "SpeechRecognition",
        "googletrans==4.0.0-rc1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
