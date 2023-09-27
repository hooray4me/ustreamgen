#! /bin/bash
# store env as export in script file to export, filter LS_color env, it interfere with the export command
#printenv | compgen -v -X '*LS_COLORS*' | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh
#chmod +x /root/project_env.sh

#create log file
touch /logs/cron.log

# remove old jobs, needed when docker restarted, otherwise there multiple rules created
crontab -r

#create cron rule(s)
if [ "$SINGLELIST" == "true" ]
then
   touch /logs/cron-singlelist.log && cd /m3u2strm && python3 main.py $SINGLELISTURL all $MOVIES $TVSHOWS $EVENTS /movies/ /tv/ /events/ $UID $GID
    if [ -z "$CRON" ]
    then
        # CRON variable empty, use the hour minute
        (crontab -l ; echo "$CRONMINUTE $CRONHOUR * * * cd /m3u2strm && python3 main.py $SINGLELISTURL all $MOVIES $TVSHOWS $EVENTS /movies/ /tv/ /events/ $UID $GID >> /logs/cron-singlelist.log") | crontab
    else
        # Use FULL CRON, so you can shedule like you want
        (crontab -l ; echo "$CRON cd /m3u2strm && python3 main.py $SINGLELISTURL all $MOVIES $TVSHOWS $EVENTS /movies/ /tv/ /events/ $UID $GID >> /logs/cron-singlelist.log") | crontab
    fi
else
    if [ "$TVSHOWS" == "true" ]
    then 
        touch /logs/cron-tvshows.log && cd /m3u2strm && python3 main.py $TVSHOWURL tvshows $APOLLO /tv/ $UID $GID
        if [ -z "$TVCRON" ]
        then
            # CRON variable empty, use the hour minute
            (crontab -l ; echo "$TVCRONMINUTE $TVCRONHOUR * * * cd /m3u2strm && python3 main.py $TVSHOWURL tvshows $APOLLO /tv/ $UID $GID >> /logs/cron-tvshows.log") | crontab
        else
            # Use FULL CRON, so you can shedule like you want
            (crontab -l ; echo "$TVCRON cd /m3u2strm && python3 main.py $TVSHOWURL tvshows $APOLLO /tv/ $UID $GID >> /logs/cron-tvshows.log") | crontab
        fi
    fi
    if [ "$MOVIES" == "true" ]
    then
        touch /logs/cron-movies.log && cd /m3u2strm && python3 main.py $MOVIEURL movies $APOLLO /movies/ $UID $GID
        if [ -z "$MOVIECRON" ]
        then
            # CRON variable empty, use the hour minute
            (crontab -l ; echo "$MOVIECRONMINUTE $MOVIECRONHOUR * * * cd /m3u2strm && python3 main.py $MOVIEURL movies $APOLLO /movies/ $UID $GID >> /logs/cron-movies.log") | crontab
        else
            # Use FULL CRON, so you can shedule like you want
            (crontab -l ; echo "$MOVIECRON cd /m3u2strm && python3 main.py $MOVIEURL movies $APOLLO /movies/ $UID $GID >> /logs/cron-movies.log") | crontab
        fi
    fi
    if [ "$EVENTS" == "true" ]
    then
        touch /logs/cron-events.log && cd /m3u2strm && python3 main.py $EVENTURL events $APOLLO /events/ $UID $GID
        if [ -z "$EVENTCRON" ]
        then
            # CRON variable empty, use the hour minute
            (crontab -l ; echo "$EVENTCRONMINUTE $EVENTCRONHOUR * * * cd /m3u2strm && python3 main.py $EVENTURL events $APOLLO /events/ $UID $GID >> /logs/cron-events.log") | crontab
        else
            # Use FULL CRON, so you can shedule like you want
            (crontab -l ; echo "$EVENTCRON cd /m3u2strm && python3 main.py $EVENTURL events $APOLLO /events/ $UID $GID >> /logs/cron-events.log") | crontab
        fi
    fi
fi
cron && tail -f /logs/cron.log