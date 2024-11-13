import http.client
import ssl
import re
import urllib.parse
import webbrowser

# Read credentials from the file
with open("cred.txt", "r") as cred_file:
    username = cred_file.readline().strip()  # First line is username
    password = cred_file.readline().strip()  # Second line is password

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_NONE

conn = http.client.HTTPSConnection("172.18.10.10", 1000, context=context)

get_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '172.18.10.10:1000',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

conn.request("GET", "/login?", headers=get_headers)

try:
    response = conn.getresponse()
    data = response.read()
    cookies = response.getheader("Set-Cookie")

    match = re.search(r'name="magic" value="([^"]+)"', data.decode())

    if match:
        magic_value = match.group(1)

        params = {
            'username': username,
            'password': password,
            'magic': magic_value,
            '4Tredir': "https://172.18.10.10:1000/login?"
        }

        body = urllib.parse.urlencode(params)

        post_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': str(len(body)),
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Host': '172.18.10.10:1000',
            'Origin': 'http://172.18.10.10:1000',
            'Referer': 'http://172.18.10.10:1000/login?',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        if cookies:
            post_headers['Cookie'] = cookies

        conn.request("POST", "/login?", body=body, headers=post_headers)

        response = conn.getresponse()
        data = response.read()

        redirect_match = re.search(r'window\.location="([^"]+)"', data.decode())

        if redirect_match:
            redirect_url = redirect_match.group(1)
            webbrowser.open_new_tab(redirect_url)
        else:
            print("No redirect URL found in the response.")
            
    else:
        print("Magic value not found in the response.")
        
except Exception as e:
    print("Error during request:", e)
finally:
    conn.close()
