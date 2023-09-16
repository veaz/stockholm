# Stockholm v0.1 

### Created during a cybersecurity bootcamp at 42 Barcelona by vaguilar

Stockholm is a cybersecurity tool designed for educational purposes. It simulates the behavior of ransomware by targeting specific file extensions, similar to the infamous Wannacry ransomware.

> **Disclaimer**: This tool is intended for educational and research purposes only. Do not use it for malicious intent or on any system without explicit permission.

## Features:

- Targets the "infection" folder and its subfolders in the user's root directory.
- Searches for and "infects" files with specific extensions.
- Generates a "key.key" file to store the decryption key. If this file already exists, the program will utilize the existing key.

## Usage:

1. **Encryption**: 
   ```bash
   python stockholm.py
    ```

2. **Decryption with a specified key**:
    ```bash
   python stockholm.py -r KEY
    ```

3. **Decryption using the key in "key.key"**:
    ```bash
   python stockholm.py -rk
    ```

## Flags:
- -h : Display help message.
- -k : Generate a new key.
- -r : Decrypt all encrypted files.
- -rk : Decrypt files using the key stored in "key.key".
- -s : Run the program silently (no output).
- -v : Display program version.