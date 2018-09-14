import FWCore.ParameterSet.Config as cms

from PhysicsTools.NanoAOD.common_cff import *

BToKstmumu=cms.EDProducer("BToKstmumuProducer",
                          beamSpot=cms.InputTag("offlineBeamSpot"),
                          vertexCollection=cms.InputTag("offlineSlimmedPrimaryVertices"),
                          muonCollection=cms.InputTag("linkedObjects","muons"), #same collection as in NanoAOD
                          PFCandCollection=cms.InputTag("packedPFCandidates"),
                          lostTrackCollection = cms.InputTag("lostTracks"),
                          MuonMinPt=cms.double(1.),
                          MuonMaxEta=cms.double(2.4),
                          KaonMinPt=cms.double(1.),
                          KaonMaxEta=cms.double(2.4),
                          KaonMinDCASig=cms.double(3.3),
                          PionMinPt=cms.double(1.),
                          PionMaxEta=cms.double(2.4),
                          PionMinDCASig=cms.double(3.3),
                          DiMuonChargeCheck=cms.bool(False),
                          KstarChargeCheck=cms.bool(True),
                          JPsiMassConstraint=cms.double(-1), #2-trk refitting uses measured di-ele mass
                          KstMassConstraint=cms.double(0.89176), #2-trk refitting uses nominal K*(892) mass
                          save2TrackRefit=cms.bool(False),
                          save4TrackRefit=cms.bool(False),
                          useLostTracks=cms.bool(False)
                          )

