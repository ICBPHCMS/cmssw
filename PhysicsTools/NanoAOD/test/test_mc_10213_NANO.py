# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test_mc_1025 --mc -s NANO --eventcontent NANOAODSIM --datatier NANOAODSIM --filein /store/mc/RunIIAutumn18MiniAOD/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PUPoissonAve20_102X_upgrade2018_realistic_v15-v2/00000/035481CF-7C75-1046-B916-72ACA28654DE.root --no_exec --conditions 102X_upgrade2018_realistic_v15 -n 100 --era Run2_2018 --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) --customise_commands=process.NANOAODSIMoutput.fakeNameForCrab=cms.untracked.bool(True) --customise_commands=process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")

runBToKstll = True
eleFinalState = True
lowPtEleFinalState = True
lowPtAndPfEleFinalState = False
kstarFinalState = False
useLostSubLeadLepTracks = False  ## cannot be true if lowPtEleFinalState == true
useLostChHadrTracks = True

import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
fileNames = cms.untracked.vstring('/store/mc/RunIIAutumn18MiniAOD/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PUPoissonAve20_102X_upgrade2018_realistic_v15-v2/00000/F61219E1-1981-2B4A-B811-274A745C3443.root'),

       secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test_mc_10213 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('test_mc_10213_NANO.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 
#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

##the following should be enough                                                   
if runBToKstll:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeBToKstll
    process = nanoAOD_customizeBToKstll(process)
if eleFinalState:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeEleFinalState
    process = nanoAOD_customizeEleFinalState(process)
if lowPtEleFinalState:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeLowPtEleFinalState
    process = nanoAOD_customizeLowPtEleFinalState(process)
if lowPtAndPfEleFinalState:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeLowPtAndPfEleFinalState
    process = nanoAOD_customizeLowPtAndPfEleFinalState(process)
if kstarFinalState:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeKstarFinalState
    process = nanoAOD_customizeKstarFinalState(process)
if useLostSubLeadLepTracks:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeLostSubLeadLepTracks
    process = nanoAOD_customizeLostSubLeadLepTracks(process)
if useLostChHadrTracks:
    from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeLostChHadrTracks
    process = nanoAOD_customizeLostChHadrTracks(process)


# End of customisation functions

# Customisation from command line

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
