# OpenAirFlow
**Why should a rooster crows in your office?**

Everyone is talking about Airflow. - We took it literally and created a kit for you to solve a problem everyone is 
talking about as well: 
Whether you are three or a thousand employees - every organization is now facing the challenge to air spaces in a way 
that viruses cannot spread within the team. 
We mean real viruses of course, but use software we already integrated in our work at Birds on Mars: 
When it comes to the productive and sustainable development of AI, “Apache Airflow” is currently on everyone’s lips. 
Our open source library “OpenAirFlow” provides you on the golden docker tray with the possibility to program a 
crowing tap that coordinates your airing. 
Just install the software on a Raspberry Pi, set the times of your “airflow” according to your individual conditions 
and be reminded regularly to air your place! Join in, bring airflow into your environment and help us develop a second version with integrated CO2 sensors. We are excited about your ideas!
## Project Setup

### Requirements
1. Raspberry Pi with Raspbian OS installed
2. Docker
3. Connected audio device

### RaspberryPi Setup
TODO

### Installing Docker on Raspbian
We followed [this](https://phoenixnap.com/kb/docker-on-raspberry-pi) guide.

From the terminal run:

1. `sudo apt-get update && sudo apt-get upgrade` to update your software
2. `curl -fsSL https://get.docker.com -o get-docker.sh` to download the install script
3. `sudo sh get-docker.sh` to run the install script.
4. `sudo usermod -aG docker pi` to add the `pi` user to the docker group, to allow it to run docker commands

If your installation worked, `docker version` will show you the installed docker version.

### Connect Audio Device
Connect any speakers you want to the AUX Audio Output of the Raspberry Pi.

## Installing OpenAirFlow
There are two options to get the Docker image.
1. From Docker Hub
2. Building it from GitHub sources

### From Docker Hub
TODO

### Building it from GitHub
From the terminal:
1. With `cd <directory>` move to the desired target directory
2. Clone this repository onto the Raspberry Pi: `git clone git@github.com:birds-on-mars/OpenAirFlow.git`
3. Go to the project folder: `cd openairflow`
4. Build the image: `docker build --rm -t openairflow:v1 .` (this step might take quite long, up to several hours)

## Starting OpenAirFlow
Run `docker run -it --device /dev/snd -p 8080:8080 --name openairflow --restart unless-stopped openairflow:v1`

- The `--device /dev/snd` flag provides the docker container with access to the audio device.
- The `-p 8080:8080` forwards port 8080 from the host to port 8080 of the docker container (where airflow is running). Change the first port however you like if needed.
- `--name openairflow` (optional) defines the name of the container. Change it as you like.
- `--restart unless-stopped` will restart the docker container after rebooting the Raspberry Pi. To stop it run `docker stop <container ID or name>`. You can get the ID or name with `docker ps`.
- `openairflow:v1` is the name if the docker image to start

### Changing the config and sound file
To load your own config and/or sound file(s) into the docker container you need to have a folder containing the config.yml and/or sound file you want to use.

Mount it to the docker container on startup by adding the following flag to the run command: `-v <path to folder>:/usr/local/airflow/dags/mount`
#### config.yml
To change any settings copy the `config.yml` from the GitHub repository and change any values you want.

#### Sound File(s)
The sound file we use is from [here](https://freesound.org/people/Lydmakeren/sounds/510906/) and converted to mp3.

To use different sounds for the open and close reminder, or another sound in general, add it to the folder you will be mounting to the docker container. Change the values `start_file` and `end_file` in the `config.yml` to match the name(s) of your sound file(s). As by now only mp3 files are supported.
