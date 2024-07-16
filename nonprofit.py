import re
import os
import random
from lxml import etree

datadir = "/stat129/all990files/"

all990 = [datadir + p for p in os.listdir(datadir)]
# Has 2.3 million files

def extract(xmlfile):
    """
    Extract a dictionary containing the elements of interest
    """
    tree = etree.parse(xmlfile)
    fields990 = ["ActivityOrMissionDesc", "MissionDesc", "TotalEmployeeCnt", "TotalAssetsEOYAmt", "TotalContributionsAmt", "CYTotalRevenueAmt"]

    # Hold all the results
    result = {}
    for f in fields990:
        # Won't always be there
        try:
            result[f] = tree.xpath("/Return/ReturnData/IRS990/" + f + "/text()")[0]
        except:
            # xpath fails for some reason, so just give up!
            # A better way to handle this is to actually *look* 
            # at this XML file, which may have a different structure.
    
            return None
        
    #extracts the file return date
    
    try:
        result["returnDateStamp"] = tree.xpath("/Return/ReturnHeader/ReturnTs/text()")[0]
    except:
        return None
   
    #extract the EIN for the business
    try:
        result["EIN"] = tree.xpath("/Return/ReturnHeader/Filer/EIN/text()")[0]
    except:
        return None
    
    #exctacts the company name
    try:
        result["BusinessName"] = tree.xpath("/Return/ReturnHeader/Filer/BusinessName/BusinessNameLine1Txt/text()")[0]
    except:
        return None
    
    #regular expression to filter out nonprofits for education
    pattern = r'\beducation\b'
    value = 'ActivityOrMissionDesc'

    if value in result and re.search(pattern, result[value], flags=re.IGNORECASE) is None:
            return None
            
        

    return result

from multiprocessing import Pool

# 10 parallel workers
with Pool(10) as p:
    # Parallel map
    r = p.map(extract, all990)
    
    #filters out the None in Results
    output = list(filter(None,r))
    