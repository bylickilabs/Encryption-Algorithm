# Encryption and Decryption Using Bylickilabs Algorithm

This Python program demonstrates a simple encryption and decryption algorithm using the Bylickilabs Algorithm. The algorithm utilizes a pair of public and private keys to encode and decode messages.

## Usage

### Prerequisites

Before running the program, make sure you have Python installed on your system.

### Running the Program

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the program is located.
4. Run the program using the following command:

```bash
python main.py
```

### Modes

The program has two modes:

- `Encryption`: In this mode, you can enter a text to be encrypted. The program will generate an encrytion key pair and display the public and private keys. It will then encrypt the input text and display the ciphertext.
- `Decryption`: In this mode, you can enter a list of cipertext values and the private key. The program will decrypt the ciphertext and display the original text.

## Code Structure

The code is organized as follows:

- `in_prime(n)`: Function to check if a number is prime.
- `creation_keys()`: Function to generate the public and private keys.
- `encoding(text, open_key)`: Function to encrypt a text using the public key.
- `decoding(cipher_list, close_key)`: Functtion to decrypt a list of ciphertext values using the private key.
- `encoding_mode(lang)`: Function for the encryption mode.
- `decoding_mode(lang)`: Function for the decryption mode.
- `main()`: Main function to run the program.

## Example Usage

```plaintext
[x] Bylickilabs Encrypt Algorithm. [x]
 • 0. English.
 • 1. German.
 • 2. Russian.
 • 3. French.
 • 4. Spanish.
 • 5. Hindi.
[?] Language - 1
[x] German. [x]
 • 0. Verschlüsselung.
 • 1. Entschlüsselung.
[?] Was möchten Sie tun?  0

 --> Verschlüsselung <-- (~˘▾˘)~
[+] Text Eingabe - Hello, world!
[~] Offen - [5,333859].
[~] Geschlossene - [66541,333859].

 --> Ausgabe <--
[204727, 219181, 146178, 146178, 50103, 323737, 168532, 296856, 50103, 163435, 146178, 255232, 73890]
```

## Disclaimer

This is a simple encryption algorithm and should not be used for sensitive or critical data. It is provided for educational purposes only.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
