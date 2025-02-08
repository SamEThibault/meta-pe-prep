"""
Reading from STDIN and receiving two parameters which was host and ports that I need to reach and print status,
what if this input is a file with 1tb?
"""

# Assuming input stream from a file looks like "IPv4 hostname, port"
import sys, socket
from concurrent.futures import ThreadPoolExecutor

def check_port(hostname, port):
    # with this setup, when we return (get out of with: context, the socket automatically closes)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.connect((hostname, int(port)))
            return f"{hostname}:{port} is OPEN" 
        except (socket.timeout, ConnectionRefusedError):
            return f"{hostname}:{port} is CLOSED"
        except Exception as e:
            return f"Error connecting to {hostname}:{port} -> {str(e)}"


def process_line(line):
    hostname, port = line.strip().split(", ")
    return check_port(hostname, port)




def main():
    # we can do a parallel approach
    """
    Notes:
    - This isn't technically true parallelism (where tasks are run simultaneously on multiple cores)
    - The GIL (global interpreter lock) permits only one thread to hold control over the python interpreter at a time
    - So none of this is really parallel... 
    - But this does allow us to do other stuff on different threads while another one is blocked by waiting for network I/O 
    - You can do multiprocessing in Python by creating multiple intepreters (that's true parallelism)
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(process_line, sys.stdin)
        for res in results:
            print(res)