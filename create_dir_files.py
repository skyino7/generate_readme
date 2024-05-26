#!/usr/bin/env python3
"""
Create Directory with Files
"""

import os
import openai

# OpenAI API key from the system environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_sample_content(extension):
    """
    Generate sample content based on the file extension using ChatGPT.
    """
    # Define prompts for different file types
    prompts = {
        "txt": "Generate boilerplate for text content for a text file.",
        "py": "Generate boilerplate for Python code.",
        "md": "Generate boilerplate for content for a Markdown file.",
        "json": "Generate boilerplate for JSON data.",
        "html": "Generate boilerplate for HTML content.",
        "css": "Generate boilerplate for CSS styles.",
        "js": "Generate boilerplate for JavaScript code.",
        "c": "Generate boilerplate for C code.",
        "cpp": "Generate boilerplate for C++ code.",
        "java": "Generate boilerplate for Java code.",
        "php": "Generate boilerplate for PHP code.",
        "sql": "Generate boilerplate for SQL code.",
        "sh": "Generate boilerplate for shell script content.",
        "bat": "Generate boilerplate for batch script content.",
        "ps1": "Generate boilerplate for PowerShell script content.",
        "rb": "Generate boilerplate for Ruby code.",
        "jsx": "Generate boilerplate for JSX code.",
        "tsx": "Generate boilerplate for TypeScript code.",
        # Add more prompts for other file types as needed
    }

    # Select prompt based on file extension
    prompt = prompts.get(extension.lower(),
                         "Generate sample content for a file.")

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return res.choices[0].message['content'].strip()


def create_directory_and_files(directory_name, file_names):
    """
    Creates a directory and files inside it with sample
    content based on the file extension using ChatGPT.
    """
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)

    # Create files inside the directory
    for file_name in file_names:
        file_path = os.path.join(directory_name, file_name)
        # Extract file extension
        _, extension = os.path.splitext(file_name)
        # Generate sample content based on file extension
        sample_content = generate_sample_content(extension[1:])
        with open(file_path, 'w') as file:
            # Write sample content to the file using Chatgpt
            file.write(sample_content)
    print()
    # Print a message indicating successful creation of directory and files
    print(f"Directory '{directory_name}' and {file_names}
          created successfully!")

    # Display the directory structure after creating the directory and files
    print("Directory Structure:")
    for root, dirs, files in os.walk(directory_name):
        level = root.replace(directory_name, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        inFiles = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{inFiles}{f}")


if __name__ == "__main__":
    directory_name = input("Enter the directory name: ")
    file_names = input("Enter the file names separated by space: ").split()

    create_directory_and_files(directory_name, file_names)
