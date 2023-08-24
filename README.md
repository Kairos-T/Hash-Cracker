# Hash Cracker

Python script that attempts to crack password hashes using various hash algorithms and a dictionary of possible passwords. It supports bcrypt, SHA-256, and MD5 hash algorithms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Features

- Supports cracking bcrypt, SHA-256, and MD5 hash algorithms.
- Utilises a dictionary file containing possible passwords.
- Multithreaded processing for faster hash cracking.

## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/Kairos-T/Hash-Cracker
   ```

2. Navigate to the project directory:
    ```
    cd Hash-Cracker

    ```

3. Install the required dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the script by executing:

``` bash
python hashcracker.py
```

2. Follow the prompts to provide the hash to crack, the path to the dictionary file, and the hash algorithm.

3. The script will attempt to crack the hash using the provided dictionary and algorithm.

4. If a match is found, the script will display the cracked password.

## Contributing
Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.
