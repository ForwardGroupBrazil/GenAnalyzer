import FWCore.ParameterSet.Config as cms

process = cms.Process('Analysis')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
        ##fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/d/dmf/private/PrivateMCProduction/Pomwig/CMSSW_6_2_0_patch1/src/POMWIG_SingleDiffractivePlusWEnu_7TeV_cff_py_GEN_SIM.root")
        #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/d/dmf/private/PrivateMCProduction/Pomwig/CMSSW_6_2_0_patch1/src/POMWIG_SingleDiffractivePlusWmunu_7TeV_cff_py_GEN_SIM.root")
       fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/d/dmf/private/PrivateMCProduction/Pomwig/CMSSW_6_2_0_patch1/src/POMWIG_SingleDiffractivePlusZee_7TeV_cff_py_GEN_SIM.root")
)

###process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
###process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')

###process.genParticles.abortOnUnknownPDGCode = False

##
## PDG ID
##
## electron: 11
## positron: -11
## neutrino electron: 12
## antineutrino electron: -12
## muon: 13
## antimuon: -13
## neutrino muon: 14
## antineutrino muon: -14
##
## POMWIG W->E+Nu, PDGId(24)->PDGId(11)+PDGId(12)
## POMWIG W->Mu+Nu, PDGId(24)->PDGId(14)+PDGId(13)

process.SDW = cms.EDAnalyzer("SDWAnalyzer",
	GenParticleTag = cms.InputTag("genParticles"),
	Particle1Id = cms.int32(11), # fabs(Particle1Id)
	Particle2Id = cms.int32(11), # fabs(Particle2Id)
        EBeam = cms.double(3500),
        cmsAccept = cms.untracked.bool(False),
	debug = cms.untracked.bool(True)
)

process.add_(cms.Service("TFileService",
		fileName = cms.string("output.root")
	)
)

process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("genParticles"),
                                   printP4 = cms.untracked.bool(True),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(True),
                                   printStatus = cms.untracked.bool(True),
                                   printIndex = cms.untracked.bool(True),
                                   status = cms.untracked.vint32( 3,2,1 )
                                   )

#process.analysis = cms.Path(process.genParticles*process.SDW*process.printTree)
#process.analysis = cms.Path(process.genParticles*process.SDW)
process.analysis = cms.Path(process.SDW)
