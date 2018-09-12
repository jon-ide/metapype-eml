#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: names

:Synopsis:

:Author:
    servilla

:Created:
    6/18/18
"""
import daiquiri


logger = daiquiri.getLogger('names: ' + __name__)

# Named constants for EML 2.1.1 metadata element names
ABSTRACT = 'abstract'
ACCESS = 'access'
ADDITIONALINFO = 'additionalInfo'
ADDITIONALMETADATA = 'additionalMetadata'
ADDRESS = 'address'
ADMINISTRATIVEAREA = 'administrativeArea'
ALLOW = 'allow'
ALTERNATEIDENTIFIER = 'alternateIdentifier'
ASSOCIATEDPARTY = 'associatedParty'
ATTRIBUTELIST = 'attributeList'
ATTRIBUTEORIENTATION = 'attributeOrientation'
AUTHENTICATION = 'authentication'
BANDGAPBYTES = 'bandgapbytes'
BANDROWBYTES = 'bandrowbytes'
BEGINDATE = 'beginDate'
BINARYRASTERFORMAT = 'binaryRasterFormat'
BOUNDINGCOORDINATES = 'boundingCoordinates'
BYTEORDER = 'byteorder'
CALENDARDATE = 'calendarDate'
CHARACTERENCODING = 'characterEncoding'
CITATION = 'citation'
CITY = 'city'
COLLAPSEDELIMITERS = 'collapseDelimiters'
COMMONNAME = 'commonName'
COMPLEX = 'complex'
COMPRESSIONMETHOD = 'compressionMethod'
CONNECTION = 'connection'
CONTACT = 'contact'
COVERAGE = 'coverage'
COUNTRY = 'country'
CREATOR = 'creator'
DATAFORMAT = 'dataFormat'
DATASET = 'dataset'
DATATABLE = 'dataTable'
DELIVERYPOINT = 'deliveryPoint'
DENY = 'deny'
DISTRIBUTION = 'distribution'
EASTBOUNDINGCOORDINATE = 'eastBoundingCoordinate'
ELECTRONICMAILADDRESS = 'electronicMailAddress'
EXTERNALLYDEFINEDFORMAT = 'externallyDefinedFormat'
EML = 'eml'
ENCODINGMETHOD = 'encodingMethod'
ENDDATE = 'endDate'
ENTITYDESCRIPTION = 'entityDescription'
ENTITYNAME = 'entityName'
FIELDDELIMITER = 'fieldDelimiter'
FIELDSTARTCOLUMN = 'fieldStartColumn'
FIELDWIDTH = 'fieldWidth'
FORMATNAME = 'formatName'
FORMATVERSION = 'formatVersion'
GIVENNAME = 'givenName'
GENERALTAXONOMICCOVERAGE = 'generalTaxonomicCoverage'
GEOGRAPHICCOVERAGE = 'geographicCoverage'
GEOGRAPHICDESCRIPTION = 'geographicDescription'
INDIVIDUALNAME = 'individualName'
INLINE = 'inline'
KEYWORD = 'keyword'
KEYWORDSET = 'keywordSet'
KEYWORDTHESAURUS = 'keywordThesaurus'
LAYOUT = 'layout'
LINENUMBER = 'lineNumber'
LITERALCHARACTER = 'literalCharacter'
MAXRECORDLENGTH = 'maxRecordLength'
MEDIUMNAME = 'mediumName'
MEDIUMDENSITY = 'mediumDensity'
MEDIUMDENSITYUNITS = 'mediumDensityUnits'
MEDIUMVOLUME = 'mediumVolume'
MEDIUMFORMAT = 'mediumFormat'
MEDIUMNOTE = 'mediumNote'
METADATA = 'metadata'
METADATAPROVIDER = 'metadataProvider'
METHODS = 'methods'
METHODSTEP = 'methodStep'
MULTIBAND = 'multiBand'
NBANDS = 'nbands'
NBITS = 'nbits'
NORTHBOUNDINGCOORDINATE = 'northBoundingCoordinate'
NUMFOOTERLINES = 'numFooterLines'
NUMHEADERLINES = 'numHeaderLines'
NUMPHYSICALLINESPERRECORD = 'numPhysicalLinesPerRecord'
OBJECTNAME = 'objectName'
OFFLINE = 'offline'
ONLINE = 'online'
ONLINEDESCRIPTION = 'onlineDescription'
ONLINEURL = 'onlineUrl'
ORGANIZATIONNAME = 'organizationName'
PERMISSION = 'permission'
PHONE = 'phone'
PHYSICAL = 'physical'
PHYSICALLINEDELIMITER = 'physicalLineDelimiter'
POSITIONNAME = 'positionName'
POSTALCODE = 'postalCode'
PRINCIPAL = 'principal'
PUBDATE = 'pubDate'
QUALITYCONTROL = 'qualityControl'
QUOTECHARACTER = 'quoteCharacter'
RANGEOFDATES = 'rangeOfDates'
ROWCOLUMNORIENTATION = 'rowColumnOrientation'
RECORDDELIMITER = 'recordDelimiter'
SALUTATION = 'salutation'
SAMPLING = 'sampling'
SIMPLEDELIMITED = 'simpleDelimited'
SINGLEDATETIME = 'singleDateTime'
SIZE = 'size'
SKIPBYTES = 'skipbytes'
SOUTHBOUNDINGCOORDINATE = 'southBoundingCoordinate'
SURNAME = 'surName'
TAXONOMICCLASSIFICATION = 'taxonomicClassification'
TAXONOMICCOVERAGE = 'taxonomicCoverage'
TAXONRANKNAME = 'taxonRankName'
TAXONRANKVALUE = 'taxonRankValue'
TEXTDELIMITED = 'textDelimited'
TEXTFIXED = 'textFixed'
TEXTFORMAT = 'textFormat'
TEMPORALCOVERAGE = 'temporalCoverage'
TITLE = 'title'
TOTALROWBYTES = 'totalrowbytes'
URL = 'url'
USERID = 'userId'
VALUE = 'value'
WESTBOUNDINGCOORDINATE = 'westBoundingCoordinate'
