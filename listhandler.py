import tools
import streamClasses
import wget
import os
import shutil
import filecmp

def parseIPTVLists( type, url, localdir, moviesDestination=None, tvShowsDestination=None, eventsDestination=None, endrange=None, uid=None, gid=None):
    downloadAndParseLists(type, url, endrange)

    if moviesDestination is not None:
        moveToDestination(localdir,'movies',moviesDestination, uid, gid)

    if tvShowsDestination is not None: 
        moveToDestination(localdir,'tvshows',tvShowsDestination, uid, gid)

    if eventsDestination is not None:   
        moveToDestination(localdir,'events',eventsDestination, uid, gid)

    #clean up fir single list, but 1 skipped destionation, for multiple skipped it's better to use multiple lists
    if moviesDestination  is None and tvShowsDestination is not None and eventsDestination is not None:
        cleanTempDirectory(localdir, 'movies')
    if moviesDestination  is not None and tvShowsDestination is None and eventsDestination is not None:
        cleanTempDirectory(localdir, 'tvshows')
    if moviesDestination  is not None and tvShowsDestination is not None and eventsDestination is None:
        cleanTempDirectory(localdir, 'events')

    print('done')

def downloadAndParseLists(type, url, endrange):
    if endrange is None:
        downloadAndParseList(url, type)
    else:
        for i in range(1, endrange):
            downloadAndParseList(url  + str(i), type + '-' + str(i))

def downloadAndParseList( url, filename):
        print('...Starting Download...')
        print(wget.download(url, ('m3u/' + filename + '.m3u')))
        streamClasses.rawStreamList('m3u/' + filename + '.m3u')
        os.remove('m3u/' + filename + '.m3u')

def moveToDestination(localdir, localfolder, destination, uid, gid):
    print('comparing destination ',destination)
    c = filecmp.dircmp(localdir + '/' + localfolder, destination)
    tools.compare_and_update(c, uid, gid)
    cleanTempDirectory(localdir, localfolder)

def cleanTempDirectory(localdir,localfolder):
    print('cleaning up events temp space')       
    shutil.rmtree(localdir + '/' + localfolder + '/')

def parseMultipleLists( type, url, localdir, moviesDestination=None, tvShowsDestination=None, uid=None, gid=None):
    downloadAndParseMultipleLists(type, url)

    if moviesDestination is not None:
        moveToDestination(localdir,'movies',moviesDestination, uid, gid)

    if tvShowsDestination is not None: 
        moveToDestination(localdir,'tvshows',tvShowsDestination, uid, gid)

def downloadAndParseMultipleLists(type, providerfile):
    for i, line in enumerate(providerfile):
        downloadAndParseList(line, type + '-' + str(i))