# Why you should have a rooster in your office
TODO: Einleitung

# Project Setup
## Requirements
1. RaspberryPi with Raspbian OS installed
2. Docker
3. Connected audio device

### RaspberryPi Setup
TODO

### Installing Docker on Rasbian
[this](https://phoenixnap.com/kb/docker-on-raspberry-pi) (TODO)

### Connect Audio Device
We chose to have Bluetooth speakers connected to the RaspberryPi. Alternatively you can simply connect any speaker via the Raspberrys AUX Audio Output.

## Pull OpenAir-Flow
There are two options to get the Docker image.
1. From Docker Hub
2. Building it from GitHub

### From Docker Hub
TODO

### Building it from GitHub
From the terminal:
1. With `cd <directory>` move to the desired project directory
2. Clone this repository onto the RaspberryPi: `git clone <link>`
3. Move into the projects folder: `cd air-hahn`
4. Build the image: `docker build --rm -t air-hahn:v1 .` (this step might take quite long, up to more than an hour)

# Starting Docker container
Run `docker run -it -p 8080:8080 air-Hahn:v1`

TODO: Audio exposure

## Changing the config and sound file
To load your own config and/or sound file(s) into the docker container you need to have a folder containing the config.yml and/or sound file you want to use.

Mount it to the docker container on startup by adding the flag: `-v <path to folder>:/air-hahn/dags/mount`
### config.yml
To change any settings copy the `config.yml` from the GitHub repository and change any values you want.

### Sound File(s)
The sound file we use is from [here](https://freesound.org/people/Lydmakeren/sounds/510906/).

To use different sounds for the open and close reminder, or another sound in general, add it to the folder you will be mounting to the docker container. Change the values `start_file` and `end_file` in the `config.yml` to match the name(s) of your sound file(s).
