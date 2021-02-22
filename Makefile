
pythia8path=pythia8
hepmcpath=HepMC

CXX      := g++
CXXFLAGS := -O3 -std=c++11 -I$(pythia8path)/include -I$(pythia8path)/include/Pythia8/ -I$(hepmcpath)/include
LDFLAGS  := -L$(pythia8path)/lib/ -L$(pythia8path)/lib -Wl,-rpath,$(pythia8path)/lib
XMLDOC   := $(pythia8path)/share/Pythia8/xmldoc

all: pythia8ToHepMC.exe

clean:
	rm pythia8ToHepMC.exe

pythia8ToHepMC.exe: pythia8ToHepMC.cc
	echo $(XMLDOC) > xml.doc
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ pythia8ToHepMC.cc -lpythia8 -ldl -DGZIPSUPPORT -lz  -L$(hepmcpath)/lib -Wl,-rpath,$(hepmcpath)/lib -lHepMC
	


main42.exe: main42.cc
	echo $(XMLDOC) > xml.doc
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ main42.cc -lpythia8 -ldl -DGZIPSUPPORT -lz  -L$(hepmcpath)/lib -Wl,-rpath,$(hepmcpath)/lib -lHepMC
	

