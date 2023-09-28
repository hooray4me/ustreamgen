# ustreamgen
This is *hopefully* a universal M3U to strm file generator.  

Docker Image: https://hub.docker.com/r/hooray4rob/ustreamgen  

It creates a folder structure of strm files for movies and tv series.

When the container starts up it will **immediately** pull all tvshows and then movies. 

It will also **create a job** that runs at an interval you specify, to pull the latest content.  

Make sure you have the **correct** tv, movie events paths...  

**DON'T point it at your existing movies and tv shows**... make **new** folders first!

> The example below creates a job that pulls new tv shows at 12:10am, new movies at 12:20am  and new events at 12:30am in the timezone specified.

Create a **.env** file in the same folder you will run the container from.

```
TZ=America/Chicago #Optional timezone.
PUID=1024 #Optional UserID of the account that will run the service
PGID=100 #Optional GroupID of the account that will run the service
UID=1024 #Optional UserID for file permissions. Default: 1000
GID=100 #Optional GroupID for file permissions. Default: 1000
UNAME=admin #Optional name of UID. If used MUST match id of UID. Default: root
GROUP=users #Optional name of GID. If used MUST match id of GID. Default: root
SINGLELIST=false #A single list is used for all movies, tv shows and events. Default: false
SINGLELISTURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ #Full M3U Provider URL for all content in one list **SINGLELIST must be true
CRONHOUR=0 #0-23 # sets the hour of the day the script will run again for all content in 1 list **SINGLELIST must be true
CRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for all content 1 list **SINGLELIST must be true
MOVIES=true #A seperate list is used for movies. Default: false
MOVIEURL=https://tvnow.best/api/list/USER/PASS/m3u8/movies/ #Full M3U Provider URL for Movies **MOVIES must be true
MOVIECRONHOUR=0 #0-23 # sets the hour of the day the script will run again for movies **MOVIES must be true
MOVIECRONMINUTE=20 #0-59 # sets the minute of the day the script will run again for movies **MOVIES must be true
TVSHOWS=true #A seperate list is used for tv shows. Default: true
TVSHOWURL=https://tvnow.best/api/list/USER/PASS/m3u8/tvshows/ # Full M3U Provider URL for TV Shows **TVSHOWS must be true
TVCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for tv shows **TVSHOWS must be true
TVCRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for tv shows **TVSHOWS must be true
EVENTS=false #A seperate list is used for events. Default: false
EVENTURL=https://tvnow.best/api/list/user/pass/m3u8/events/ #Full M3U Provider URL for Events **EVENTS must be true
EVENTCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for events **EVENTS must be true
EVENTCRONMINUTE=30 #0-59 # sets the minute of the day the script will run again for events **EVENTS must be true
APOLLO=true #Optional change to true if your Provider is Apollo. Default: false
```
docker-compose:
```yaml
version: "3"
services:
  streamgen:
    image: ghcr.io/hooray4me/ustreamgen:latest
    container_name: ustreamgen
    command: /root/initialize_cron.sh
    env_file: .env
    volumes:
      - /path/to/folder/for/tv/strm/files:/tv
      - /path/to/folder/for/movie/strm/files:/movies
      - /path/to/folder/for/events/strm/files:/events
      - ./logs:/logs
    restart: unless-stopped
```

docker-cli
```yaml
docker run -d \
  --name ustreamgen \
  --env-file ./.env \
  -v /path/to/folder/for/tv/strm/files:/tv \
  -v /path/to/folder/for/movie/strm/files:/movies \
  -v /path/to/folder/for/events/strm/files:/events \
  -v /path/to/logs:/logs \
  /root/initialize_cron.sh
ghcr.io/hooray4me/ustreamgen:v1.39-dev
```

**Experimental** support for multiple providers:

Add tvproviders.txt and/or movieproviders.txt file to the container folder next to the .env file.

Populate the aforementioned files with the url to pull the m3u for each provider:
IE
tvproviders.txt
```
https://tvnow.best/api/list/user/pass/m3u8/tvshows/1
https://tvnow.best/api/list/user/pass/m3u8/tvshows/2
https://tvnow.best/api/list/user/pass/m3u8/tvshows/3
https://tvnow.best/api/list/user/pass/m3u8/tvshows/4
https://tvnow.best/api/list/user/pass/m3u8/tvshows/5
```
movieproviders.txt
```
https://tvnow.best/api/list/user1/pass1/m3u8/movies/
https://tvnow.best/api/list/user2/pass2/m3u8/movies/
```
Trim the .env file to **only** these variables.

```
TZ=America/Chicago #Optional timezone.
PUID=1024 #Optional UserID of the account that will run the service
PGID=100 #Optional GroupID of the account that will run the service
UID=1024 #Optional UserID for file permissions. Default: 1000
GID=100 #Optional GroupID for file permissions. Default: 1000
UNAME=admin #Optional name of UID. If used MUST match id of UID. Default: root
GROUP=users #Optional name of GID. If used MUST match id of GID. Default: root
MOVIECRONHOUR=0 #0-23 # sets the hour of the day the script will run again for movies
MOVIECRONMINUTE=20 #0-59 # sets the minute of the day the script will run again for movies 
TVCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for tv shows
TVCRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for tv shows
MULTIPLETVPROVIDERS=true
MULTIPLEMOVIEPROVIDERS=true
```
Amend your docker-compose.yaml to include a volume for each provider.
```yaml
version: "3"
services:
  streamgen:
    image: ghcr.io/hooray4me/ustreamgen:v1.39-dev
    container_name: ustreamgen
    command: /root/initialize_cron.sh
    env_file: .env
    volumes:
      - ./tvshows1:/multipletvshows1 #naming convention :/multipletvshows* must stay the same
      - ./tvshows2:/multipletvshows2
      - ./movies1:/multiplemovies1 #naming convention :/multiplemovies* must stay the same
      - ./movies2:/multiplemovies2
      - ./movies3:/multiplemovies3
      - ./movies4:/multiplemovies4
      - ./movies5:/multiplemovies5
      
      - ./logs:/logs
    restart: unless-stopped
```
docker-cli
```yaml
docker run -d \
  --name ustreamgen \
  --env-file ./.env \
  -v ./tvshows1:/multipletvshows1 \
  -v ./tvshows2:/multipletvshows2 \
  -v ./movies1:/multiplemovies1 \
  -v ./movies2:/multiplemovies2 \
  -v ./movies3:/multiplemovies3 \
  -v ./movies4:/multiplemovies4 \
  -v ./movies5:/multiplemovies5 \
  -v /path/to/logs:/logs \
  /root/initialize_cron.sh
ghcr.io/hooray4me/ustreamgen:v1.39-dev
```