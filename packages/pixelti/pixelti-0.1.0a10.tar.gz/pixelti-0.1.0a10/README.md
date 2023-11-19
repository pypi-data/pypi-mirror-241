# Pixelti - Transform Your Pictures into Pixel Art

Pixelti is a Python program designed to effortlessly convert any image into captivating pixel art. Follow these simple steps to get started with Pixelti on your local machine.

## Prerequisites

Ensure that you have the following installed on your system:
- [Python 3.6 or later](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [make](https://www.gnu.org/software/make/)

## Setup

1. Clone the Pixelti repository to your local machine.

    ```bash
    git clone https://github.com/your-username/pixelti.git
    ```

2. Navigate to the project directory.

    ```bash
    cd pixelti
    ```

3. Run the following command to initialize the required environment.

    ```bash
    make init
    ```

## Installation

After initialization, install Pixelti dependencies with:

```bash
make install
```

With this, your Pixelti environment is set up and ready to go.

## Usage

Explore Pixelti's capabilities by running the program. Utilize the python --help command to view available options.

Example Usage:

```bash
python cli.py http://image-url.dev/sampleimage.jpg --pixelsize 10 --save --filename cool-pixelart.jpg
```

Adjust the parameters according to your preferences
- `--pixelsize` This parameter determines how many original pixels will be combined into one pixel in the resulting pixel ar
- `--save` Save pixel art into a file
- `--filename` Define output file name, default: random string

## Contribution

If you wish to contribute to Pixelti, please fork the repository, make your changes, and submit a pull request. Your contributions are highly appreciated!
