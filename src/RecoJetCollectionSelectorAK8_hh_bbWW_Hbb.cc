#include "hhAnalysis/bbww/interface/RecoJetCollectionSelectorAK8_hh_bbWW_Hbb.h" // RecoJetSelectorAK8_hh_bbWW_Hbb

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // get_BtagWP()

RecoJetSelectorAK8_hh_bbWW_Hbb::RecoJetSelectorAK8_hh_bbWW_Hbb(Era era,
                                                               int index,
                                                               bool debug)
  : min_pt_(200.)
  , max_absEta_(2.4)
  , min_msoftdrop_(30.)
  , max_msoftdrop_(210.)
  , max_tau2_div_tau1_(0.75)
  , min_subJet1_pt_(20.)
  , max_subJet1_absEta_(2.4)
  , min_subJet2_pt_(20.)
  , max_subJet2_absEta_(2.4)
  , min_BtagCSV_loose_(get_BtagWP(era, Btag::kDeepCSV, BtagWP::kLoose))
  , min_BtagCSV_medium_(get_BtagWP(era, Btag::kDeepCSV, BtagWP::kMedium))
  , min_numSubJetsBtag_loose_(-1)
  , min_numSubJetsBtag_medium_(1)
  , debug_(debug)
{
  switch(era)
  {
    case Era::kUndefined: throw cmsException(this) << "Undefined era!";
    case Era::k2016: min_jetId_ = 1; break; // 1 means loose
    case Era::k2018:
    case Era::k2017: min_jetId_ = 2; break; // 2 means tight (loose jet ID deprecated since 94x)
    default: throw cmsException(this) << "Implement me!";
  }
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_pt(double min_pt)
{
  min_pt_ = min_pt;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_msoftdrop(double min_msoftdrop)
{
  min_msoftdrop_ = min_msoftdrop;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_max_msoftdrop(double max_msoftdrop)
{
  max_msoftdrop_ = max_msoftdrop;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_max_tau2_div_tau1(double max_tau2_div_tau1)
{
  max_tau2_div_tau1_ = max_tau2_div_tau1;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_subJet1_pt(double min_pt)
{
  min_subJet1_pt_ = min_pt;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_max_subJet1_absEta(double max_absEta)
{
  max_subJet1_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_subJet2_pt(double min_pt)
{
  min_subJet2_pt_ = min_pt;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_max_subJet2_absEta(double max_absEta)
{
  max_subJet2_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_BtagCSV_loose(double min_BtagCSV_loose) 
{
  min_BtagCSV_loose_ = min_BtagCSV_loose;
}
 
void 
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_BtagCSV_medium(double min_BtagCSV_medium) 
{
  min_BtagCSV_medium_ = min_BtagCSV_medium;
}

void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_numSubJetsBtag_loose(int min_numSubJetsBtag_loose) 
{
  min_numSubJetsBtag_loose_ = min_numSubJetsBtag_loose;
}
 
void
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_numSubJetsBtag_medium(int min_numSubJetsBtag_medium) 
{
  min_numSubJetsBtag_medium_ = min_numSubJetsBtag_medium;
}

void 
RecoJetSelectorAK8_hh_bbWW_Hbb::set_min_jetId(int min_jetId)
{
  min_jetId_ = min_jetId;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_pt() const
{
  return min_pt_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_max_absEta() const
{
  return max_absEta_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_msoftdrop() const
{
  return min_msoftdrop_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_max_msoftdrop() const
{
  return max_msoftdrop_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_max_tau2_div_tau1() const
{
  return max_tau2_div_tau1_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_subJet1_pt() const
{
  return min_subJet1_pt_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_max_subJet1_absEta() const
{
  return max_subJet1_absEta_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_subJet2_pt() const
{
  return min_subJet2_pt_;
}

double
RecoJetSelectorAK8_hh_bbWW_Hbb::get_max_subJet2_absEta() const
{
  return max_subJet2_absEta_;
}

double 
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_BtagCSV_loose() const
{
  return min_BtagCSV_loose_;
}
 
double 
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_BtagCSV_medium() const
{
  return min_BtagCSV_medium_;
}

int 
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_numSubJetsBtag_loose() const
{
  return min_numSubJetsBtag_loose_;
}
 
int 
RecoJetSelectorAK8_hh_bbWW_Hbb::get_min_numSubJetsBtag_medium() const
{
  return min_numSubJetsBtag_medium_;
}

bool
RecoJetSelectorAK8_hh_bbWW_Hbb::operator()(const RecoJetAK8 & jet) const
{
  int numSubJetsBtag_loose  = 0;
  int numSubJetsBtag_medium = 0;
  if(jet.subJet1() && jet.subJet1()->is_Btaggable())
  {
    const double subJet1BtagCSV = jet.subJet1()->BtagCSV();
    if(subJet1BtagCSV >= min_BtagCSV_loose_ ) ++numSubJetsBtag_loose;
    if(subJet1BtagCSV >= min_BtagCSV_medium_) ++numSubJetsBtag_medium;
  }

  if(jet.subJet2() && jet.subJet2()->is_Btaggable())
  {
    const double subJet2BtagCSV = jet.subJet2()->BtagCSV();
    if(subJet2BtagCSV >= min_BtagCSV_loose_ ) ++numSubJetsBtag_loose;
    if(subJet2BtagCSV >= min_BtagCSV_medium_) ++numSubJetsBtag_medium;
  }
  const bool passes =
    jet.pt()                  >= min_pt_                   &&
    jet.absEta()              <= max_absEta_               &&
    jet.jetId()               >= min_jetId_                &&
    jet.msoftdrop()           >= min_msoftdrop_            &&
    jet.msoftdrop()           <= max_msoftdrop_            &&
    jet.tau2() / jet.tau1()   <= max_tau2_div_tau1_        &&
    jet.subJet1() && jet.subJet2()                         &&
    ((jet.subJet1()->pt()     >= min_subJet1_pt_           && 
      jet.subJet1()->absEta() <= max_subJet1_absEta_       && 
      jet.subJet2()->pt()     >= min_subJet2_pt_           && 
      jet.subJet2()->absEta() <= max_subJet2_absEta_)      && 
     (jet.subJet1()->pt()     >= min_subJet2_pt_           && 
      jet.subJet1()->absEta() <= max_subJet2_absEta_       && 
      jet.subJet2()->pt()     >= min_subJet1_pt_           && 
      jet.subJet2()->absEta() <= max_subJet1_absEta_))     &&
     numSubJetsBtag_loose     >= min_numSubJetsBtag_loose_ &&
     numSubJetsBtag_medium    >= min_numSubJetsBtag_medium_
  ;
  if(debug_)
  {
    std::cout << get_human_line(this, __func__, __LINE__) << "\n"
                 "jet: " << jet << " (" << (passes ? "passes" : "fails") << ")\n"
    ;
  }
  return passes;
}
