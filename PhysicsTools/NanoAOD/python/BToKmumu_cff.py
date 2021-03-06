from PhysicsTools.NanoAOD.common_cff import *
import FWCore.ParameterSet.Config as cms


BToKmumu=cms.EDProducer("BToKmumuProducer",
                        beamSpot=cms.InputTag("offlineBeamSpot"),
                        vertexCollection=cms.InputTag("offlineSlimmedPrimaryVertices"),
                        muonCollection = cms.InputTag("linkedObjects","muons"),
                        PFCandCollection=cms.InputTag("packedPFCandidates"),
                        lostSubLeadMuonTrackCollection = cms.InputTag("lostTracks"),
                        lostChHadrTrackCollection = cms.InputTag("lostTracks"),
                        LeadMuonMinPt=cms.double(1.),
                        LeadMuonMaxEta=cms.double(2.4),
                        SubLeadMuonMinPt=cms.double(1.),
                        SubLeadMuonMaxEta=cms.double(2.4),                        
                        KaonMinPt=cms.double(1.),
                        KaonMaxEta=cms.double(2.4),
                        KaonMinDCASig=cms.double(-1.),
                        DiMuonChargeCheck=cms.bool(True),
                        JPsiMassConstraint=cms.double(-1), #2-trk refitting uses measured di-muon mass
                        save2TrackRefit=cms.bool(False),
                        useLostSubLeadMuonTracks=cms.bool(False),
                        useLostChHadrTracks=cms.bool(False),
                        vtxCL_min=cms.double(1.e-3),
                        Bmass_min=cms.double(2.),
                        Bmass_max=cms.double(8.)
                        )


#Example not used for now: could replace BToKmumu collection in BToKmumuTable or be used in a cloned BToKJPsimumuTable
BToKJPsimumu=BToKmumu.clone(JPsiMassConstraint = cms.double(3.096916))



