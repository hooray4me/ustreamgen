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
path = sys.argv[3]
apollo = sys.argv[4]

directory =  os.path.abspath(os.path.dirname(__file__))

print('...Starting Download...')
if funct == 'tv' and apollo == 'true':
    for i in range(1,24):
        url = providerurl  + str(i)
        print(wget.download(url, ('m3u/tvshows-'+str(i)+'.m3u')))
        apollolist = streamClasses.rawStreamList('m3u/tvshows-'+str(i)+'.m3u')
        os.remove('m3u/tvshows-'+str(i)+'.m3u')
    print('comparing destination ',path)
    c = filecmp.dircmp(directory+'/tvshows', path)
    tools.compare_and_update(c)
    print('cleaning up temp space')
    cleanup = shutil.rmtree('tvshows/')
elif funct == 'tv':
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
