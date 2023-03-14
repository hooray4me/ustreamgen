#! /bin/bash
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh
chmod +x /root/project_env.sh
touch /logs/cron.log
cd /m3u2strm && python3 main.py $TVSHOWURL tv /tv/ $APOLLO
cd /m3u2strm && python3 main.py $MOVIEURL movies /movies/ $APOLLO
(crontab -l ; echo "$TVCRONMINUTE $TVCRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $TVSHOWURL tv /tv/ $APOLLO >> /logs/cron.log") | crontab
(crontab -l ; echo "$MOVIECRONMINUTE $MOVIECRONHOUR * * * . /root/project_env.sh; cd /m3u2strm && python3 main.py $MOVIEURL movies /movies/ $APOLLO >> /logs/cron.log") | crontab
cron && tail -f /logs/cron.log