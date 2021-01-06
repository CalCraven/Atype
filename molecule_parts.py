#Contains all of the building blocks for basic atoms building to do forcefield testing on

import mbuild as mb
import numpy as np
import warnings
from mbuild.lib.recipes import Polymer
from mbuild.lib.moieties import Silane

class Methyl(mb.Compound):
    """A methyl group with one port labeled 'down' """
    def __init__(self):
        super(Methyl, self).__init__()
        
        #Add CH3
        CH3=mb.lib.moieties.CH3()
        self.add(CH3)
        self.add(self.all_ports()[0],'up',containment=False)
        
class Ethyl(mb.Compound):
    """A methyl group with one port labeled 'down' """
    def __init__(self):
        super(Ethyl, self).__init__()
        
        #Add CH3
        CH3=mb.lib.moieties.CH3()
        self.add(CH3)
        CH3_2=mb.lib.moieties.CH3()
        CH3_2.translate([0.2,0,0])
        mb.force_overlap(CH3_2, CH3_2.all_ports()[0], self.all_ports()[0])
        self.add(CH3_2)
        #remove a hydrogen to add a port for connecting to the main carbon
        self.remove(self[1])
        self.add(self.all_ports()[0],'up',containment=False)
        
class Carboxylate(mb.Compound):
    """A carboxylate group with one extra port labeled ['C']['down'] """
    def __init__(self):
        super(Carboxylate, self).__init__()
        
        #Add central carbonyl with two extra ports
        self.add(mb.Particle(name='C'))
        
        self.add(mb.Port(anchor=self[0]), 'double')
        self['double'].translate(np.array([0, 0.062, 0]))

        self.add(mb.Port(anchor=self[0]), 'posterior')
        self['posterior'].translate(np.array([0, 0.07, 0]))
        self['posterior'].rotate(np.pi * 120/180, [0, 0, 1])
        
        self.add(mb.Port(anchor=self[0]), 'anterior')
        self['anterior'].translate(np.array([0, 0.07, 0]))
        self['anterior'].rotate(np.pi * 120/180, [0, 0, -1])
        
        self.add(mb.Particle(name='O'))
        self.add(mb.Port(anchor=self[1]), label='Odouble')
        self['Odouble'].translate(np.array([0, 0.062, 0]))
        

        mb.force_overlap(self[1], self['Odouble'], self['double'], add_bond=True)
        
        
        #Add posterior OH
        self.add(mb.Particle(name='O'))

        self.add(mb.Port(anchor=self[2]), label='Oanterior')
        self['Oanterior'].translate(np.array([0, .07, 0]))
        mb.force_overlap(self[2], self['Oanterior'], self['posterior'])
        
        self.add(mb.Port(anchor=self[2]), label='Oposterior')
        self['Oposterior'].translate(np.array([0, -.0485, 0]))
        
        self.add(mb.Particle(name='H'))
        self.add(mb.Port(anchor=self[3]), label='Hbond')
        self['Hbond'].translate(np.array([0, .0485, 0]))
        mb.force_overlap(self[3], self['Hbond'], self['Oposterior'])
        #self.add(self.all_ports()[0],'anterior',containment=False) 
        
        #Add CH2
        #CH2=mb.lib.moieties.CH2()
        #mb.force_overlap(CH2, CH2['up'], self['anterior'])
        #self.add(CH2)
        
class H(mb.Compound):
    """A hydrogen atom with two overlayed ports."""
    def __init__(self):
        super(H, self).__init__()
        self.add(mb.Particle(name='H'))

        self.add(mb.Port(anchor=self[0]), 'down')
        self['down'].spin(np.pi, [0, 0, 1])
        self['down'].translate(np.array([0, 0.07, 0]))
        
class H_Cap(mb.Compound):
    """A hydrogen atom with two overlayed ports."""
    def __init__(self,molecule):
        super(H_Cap, self).__init__()
        hydrogen=H()
        for port in molecule.all_ports():
            mb.force_overlap(hydrogen,hydrogen['down'], port)
            self.add(hydrogen)
            hydrogen=H()
        self.add(molecule)
        
