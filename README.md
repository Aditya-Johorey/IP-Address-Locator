# IP-Address-Locator
This is a project developed in Python Programming Language that can track a Global IP address around the globe, and visualize it on a map, with precise coordinates.

You can access information like Location, Coordinates, Hosting Service and Time zone of that location.

Technologies used:
* Python
* Requests
* WebBrowser
* OS
* Tkinter

The interface looks like this:

<img width="446" alt="image" src="https://user-images.githubusercontent.com/77609727/210573999-1987fb9e-79b9-4448-b762-d0248bdd80ab.png">

You are required to connect to an internet service for this application to run smoothly.

After connecting to an internet connection, you are required to enter your desired ip address in the Entry box, to determine its location.

<img width="446" alt="image" src="https://user-images.githubusercontent.com/77609727/210575502-1363ee2d-1b8c-42a0-aeca-c87d7c4e6931.png">

The ip address needs to be a global address.

You can determine that for yourself using this link: https://api.ipify.org?format=json

Click the **Submit** button, and the application will open a new tab in your browser, displaying the location of the ip address entered, using its coordinates on the map.

<img width="960" alt="image" src="https://user-images.githubusercontent.com/77609727/210576476-e1563a93-a53b-44cd-a341-657256823f02.png">

You can click on the marker to get additional information from the popup box.

You can also zoom in/ zoom out using the zoom buttons on the top left corner of the page.

The information is fetched from the API by [Ipinfo](https://ipinfo.io/ "Ipinfo website").

The API is generated using this format `https://ipinfo.io/{the ip address in interest}/json`
Info from here is then grabed and stored in a json file.

**WebBrowser** library is used to open the html in a web browser on your device.

Also in case you enter an illegitimate ip, you will recive a warning message and need to resubmit a valid global ip address.

<img width="447" alt="image" src="https://user-images.githubusercontent.com/77609727/210577897-828cf450-32a7-4cdf-a359-c66c9ae2efa6.png">

You can install the executable file for this project from [here](https://drive.google.com/file/d/14ClCUwPtVzTBYUAI1o4ONF6cvnRqWJBA/view?usp=sharing)

Hope you will like the efforts.💖

Thank You
