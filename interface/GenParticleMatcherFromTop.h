#ifndef hhAnalysis_bbww_GenParticleMatcherFromTop_h
#define hhAnalysis_bbww_GenParticleMatcherFromTop_h

#include "hhAnalysis/bbww/interface/GenParticleMatcherBase.h" // GenParticleMatcherBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetBase.h" // RecoJetBase
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton

#include <vector> // std::vector<>

class GenParticleMatcherFromTop : public GenParticleMatcherBase
{
 public:
  GenParticleMatcherFromTop();
  ~GenParticleMatcherFromTop();

  void setGenParticles(const std::vector<GenLepton>& genLeptonsFromTop, 
	               const std::vector<GenParticle>& genNeutrinosFromTop,
                       const std::vector<GenParticle>& genLightQuarksFromTop, 
                       const std::vector<GenParticle>& genBQuarksFromTop);
};

const GenLepton* getLeptonFromTop(const std::vector<GenLepton>& genLeptons);
const GenLepton* getLeptonFromAntiTop(const std::vector<GenLepton>& genLeptons);
const GenParticle* getBQuarkFromTop(const std::vector<GenParticle>& genBQuarks);
const GenParticle* getBQuarkFromAntiTop(const std::vector<GenParticle>& genBQuarks);

#endif // GenParticleMatcherFromTop_h

