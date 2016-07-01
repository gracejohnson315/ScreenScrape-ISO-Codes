# ----------------------------------------------------------------------------
# SCREEN SCRAPE ISO CODES
# Author: Grace Johnson
# Description: Screen Scrape ISO codes using Regular Expressions. The source
# website will not allow for direct screen scraping. If you would like to test
# this script, you must first copy the source html text from
# http://dev.maxmind.com/geoip/legacy/codes/iso3166/ and paste it into a text
# file (named web_text in the script below). 
# ----------------------------------------------------------------------------

import re
import csv

## Input Variables -----------------------------------------------------------
web_text = open(r'/Users/gj92/Desktop/GIS_Programming/Project/Data/web_text.txt', 'r')
text = web_text.read()
regex_pattern = r'([a-zA-Z]*|[a-zA-Z]*[0-9]*)(,&quot;)([a-zA-Z\s]*)(&quot;)'
codes_dict = {}


## Functions -----------------------------------------------------------------
def ScreenScrape_ISO(inPattern, inText, inDict):
    '''This function uses regular expressions to extract ISO codes from a text input'''
    '''Extracted ISO codes and associated country names are stored in a dictionary'''
    '''ISO codes are keys and country names are the values of the dictionary'''
    '''Text was extracted from http://dev.maxmind.com/geoip/legacy/codes/iso3166/'''
    for match in re.findall(inPattern, inText):        
        iso = match[0]
        country = match[2]
        inDict[iso] = country
    print "%s ISO country codes were found in this text" %(len(inDict))


def WriteDictToCSV(output_file, inDict):
    '''This function writes an input dictionary of ISO codes to a csv file'''
    with open(output_file, 'w') as outfile:
        writer = csv.writer(outfile, delimiter = ',')
        writer.writerow(['ISO code', 'Country'])
        writer.writerows(inDict.items())
    print "Your file has been created"


## Calling Functions ------------------------------------------------------------
ScreenScrape_ISO(regex_pattern, text, codes_dict)
WriteDictToCSV(r'/Users/gj92/Desktop/GIS_Programming/Project/ISO_CODES.csv', codes_dict)





