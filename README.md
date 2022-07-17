# Crux: Demonstration Malicious Chrome Extension

This repository is for **educational purposes only**. If you use this outside of security research or authorized pentests, you're doing crimes. Don't do crimes.

## Objective

This tool is intended to demonstrate the risk posed by malicious Chrome extensions, and how they can be loaded into users' browsers to disclose secrets.

The extension is designed to report cookies, URLs, and form data to a listening server. The result is an extension that can move an unprivileged RCE to credentialed elevation and other kinds of pivoting.

## Usage

The repository contains 2 directories: `extension` and `server`. Let's begin with the server.

### Server

Clone this repository to any server accessible from your victim. Make sure Flask and Rich are installed with `pip3 install flask rich`. Then, simply run `flask run [port]`. Your server is now listening for data.

### Extension

Before launching the extension on the victim server, make sure to change the `server_host` variable in `background.js` to match your listening server.

### Deployment

This is a post-compromise tool. With the delivery option of your choice, upload the extension folder to a location on the target system. For proper OPSEC, I recommend the appropriate folder for extensions for the given browser.

Once the unpacked extension has been deployed, launch the desired Chromium-based browser with

`/path/to/browser --load-extension='C:/path/to/extension`. You can use other command-line options as desired, or even follow the [ChromeLoader](https://unit42.paloaltonetworks.com/chromeloader-malware/) playbook:

![ChromeLoader stopping existing Chrome Windows and launching with an evil extension](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/07/Screen-Shot-2022-07-11-at-6.48.29-PM.png)

Once the browser is open and communicating with the server, all you have to do is wait for data to come in.
