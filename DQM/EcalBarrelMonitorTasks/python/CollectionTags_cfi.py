import FWCore.ParameterSet.Config as cms

ecalDQMCollectionTags = cms.untracked.PSet(
    Source = cms.untracked.InputTag("rawDataCollector"),
    EcalRawData = cms.untracked.InputTag("ecalDigis"),
    EBGainErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityGainErrors"),
    EEGainErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityGainErrors"),
    EBChIdErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityChIdErrors"),
    EEChIdErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityChIdErrors"),
    EBGainSwitchErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityGainSwitchErrors"),
    EEGainSwitchErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityGainSwitchErrors"),
    TowerIdErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityTTIdErrors"),
    BlockSizeErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityBlockSizeErrors"),
    MEMTowerIdErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityMemTtIdErrors"),
    MEMBlockSizeErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityMemBlockSizeErrors"),
    MEMChIdErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityMemChIdErrors"),
    MEMGainErrors = cms.untracked.InputTag("ecalDigis", "EcalIntegrityMemGainErrors"),
    EBSrFlag = cms.untracked.InputTag("ecalDigis"),
    EESrFlag = cms.untracked.InputTag("ecalDigis"),
    EBDigi = cms.untracked.InputTag("ecalDigis", "ebDigis"),
    EEDigi = cms.untracked.InputTag("ecalDigis", "eeDigis"),
    PnDiodeDigi = cms.untracked.InputTag("ecalDigis"),
    TrigPrimDigi = cms.untracked.InputTag("ecalDigis", "EcalTriggerPrimitives"),
    TrigPrimEmulDigi = cms.untracked.InputTag("valEcalTriggerPrimitiveDigis"),
    EBUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEB"),
    EEUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEE"),
#    EBLaserLedUncalibRecHit = cms.untracked.InputTag("ecalLaserLedUncalibRecHit", "EcalUncalibRecHitsEB"),
#    EELaserLedUncalibRecHit = cms.untracked.InputTag("ecalLaserLedUncalibRecHit", "EcalUncalibRecHitsEE"),
    EBLaserLedUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEB"),
    EELaserLedUncalibRecHit = cms.untracked.InputTag("ecalGlobalUncalibRecHit", "EcalUncalibRecHitsEE"),
    EBTestPulseUncalibRecHit = cms.untracked.InputTag("ecalTestPulseUncalibRecHit", "EcalUncalibRecHitsEB"),
    EETestPulseUncalibRecHit = cms.untracked.InputTag("ecalTestPulseUncalibRecHit", "EcalUncalibRecHitsEE"),
    EBRecHit = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEB"),
    EERecHit = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEE"),
    EBReducedRecHit = cms.untracked.InputTag("reducedEcalRecHitsEB"),
    EEReducedRecHit = cms.untracked.InputTag("reducedEcalRecHitsEE"),
    EBBasicCluster = cms.untracked.InputTag("particleFlowClusterECAL"),
    EEBasicCluster = cms.untracked.InputTag("particleFlowClusterECAL"),
    EBSuperCluster = cms.untracked.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALBarrel"),
    EESuperCluster = cms.untracked.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALEndcapWithPreshower")
)
