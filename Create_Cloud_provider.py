import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession("1.1.1.1","admin","admin","Global")
def clp_selector (clp_type):
    if clp_type=="VC":
        clp_vcenter_creator("VMware vCenter")
    elif clp_type=="MA":
        clp_Azure_creator("Microsoft Azure")
    elif clp_type=="OS":
        clp_OpenStack_creator("OpenStack")
    elif clp_type=="AWS":
        clp_AWS_creator("AWS EC2")
    elif clp_type=="-hlp" or clp_type=="--help" or clp_type=="-h":
        help_doco()
def help_doco():
    print "AWS for aws Ec2 \n"\
          "VC for VMWare vCenter \n"\
          "OS for OpenStack \n"\
          "MA for Microsoft Azure \n"
    return



def clp_vcenter_creator (clp_type):
    try:
        vCenter = session.CreateResource("Cloud Provider",clp_type,clp_type,"192.168.42.110")
        print "Creating "+clp_type+" cloudProvider"
    except:
        print "There is already cloudprovider named VMWare vCenter"
    set_attributes = []
    User = ""
    password = ""
    dataCenter = api.AttributeNameValue("Default Datacenter","QualiSB")
    dvSwitch = api.AttributeNameValue("Default dvSwitch","dvSwitch")
    holding_network = api.AttributeNameValue("Holding Network","Anetwork")
    vm_cluster = api.AttributeNameValue("VM Cluster","QualiSB Cluster")
    vm_location = api.AttributeNameValue("VM Location","Tor")
    vm_resource_pool=api.AttributeNameValue("VM Resource Pool","LiverPool")
    vm_storage=api.AttributeNameValue("VM Storage","SB-DS2")
    user_name=api.AttributeNameValue("User",User)
    vcenter_password=api.AttributeNameValue("Password",password)
    set_attributes=[dataCenter,dvSwitch,holding_network,vm_cluster,vm_location,vm_resource_pool,vm_storage,user_name,vcenter_password]
    vCenter_attributes = api.ResourceAttributesUpdateRequest(clp_type,set_attributes)
    session.SetAttributesValues(vCenter_attributes)
    session.AutoLoad(clp_type)
    print "vCenter created successfully"
    return

def clp_Azure_creator (clp_type):
    try:
        Azure = session.CreateResource("Cloud Provider", clp_type, clp_type, "None")
        print "Creating " + clp_type + " cloudProvider"
    except:
        print "There is already cloudprovider named Microsoft Azure"
    azure_application_id=api.AttributeNameValue("Azure Application ID","")
    azure_application_key=api.AttributeNameValue("Azure Application Key","")
    azure_subscription_id=api.AttributeNameValue("Azure Subscription ID", "")
    azure_Tenant_ID=api.AttributeNameValue("Azure Tenant ID","")
    management_group_name=api.AttributeNameValue("Management Group Name","TorManagementA")
    vm_size=api.AttributeNameValue("VM Size","Basic_A0")
    region=api.AttributeNameValue("Region","southeastasia")
    network_in_use=api.AttributeNameValue("Networks In Use","10.0.0.0/24")
    set_attributes=[azure_application_id,azure_application_key,azure_subscription_id,azure_Tenant_ID,management_group_name,vm_size,region,network_in_use]
    Azure_attributes=api.ResourceAttributesUpdateRequest(clp_type,set_attributes)
    session.SetAttributesValues(Azure_attributes)
    session.AutoLoad(clp_type)
    print "Azure created successfully"
    return

def clp_OpenStack_creator (clp_type):
    try:
        OpenStack = session.CreateResource("Cloud Provider", clp_type, clp_type, "None")
        print "Creating " + clp_type + " cloudProvider "
    except:
        print "There is already cloudprovider named OpenStack"
    controller_url=api.AttributeNameValue("Controller URL","http://192.168.170.3:5000/v3")
    floating_ip_subnet_id=api.AttributeNameValue("Floating IP Subnet ID","9bce5bca-dba5-4244-86e3-605a438ad17b")
    openstack_domain_name=api.AttributeNameValue("OpenStack Domain Name","default")
    openstack_management_network_id=api.AttributeNameValue("OpenStack Management Network ID","c14241d2-376c-4fb3-8d1e-61f5c1408448")
    user_name=api.AttributeNameValue("User Name","admin")
    password=api.AttributeNameValue("Password","admin")
    vlan_type=api.AttributeNameValue("Vlan Type","VXLAN")
    project_name=api.AttributeNameValue("OpenStack Project Name","admin")
    set_attributes=[project_name,controller_url,floating_ip_subnet_id,openstack_domain_name,openstack_management_network_id,user_name,password,vlan_type]
    openstack_attributes=api.ResourceAttributesUpdateRequest(clp_type,set_attributes)
    session.SetAttributesValues(openstack_attributes)
    session.AutoLoad(clp_type)
    print "OpenStack created successfully"
    return

def clp_AWS_creator(clp_type):
    try:
        AWS= session.CreateResource("Cloud Provider", clp_type, clp_type, "None")
        print "Creating " + clp_type + " cloudProvider"
    except:
        print "There is already cloudprovider named AWS"
    aws_access_key_id=api.AttributeNameValue("AWS Access Key ID","")
    aws_mgmt_sg_id=api.AttributeNameValue("AWS Mgmt SG ID","")
    aws_mgmt_vpc_id=api.AttributeNameValue("AWS Mgmt VPC ID","")
    aws_secret_access_key=api.AttributeNameValue("AWS Secret Access Key","")
    instance_type=api.AttributeNameValue("Instance Type","t2.nano")
    keypairs_location=api.AttributeNameValue("Keypairs Location","")
    max_storage_iops=api.AttributeNameValue("Max Storage IOPS","1500")
    max_storage_size=api.AttributeNameValue("Max Storage Size","30")
    networks_in_use=api.AttributeNameValue("Networks In Use","10.0.0.0/24")
    region=api.AttributeNameValue("Region","us-east-1")
    set_attributes=[aws_access_key_id,aws_mgmt_sg_id,aws_mgmt_vpc_id,aws_secret_access_key,instance_type,keypairs_location,max_storage_iops,max_storage_size,networks_in_use,region]
    aws_attributes=api.ResourceAttributesUpdateRequest(clp_type,set_attributes)
    session.SetAttributesValues(aws_attributes)
    session.AutoLoad(clp_type)
    print "AWS EC2 created successfully"
    return


#clp_selector(sys.argv[1])