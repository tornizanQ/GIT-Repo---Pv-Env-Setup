import Create_Cloud_provider as clp_creator
from optparse import OptionParser
import sys

def main():

    parser = OptionParser(usage="usage: %prog [options] filename",version="%prog 1.0")
    parser.add_option("-c", "--create",
                      action="store",  # optional because action defaults to "store"
                      dest="action",
                      default="create",
                      help="Choose the action you would like to do: Create, Delete, Autoload", )
    parser.add_option("-z", "--cloudprovider",
                      action="store",  # optional because action defaults to "store"
                      dest="clp",
                      default="None",
                      help="Choose the cloud providers testing:\nVC - vCenter\nOS - OpenStack\nMA - Microsoft Azure\nAWS - AWS EC2", )
    parser.add_option("-b", "--bridgeconstructor",
                      action="bridger",  # optional because action defaults to "store"
                      dest="construct_bridges",
                      default="0",
                      help="Choose the cloud providers testing:\nVC - vCenter\nOS - OpenStack\nMA - Microsoft Azure\nAWS - A",)
    (options, args) = parser.parse_args()

    if options.action=="create":
        if options.clp!="None":
            clp_creator.clp_selector(options.clp)
        else:
            if options.construct_bridges!=0:
                print "under construction"



    return



if __name__ == '__main__':
    main()