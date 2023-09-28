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
    uid = sys.argv[9]
    gid = sys.argv[10]
    listhandler.parseIPTVLists(funct, providerurl, directory, moviesDestination, tvshowsDestination, eventsDestination, None, int(uid), int(gid))

else:
    apollo = sys.argv[3]
    path = sys.argv[4]
    uid = sys.argv[5]
    gid = sys.argv[6]

    if funct == 'multipletvshows':
        providerlist = sys.argv[1]
        print("provider - %s - something" % (providerlist))
        listhandler.parseMultipleLists(funct, providerurl, directory, None, path, int(uid), int(gid))
    elif funct == 'multiplemovies':
        providerlist = sys.argv[1]
        listhandler.parseMultipleLists(funct, providerurl, directory, path, None ,int(uid), int(gid))
    else:
      if funct == 'movies' or apollo == 'false':
          listhandler.parseIPTVLists(funct, providerurl, directory, path, None, None, None ,int(uid), int(gid))
      elif funct == 'tvshows':
          listhandler.parseIPTVLists(funct, providerurl, directory, None, path, None, 24, int(uid), int(gid))
      elif funct == 'events':
          listhandler.parseIPTVLists(funct, providerurl, directory, None, None, path, 7, int(uid), int(gid))


