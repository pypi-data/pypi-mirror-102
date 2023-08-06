'''
Created on 2021-04-06

@author: wf
'''
from lodstorage.jsonable import JSONAble,JSONAbleList
from datetime import datetime
from wikibot.wikiuser import WikiUser
from wikibot.wikiclient import WikiClient
from wikibot.wikipush import WikiPush
from pathlib import Path
import os
import time

from ormigrate.issue41 import AcronymLengthFixer
from ormigrate.painscale import PainScale


class OREntityList(JSONAbleList):
    '''
    wrapper for JSONAble
    '''
    def __init__(self,listName:str=None,clazz=None,tableName:str=None):
        super(OREntityList, self).__init__(listName,clazz,tableName)
        self.profile=False
        self.debug=False
        self.wikiClient=None
        self.wikiPush=None
        self.askExtra=""
        
    def getList(self):
        return self.__dict__[self.listName]
    
    def getLookup(self,attrName:str,withDuplicates:bool=False):
        '''
        create a lookup dictionary by the given attribute name
        
        Args:
            attrName(str): the attribute to lookup
            withDuplicates(bool): whether to retain single values or lists
        
        Return:
            a dictionary for lookup
        '''
        lookup={}
        duplicates=[]
        for entity in self.getList():
            if hasattr(entity, attrName):
                value=getattr(entity,attrName)
                if value in lookup:
                    if withDuplicates:
                        lookupResult=lookup[value]
                    else:
                        duplicates.append(entity)
                else:
                    if withDuplicates:
                        lookupResult=[entity]
                    else:
                        lookupResult=entity
                lookup[value]=lookupResult  
        if withDuplicates:
            return lookup  
        else:
            return lookup,duplicates
    
    def getEntityName(self):
        '''
        get my entity name
        '''
        return self.clazz.__name__
    
    def getAskQuery(self,askExtra="",propertyLookupList=None):
        '''
        get the query that will ask for all my events
        
        Args:
           askExtra(str): any additional SMW ask query constraints
           propertyLookupList:  a list of dicts for propertyLookup
           
        Return:
            str: the SMW ask query
        '''
        entityName=self.getEntityName()
        selector="IsA::%s" % entityName
        ask="""{{#ask:[[%s]]%s
|mainlabel=pageTitle
|?_CDAT=creationDate
|?_MDAT=modificationDate
|?_LEDT=lastEditor
""" % (selector,askExtra)
        if propertyLookupList is None:
            propertyLookupList=self.propertyLookupList
        for propertyLookup in propertyLookupList:
            propName=propertyLookup['prop']
            name=propertyLookup['name']
            ask+="|?%s=%s\n" % (propName,name)
        ask+="}}"
        return ask
    
    @staticmethod        
    def getCachePath():
        home = str(Path.home())
        cachedir="%s/.or/" %home
        return cachedir
    
    @classmethod
    def getResourcePath(cls):
        path = os.path.dirname(__file__) + "/../ormigrate/resources"
        return path
    
    def getJsonFile(self):
        '''
        get the json File for me
        '''
        cachePath=OREntityList.getCachePath()
        os.makedirs(cachePath,exist_ok=True)
        jsonPrefix="%s/%s" % (cachePath,self.getEntityName())
        jsonFilePath="%s.json" % jsonPrefix
        return jsonFilePath
    
    def fromCache(self,wikiuser:WikiUser):
        '''
        Args:
            wikiuser: the wikiuser to use 
        '''
        jsonFilePath=self.getJsonFile()
        # TODO: fix upstream pyLodStorage
        jsonPrefix=jsonFilePath.replace(".json","")
        if os.path.isfile(jsonFilePath):
            self.restoreFromJsonFile(jsonPrefix)
        else:
            self.fromWiki(wikiuser,askExtra=self.askExtra,profile=self.profile)
            self.storeToJsonFile(jsonPrefix)
            
    def fromWiki(self,wikiuser:WikiUser,askExtra="",profile=False):
        '''
        read me from a wiki using the givne WikiUser configuration
        '''
        if self.wikiClient is None:
            self.wikiclient=WikiClient.ofWikiUser(wikiuser)
            self.wikiPush = WikiPush(fromWikiId=wikiuser.wikiId)
        askQuery=self.getAskQuery(askExtra)
        if self.debug:
            print(askQuery)
        startTime=time.time()
        entityName=self.getEntityName()
        records = self.wikiPush.formatQueryResult(askQuery, self.wikiClient, entityName=entityName)
        elapsed=time.time()-startTime
        if profile:
            print("query of %d %s records took %5.1f s" % (len(records),entityName,elapsed))
        self.fromLoD(records)
        return records
    
    def fromSQLTable(self,sqlDB,entityInfo):
        lod=sqlDB.queryAll(entityInfo)
        self.fromLoD(lod)
        
    def fromLoD(self,lod): 
        '''
        create me from the given list of dicts
        '''
        errors=[] 
        entityList=self.getList()  
        for record in lod:
            # call the constructor to get a new instance
            try:
                entity=self.clazz()
                if hasattr(entity,"fixRecord"):
                    fixRecord=getattr(entity,'fixRecord');
                    if callable(fixRecord):
                        fixRecord(record)
                entity.fromDict(record)
                entityList.append(entity)
            except Exception as ex:
                error={
                    self.getEntityName():record,
                    "error": ex
                }
                errors.append(error)
                if self.debug:
                    print(error)
        return errors
    
    def getRatedLod(self,ratingCallback=None):
        '''
        get the list of dicts with a potential rating
        
        Args:
            ratingCallback(func): a function to be called for rating of this entity
        '''
        lod=[]
        for entity in self.getList():
            eventRecord={'pageTitle':entity.pageTitle}
            for propertyLookup in self.propertyLookupList:
                name=propertyLookup['name']
                if hasattr(entity,name):
                    eventRecord[name]=getattr(entity,name)
            if ratingCallback is not None:
                ratingCallback(entity,eventRecord)    
            lod.append(eventRecord)
        return lod
        
