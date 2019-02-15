
import socket                   # Import socket module
import os
from contextlib import redirect_stdout

def processrequest(request):
    req = request.decode("utf-8")

    info = req.split(" ")
    req_resource = ""
    req_type = info[0]
    if len(info)>1:
        req_resource = info[1]

    print(req_resource)

    return req_resource


def sendfile(filepath,conn):

    img_type = ["ico","jpg","png","gif"]
    vid_type = ["mp4"]

    l = b"""HTTP/1.1 200 OK"""
    filename = filepath.split("/")
    if filename == []:
        filepath += "index.html"
        l+=b"""\nContent-Type: text/html\n\n"""
    else:
        file_ext = filename[-1].split(".")
        if len(file_ext)==1:
            filepath += "index.html"
            l += b"""\nContent-Type: text/html\n\n"""
        else:
            if file_ext[1] == "css":
                l+=b"""\nContent-Type: text/css\n\n"""
            if file_ext[1] in img_type:
                l += f"""\nContent-Type: image/{file_ext[1]}\n\n""".encode("utf-8")
            if file_ext[1] in vid_type:
                l += f"""\nContent-Type: video/{file_ext[1]}\n\n""".encode("utf-8")
            if file_ext[1] in "svg":
                l += f"""\nContent-Type: image/svg+xml\n\n""".encode("utf-8")
            if file_ext[1] in "js":
                l += f"""\nContent-Type: text/javascript\n\n""".encode("utf-8")

    filename = filepath.split("/")
    file_ext = filename[-1].split(".")


    try:

        f = open(filepath[1:], 'rb')


        text = f.read()
        if file_ext[-1] == "html":
            start = text.find(b"<python>")
            temp = text[:start]
            stop = text.find(b"</python>")


            pyth = text[start+len("<python>"):stop]
            pyth = pyth.replace(b"    ", b"")
            s = pyth.decode()
            print(s)

            print(pyth)
            with open('help.txt', 'w+') as fr:
                with redirect_stdout(fr):
                    eval(s)
                fr.seek(0)
                ev = fr.read()
                t = ev.encode()
                temp+=t

            temp += text[stop:]
            text = temp

        l+=text
        while (l):
            conn.send(l)
            l = f.read(1024)
        f.close()

    except Exception as e:
        l = b"""HTTP/1.1 404"""
        print(e)
        conn.send(l)

port = 12345                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name

s.bind(("localhost", port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)

    res = processrequest(data)

    sendfile(res,conn)
    print('Done sending')
    conn.close()
