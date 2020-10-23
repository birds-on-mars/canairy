# OpenAirFlow - Warum in eurem Büro ein Hahn krähen sollte
Alle sprechen von Airflow - Wir haben es mal ganz wörtlich genommen und geben euch ein Bastelkit an die Hand, mit dem ihr ein Problem lösen könnt, über das ebenfalls alle sprechen: Ob drei oder tausend Mitarbeiter*innen stark - jedes Unternehmen ist gerade vor die Herausforderung gestellt, so zu lüften, dass sich Viren im Team nicht verbreiten können - wir meinen natürlich echte Viren, machen uns aber Software zunutze, die wir bei Birds on Mars ohnehin schon an vielen Stellen nutzen: „Apache Airflow” ist derzeit in aller Munde, wenn es um die produktive und nachhaltige Entwicklung von KI geht. Unsere Open Source Bibliothek „OpenAirFlow” liefert euch auf dem goldenen Dockertablett die Möglichkeit, einen krähenden Hahn zu programmieren, der euer Lüften koordiniert. Installiert die Software einfach auf einem Raspberry Pi, konfiguriert die Zeiten eures „Airflows” entsprechend eurer individuellen Voraussetzungen und werdet regelmäßig an das Lüften erinnert! Macht mit, bringt Airflow in eure Umgebung und helft uns eine zweite Version mit integrierten CO2 Sensoren zu entwickeln. Wir sind gespannt auf eure Ideen!


# Project Setup
## Requirements
1. Raspberry Pi with Raspbian OS installed
2. Docker
3. Connected audio device

### RaspberryPi Setup
TODO

### Installing Docker on Rasbian
[this](https://phoenixnap.com/kb/docker-on-raspberry-pi) (TODO)

### Connect Audio Device
Connect any speakers you want to the AUX Audio Output of the Raspberry Pi

## Pull OpenAirFlow
There are two options to get the Docker image.
1. From Docker Hub
2. Building it from GitHub

### From Docker Hub
TODO

### Building it from GitHub
From the terminal:
1. With `cd <directory>` move to the desired project directory
2. Clone this repository onto the Raspberry Pi: `git clone <link>`
3. Move into the projects folder: `cd openairflow`
4. Build the image: `docker build --rm -t openairflow:v1 .` (this step might take quite long, up to several hours)

# Starting Docker container
Run `docker run -it -p 8080:8080 openairflow:v1`

TODO: Audio exposure

## Changing the config and sound file
To load your own config and/or sound file(s) into the docker container you need to have a folder containing the config.yml and/or sound file you want to use.

Mount it to the docker container on startup by adding the flag: `-v <path to folder>:/air-hahn/dags/mount`
### config.yml
To change any settings copy the `config.yml` from the GitHub repository and change any values you want.

### Sound File(s)
The sound file we use is from [here](https://freesound.org/people/Lydmakeren/sounds/510906/) and converted to mp3.

To use different sounds for the open and close reminder, or another sound in general, add it to the folder you will be mounting to the docker container. Change the values `start_file` and `end_file` in the `config.yml` to match the name(s) of your sound file(s). As by now only mp3 files are supported.
