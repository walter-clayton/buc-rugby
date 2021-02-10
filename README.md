# buc-rugby
## Training plan for the Buc rugby.

![QR CODE](qr-code.png)

To build the docker image 'part_9', long as you are in the same directory as the 'Dockerfile', would be:

docker build . --tag=part_9

To run the docker container using the image called 'part_9' requires:

docker run -p 5000:5000 part_9