BToKstmumuTable=cms.EDProducer("SimpleCompositeCandidateFlatTableProducer", 
                               src=cms.InputTag("BToKstmumu"),
                               cut=cms.string(""),
                               name=cms.string("BToKstmumu"),
                               doc=cms.string("BToKstmumu Variable"),
                               singleton=cms.bool(False),
                               extension=cms.bool(False),
                               variables=cms.PSet(
                                mu1_index=Var("userInt('mu1_index')", int,doc="index of corresponding leading muon"),
                                mu2_index=Var("userInt('mu2_index')", int,doc="index of corresponding subleading muon"),
                                kaon_index=Var("userInt('kaon_index')", int,doc="PFCand index of corresponding kaon"),
                                kaon_lostTrack_index=Var("userInt('kaon_lostTrack_index')", int,doc="LostTrack index of corresponding kaon"),
                                kaon_isPFCand=Var("userInt('kaon_isPFCand')", int,doc="flag is kaon from PFCand"),
                                pion_index=Var("userInt('pion_index')", int,doc="PFCand index of corresponding pion"),
                                pion_lostTrack_index=Var("userInt('pion_lostTrack_index')", int,doc="LostTrack index of corresponding pion"),
                                pion_isPFCand=Var("userInt('pion_isPFCand')", int,doc="flag is pion from PFCand"),
                                mu1_pt=Var("userFloat('mu1_pt')", float,doc="pt of leading muon (refitted)"),
                                mu1_eta=Var("userFloat('mu1_eta')", float,doc="eta of leading muon (refitted)"),
                                mu1_phi=Var("userFloat('mu1_phi')", float,doc="phi of leading muon (refitted)"),
                                mu1_charge=Var("userInt('mu1_charge')", int,doc="charge of leading muon"),
                                mu1_dxy=Var("daughter('muon1').dB('PV2D')", float,doc="dxy of leading muon (with sign) wrt first PV, in cm"),
                                mu1_dz=Var("daughter('muon1').dB('PVDZ')", float,doc="dz of leading muon (with sign) wrt first PV, in cm"),
                                mu2_pt=Var("userFloat('mu2_pt')", float,doc="pt of subleading muon (refitted)"),
                                mu2_eta=Var("userFloat('mu2_eta')", float,doc="eta of subleading muon (refitted)"),
                                mu2_phi=Var("userFloat('mu2_phi')", float,doc="phi of subleading muon (refitted)"),
                                mu2_charge=Var("userInt('mu2_charge')", int,doc="charge of subleading muon"),
                                mu2_dxy=Var("daughter('muon2').dB('PV2D')", float,doc="dxy of subleading muon (with sign) wrt first PV, in cm"),
                                mu2_dz=Var("daughter('muon2').dB('PVDZ')", float,doc="dz of subleading muon (with sign) wrt first PV, in cm"),
                                kaon_pt=Var("userFloat('kaon_pt')", float,doc="pt of kaon (refitted)"),
                                kaon_eta=Var("userFloat('kaon_eta')", float,doc="eta of kaon (refitted)"),
                                kaon_phi=Var("userFloat('kaon_phi')", float,doc="phi of kaon (refitted)"),
                                kaon_charge=Var("userInt('kaon_charge')", int,doc="charge of kaon"),
                                kaon_DCASig=Var("userFloat('kaon_DCASig')", float,doc="significance of xy-distance of closest approach kaon-beamspot"),
                                kaon_dxy=Var("daughter('kaon').dxy()", float,doc="dxy of kaon (not refitted)"),
                                kaon_dz=Var("daughter('kaon').dz()", float,doc="dz of kaon (not refitted)"),
                                pion_pt=Var("userFloat('pion_pt')", float,doc="pt of kaon (refitted)"),
                                pion_eta=Var("userFloat('pion_eta')", float,doc="eta of kaon (refitted)"),
                                pion_phi=Var("userFloat('pion_phi')", float,doc="phi of kaon (refitted)"),
                                pion_charge=Var("userInt('pion_charge')", int,doc="charge of kaon"),
                                pion_DCASig=Var("userFloat('pion_DCASig')", float,doc="significance of xy-distance of closest approach kaon-beamspot"),
                                pion_dxy=Var("daughter('pion').dxy()", float,doc="dxy of kaon (not refitted)"),
                                pion_dz=Var("daughter('pion').dz()", float,doc="dz of kaon (not refitted)"),
                                mumu_pt=Var("userFloat('mumu_pt')", float,doc="dimuon pt (refitted)"),
                                mumu_eta=Var("userFloat('mumu_eta')", float,doc="dimuon eta (refitted)"),
                                mumu_phi=Var("userFloat('mumu_phi')", float,doc="dimuon phi (refitted)"),
                                mumu_mass=Var("userFloat('mumu_mass')", float,doc="dimuon mass (refitted)"),
                                mumu_mass_err=Var("userFloat('mumu_mass_err')", float,doc="error on dimuon mass"),
                                mumu_Lxy=Var("userFloat('mumu_Lxy')", float,doc="significance of dimuon vertex-beamspot xy-separation"),
                                mumu_ctxy=Var("userFloat('mumu_ctxy')", float,doc="dimuon vertex-beamspot xy-separation/dimuon pt"),
                                mumu_Chi2_vtx=Var("userFloat('mumu_Chi2_vtx')", float,doc="dimuon vertex chi2"),
                                mumu_CL_vtx=Var("userFloat('mumu_CL_vtx')", float,doc="dimuon chi2 vertex probability"),
                                Kst_pt=Var("userFloat('Kst_pt')", float,doc="K* pt (refitted)"),
                                Kst_eta=Var("userFloat('Kst_eta')", float,doc="K* eta (refitted)"),
                                Kst_phi=Var("userFloat('Kst_phi')", float,doc="K* phi (refitted)"),
                                Kst_mass=Var("userFloat('Kst_mass')", float,doc="K* mass (refitted)"),
                                Kst_mass_err=Var("userFloat('Kst_mass_err')", float,doc="error on K* mass"),
                                Kst_Lxy=Var("userFloat('Kst_Lxy')", float,doc="significance of K* vertex-beamspot xy-separation"),
                                Kst_ctxy=Var("userFloat('Kst_ctxy')", float,doc="K* vertex-beamspot xy-separation/K* pt"),
                                Kst_Chi2_vtx=Var("userFloat('Kst_Chi2_vtx')", float,doc="K* vertex chi2"),
                                Kst_CL_vtx=Var("userFloat('Kst_CL_vtx')", float,doc="K* chi2 vertex probability"),
                                pt=Var("userFloat('pt')", float,doc="pt of BToKstmumu candidate (3-trk refitted)"),
                                eta=Var("userFloat('eta')", float,doc="eta of BToKstmumu candidate (3-trk refitted)"),
                                phi=Var("userFloat('phi')", float,doc="phi of BToKstmumu candidate (3-trk refitted)"),
                                mass=Var("userFloat('mass')", float,doc="mass of BToKstmumu candidate (3-trk refitted)"),
                                mass_err=Var("userFloat('mass_err')", float,doc="error on mass of BToKstmumu candidate (3-trk refitted)"),
                                Lxy=Var("userFloat('Lxy')", float,doc="significance of BToKstmumu vertex-beamspot xy-separation (3-trk refitted)"),
                                ctxy=Var("userFloat('ctxy')", float,doc="BToKstmumu vertex-beamspot xy-separation/pt (3-trk refitted)"),
                                Chi2_vtx=Var("userFloat('Chi2_vtx')", float,doc="BToKstmumu vertex chi2 (3-trk refitted)"),
                                CL_vtx=Var("userFloat('CL_vtx')", float,doc="BToKstmumu chi2 vertex probability (3-trk refitted)"),
                                cosAlpha=Var("userFloat('cosAlpha')", float,doc="cosine of angle between BToKmumu momentum and vertex-beamspot separation (3-trk refitted)"),
                                pt_2trk=Var("userFloat('pt_2trk')", float,doc="pt of BToKstmumu candidate (2-trk refitted)"),
                                eta_2trk=Var("userFloat('eta_2trk')", float,doc="eta of BToKstmumu candidate (2-trk refitted)"),
                                phi_2trk=Var("userFloat('phi_2trk')", float,doc="phi of BToKstmumu candidate (2-trk refitted)"),
                                mass_2trk=Var("userFloat('mass_2trk')", float,doc="mass of BToKstmumu candidate (2-trk refitted)"),
                                mass_err_2trk=Var("userFloat('mass_err_2trk')", float,doc="error on mass of BToKstmumu candidate (2-trk refitted)"),
                                Lxy_2trk=Var("userFloat('Lxy_2trk')", float,doc="significance of BToKstmumu vertex-beamspot xy-separation (2-trk refitted)"),
                                ctxy_2trk=Var("userFloat('ctxy_2trk')", float,doc="BToKstmumu vertex-beamspot xy-separation/pt (2-trk refitted)"),
                                Chi2_vtx_2trk=Var("userFloat('Chi2_vtx_2trk')", float,doc="BToKstmumu vertex chi2 (2-trk refitted)"),
                                CL_vtx_2trk=Var("userFloat('CL_vtx_2trk')", float,doc="BToKstmumu chi2 vertex probability (2-trk refitted)"),
                                cosAlpha_2trk=Var("userFloat('cosAlpha_2trk')", float,doc="cosine of angle between BToKstmumu momentum and vertex-beamspot separation (2-trk refitted)"),
                                pt_4trk=Var("userFloat('pt_4trk')", float,doc="pt of BToKstmumu candidate (4-trk refitted)"),
                                eta_4trk=Var("userFloat('eta_4trk')", float,doc="eta of BToKstmumu candidate (4-trk refitted)"),
                                phi_4trk=Var("userFloat('phi_4trk')", float,doc="phi of BToKstmumu candidate (4-trk refitted)"),
                                mass_4trk=Var("userFloat('mass_4trk')", float,doc="mass of BToKstmumu candidate (4-trk refitted)"),
                                mass_err_4trk=Var("userFloat('mass_err_4trk')", float,doc="error on mass of BToKstmumu candidate (4-trk refitted)"),
                                Lxy_4trk=Var("userFloat('Lxy_4trk')", float,doc="significance of BToKstmumu vertex-beamspot xy-separation (4-trk refitted)"),
                                ctxy_4trk=Var("userFloat('ctxy_4trk')", float,doc="BToKstmumu vertex-beamspot xy-separation/pt (4-trk refitted)"),
                                Chi2_vtx_4trk=Var("userFloat('Chi2_vtx_4trk')", float,doc="BToKstmumu vertex chi2 (4-trk refitted)"),
                                CL_vtx_4trk=Var("userFloat('CL_vtx_4trk')", float,doc="BToKstmumu chi2 vertex probability (4-trk refitted)"),
                                cosAlpha_4trk=Var("userFloat('cosAlpha_4trk')", float,doc="cosine of angle between BToKstmumu momentum and vertex-beamspot separation (4-trk refitted)"),
                                )
                             )

BToKstmumuSequence=cms.Sequence(BToKstmumu)
BToKstmumuTables=cms.Sequence(BToKstmumuTable)