BToKmumuTable=cms.EDProducer("SimpleCompositeCandidateFlatTableProducer", 
                             src=cms.InputTag("BToKmumu"),
                             cut=cms.string(""),
                             name=cms.string("BToKmumu"),
                             doc=cms.string("BToKmumu Variable"),
                             singleton=cms.bool(False),
                             extension=cms.bool(False),
                             variables=cms.PSet(
                                mu1_index=Var("userInt('mu1_index')", int,doc="index of corresponding leading muon"),
                                mu2_index=Var("userInt('mu2_index')", int,doc="index of corresponding subleading muon"),
                                kaon_index=Var("userInt('kaon_index')", int,doc="PFCand index of corresponding kaon"),
                                mu2_lostTrack_index=Var("userInt('mu2_lostTrack_index')", int,doc="LostTrack index of corresponding subleading muon"),
                                kaon_lostTrack_index=Var("userInt('kaon_lostTrack_index')", int,doc="LostTrack index of corresponding kaon"),
                                mu2_isPFCand=Var("userInt('mu2_isPFCand')", int,doc="flag is subleading muon from PFCand"),
                                kaon_isPFCand=Var("userInt('kaon_isPFCand')", int,doc="flag is kaon from PFCand"),
                                mumuRefit=Var("userInt('mumuRefit')", int,doc="result of di muon refit"),
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
                                mu2_dxy=Var("daughter('muon2').dxy()", float,doc="dxy of subleading muon "),
                                mu2_dz=Var("daughter('muon2').dz()", float,doc="dz of subleading muon in cm"),
                                mumuKFit_mumu_mass=Var("userFloat('mumuKFit_mumu_mass')", float, doc="dimuon invariant mass post 3tracks refit"),
                                kaon_pt=Var("userFloat('kaon_pt')", float,doc="pt of kaon (refitted)"),
                                kaon_eta=Var("userFloat('kaon_eta')", float,doc="eta of kaon (refitted)"),
                                kaon_phi=Var("userFloat('kaon_phi')", float,doc="phi of kaon (refitted)"),
                                kaon_charge=Var("userInt('kaon_charge')", int,doc="charge of kaon"),
                                kaon_DCASig=Var("userFloat('kaon_DCASig')", float,doc="significance of xy-distance of closest approach kaon-beamspot"),
                                kaon_dxy=Var("daughter('kaon').dxy()", float,doc="dxy of kaon (not refitted)"),
                                kaon_dz=Var("daughter('kaon').dz()", float,doc="dz of kaon (not refitted)"),
                                mumu_pt=Var("userFloat('mumu_pt')", float,doc="dimuon pt (refitted)"),
                                mumu_eta=Var("userFloat('mumu_eta')", float,doc="dimuon eta (refitted)"),
                                mumu_phi=Var("userFloat('mumu_phi')", float,doc="dimuon phi (refitted)"),
                                mumu_mass=Var("userFloat('mumu_mass')", float,doc="dimuon mass (refitted)"),
                                mumu_mass_err=Var("userFloat('mumu_mass_err')", float,doc="error on dimuon mass"),
                                mumu_Lxy=Var("userFloat('mumu_Lxy')", float,doc="significance of dimuon vertex-beamspot xy-separation"),
                                mumu_ctxy=Var("userFloat('mumu_ctxy')", float,doc="dimuon vertex-beamspot xy-separation/pt"),
                                mumu_Chi2_vtx=Var("userFloat('mumu_Chi2_vtx')", float,doc="dimuon vertex chi2"),
                                mumu_CL_vtx=Var("userFloat('mumu_CL_vtx')", float,doc="dimuon chi2 vertex probability"),
                                pt=Var("userFloat('pt')", float,doc="pt of BToKmumu candidate (refitted)"),
                                eta=Var("userFloat('eta')", float,doc="eta of BToKmumu candidate (refitted)"),
                                phi=Var("userFloat('phi')", float,doc="phi of BToKmumu candidate (refitted)"),
                                mass=Var("userFloat('mass')", float,doc="mass of BToKmumu candidate (refitted)"),
                                mass_err=Var("userFloat('mass_err')", float,doc="error on mass of BToKmumu candidate"),                                
                                Lxy=Var("userFloat('Lxy')", float,doc="significance of BToKmumu vertex-beamspot xy-separation"),
                                ctxy=Var("userFloat('ctxy')", float,doc="BToKmumu vertex-beamspot xy-separation/pt"),
                                Chi2_vtx=Var("userFloat('Chi2_vtx')", float,doc="BToKmumu vertex chi2"),
                                CL_vtx=Var("userFloat('CL_vtx')", float,doc="BToKmumu chi2 vertex probability"),
                                cosAlpha=Var("userFloat('cosAlpha')", float,doc="cosine of angle between BToKmumu momentum and vertex-beamspot separation"),
                                pt_2trk=Var("userFloat('pt_2trk')", float,doc="pt of BToKmumu candidate (2-trk refitted)"),
                                eta_2trk=Var("userFloat('eta_2trk')", float,doc="eta of BToKmumu candidate (2-trk refitted)"),
                                phi_2trk=Var("userFloat('phi_2trk')", float,doc="phi of BToKmumu candidate (2-trk refitted)"),
                                mass_2trk=Var("userFloat('mass_2trk')", float,doc="mass of BToKmumu candidate (2-trk refitted)"),
                                mass_err_2trk=Var("userFloat('mass_err_2trk')", float,doc="error on mass of BToKmumu candidate (2-trk refitted)"),
                                Lxy_2trk=Var("userFloat('Lxy_2trk')", float,doc="significance of BToKmumu vertex-beamspot xy-separation (2-trk refitted)"),
                                ctxy_2trk=Var("userFloat('ctxy_2trk')", float,doc="BToKmumu vertex-beamspot xy-separation/pt (2-trk refitted)"),
                                Chi2_vtx_2trk=Var("userFloat('Chi2_vtx_2trk')", float,doc="BToKmumu vertex chi2 (2-trk refitted)"),
                                CL_vtx_2trk=Var("userFloat('CL_vtx_2trk')", float,doc="BToKmumu chi2 vertex probability (2-trk refitted)"),
                                cosAlpha_2trk=Var("userFloat('cosAlpha_2trk')", float,doc="cosine of angle between BToKmumu momentum and vertex-beamspot separation (2-trk refitted)"),
                                )
                             )

BToKmumuSequence=cms.Sequence(BToKmumu)
BToKmumuTables=cms.Sequence(BToKmumuTable)
