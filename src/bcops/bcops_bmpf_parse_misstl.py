
from lxml import etree
from datetime import datetime

def parse_mission_timeline_swath_cycle(file_misstl: str, logger, debug = False):
    
    if debug == True and logger is not None:
       logger.info(f'Parsing {file_misstl}')

    xml_file    = None
    xml_root    = None

    try:
        xml_file = etree.parse(file_misstl)
        xml_root = xml_file.getroot() 
    except:
        logger.error(f'Error parsing {file_misstl}')
        raise(f'Error parsing {file_misstl}')
    
    path                = '/Earth_Explorer_File/Data_Block/List_of_Global_Coverages/Global_Coverage/List_of_Major_Cycles/Major_Cycle'
    list_major_cycle    = xml_root.xpath(path)

    if debug == True and logger is not None:
        logger.info(f'Found {len(list_major_cycle)} major cycles')
        for major_cycle in list_major_cycle:
            logger.debug(major_cycle.tag)
            logger.debug(major_cycle.attrib)
            logger.debug(major_cycle.attrib['id'])

    path            = '/Earth_Explorer_File/Data_Block/List_of_Global_Coverages/Global_Coverage/List_of_Major_Cycles/Major_Cycle/List_of_Swaths/Swath'
    list_xml_swath  = xml_root.xpath(path)
    date_format     = 'UTC=%Y-%m-%dT%H:%M:%S'
    list_swath      = []

    for xml_swath in list_xml_swath:
        swath               = {}
        swath_start         = datetime.strptime(xml_swath.xpath('Start_Time')[0].text, date_format)
        swath_stop          = datetime.strptime(xml_swath.xpath('Stop_Time')[0].text, date_format)
        swath['id']         = xml_swath.attrib['id']
        swath['Start_Time'] = swath_start
        swath['Stop_Time']  = swath_stop
        if debug == True and logger is not None:
            logger.debug(swath['id'])
            logger.debug(swath_start)
            logger.debug(swath_stop)
        list_swath.append(swath)

    return list_swath