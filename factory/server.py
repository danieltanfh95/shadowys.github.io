import sys
import webbrowser
from urllib.request import urlopen
from urllib.error import *
from threading import Thread

if sys.version < '3':
   import BaseHTTPServer as server
   from CGIHTTPServer import CGIHTTPRequestHandler
else:
   import http.server as server
   from http.server import CGIHTTPRequestHandler

def serve(port=8000,url=None):
   if url==None: url="http://localhost:%s"%port
   try:
      #Check if the local server already exists.
      exist=urlopen(url)
      print("The port, %s is already open for %s"%(port,url))
      input("Press enter to exit.")
   except URLError:
      server_address = ('', port)
      handler = CGIHTTPRequestHandler
      httpd = server.HTTPServer(server_address, handler)
      print("server running on port %s" % server_address[1])
      serverthread=Thread(target=httpd.serve_forever)
      serverthread.start()
      webbrowser.open(url,new=2)

if __name__=="__main__":
   data=input("\nContinue to view webpage on the localhost?\nType y for yes.[y]>>>")
   if data.upper()=="Y":
      serve()
