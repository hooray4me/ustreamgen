#!/usr/bin/env python3
import tools
import streamClasses
import wget
import sys
import os
import shutil
import filecmp

providerurl = sys.argv[1]
funct = sys.argv[2]

directory =  os.path.abspath(os.path.dirname(__file__))

print('...Starting Download...')
if funct == 'all':
    print(wget.download(providerurl, ('m3u/tvshows.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/tvshows.m3u')
    os.remove('m3u/tvshows.m3u')
    print('comparing destination ')
    if sys.argv[3] =='true': #movies
        c = filecmp.dircmp(directory+'/movies', sys.argv[6])
        tools.compare_and_update(c)
    if sys.argv[4] =='true': #series/tvshows
        c = filecmp.dircmp(directory+'/tvshows', sys.argv[7])
        tools.compare_and_update(c)
    if sys.argv[5] =='true': #events
        c = filecmp.dircmp(directory+'/events', sys.argv[8])
        tools.compare_and_update_events(c)
      
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
    cleanup = shutil.rmtree('movies/')
    cleanup = shutil.rmtree('events/')
else:
    apollo = sys.argv[3]
    path = sys.argv[4]

    if funct == 'tv' and apollo == 'true':
        for i in range(1,27):
            url = providerurl  + str(i)
            print(wget.download(url, ('m3u/tvshows-'+str(i)+'.m3u')))
            apollolist = streamClasses.rawStreamList('m3u/tvshows-'+str(i)+'.m3u')
            os.remove('m3u/tvshows-'+str(i)+'.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/tvshows', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('tvshows/')
    elif funct == 'events' and apollo == 'true':
        urltype = 'events'
        for i in range(1,7):
            url = providerurl + urltype +'/' + str(i)
            print(wget.download(url, ('m3u/apolloevents-'+str(i)+'.m3u')))
            apollolist = streamClasses.rawStreamList('m3u/apolloevents-'+str(i)+'.m3u')
            os.remove('m3u/apolloevents-'+str(i)+'.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/events', path)
        tools.compare_and_update_events(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('events/')
    elif funct == 'events' and apollo == 'false':
        print(wget.download(providerurl, ('m3u/apolloevents.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/apolloevents.m3u')
        os.remove('m3u/apolloevents.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/events', path)
        tools.compare_and_update_events(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('events/')
    elif funct == 'tv' and apollo == 'false':
        print(wget.download(providerurl, ('m3u/tvshows.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/tvshows.m3u')
        os.remove('m3u/tvshows.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/tvshows', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('tvshows/')
    elif funct == 'movies':
        print(wget.download(providerurl, ('m3u/movies.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/movies.m3u')
        os.remove('m3u/movies.m3u')
        print('comparing destination ',path)
        c = filecmp.dircmp(directory+'/movies', path)
        tools.compare_and_update(c)
        print('cleaning up temp space')
        cleanup = shutil.rmtree('movies/')
    print('done')
