# auto-johnssh2

Great idea! Having an English README.md is essential for visibility and clarity on GitHub.

Here is the full content for your README.md file, including the necessary license disclaimers and a clear usage guide.

README.md

SSH Key Hash Converter (auto_hash.py)

This Python utility automates the crucial first step in cracking an encrypted SSH private key's passphrase. It converts a raw, encrypted key file (like id_rsa or hash.txt) into the compact hash format required by tools like Hashcat and John the Ripper (JtR).

Requirements

    Python 3

    The ssh2john.py script: This script is part of the John the Ripper (Jumbo) suite. You must have this script downloaded and available on your system, as this utility relies on it.

License & Source Disclaimer

Important: The utility relies on the script ssh2john.py, which is a third-party tool that is part of the John the Ripper project. ssh2john.py is distributed under the GNU General Public License (GPL).

    Original Source for ssh2john.py: Openwall John the Ripper GitHub

Usage Guide

Step 1: Preparation

Make sure you have all three files ready:

    auto_hash.py (this conversion script).

    The original, encrypted SSH key file (e.g., hash.txt).

    The ssh2john.py script (ensure you know its full path).

Step 2: Run the Converter

Execute the auto_hash.py script using Python 3:
Bash

python3 auto_hash.py

Step 3: Provide File Paths

The script will ask you for three pieces of information:

    Enter the FULL path to the ssh2john.py script:

        Example: /usr/share/john/ssh2john.py

    Enter the FULL path to the UNCONVERTED SSH key:

        Example: /home/jodio/hash.txt

    Enter a name for the output HASH file:

        (Press Enter to use the default: ssh_hash_out.txt)

Step 4: Cracking the Passphrase

Upon successful conversion, a new file (ssh_hash_out.txt) will appear in the current directory, containing the hash ready for brute-forcing.

🔑 Using with Hashcat

Use Mode -m 22000 (SSH Private Key):
Bash

hashcat -m 22000 -a 0 ssh_hash_out.txt /path/to/wordlist/rockyou.txt

🔑 Using with John the Ripper (JtR)

JtR will automatically recognize the format:
Bash

john --wordlist=/path/to/wordlist/rockyou.txt ssh_hash_out.txt

Post-Crack: Key Decryption

Once the passphrase is found (e.g., mysecretpass), you must decrypt the key so the SSH client can use it without prompting for a password every time.
Bash

ssh-keygen -p -f /path/to/original/key/hash.txt
# Enter old passphrase: [Type your found passphrase]
# Enter new passphrase (empty for no passphrase): [Press Enter]
# Enter same passphrase again: [Press Enter]

# Set mandatory file permissions
chmod 600 /path/to/original/key/hash.txt

You can now use the key to connect via SSH: ssh -i /path/to/original/key/hash.txt user@target_ip.