class EventSeriesList(OREntityList):
    '''
    i represent a list of EventSeries
    '''
    def __init__(self):
        self.eventSeries=[]
        super(EventSeriesList, self).__init__("eventSeries",EventSeries)
        self.propertyLookupList=[
            { 'prop':'EventSeries acronym', 'name': 'acronym'},
            { 'prop':'Homepage',   'name': 'homepage'},
            { 'prop':'Title',      'name': 'title'},
            #{ 'prop':'Field',      'name': 'subject'},
            { 'prop':'Wikidataid',  'name': 'wikiDataId'},
            { 'prop':'DblpSeries',  'name': 'dblpSeries' }
        ]
        
class EventSeries(JSONAble):
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    @classmethod
    def getSamples(self):
        '''
        Returns a sample LOD of an event Series
        '''
        samplesLOD= [{
            'pageTitle': 'AAAI',
            'acronym' : 'AAAI',
            'Title' : 'Conference on Artificial Intelligence',
            'Field' : 'Artificial Intelligence',
            'Homepage' : 'www.aaai.org/Conferences/AAAI/aaai.php',
            'WikiDataId' : 'Q56682083',
            'DblpSeries' : 'aaai'
        }]
        return samplesLOD

    @classmethod
    def getSampleWikiSon(cls, mode='legacy'):
        '''
        Returns a sample of Event Series in wikison format
        Args:
            mode(str): Default legacy, used to provide the mode dependant on updates and changes to structure of Event series
        '''
        if mode == 'legacy':
            samplesWikiSon = ["""{{Event series
|Acronym=AAAI
|Title=Conference on Artificial Intelligence
|Logo=Aaai-logo.jpg
|has CORE2017 Rank=A*
|Field=Artificial intelligence
|Period=1
|Unit=year
|Homepage=www.aaai.org/Conferences/AAAI/aaai.php
|WikiDataId=Q56682083
|has CORE2018 Rank=A*
|has Bibliography=dblp.uni-trier.de/db/conf/aaai/
|has CORE2014 Rank=A*
|DblpSeries=aaai
}}"""]
        else:
            samplesWikiSon = "..."

        return samplesWikiSon
    
    def __str__(self):
        text=self.pageTitle
        if hasattr(self, "acronym"):
            text+="(%s)" %self.acronym
        return text

class EventList(OREntityList):
    '''
    i represent a list of Events
    '''
    def __init__(self):
        self.events=[]
        super(EventList, self).__init__("events",Event)
        self.propertyLookupList=[
            { 'prop':'Acronym',             'name': 'acronym'},
            { 'prop':'Ordinal',             'name': 'ordinal'},
            { 'prop':'Homepage',            'name': 'homepage'},
            { 'prop':'Title',               'name': 'title'},
            { 'prop':'Event type',          'name': 'eventType'},
            { 'prop':'Start date',          'name': 'startDate'},
            { 'prop':'End date',            'name': 'endDate'},
            { 'prop':'Event in series',     'name': 'inEventSeries'},
            { 'prop':'Has_location_country','name': 'country'},
            { 'prop':'Has_location_state',  'name': 'region'},
            { 'prop':'Has_location_city',   'name': 'city'},
            { 'prop':'Accepted_papers',     'name': 'acceptedPapers'},
            { 'prop':'Submitted_papers',    'name': 'submittedPapers'}
        ]               
    
