#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
    def build(self):
        

        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
        switch7 = self.addSwitch('s7')
        switch8 = self.addSwitch('s8')
        switch9 = self.addSwitch('s9')

        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')


        self.addLink(host1,switch1,bw = 10,delay = '50us',loss = 12)
        self.addLink(host2,switch2,bw = 5,delay = '2ms',loss = 3)
        self.addLink(host3,switch3,bw = 7,delay = '63us',loss = 9)
        self.addLink(host4,switch4,bw = 12,delay = '40us',loss = 14)
        self.addLink(host5,switch5,bw = 15,delay = '30us',loss = 18)
        self.addLink(host6,switch6,bw = 3,delay = '5ms',loss = 2)
        self.addLink(switch1,switch7,bw = 23,delay = '1ms',loss = 8)
        self.addLink(switch2,switch7,bw = 18,delay = '2ms',loss = 9)
        self.addLink(switch3,switch7,bw = 15,delay = '3ms',loss = 5)
        self.addLink(switch4,switch8,bw = 19,delay = '80us',loss = 7)
        self.addLink(switch5,switch8,bw = 30,delay = '95us',loss = 2)
        self.addLink(switch6,switch8,bw = 20,delay = '60us',loss = 6)
        self.addLink(switch7,switch9,bw = 40,delay = '5ms',loss = 2)
        self.addLink(switch8,switch9,bw = 50,delay = '4ms',loss = 3)




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

    CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
