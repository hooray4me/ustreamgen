# ustreamgen
This is *hopefully* a universal M3U to strm file generator.  

Docker Image: https://hub.docker.com/r/hooray4rob/ustreamgen  

It creates a folder structure of strm files for movies and tv series.

When the container starts up it will **immediately** pull all tvshows and then movies. 

It will also **create a job** that runs at an interval you specify, to pull the latest content.  

Make sure you have the **correct** tv and movie paths...  

**DON'T point it at your existing movies and tv shows**... make **new** folders first!

> The example below creates a job that pulls new tv shows at 12:10am and new movies at 12:20am in the timezone specified.

docker-compose:
```yaml
version: "3"
services:
  streamgen:
    image: hooray4rob/ustreamgen:latest
    container_name: ustreamgen
    command: /root/initialize_cron.sh
    environment:
      - PUID=1000
      - PGID=1000
      - TVCRONHOUR=0 #0-23 # sets the hour of the day the script will run again for tv shows
      - TVCRONMINUTE=10 #0-59 # sets the minute of the day the script will run again for tv shows
      - MOVIECRONHOUR=0 #0-23 # sets the hour of the day the script will run again for movies
      - MOVIECRONMINUTE=20 #0-59 # sets the minute of the day the script will run again for movies
      - TZ=America/Chicago
      - MOVIEURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ # Full M3U Provider URL for Movies
      - TVSHOWURL=https://tvnow.best/api/list/user/pass/m3u8/tvshows/ # Full M3U Provider URL for TV Shows
      - APOLLO=false #Optional change to true if your Provider is Apollo
    volumes:
      - /path/to/folder/for/tv/strm/files1:/tv
      - /path/to/folder/for/movie/strm/files1:/movies
      - /path/to/logs:/logs
```

docker-cli
```yaml
docker run -d \
  --name ustreamgen \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TVCRONHOUR=0 #0-23 \
  -e TVCRONMINUTE=10 #0-59 \
  -e MOVIECRONHOUR=0 #0-23 \
  -e MOVIECRONMINUTE=20 #0-59 \
  -e TZ=America/Chicago \
  -e MOVIEURL=https://tvnow.best/api/list/user/pass/m3u8/movies/ \
  -e TVSHOWURL=https://tvnow.best/api/list/user/pass/m3u8/tvshows/ \
  -e APOLLO=false \
  -v /path/to/folder/for/tv/strm/files:/tv \
  -v /path/to/folder/for/movie/strm/files:/movies \
  -v /path/to/logs:/logs
  /root/initialize_cron.sh
hooray4rob/ustreamgen:latest
```
