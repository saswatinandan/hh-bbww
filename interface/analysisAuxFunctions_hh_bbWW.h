#ifndef hhAnalysis_bbww_analysisAuxFunctions_hh_bbWW_h
#define hhAnalysis_bbww_analysisAuxFunctions_hh_bbWW_h

#include "FWCore/ParameterSet/interface/ParameterSet.h"                           // edm::ParameterSet

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h"                       // RecoJetAK8
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h"                      // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h"                    // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterfaceLBN.h"           // TensorFlowInterfaceLBN

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj

#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h"   // RecoJetSelectorAK8_hh_bbWW_Hbb

#include <string> // std::string
#include <vector> // std::vector<>

std::vector<TMVAInterface *>
makeTMVAInterface(const edm::ParameterSet & cfg, const std::string & era, bool is_nonresonant);

std::map<std::string, TMVAInterface *>
makeTMVAInterfaceMap(const edm::ParameterSet & cfg, const std::string & era, bool is_nonresonant);

std::vector<TensorFlowInterfaceLBN *>
makeTensorFlowInterfaceLBN(const edm::ParameterSet & cfg, const std::string & era, bool spin0, bool spin2, bool split_resonant_training=false);

std::map<std::string, TensorFlowInterfaceLBN *>
  makeTensorFlowInterfaceLBNMap(const edm::ParameterSet & cfg, const std::string & era, bool spin0, bool spin2, bool split_resonant_training=false);

void printHbb(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_bbWW_Hbb& jetSelectorAK8_Hbb,
	      const std::vector<GenParticle>& genBJets);

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj,
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets);

double comp_mHH_analytic(const Particle::LorentzVector &HHvisP4, const Particle::LorentzVector &metP4);
#endif