class Event(JSONAble):
    '''
    I represent an Event
    
    see https://rq.bitplan.com/index.php/Event
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    @classmethod
    def getSamples(cls):
        samplesLOD=[{
            "pageTitle": "ICSME 2020",
            "acronym":"ICSME 2020",
            "ordinal": 36,
            "evenType": "Conference",
            "subject": "Software engineering",
            "startDate":  datetime.fromisoformat("2020-09-27"),
            "endDate":  datetime.fromisoformat("2020-09-27")
        },
        {
            "pageTitle": "WebSci 2019",
            "acronym": "WebSci 2019",
            "ordinal": 10,
            "homepage": "http://websci19.webscience.org/",
            "title": "10th ACM Conference on Web Science",
            "eventType": "Conference",
            "startDate": datetime.fromisoformat("2019-06-30"),
            "endDate": datetime.fromisoformat("2019-07-03"),
            "inEventSeries": "WebSci",
            "country": "USA",
            "region": "US-MA",
            "city": "Boston",
            "acceptedPapers": 41,
            "submittedPapers": 120
        }
        ]
        return samplesLOD
    
    @classmethod
    def getSampleWikiSon(cls,mode='legacy'):
        if mode=='legacy':
            samplesWikiSon=["""{{Event
|Acronym=ICSME 2020
|Title=36th IEEE International Conference on Software Maintenance and Evolution
|Series=ICSME
|Ordinal=36th
|Type=Conference
|Field=Software engineering
|Start date=27th Sept, 2020
|End date=2020/10/03
|Homepage=https://icsme2020.github.io/
|City=Adelaide
|State=Online
|Country=Australia
|Abstract deadline=2020/05/22
|Paper deadline=28th May, 2020
|Notification=2020/08/04
|Camera ready=2020/08/25
|Has host organization=Institute of Electrical and Electronics Engineers
|Has coordinator=Sebastian Baltes
|has general chair=Christoph Treude, Hongyu Zhang
|has program chair=Kelly Blincoe, Zhenchang Xing
|has demo chair=Mario Linares Vasquez, Hailong Sun
}}""","""{{Event
|Acronym=AISB 2009
|Title=AISB Symposium: New Frontiers in Human-Robot Interaction
|Type=Conference
|Field=Uncategorized
|Start date=2009/04/08
|End date=2009/04/09
|Submission deadline=2009/01/05
|Homepage=homepages.feis.herts.ac.uk/~comqkd/HRI-AISB2009-Symposium.html
|City=Edinburgh
|Country=United Kingdom
|Notification=2009/02/02
|Camera ready=2009/02/23
}}	
This CfP was obtained from [http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=3845&amp;copyownerid=2048 WikiCFP]
"""]
        else:
            samplesWikiSon="..."
        
        return samplesWikiSon
    
    def fixRecord(self,record):
        '''
        fix my dict representation
        '''
        invalidKeys=[]
        for key in record.keys():
            value=record[key]
            if type(value)==list:
                # TODO: handle properly e.g. by marking and converting list to 
                # comma separated list
                invalidKeys.append(key)
                print ("invalid list %s=%s in %s"  % (key,record[key],record ))
            if value is None:
                invalidKeys.append(key)
                
        for key in invalidKeys:
            record.pop(key)
            
    @classmethod       
    def rateMigration(cls,event,eventRecord):
        rating = AcronymLengthFixer.getRating(eventRecord)
        eventRecord['acronym length'] = PainScale.lookupPainImage(rating)
        pass
    
    def __str__(self):
        text=self.pageTitle
        if hasattr(self, "acronym"):
            text+="(%s)" %self.acronym
        return text
    
class CountryList(OREntityList):
    '''
    a list of countries
    '''
    def __init__(self):
        self.countries=[]
        super(CountryList, self).__init__("countries",Country)
        
        self.propertyLookupList=[
            { 'prop':'Country name',    'name': 'name'},
            { 'prop':'Country wikidatid', 'name': 'wikidataId'}
        ]       
        
    def getDefault(self):
        jsonFilePrefix="%s/countries" % CountryList.getResourcePath()
        self.restoreFromJsonFile(jsonFilePrefix)

    @classmethod
    def getPluralname(cls):
        return "Countries" 
    
class Country(JSONAble):
    '''
    distinct region in geography; a broad term that can include political divisions or 
    regions associated with distinct political characteristics 
    '''
    
    @classmethod
    def getSamples(cls):
        '''
        get my samples
        TODO:
           remove countryPrefix and change country attribute to "name"
        '''
        samplesLOD=[
    {
      "name" : "USA",
      "wikidataName" : "United States of America",
      "wikidataId" : "Q30"
    },
    {
      "name" : "China",
      "wikidataName" : "People's Republic of China",
      "wikidataId" : "Q148"
    },
    {
      "name" : "Germany",
      "wikidataName" : "Germany",
      "wikidataId" : "Q183"
    },
    {
      "name" : "Italy",
      "wikidataName" : "Italy",
      "wikidataId" : "Q38"
    },
    {
      "name" : "France",
      "wikidataName" : "France",
      "wikidataId" : "Q142"
    }
    ]
        return samplesLOD
    
    def __str__(self):
        text=self.name
        return text
    