# Secure-Chatroom
Welcome to the Secure Chatroom repository. Here I will aim to be pushing new updates to help improve the chatroom by optimizing the UX as well as everything behind the scenes such as the bespoke server in the background.

# How it works?
The Secure Chatroom works by being managed by the server itself, which is solely built in Python and it uses socket to establish a digital handshake between the client (users) and the server (host). This project is built upon the client-server architecture because it is the most simplest architectures for creating little social networks between multiple users whilst maintaining user privacy as well.

Once the server launches, it idles and listens for incoming client connections. When a new client connection is heard, the server processes it by adding them to the clients list, which is saved in RAM only. This is the first security feature. I have configured to save in RAM because I want it to clean all processes when the chatroom is closed or if the server is closed or if both are closed.

Then, once the server accepts the client, the client then prompts the user to key in their name (or nickname). Once keying in their name, they are automatically entered into the chatroom where they can send messages to participants in the chatroom.

# How is the Secure Chatroom different to more professional communication applications?
The Secure Chatroom is different to the vast selection professional-grade communication applications because modern applications like MS Teams, Zoom, Skype, WhatsApp and many more, they are all stored and managed in one central location, which is most likely the servers. But the downside of this is, this can be hacked. The reason why they can be hacked is because the attack surface huge, which means hackers/creators of viruses can target one specific area; the heart of the computer network.

The Secure Chatroom, however, doesn't have large attack surface. The reason for this is, everything is saved in RAM so whenever the client closes, or the server closes or even both, the chatroom ceases and ends the client ends the connection to the server. Thus, dumping anything and everything that was stored in RAM so that there is no trace of anything.

# Installation
To install the Secure Chatroom, you need to download the executable file named 'LAZY-SERVER' and then download the Secure Chatroom setup executable file. You then install the Secure Chatroom setup file and follow the steps in the Installation Wizard. During initial installation, it will create a desktop icon which is blue floppy disk with the Python logo floating on top of it.

Important Note: before you launch the Secure Chatroom client UI, it is heavily advised that you launch the server first because the chatroom is dependent upon the server. If you try to launch the Secure Chatroom client UI first and attempt to join the chatroom, you will be faced with an "Oops! An error has occurred".

# Future Updates
I will be planning to push out future updates and frequent security updates to help improve the user experience. Enjoy the chatroom! Thanks :)
