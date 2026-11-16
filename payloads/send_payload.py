import argparse
import socket
import sys


def send_payload(ip, port, filepath):
    with open(filepath, "rb") as payload_file:
        payload = payload_file.read()

    response = []
    with socket.create_connection((ip, port)) as sock:
        sock.sendall(payload)
        sock.shutdown(socket.SHUT_WR)

        while True:
            try:
                chunk = sock.recv(4096)
            except ConnectionResetError:
                break

            if not chunk:
                break

            response.append(chunk)

    sys.stdout.write(b"".join(response).decode("utf-8", errors="replace"))


def main():
    parser = argparse.ArgumentParser(description="Send a Python payload to Yarpe")
    parser.add_argument("ip", help="Console IP address")
    parser.add_argument("port", type=int, help="Yarpe listener port")
    parser.add_argument("payload", help="Path to the Python payload")
    args = parser.parse_args()

    try:
        send_payload(args.ip, args.port, args.payload)
    except OSError as exc:
        print("send_payload: %s" % exc, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
