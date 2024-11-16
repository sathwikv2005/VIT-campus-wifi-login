# College Portal Auto Login Script

This Python script automates logging into VIT AP college wifi portal. It retrieves the username and password from a `cred.txt` file, navigates through the login page, and opens the redirected page in a web browser after a successful login.

## Features

- Uses HTTPS requests to communicate with the college portal server.
- Reads login credentials securely from a local `cred.txt` file.
- Handles redirects by extracting and opening the destination URL in a browser.

## Prerequisites

- **Python 3** installed on your system.
- Required modules:
  - `http.client`
  - `ssl`
  - `re`
  - `urllib.parse`
  - `webbrowser`

These are standard Python libraries, so no additional installation is needed.

## Setup

1. **Prepare your credentials file**: Create a `cred.txt` file in the same directory as the script, with your username and password on separate lines, as shown below:

   ```
   your_username
   your_password
   ```

2. **Run the Script**: Open a terminal, navigate to the script’s directory, and execute:

   ```bash
   python VITCampusLogin.py
   ```


## How It Works

1. **Reads Credentials**: The script reads the username and password from `cred.txt`.
2. **Sends GET Request**: It initiates a GET request to retrieve the login page and captures the `magic` token required for the login.
3. **Sends POST Request**: Using the extracted `magic` value, the script sends a POST request with login credentials.
4. **Handles Redirect**: After a successful login, it captures the redirect URL from the response and opens it in the default web browser.

## Disclaimer

This script is for personal use only. Unauthorized access or misuse may violate college policies.
