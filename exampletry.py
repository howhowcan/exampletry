#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        host = self.addHost('h1')
        self.addLink(host,switch,bw = 10,delay = '5ms',loss = 0)

        host = self.addHost('h2')
        self.addLink(host,switch,bw = 10,delay = '5ms',loss = 0)



'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = SingleSwitchTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    # Stop a network
    net.stop()

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()