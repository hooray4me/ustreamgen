# ustreamgen
This is *hopefully* a universal M3U to strm file generator.  

Docker Image: https://hub.docker.com/r/hooray4rob/ustreamgen  

It creates a folder structure of strm files for movies and tv series.

When the container starts up it will **immediately** pull all tvshows and then movies. 

It will also **create a job** that runs at an interval you specify, to pull the latest content.  

Make sure you have the **correct** tv, movie events paths...  

**DON'T point it at your existing movies and tv shows**... make **new** folders first!

> The example below creates a job that pulls new tv shows at 12:10am, new movies at 12:20am  and new events at 12:30am in the timezone specified.

docker-compose:
```yaml
version: "3"
services:
  streamgen:
    image: hooray4rob/ustreamgen:latest
    container_name: ustreamgen
    command: /root/initialize_cron.sh
    environment:
      - UID=1024
      - GID=100
      - USER=admin
      - GROUP=users
      - SINGLELIST=true #when true a single list of movies, series and events is used. flase for multiple lists
      - MOVIES=true #set to false if movies are not desired
      - TVSHOWS=true #set to false if tv shows are not desired
      - EVENTS=true # set to false is live sporting events are not desired
      - CRONHOUR=0 #0-23 # sets the hour of the day the script will run again for all content in 1 list **ALL must be true
      - CRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for all content 1 list **ALL must be true
      - TVCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for tv shows **TVSHOWS must be true
      - TVCRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for tv shows **TVSHOWS must be true
      - MOVIECRONHOUR=0 #0-23 # sets the hour of the day the script will run again for movies **MOVIES must be true
      - MOVIECRONMINUTE=20 #0-59 # sets the minute of the day the script will run again for movies **MOVIES must be true
      - EVENTCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for events **EVENTS must be true
      - EVENTCRONMINUTE=30 #0-59 # sets the minute of the day the script will run again for events **EVENTS must be true
      - TZ=America/Chicago
      - SINGLELISTURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ # Full M3U Provider URL for all content in one list **SINGLELIST must be true
      - MOVIEURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ # Full M3U Provider URL for Movies **MOVIES must be true
      - TVSHOWURL=https://tvnow.best/api/list/user/pass/m3u8/tvshows/ # Full M3U Provider URL for TV Shows **TVSHOWS must be true
      - EVENTURL=https://tvnow.best/api/list/user/pass/m3u8/events/ # Full M3U Provider URL for Events **EVENTS must be true
      - APOLLO=true #Optional change to true if your Provider is Apollo
    volumes:
      - /path/to/folder/for/tv/strm/files1:/tv
      - /path/to/folder/for/movie/strm/files1:/movies
      - /path/to/folder/for/events/strm/files1:/events
      - /path/to/logs:/logs
```

docker-cli
```yaml
docker run -d \
  --name ustreamgen \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MOVIES=true \
  -e TVSHOWS=true \
  -e EVENTS=true \
  -e TVCRONHOUR=0 #0-23 \
  -e TVCRONMINUTE=10 #0-59 \
  -e MOVIECRONHOUR=0 #0-23 \
  -e MOVIECRONMINUTE=20 #0-59 \
  -e EVENTCRONHOUR=0 #0-23 \
  -e EVENTCRONMINUTE=30 #0-59 \
  -e TZ=America/Chicago \
  -e MOVIEURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ \
  -e TVSHOWURL=https://tvnow.best/api/list/user/pass/m3u8/tvshows/ \
  -e EVENTURL=https://tvnow.best/api/list/user/pass/m3u8/events/ \
  -e APOLLO=false \
  -e SINGLELIST=false \
  -v /path/to/folder/for/tv/strm/files:/tv \
  -v /path/to/folder/for/movie/strm/files:/movies \
  -v /path/to/folder/for/events/strm/files:/events \
  -v /path/to/logs:/logs
  /root/initialize_cron.sh
hooray4rob/ustreamgen:latest
```
