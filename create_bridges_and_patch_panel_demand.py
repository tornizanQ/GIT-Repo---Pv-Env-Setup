import cloudshell.api.cloudshell_api as api
session = api.CloudShellAPISession("1.1.1.1","admin","admin","Global")
def construct_params(x,z,p):
#x is the number of bridges
x=10
#y is the number of ports for each bridge
z=10
#p if set to true all the ports will be connected to a patch panels the number of patch panels
p=True
def construct_bridges(number_of_bridges,number_of_ports,patch_panel_requiered):
    PP_port_counter=0
    port_mapping_list = []
    if p==True:
        try:
            temp_pp= session.CreateResource("PatchPanel","Generic PatchPanel","Patch Panel","1.1.1.1")
        except:
            temp_pp=session.GetResourceDetails("Patch Panel")
            print "failed1 - pp backup is used"

    for i in range(x):
        try:
            temp_bridge=session.CreateResource("Bridge","Bridge Generic Model","Br"+str(i),"1.1.1.1")
        except:
            print "failed2"

        for y in range(z):
            try:
                temp_pp_port = session.CreateResource("Panel Jack","Generic Jack","P"+str(PP_port_counter),"1.1.1.1","","Patch Panel")
            except:
                print "failed3"
            PP_port_counter += 1
            try:
                temp_port=session.CreateResource("Bridge Port","Bridge Port Generic Model","P"+str(y),"1.1.1.1","","Br"+str(i))
            except:
                print "failed4"
            port_mapping_list.append(api.PhysicalConnectionUpdateRequest(temp_pp_port.Name,temp_port.Name,""))
    session.UpdatePhysicalConnections(port_mapping_list)
    print"success"




