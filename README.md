# Raspberry Pi Smart Hub

This project uses a Raspberry Pi 3 as a smart hub for dumb lights.

A more detailed writeup of the project can be found at: https://sweisss.github.io/projects/smarthubfordumblights.html

## Setup
### Discord Integration
After importing the flow to Node-RED, be sure to install [node-red-contrib-discord 5.0.0](https://flows.nodered.org/node/node-red-contrib-discord) from the Manage palatte. 

Replace the "Token" entry value of the Discord node with the token of your bot. 

<img width="408" height="128" alt="image" src="https://github.com/user-attachments/assets/c30943b8-6aa9-4933-8886-c03d0c7f9c62" />

Alternatively, save the token under the  name `DISCORD_TOKEN` at the top of your _settings.js_ file located in _/home/raspberry/.node-red_.
The line should look like the following:
```
process.env.DISCORD_TOKEN = '<token>'
```

### eWeLink Integration
To control a smart switch using the [eWeLink API]([url](https://github.com/CoolKit-Technologies/eWeLink-API/blob/main/en/APICenterV2.md)):
1. Log in to https://web.ewelink.cc/
2. Get the bearer token from developer tools
    - Right-click anywhere on the web application and select "Inspect"
    - Go to the Network tab and refresh the page
    - Some of the files, including _profile_, _my-scene_, and _query_, will display the Bearer Token in the Request Headers
    - **NOTE:** The token will refresh after logging in on a different device.
4. Add the device id to _settings.js_ with the name `PORCHSWITCH_ID`, similar to the `DISCORD_TOKEN`, and reference it from an environment variable in the "Set HTTP POST headers and body" node.
5. Add the bearer token to a file named _token.txt_ adjacent to the _rf_transmit.py_ script. Update the file paths in the _readToken_ and _writeToken_ nodes if necessary. 

### Python Script
Be sure to update the exec node with the correct location of the python script on your system. 
