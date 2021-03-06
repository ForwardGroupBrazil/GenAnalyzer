import FWCore.ParameterSet.Config as cms

process = cms.Process('Analysis')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/storage1/dmf/Samples/DiffractiveZ/GEN/pompyt_minus_Z_M20_cff_py_GEN_7TeV.root")
                                          #"file:/storage1/dmf/Samples/DiffractiveZ/GEN/pompyt_plus_Z_M20_cff_py_GEN_7TeV.root")
        #fileNames = cms.untracked.vstring("file:/storage1/dmf/Samples/DiffractiveZ/GEN/pompyt_minus_Z_M20_cff_py_GEN_13TeV.root")
        #                                  "file:/storage1/dmf/Samples/DiffractiveZ/GEN/pompyt_plus_Z_M20_cff_py_GEN_13TeV.root")
)

###process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
###process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')
###process.genParticles.abortOnUnknownPDGCode = False

##
## PDG ID
##
## electron: 11
## positron: -11
## muon: 13
## antimuon: -13
##

process.SDDY = cms.EDAnalyzer("SDDYAnalyzer",
	GenParticleTag = cms.InputTag("genParticles"),
	Particle1Id = cms.int32(13),
	Particle2Id = cms.int32(-13),
        EBeam = cms.double(3500),
	debug = cms.untracked.bool(True)
)

process.add_(cms.Service("TFileService",
		fileName = cms.string("minus_muon_output7TeV.root")
                #fileName = cms.string("output13TeV.root")
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

#process.analysis = cms.Path(process.genParticles*process.SDDY*process.printTree)
#process.analysis = cms.Path(process.genParticles*process.SDDY)
process.analysis = cms.Path(process.SDDY)
