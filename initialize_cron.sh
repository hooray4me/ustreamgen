#! /bin/bash
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh
chmod +x /root/project_env.sh
touch /logs/cron.log
if [ "$TVSHOWS" == "true" ]
then
    cd /m3u2strm && python3 main.py $TVSHOWURL tv /tv/ $APOLLO
    (crontab -l ; echo "$TVCRONMINUTE $TVCRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $TVSHOWURL tv /tv/ $APOLLO >> /logs/cron.log") | crontab
fi
if [ "$MOVIES" == "true" ]
then
    cd /m3u2strm && python3 main.py $MOVIEURL movies /movies/ $APOLLO
    (crontab -l ; echo "$MOVIECRONMINUTE $MOVIECRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $MOVIEURL movies /movies/ $APOLLO >> /logs/cron.log") | crontab
fi
if [ "$EVENTS" == "true" ]
then
    cd /m3u2strm && python3 main.py $EVENTURL events /events/ $APOLLO
    (crontab -l ; echo "$EVENTCRONMINUTE $EVENTCRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $EVENTURL events /events/ $APOLLO >> /logs/cron.log") | crontab
fi
cron && tail -f /logs/cron.log