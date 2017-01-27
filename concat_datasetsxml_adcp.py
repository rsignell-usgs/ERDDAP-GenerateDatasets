#!/usr/bin/env python

import os,sys,fnmatch
import xml.etree.ElementTree as etree
import glob


idir='/home/om/cron/pioneer/data/ADCP/'
maskfile_rec='datasets_mask_ADCP_REC.xml'
maskfile_tel='datasets_mask_ADCP_TEL.xml'
infile='datasets_WFP_MOAS.xml'
outfile='dataset_WFP_MOAS_adcp.xml'

def main(argv):
    print 'APPENDING'
    tree=etree.parse(infile)
    dxml=tree.getroot()
    
    #RECOVERED
    files=glob.glob(idir+'PIONEER_ADCP_RECOVERED_*.nc')    
    for file in files:
        print file
        parts=file.split('/')
        filename=parts[-1:]
        print filename[0]
        parts2=filename[0].split('.')
        Did=parts2[0]
        print Did
        newelement=etree.parse(maskfile_rec).getroot()
        newelement.find('fileNameRegex').text=filename[0]
        newelement.set('datasetID',Did)
        dxml.append(newelement)   
#    
#        


    #TELEMETERED
    files=glob.glob(idir+'PIONEER_ADCP_TELEMETERED_*.nc')    
    for file in files:
        print file
        parts=file.split('/')
        filename=parts[-1:]
        print filename[0]
        parts2=filename[0].split('.')
        Did=parts2[0]
        print Did
        newelement=etree.parse(maskfile_tel).getroot()
        newelement.find('fileNameRegex').text=filename[0]
        newelement.set('datasetID',Did)
        dxml.append(newelement)   
#    
    
    
    tree.write(outfile, encoding="ISO-8859-1", xml_declaration=True)
        
    

#       
#       
    
#    try:
#        response=urllib2.urlopen(allurls[0])
#   except urllib2.URLError,e:
#       print "Error accessing site:",e
#   
#    print response.read()
#        
if __name__ == "__main__":
   # parser = optparse.OptionParser()
   # parser.add_option('-t', '--type',dest='type',help='MOAS,WFP,SPP,BPRESS',default='MOAS',type='str')
   # parser.add_option('-s', '--state',dest='state',help='REC,TEL',default='REC',type='str')
   # (opts, args) = parser.parse_args()
    
    
    print 'RUNNING'
    main(sys.argv)
