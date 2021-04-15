# $language = "python"
# $interface = "1.0"

def main():
    crt.Screen.Send("e: \r")
    # time.sleep(1)
    crt.Screen.Send("cd E:\green\Redis-x64-3.2.100 \r")
    crt.Screen.Send("redis-server.exe redis.windows.conf \r")
    # os.system('e: \r')
    # os.system('cd E:\green\Redis-x64-3.2.100')
    # os.system('redis-server.exe redis.windows.conf')


main()
