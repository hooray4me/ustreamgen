#!/usr/bin/env python3
import sys
import os
import listhandler

directory =  os.path.abspath(os.path.dirname(__file__))
providerurl = sys.argv[1]
funct = sys.argv[2]

if funct == 'all':
    movies = sys.argv[3]
    tvshows = sys.argv[4]
    events = sys.argv[5]

    moviesDestination = None
    if movies == 'true':
        moviesDestination = sys.argv[6]

    tvshowsDestination = None
    if tvshows == 'true':
        tvshowsDestination = sys.argv[7]

    eventsDestination = None  
    if events == 'true':
        eventsDestination = sys.argv[8]

    listhandler.parseIPTVLists(funct, providerurl, directory, moviesDestination, tvshowsDestination, eventsDestination)

else:
    apollo = sys.argv[3]
    path = sys.argv[4]

    if funct == 'movies' or apollo == 'false':
        listhandler.parseIPTVLists(funct, providerurl, directory, path)
    elif funct == 'tvshows':
        listhandler.parseIPTVLists(funct, providerurl, directory, None, path, None, 27)
    elif funct == 'events':
        listhandler.parseIPTVLists(funct, providerurl, directory, None, None, path, 7)


