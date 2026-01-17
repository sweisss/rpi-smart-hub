# Raspberry Pi Smart Hub

This project uses a Raspberry Pi 3 as a smart hub for dumb lights.

A more detailed writeup of the project can be found at: https://sweisss.github.io/projects/smarthubfordumblights.html

After importing the flow to Node-RED, be sure to install [node-red-contrib-discord 5.0.0](https://flows.nodered.org/node/node-red-contrib-discord) from the Manage palatte. 

Replace the `token` entry of the Discord node with the token of your bot. 

<img width="408" height="128" alt="image" src="https://github.com/user-attachments/assets/c30943b8-6aa9-4933-8886-c03d0c7f9c62" />

Alternatively, save the token under the  name `DISCORD_TOKEN` at the top of your _settings.js_ file located in _/home/raspberry/.node-red_.
The line should look like the following:
```
process.env.DISCORD_TOKEN = '<token>'
```
