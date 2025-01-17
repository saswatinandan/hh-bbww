
/** \executable addSysTT
 *
 * Compute systematic uncertainty on TT background.
 *
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "FWCore/Utilities/interface/Exception.h"

#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "DataFormats/FWLite/interface/InputSource.h"
#include "DataFormats/FWLite/interface/OutputFiles.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/addBackgroundsAuxFunctions.h" // getSubdirectories, getSubdirectoryNames
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <TFile.h>
#include <TH1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TError.h> // gErrorAbortLevel, kError
#include "TPRegexp.h"
#include "TDirectory.h"
#include "TList.h"
#include "TKey.h"
#include "TObject.h"

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h>

typedef std::vector<std::string> vstring;

namespace
{
  bool sortbyfirstmax(const std::pair<float,float> &a,
                      const std::pair<float,float> &b)
  {
    return (a.first > b.first);
  }

  float sqr(float x) 
  {
    return x*x;
  }

  float funcvalue(float bincenter, float xmin, float xmax) 
  {
    float funcvalue_ = (bincenter - 0.5*(xmin+xmax))*2/(xmax-xmin);
    return funcvalue_;
  }


  void add_sysmass(TH1* hist_central, TH1* hist_up, TH1* hist_dn, std::string syst, std::string era)
  {
    std::string histname = hist_central->GetName();
    if ( era == "2016" )
    {
      for ( int i = 0; i < hist_central->GetNbinsX(); ++i )
      {
        float bincont = hist_central->GetBinContent(i + 1);
        float bincontErr = hist_central->GetBinError(i + 1);
        float bincontup = hist_up->GetBinContent(i + 1);
        float bincontdn = hist_dn->GetBinContent(i + 1);
        float delta = ( bincont - bincontup ) / 3.;
        float bincontnew = bincont + delta;
        float bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(delta));
        hist_up->SetBinContent(i + 1, bincontnew);
        hist_up->SetBinError(i + 1, bincontnewErr);
        hist_up->SetName(Form("%smodUp_%s", syst.data(), histname.data()));
        delta = ( bincont - bincontdn ) / 3.;
        bincontnew = bincont + delta;
        bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(delta));
        hist_dn->SetBinContent(i + 1, bincontnew);
        hist_dn->SetBinError(i + 1, bincontnewErr);
        hist_dn->SetName(Form("%smodDown_%s", syst.data(), histname.data()));
      }
    }
    else {
      hist_up->SetName(Form("%smodUp_%s", syst.data(), histname.data()));
      hist_dn->SetName(Form("%smodDown_%s", syst.data(), histname.data()));
      hist_up->Write();
      hist_dn->Write();
    }
  }

  void add_syshist(TH1* hist_central, TH1* hist_up, TH1* hist_dn, std::string syst, bool modify)
  {
    std::string histname = hist_central->GetName();
    if ( modify )
    {
      for ( int i = 0; i < hist_central->GetNbinsX(); ++i )
      {
        float bincont = hist_central->GetBinContent(i + 1);
        float bincontErr = hist_central->GetBinError(i + 1);
        float bincontup = hist_up->GetBinContent(i + 1);
        float bincontupErr = hist_up->GetBinError(i + 1);
        float bincontdn = hist_dn->GetBinContent(i + 1);
        float bincontdnErr = hist_dn->GetBinError(i + 1);
        float bincontnew = bincont + 0.5*(bincontup - bincontdn);
        float bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(0.5) * ( sqr(bincontupErr) + sqr(bincontdnErr)));
        hist_up->SetBinContent(i + 1, bincontnew );
        hist_up->SetBinError(i + 1, bincontnewErr );
        hist_up->SetName(Form("%smodUp_%s", syst.data(), histname.data()));
        bincontnew = bincont - 0.5*(bincontup-bincontdn);
        bincontnewErr = std::sqrt(sqr(bincontErr) + sqr(0.5) * ( sqr(bincontupErr) + sqr(bincontdnErr)));
        hist_dn->SetBinContent(i + 1, bincontnew );
        hist_dn->SetBinError(i + 1, bincontnewErr );
        hist_dn->SetName(Form("%smodDown_%s", syst.data(), histname.data()));
      }
    }
    else
    {
      hist_up->SetName( Form("%smodUp_%s", syst.data(), histname.data()) );
      hist_dn->SetName( Form("%smodDown_%s", syst.data(), histname.data()) );
    }
    hist_up->Write();
    hist_dn->Write();
  }

  void add_sysCR(TH1* hist_central, const std::vector<std::string>& histNames, const TDirectory* dir, const std::string& process_input, std::string syst, bool modify)
  {
    std::vector<TH1*> hists_cr;

    for ( unsigned int ihistName = 0; ihistName < histNames.size(); ++ihistName ) 
    {
      TString histName = hist_central->GetName();
      histName.Insert(0,histNames[ihistName]+"_");
      TH1* hist_cr = getHistogram(dir, process_input, histName.Data(), "", true);
      assert(hist_cr);
      hists_cr.push_back(hist_cr);
    }

    for (unsigned int icr=0; icr<histNames.size(); icr++)
    {
      TString histName = hist_central->GetName();
      TString histNameUp = Form("%sUp_%s" , histNames[icr].data(), histName.Data());
      TString histNameDown = Form("%sDown_%s" , histNames[icr].data(), histName.Data());
      TH1* hist_up = (TH1*) hist_central->Clone(histNameUp.Data());
      TH1* hist_dn = (TH1*) hist_central->Clone(histNameDown.Data());
      hist_up->Reset();
      hist_dn->Reset();
      histName.Insert(0, histNames[icr]+"_");
      TH1* hist_cr = getHistogram(dir, process_input, histName.Data(), "", true);
      assert(hist_cr);
      for ( int i = 0; i < hist_central->GetNbinsX(); ++i )
      {
        float bincont = hist_central->GetBinContent(i + 1);
        float bincontErr = hist_central->GetBinError(i + 1);
        float bincont_cr = hist_cr->GetBinContent(i + 1);
        float bincontErr_cr = hist_cr->GetBinError(i + 1);
        float diff = bincont_cr - bincont;
        hist_up->SetBinContent(i+1, bincont_cr);
        hist_up->SetBinError(i+1, bincontErr_cr);
        hist_dn->SetBinContent(i+1, bincont - diff);
        hist_dn->SetBinError(i+1, std::sqrt( sqr(bincontErr) + sqr(diff)));
      }
    }

    std::string histNameUp = syst + "Up_";
    histNameUp += hist_central->GetName();
    std::string histNameDown = syst + "Down_";
    histNameDown += hist_central->GetName();
    TH1* hist_up = (TH1*) hist_central->Clone(histNameUp.data());
    TH1* hist_dn = (TH1*) hist_central->Clone(histNameDown.data());
    hist_up->Reset();
    hist_dn->Reset();
    float xmin = hist_central->GetBinLowEdge(1);
    float xmax = hist_central->GetBinLowEdge(hist_central->GetNbinsX()) + hist_central->GetBinWidth(hist_central->GetNbinsX());

    std::vector<std::pair<float, float> > hist_diff;
    for ( int i = 0; i < hist_central->GetNbinsX(); ++i ) 
    {
      float bincont = hist_central->GetBinContent(i + 1);
      float bincontErr = hist_central->GetBinError(i + 1);
      hist_diff.clear();
      for ( size_t hist_cr = 0; hist_cr < hists_cr.size(); ++hist_cr ) 
      {
        float bincont_shift = hists_cr[hist_cr]->GetBinContent(i + 1);
        float bincont_shiftErr = hists_cr[hist_cr]->GetBinError(i + 1);
        float bin_diff = fabs(bincont-bincont_shift);
        float bin_diffErr = std::sqrt( sqr(bincontErr) + sqr(bincont_shiftErr));
        hist_diff.push_back(std::make_pair(bin_diff, bin_diffErr));
      }
      sort(hist_diff.begin(), hist_diff.end(), sortbyfirstmax);
      float bincenter = hist_central->GetXaxis()->GetBinCenter(i+1);
      float funcvalue_ = (modify) ? funcvalue(bincenter, xmin, xmax) : 1;
      float maxdiff = hist_diff[0].first;
      float maxdiffErr = hist_diff[0].second;
      float bincontnew = bincont + maxdiff*funcvalue_;
      float bincontnewErr = std::sqrt( sqr(bincontErr) + sqr(funcvalue_) * sqr(maxdiffErr) );
      hist_up->SetBinContent(i + 1, bincontnew);
      hist_up->SetBinError(i + 1, bincontnewErr);
      bincontnew = bincont - maxdiff*funcvalue_;
      bincontnewErr = std::sqrt( sqr(bincontErr) + sqr(funcvalue_) * sqr(maxdiffErr) );
      hist_dn->SetBinContent(i + 1, bincontnew);
      hist_dn->SetBinError(i + 1, bincontnewErr);
    }
  }

  void processSubdirectory_recursively(TFileDirectory& fs, 
                                       const TDirectory* dir, const std::string& dirName, 
                                       const vstring& processes_input, const std::string& process_output, 
                                       const vstring& central_or_shifts,
                                       int depth_recursion, int max_depth_recursion,
                                       std::string era,
                                       bool isDEBUG = false,
                                       bool modify = false)
  {
    if ( isDEBUG )
    {
      std::cout << "<processSubdirectory_recursively>:" << std::endl;
      std::cout << " dir = '" << dirName << "'" << std::endl;
    }

    // check if directory given as function argument contains subdirectories for input processes
    bool allProcessesExist = true;
    for ( auto process_input: processes_input )
    {
      const TDirectory* subdir_input = dynamic_cast<TDirectory*>((const_cast<TDirectory*>(dir))->Get(process_input.data()));
      if ( !subdir_input ) 
      {
        allProcessesExist = false;
      }
    }
    if ( allProcessesExist ) 
    {
      if ( isDEBUG )
      {
        std::cout << "processing directory = " << dirName << std::endl;
      }

      // get list of histograms to be added
      std::string the_process_input = "TT";
      const TDirectory* the_subdir_input = dynamic_cast<TDirectory*>((const_cast<TDirectory*>(dir))->Get(the_process_input.data()));
      assert(the_subdir_input);
      //the_subdir_input->ls();
      
      TList* list = the_subdir_input->GetListOfKeys();
      for ( auto central_or_shift: central_or_shifts )
      {
        std::string find_histogramUp;
        std::string find_histogramDown;
        if ( central_or_shift == "mtop" )
        {
          find_histogramUp = ( era == "2016" ) ? "mtop175p5" : "mtop173p5";
          find_histogramDown = ( era == "2016" ) ? "mtop169p5" : "mtop171p5";
        }
        else if ( central_or_shift == "color" )
        {
          find_histogramUp = "QCDbased_";
        }
        else
        {
          find_histogramUp = central_or_shift + "Up_";
          find_histogramDown = central_or_shift + "Down_";
        }
        std::set<std::string> histogramNames;
        TIter next(list);
        TKey* key = 0;
        while ( (key = dynamic_cast<TKey*>(next())) )
        {
          TObject* object = key->ReadObj();
          TH1* histogram = dynamic_cast<TH1*>(object);
          if ( !histogram ) continue;
          std::string histogramName = histogram->GetName();

          if ( histogramName.find(find_histogramUp) != std::string::npos )
          {
            histogramNames.insert(histogramName);
          }
        } //while

        for ( auto process_input: processes_input )
        {
          std::vector<std::string> processed_histogram;
          std::string subdirName_output = Form("%s/%s", dirName.data(), process_input.data());
          if ( isDEBUG )
          {
            std::cout << "creating subdirectory = '" << subdirName_output << "'" << std::endl;
          }
          TDirectory* subdir_output = createSubdirectory_recursively(fs, subdirName_output);
          subdir_output->cd();
          for ( auto histogramName: histogramNames )
          {
            std::string histogramName_up = histogramName;
            if ( central_or_shift == "hdamp" || central_or_shift == "ue" )
            {
              std::string histogramName_central = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), "").Data();
              TH1* histogram_central = getHistogram(dir, process_input, histogramName_central, "", true);
              assert(histogram_central);

              TH1* histogram_up = getHistogram(dir, process_input, histogramName_up, "", true);
              assert(histogram_up);
              std::string histogramName_dn = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), find_histogramDown.data()).Data();
              TH1* histogram_dn = getHistogram(dir, process_input, histogramName_dn, "", true);
              assert(histogram_dn);
              add_syshist(histogram_central, histogram_up, histogram_dn, central_or_shift, modify);
            }
            else if( central_or_shift == "color" ) {
              std::string histogramName_central = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), "").Data();
              TH1* histogram_central = getHistogram(dir, process_input, histogramName_central, "", true);
              assert(histogram_central);
              add_sysCR(histogram_central, { "QCDbased", "GluonMove", "erdON" }, dir, process_input, central_or_shift, modify);
            }
            else {
              assert( central_or_shift == "mtop" );
              std::size_t idx = histogramName_up.find("_"); 
              std::string histogramName_central = histogramName_up.substr(idx+1);
              TH1* histogram_central = getHistogram(dir, process_input, histogramName_central, "", true);
              assert(histogram_central);
              TH1* histogram_up = getHistogram(dir, process_input, histogramName_up, "", true);
              assert(histogram_up);
              std::string histogramName_dn = TString(histogramName_up.data()).ReplaceAll(find_histogramUp.data(), find_histogramDown.data()).Data();
              TH1* histogram_dn = getHistogram(dir, process_input, histogramName_dn, "", true);
              assert(histogram_dn);
              add_sysmass(histogram_central, histogram_up, histogram_dn, central_or_shift, era);
              }
            }
        } //histogramName
      } // process_input
    } // central_or_shift

    // recursively process all subdirectories
    if ( !allProcessesExist )
    {
      std::vector<const TDirectory*> subdirs = getSubdirectories(dir);
      bool stopRecursion = ( max_depth_recursion != -1 && depth_recursion >= max_depth_recursion ) ? true : false;
      if ( !stopRecursion )
      {
        for ( std::vector<const TDirectory*>::iterator subdir = subdirs.begin();
            subdir != subdirs.end(); ++subdir ) {
          processSubdirectory_recursively(
            fs, *subdir, dirName + "/" + (*subdir)->GetName(),
            processes_input, process_output,
            central_or_shifts,
            depth_recursion + 1, max_depth_recursion,
            era,
            isDEBUG
         );
        }
      }
      else
      {
        if ( isDEBUG )
        {
          std::cout << "aborting recursion, because maximum-recursion-depth = " << max_depth_recursion << " has been reached." << std::endl;
        }
      }
      for ( const TDirectory* subdir: subdirs )
      {
        delete subdir;
        subdir = nullptr;
      }
    }
  }
}

int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<addSysTT2>:\n";

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("addSysTT2");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cmsException(__func__, __LINE__)
      << "No ParameterSet 'process' found in configuration file = " << argv[1];

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_addSysTT = cfg.getParameter<edm::ParameterSet>("addSysTT");

  vstring categories = cfg_addSysTT.getParameter<vstring>("categories");

  vstring central_or_shifts = cfg_addSysTT.getParameter<vstring>("sysShifts");

  vstring processes_input = cfg_addSysTT.getParameter<vstring>("processes_input");
  std::string process_output = cfg_addSysTT.getParameter<std::string>("process_output");

  int max_depth_recursion = cfg_addSysTT.exists("max_depth_recursion") ? cfg_addSysTT.getParameter<int>("max_depth_recursion") : -1;
  //int max_depth_recursion = cfg_addSysTT.getParameter<int>("max_depth_recursion");

  bool isDEBUG = cfg_addSysTT.exists("isDEBUG") ? cfg_addSysTT.getParameter<bool>("isDEBUG") : false;
  bool modify = cfg_addSysTT.exists("modify") ? cfg_addSysTT.getParameter<bool>("modify") : false;
  std::string era = cfg_addSysTT.getParameter<std::string>("era");

  //bool isDEBUG = cfg_addSysTT.getParameter<bool>("isDEBUG");

  fwlite::InputSource inputFiles(cfg);
  if ( !(inputFiles.files().size() == 1) )
    throw cmsException(__func__, __LINE__) << "Exactly one input file expected";
  TFile* inputFile = new TFile(inputFiles.files().front().data());

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  if ( categories.size() == 0 )
  {
    categories = getSubdirectoryNames(inputFile);
  }

  for ( const std::string & category: categories )
  {
    std::cout << "processing category = " << category << std::endl;

    TDirectory* dir = getDirectory(inputFile, category, true);
    assert(dir);
    processSubdirectory_recursively(
      fs, dir, category,
      processes_input, process_output,
      central_or_shifts,
      1, max_depth_recursion,
      era,
      isDEBUG, modify
    );
  } // categories

  //---------------------------------------------------------------------------------------------------
  // CV: Add (dummy) histograms for number of analyzed and processed events
  //     This is needed to avoid run-time errors/warnings when executing python/commands/get_events_count.py (called by python/sbatch-node.template.hadd.sh)
  fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  //---------------------------------------------------------------------------------------------------

  delete inputFile;

  clock.Show("addSysTT2");

  std::cout << "returning exit code = " << EXIT_SUCCESS << " (EXIT_SUCCESS)." << std::endl;
  return EXIT_SUCCESS;
}
