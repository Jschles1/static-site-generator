# Markdown to HTML Conversion Project

## Overview
This project provides a Python-based solution for converting Markdown files into HTML pages. It includes functionality to recursively process directories containing Markdown files, apply HTML templates, and serve the generated content over a simple HTTP server.

## Features
- **Markdown Parsing**: Converts Markdown syntax into HTML elements.
- **Template Application**: Integrates generated HTML content into predefined HTML templates.
- **Recursive Directory Handling**: Processes entire directories of Markdown files.
- **Static File Management**: Copies static assets to the output directory.
- **Local HTTP Server**: Serves the generated HTML files over a local server for preview.

## Project Structure
- `src/`: Contains all Python source files.
  - `main.py`: Entry point that orchestrates the file generation and server launch.
  - `gencontent.py`: Handles the conversion of Markdown to HTML and directory processing.
  - `markdown_blocks.py`: Parses Markdown blocks into HTML nodes.
  - `inline_markdown.py`: Handles inline Markdown formatting.
  - `htmlnode.py`: Defines HTML node classes for building HTML documents.
  - `copystatic.py`: Manages copying of static files.
- `template.html`: HTML template used for generating pages.
- `server.py`: Simple HTTP server for serving generated content.
- `public/`: Default output directory for generated HTML files and static content.

## Usage
1. **Prepare Markdown Files**: Place your Markdown files in the `./content` directory.
2. **Run the Main Script**: Execute the main script to generate HTML files and copy static content.

```shell
python src/main.py
```

3. **Start the Server**: Serve the generated content locally.

```shell
python server.py --dir public
```


## Dependencies
- Python 3.6 or higher
- No external Python packages are required.

## Development
- **Testing**: Unit tests are provided for various modules.
  - Run tests using:

  
```shell
python -m unittest discover
```


## Contributing
Contributions to this project are welcome. Please ensure that any pull requests maintain the existing coding style and include appropriate tests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.