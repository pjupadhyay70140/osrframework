
import json
import sys

import osrframework.entify.processing as entify
import osrframework.maltfy.lib.constants as constants
from osrframework.maltfy.lib.maltego import *
import osrframework.thirdparties.blockchain_info.getBitcoinAddressDetails as blockchain

def textToI3visioEntities(argv):
    ''' 
        Method that obtains all the entities in a given i3visio.object that contains an i3visio.text property.

        :param argv:    the serialized entity.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform()
    #me.parseArguments(argv);
    #data = sys.argv[1]

    # Trying to recover all the possible i3visio entities
    found_fields = {}

    #data = me.getVar("i3visio.text")
    data = sys.argv[1]
    entities = entify.getEntitiesByRegexp(data=data)    
    # This returns a dictionary like the following:
    """
        [{
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'a9b8c5d848205db514d4097d2b78f4528d01a79f39601e0f9c5c40ed689471'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'b28b896e6eeb8d651cacd5f4a4d1490fbe9d05dbc92221609350b0ce7a68e9'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': 'd727fed4d969b14b28165c75ad12d7dddd56c0198fa70cedc3fdad7ac395b2'
        }, {
        'attributes': [],
        'type': 'i3visio.sha256',
        'value': '3e9a2204fcfc6f7dde250e61ca35353411880024102cba14a0bd45f05f1e74'
        }]
    """

    #print json.dumps(entities, indent=2)
    for elem in entities:
        newEnt = me.addEntity(elem["type"],elem["value"])
        newEnt.setDisplayInformation("<h3>" + elem["value"] +"</h3><p>"+str(elem["attributes"])+"</p>")        
        for extraAtt in elem["attributes"]:
            newEnt.addAdditionalFields(str(extraAtt['type']), str(extraAtt['type']), True, str(extraAtt['value']))    

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    textToI3visioEntities(sys.argv)

