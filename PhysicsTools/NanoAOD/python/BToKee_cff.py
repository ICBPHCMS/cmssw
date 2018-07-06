import FWCore.ParameterSet.Config as cms

from PhysicsTools.NanoAOD.common_cff import *

BToKee=cms.EDProducer("BToKeeProducer",
                      beamSpot=cms.InputTag("offlineBeamSpot"),
                      electronCollection=cms.InputTag("slimmedElectronsWithUserData"), #NanoAOD electron collection has pT>5 GeV, can go lower here
                      PFCandCollection=cms.InputTag("packedPFCandidates"),
                      ElectronMinPt=cms.double(1.),
                      ElectronMaxEta=cms.double(2.4),
                      KaonMinPt=cms.double(1.),
                      KaonMaxEta=cms.double(2.4),
                      KaonMinDCASig=cms.double(3.3),
                      DiElectronChargeCheck=cms.bool(False),
                      RunDiElectronRefitting=cms.bool(True)
                      )

BToKeeTable=cms.EDProducer("SimpleCompositeCandidateFlatTableProducer", 
                           src=cms.InputTag("BToKee"),
                           cut=cms.string(""),
                           name=cms.string("BToKee"),
                           doc=cms.string("BToKee Variable"),
                           singleton=cms.bool(False),
                           extension=cms.bool(False),
                           variables=cms.PSet(
                                ele1_index=Var("userInt('ele1_index')", int,doc="index of corresponding leading electron"),
                                ele2_index=Var("userInt('ele2_index')", int,doc="index of corresponding subleading electron"),
                                kaon_index=Var("userInt('kaon_index')", int,doc="index of corresponding kaon"),
                                eeRefit=Var("userInt('eeRefit')", int,doc="result of di electron refit"),
                                ele1_pt=Var("userFloat('ele1_pt')", float,doc="pt of leading electron (refitted)"),
                                ele1_eta=Var("userFloat('ele1_eta')", float,doc="eta of leading electron (refitted)"),
                                ele1_phi=Var("userFloat('ele1_phi')", float,doc="phi of leading electron (refitted)"),
                                ele1_charge=Var("userFloat('ele1_charge')", int,doc="charge of leading electron"),
                                ele1_dxy=Var("daughter('ele1').dB('PV2D')", float,doc="dxy of leading electron (with sign) wrt first PV, in cm"),
                                ele1_dz=Var("daughter('ele1').dB('PVDZ')", float,doc="dz of leading electron (with sign) wrt first PV, in cm"),
                                ele2_pt=Var("userFloat('ele2_pt')", float,doc="pt of subleading electron (refitted)"),
                                ele2_eta=Var("userFloat('ele2_eta')", float,doc="eta of subleading electron (refitted)"),
                                ele2_phi=Var("userFloat('ele2_phi')", float,doc="phi of subleading electron (refitted)"),
                                ele2_charge=Var("userFloat('ele2_charge')", int,doc="charge of subleading electron"),
                                ele2_dxy=Var("daughter('ele2').dB('PV2D')", float,doc="dxy of subleading electron (with sign) wrt first PV, in cm"),
                                ele2_dz=Var("daughter('ele2').dB('PVDZ')", float,doc="dz of subleading electron (with sign) wrt first PV, in cm"),
                                kaon_pt=Var("userFloat('kaon_pt')", float,doc="pt of kaon (refitted)"),
                                kaon_eta=Var("userFloat('kaon_eta')", float,doc="eta of kaon (refitted)"),
                                kaon_phi=Var("userFloat('kaon_phi')", float,doc="phi of kaon (refitted)"),
                                kaon_charge=Var("userFloat('kaon_charge')", int,doc="charge of kaon"),
                                kaon_DCASig=Var("userFloat('kaon_DCASig')", float,doc="significance of xy-distance of closest approach kaon-beamspot"),
                                kaon_dxy=Var("daughter('kaon').dxy()", float,doc="dxy of kaon (not refitted)"),
                                kaon_dz=Var("daughter('kaon').dz()", float,doc="dz of kaon (not refitted)"),
                                ee_pt=Var("userFloat('ee_pt')", float,doc="dielectron pt (refitted)"),
                                ee_eta=Var("userFloat('ee_eta')", float,doc="dielectron eta (refitted)"),
                                ee_phi=Var("userFloat('ee_phi')", float,doc="dielectron phi (refitted)"),
                                ee_mass=Var("userFloat('ee_mass')", float,doc="dielectron mass (refitted)"),
                                ee_mass_err=Var("userFloat('ee_mass_err')", float,doc="error on dielectron mass"),
                                ee_Lxy=Var("userFloat('ee_Lxy')", float,doc="significance of dielectron vertex-beamspot xy-separation"),
                                ee_CL_vtx=Var("userFloat('ee_CL_vtx')", float,doc="dielectron chi2 vertex probability"),
                                pt=Var("userFloat('pt')", float,doc="pt of BToKee candidate (refitted)"),
                                eta=Var("userFloat('eta')", float,doc="eta of BToKee candidate (refitted)"),
                                phi=Var("userFloat('phi')", float,doc="phi of BToKee candidate (refitted)"),
                                mass=Var("userFloat('mass')", float,doc="mass of BToKee candidate (refitted)"),
                                mass_err=Var("userFloat('mass_err')", float,doc="error on mass of BToKee candidate"),                                
                                Lxy=Var("userFloat('Lxy')", float,doc="significance of BToKee vertex-beamspot xy-separation"),
                                CL_vtx=Var("userFloat('CL_vtx')", float,doc="BToKee chi2 vertex probability"),
                                cosAlpha=Var("userFloat('cosAlpha')", float,doc="cosine of angle between BToKmumu momentum and vertex-beamspot separation"),
                                )
                             )

BToKeeSequence=cms.Sequence(BToKee)
BToKeeTables=cms.Sequence(BToKeeTable)
