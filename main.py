#!/usr/bin/env python3
import tools
import streamClasses
import wget
import sys
import os
import shutil
import filecmp

def parseIPTVList( type, url, localdir, moviesDestination=None, tvShowsDestination=None, eventsDestination=None, endrange=None):
    print('...Starting Download...')
    if endrange is not None:
        for i in range(1,endrange):
            url = providerurl  + str(i)
            print(wget.download(url, ('m3u/'+type+'-'+str(i)+'.m3u')))
            streamClasses.rawStreamList('m3u/'+type+'-'+str(i)+'.m3u')
            os.remove('m3u/'+type+'-'+str(i)+'.m3u')
    else:
        print(wget.download(url, ('m3u/'+ type +'.m3u')))
        streamClasses.rawStreamList('m3u/'+type+'.m3u')
        os.remove('m3u/'+type+'.m3u')

    if moviesDestination is not None:   
        print('comparing destination ',moviesDestination)
        c = filecmp.dircmp(localdir+'/movies', moviesDestination)
        tools.compare_and_update(c)
        print('cleaning up movies temp space')       
        shutil.rmtree('movies/')

    if tvShowsDestination is not None:   
        print('comparing destination ',tvShowsDestination)
        c = filecmp.dircmp(localdir+'/tvshows', tvShowsDestination)
        tools.compare_and_update(c)
        print('cleaning up tvshows temp space')       
        shutil.rmtree('tvshows/')

    if eventsDestination is not None:   
        print('comparing destination ',eventsDestination)
        c = filecmp.dircmp(localdir+'/events', eventsDestination)
        tools.compare_and_update(c)
        print('cleaning up events temp space')       
        shutil.rmtree('events/')


directory =  os.path.abspath(os.path.dirname(__file__))
tools.printArray(sys.argv)
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

    parseIPTVList(funct, providerurl, directory, moviesDestination, tvshowsDestination, eventsDestination)

else:
    apollo = sys.argv[3]
    path = sys.argv[4]

    if funct == 'movies' or apollo == 'false':
        parseIPTVList(funct, providerurl, directory, path)
    elif funct == 'tvshows':
        parseIPTVList(funct, providerurl, directory, None, path, None, 27)
    elif funct == 'events':
        parseIPTVList(funct, providerurl, directory, None, None, path, 7)

print('done')

