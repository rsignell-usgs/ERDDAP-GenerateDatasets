#!/usr/bin/env python
#
import os,sys,fnmatch
import xml.etree.ElementTree as etree
import glob


#idir='/home/hunter/Projects/ooi/work/data/MOAS/concat/'
idir='/home/om/cron/pioneer/data/CTD_PROFILER/latest/'
maskfile_WFP='datasets_mask_WFP.xml'
maskfile_SPP='datasets_mask_SPP.xml'
infile='datasets_skel.xml'
outfile='datasets_PROFILER.xml'

def main(argv):
    print 'APPENDING'
    tree=etree.parse(infile)
    dxml=tree.getroot()
    files=glob.glob(idir+'*latest.nc')    
    
    for file in files:
        print file
        parts=file.split('/')
        filename=parts[-1:]
        print filename[0]
        parts2=filename[0].split('.')
        Did=parts2[0]
        print Did
        parts3=filename[0].split('_')
     #   FPARTS=parts3[0]
     #   print FPARTS
        
        if parts3[0]=='CP01CNSP':
            maskfile=maskfile_SPP
        elif parts3[0]=='CP03ISSP':
            maskfile=maskfile_SPP
        else:
            maskfile=maskfile_WFP
       
        newelement=etree.parse(maskfile).getroot()
        newelement.find('fileNameRegex').text=filename[0]
        newelement.set('datasetID',Did)
        for node in newelement.find('addAttributes').findall('att'):
           if node.attrib['name']=='sourceUrl':
                node.text=file
                
           if node.attrib['name']=='title':
                node.text='Coastal Pioneer array CTD profiler - '+parts3[0]+','+parts3[1] 
#        
#                
        for node in newelement.findall('dataVariable'):
            sName=node.find('sourceName')
            dName=node.find('destinationName')
            print sName.text
            if sName.text=='sci_seawater_density':
                dName.text='density'
            elif  sName.text=='sci_water_pressure_dbar':
                dName.text='pressure'
                attname=node.find('addAttributes')
                
##			<att name="scale_factor" type="int">-1</att>
#                b=etree.SubElement(attname,'att')
#                b.text='-1'      
#                b.attrib['name']='scale_factor'
#                b.attrib['type']='float'
#                
#                
#                
#            elif  sName.text=='sci_water_temp':
#                dName.text='temperature'
#            elif  sName.text=='sci_water_pracsal':
#                dName.text='salinity'
#      
#        
#        
        dxml.append(newelement)   
#    
#        
#    for node in dxml.findall('dataset'):
#        
#        if  node.attrib['datasetID'].find('deploy')==0 or node.attrib['datasetID'].find('pioneer')==0:
##          
##            
##        
#            b=etree.SubElement(node,'defaultGraphQuery')
#            b.text='time,pressure,temperature&.marker=4|5'
##        
#    #b[0]='TEST'
##    <fileNameRegex>NONE</fileNameRegex>
##    <att name="sourceUrl">NONE</att>
#
#    
#    
    tree.write(outfile, encoding="ISO-8859-1", xml_declaration=True)
#        
    

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
