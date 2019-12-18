#!/usr/bin/env python3

"""
.. module:: pylhe
   :synopsis: Simple LHE parser and event visualizer

.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>
                  Lukas Heinrich

"""


import numpy as np
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import networkx as nx
import pypdt
import matplotlib.pyplot as plt
import pyslha
import gzip

class LHEParticle(object):
    
    def __init__(self,**kargs):

        for key,val in kargs.items():
            setattr(self,key,val)
            
    def __str__(self):
        return self.getName()
    
    def __repr__(self):
        return self.__str__()
    
    def getName(self):
        
        if hasattr(self,'name'):
            return self.name
        else:
            try:
                name = pypdt.particle(int(self.id)).name
            except:
                name = str(int(self.id))
            self.name = name
            return name

            
    @classmethod
    def fromstring(cls,string):
        fieldnames = ['id','status','mother1','mother2','color1','color2','px','py','pz','e','mass','lifetime','spin']
        attrs = dict(zip(fieldnames,map(float,string.split())))
        particle = cls(**attrs)
        return particle
            
    def fourMom(self):
        
        return [self.energy()] + self.triMom()
    
    def triMom(self):
        
        return [self.px,self.py,self.pz]

    def eta(self):
        pmom = self.P()
        fPz = self.fourMom()[3]
        if pmom != abs(fPz):
            return 0.5*np.log((pmom+fPz)/(pmom-fPz))
        else:
            return 1e30        
        
    def p(self):
        
        return np.sqrt(self.px**2 + self.py**2 + self.pz**2)
    
    def energy(self):
        
        return self.e
        
    def getCalcMass(self):
        
        if hasattr(self,'mass'):        
            return self.mass
        else:
            mass = np.sqrt(np.inner(self.fourMom(),self.fourMom()))
            return mass 
        
    def pt(self):
        
        return np.sqrt(self.px**2 + self.py**2)

class LHEEventInfo(object):    

    def __init__(self,**kargs):
        for key,val in kargs.items():
            setattr(self,key,val)
            
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def fromstring(cls,string):
        fieldnames = ['nparticles', 'pid', 'weight', 'scale', 'aqed', 'aqcd']
        attrs = dict(zip(fieldnames,map(float,string.split())))
        eventInfo = cls(**attrs)
        return eventInfo
    

class LHEEvent(object):
    
    def __init__(self,**kargs):
        for key,val in kargs.items():
            setattr(self,key,val)
            
    def getParticlesWith(self,**kargs):
        
        particles = []
        for p in self.particles:
            for key,value in kargs.items():
                if not hasattr(p,key):
                    continue
                elif getattr(p,key) == value:
                    particles.append(p)
        
        return particles
    
    def MET(self,metPids = [12,14,16]):
        
        pTmiss = self.METVec(metPids)
        return np.linalg.norm(pTmiss)
    
    def METVec(self,metPids = [12,14,16]):
        
        pTmiss = np.array([0.,0.])
        for particle in self.particles:
            if particle.status != 1:
                continue
            if not particle.id in metPids and not -particle.id in metPids:
                continue
            pTmiss += np.array([particle.px,particle.py])
            
        return pTmiss    
    

                
    def visualize(self,bsmColor = 'lightcoral',smColor = 'skyblue',
                 genericColor= 'violet', nodeScale = 4,pdgLabels={}):
        
        g = nx.DiGraph()
        labels = {}
        node_size = []
        node_color = []
        #Add primary vertex node:
        g.add_node(0)
        labels[0] = 'PV'
        node_color.append('darkgray')
        node_size.append(nodeScale*100*len('PV'))
        for i,p in enumerate(self.particles):
                g.add_node(i+1,attr_dict=p)
                if int(p.id) in pdgLabels:
                    name = pdgLabels[int(p.id)]
                elif int(abs(p.id)) in pdgLabels:
                    name = pdgLabels[int(abs(p.id))]
                else:
                    name = p.getName()
                if 'susy-' in name:
                    name = name.replace('susy-','\\tilde ')
                    node_color.append(bsmColor)
                elif p.id < 101:
                    node_color.append(smColor)
                else:
                    node_color.append(genericColor)
                node_size.append(nodeScale*100*len(name))
                labels[i+1] = "${}$".format(name)
                g.node[i+1].update(texlbl = "${}$".format(name))
                
        for i,p in enumerate(self.particles):
            mom1 = int(p.mother1)
            mom2 = int(p.mother2)
            if p.status == -1:
                g.add_edge(i+1,0)
            elif self.particles[mom1-1].status == -1 or self.particles[mom2-1].status == -1:
                g.add_edge(0,i+1)
            else:
                if(p.mother1 > 0):
                    g.add_edge(mom1,i+1)
                if(p.mother2 > 0):
                    g.add_edge(mom2,i+1)
            
        pos = nx.drawing.nx_agraph.graphviz_layout(g, prog='dot')
        nx.draw(g,pos,
                with_labels=True,
                arrows=True,
                labels=labels,
                node_size=node_size,
                node_color=node_color)
        plt.show()           

class LHEFile(object):
    
    def __init__(self,lhefile):

        self.lhefile = lhefile
        if lhefile[-3:] == '.gz':
            f = gzip.open(lhefile,'r')
        else:
            f = open(lhefile,'r')
        data = str(f.read())
        data = data[data.find('<header>'):data.find('</header>')+9]
        f.close()
        self.root = ET.fromstring(data)
        
        try:
            slha = self.root.find('slha')
            self.slha = pyslha.readSLHA(slha.text.replace('\\n','\n'))
        except:
            self.slha = None

        self.events = list(readLHE(self.lhefile))
                
def readLHE(lhefile):
    
    if lhefile[-3:] == '.gz':
        source = gzip.open(lhefile,'r')
    else:
        source = lhefile

    try:
        for _,element in ET.iterparse(source,events=['end']):
            if element.tag == 'event':
                event = LHEEvent()
                data = element.text.split('\n')[1:-1]
                eventdata,particles = data[0],data[1:]
                event.info = LHEEventInfo.fromstring(eventdata)
                event.particles = [LHEParticle.fromstring(p) for p in particles]
                element.clear()
                yield event
            element.clear()

    except ET.ParseError as e:
        print("WARNING. Parse Error.")
        print(e)
        return
        
