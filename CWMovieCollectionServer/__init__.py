#!/usr/bin/python

from flask import Flask, Response, request
import jsonpickle
import time

from CWMovieCollectionLoadSaveManager import CWMovieCollectionLoadSaveManager
from CWMovieCollectionParsingManager import CWMovieCollectionParsingManager
from types import NoneType

DEBUG = True

LoadSaveManager = CWMovieCollectionLoadSaveManager()
ParsingManager = CWMovieCollectionParsingManager()

MovieCollection = []

app = Flask(__name__)

@app.route('/<ean>', methods=['GET', 'POST', 'DELETE'])
def parse(ean):
    resp = ''
    if str(ean).isdigit():
        if request.method == 'GET' or request.method == 'DELETE':
            for dvd in MovieCollection:
                if dvd.ean == ean:
                    if request.method == 'GET':
                        if DEBUG == True:
                            print 'GET: ' + ean
                            resp = jsonpickle.encode(dvd)
                            break
                        elif request.method == 'DELETE':
                            if DEBUG == True:
                                print 'DELTE: ' + ean
                                MovieCollection.remove(dvd)
                                break

        elif request.method == 'POST':
            if DEBUG == True:
                print 'POST: ' + ean
            
            dvd = ParsingManager.Parse(ean)
            MovieCollection.append(dvd)
            resp = jsonpickle.encode(dvd)
          
    return resp

@app.route('/moviecollection')
def moviecollection():
    if DEBUG == True:
        print 'GET: moviecollection'

    return jsonpickle.encode(MovieCollection)

@app.route('/savemoviecollection')
def savemoviecollection():
    if DEBUG == True:
        print 'GET: saveMovieCollection'
        
    LoadSaveManager.SaveMovieCollection(MovieCollection)
    return jsonpickle.encode('OK')

if __name__ == '__main__':
    try:
        tmp = LoadSaveManager.LoadMovieCollection()
        
        if tmp != None:
            MovieCollection = tmp 
    
        app.debug = DEBUG
        app.run()

    except:
        if DEBUG == True:
            print 'Exception: Save Movie Collection'
        LoadSaveManager.SaveMovieCollection(MovieCollection)

    finally:
        if DEBUG == True:
            print 'Finnaly: Save Movie Collection'
        LoadSaveManager.SaveMovieCollection(MovieCollection)
        time.sleep(1)
        

