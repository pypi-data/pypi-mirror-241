import socket


def get_ip_address():
    try:
        # 创建一个UDP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到公共域名
        sock.connect(("8.8.8.8", 80))
        # 获取本地IP地址
        ip_address = sock.getsockname()[0]
        if ip_address.startswith("127.") or ip_address.startswith("192.168"):
            return None
        return ip_address
    except socket.error:
        return None


if __name__ == '__main__':
    print(get_ip_address())
