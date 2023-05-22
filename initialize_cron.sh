#! /bin/bash
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh
chmod +x /root/project_env.sh
touch /logs/cron.log

if [ "$SINGLELIST" == "true" ]
then
    cd /m3u2strm && python3 main.py $SINGLELISTURL all $MOVIES $TVSHOWS $EVENTS /movies/ /tv/ /events/
    (crontab -l ; echo "$CRONMINUTE $CRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $SINGLELISTURL all $MOVIES $TVSHOWS $EVENTS /movies/ /tv/ /events/ >> /logs/cron.log") | crontab
fi
if  [ "$SINGLELIST" != "true" ]
then
    if [ "$TVSHOWS" == "true" ]
    then
        cd /m3u2strm && python3 main.py $TVSHOWURL tvshows $APOLLO /tv/
        (crontab -l ; echo "$TVCRONMINUTE $TVCRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $TVSHOWURL tvshows $APOLLO /tv/ >> /logs/cron.log") | crontab
    fi
    if [ "$MOVIES" == "true" ]
    then
        cd /m3u2strm && python3 main.py $MOVIEURL movies $APOLLO /movies/
        (crontab -l ; echo "$MOVIECRONMINUTE $MOVIECRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $MOVIEURL movies $APOLLO /movies/ >> /logs/cron.log") | crontab
    fi
    if [ "$EVENTS" == "true" ]
    then
        cd /m3u2strm && python3 main.py $EVENTURL events $APOLLO /events/
        (crontab -l ; echo "$EVENTCRONMINUTE $EVENTCRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $EVENTURL events $APOLLO /events/ >> /logs/cron.log") | crontab
    fi
fi
cron && tail -f /logs/cron.log