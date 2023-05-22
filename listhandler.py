import tools
import streamClasses
import wget
import os
import shutil
import filecmp

def parseIPTVLists( type, url, localdir, moviesDestination=None, tvShowsDestination=None, eventsDestination=None, endrange=None):
    downloadAndParseLists(type, url, endrange)

    if moviesDestination is not None:
        moveToDestination(localdir,'movies',moviesDestination)

    if tvShowsDestination is not None: 
        moveToDestination(localdir,'tvshows',tvShowsDestination)

    if eventsDestination is not None:   
        moveToDestination(localdir,'events',eventsDestination)

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

def moveToDestination(localdir, localfolder, destination):
    print('comparing destination ',destination)
    c = filecmp.dircmp(localdir + '/' + localfolder, destination)
    tools.compare_and_update(c)
    print('cleaning up events temp space')       
    shutil.rmtree(localdir + '/' + localfolder + '/')
