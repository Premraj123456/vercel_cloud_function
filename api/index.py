from http.server import BaseHTTPRequestHandler
import os
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        coin_id = os.getenv("COIN_ID")

        response = requests.get(f'https://api.coincap.io/v2/assets/{coin_id}')
        coin_data = response.json()

        print(coin_data)
        return coin_data
