import logging
import re

from hhAnalysis.multilepton.configs.analyzeConfig_hh import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight):
  lepton_selection_and_frWeight = lepton_selection
  if lepton_selection.startswith("Fakeable"):
    if lepton_frWeight == "enabled":
      lepton_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      lepton_selection_and_frWeight += "_woFakeRateWeights"
  lepton_selection_and_frWeight = lepton_selection_and_frWeight.replace("|", "_")
  return lepton_selection_and_frWeight

def getHistogramDir(category, lepton_selection, lepton_frWeight, lepton_charge_selection):
  histogramDir = category
  if lepton_charge_selection != "disabled":
    histogramDir += "_%s" % lepton_charge_selection
  histogramDir += "_%s" % lepton_selection
  if lepton_selection.find("Fakeable") != -1:
    if lepton_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_hh_bbWW_TT2lctrl(analyzeConfig_hh):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_hh_bbWW_TT2lctrl:
    None.

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        localDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        lepton_charge_selections,
        applyFakeRateWeights,
        central_or_shifts,
        lep_mva_wp,
        jet_cleaning_by_index,
        gen_matching_by_index,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        executable_addSysTT,
        executable_addBackgrounds,
        executable_addFakes,
        histograms_to_fit,
        select_rle_output = False,
        verbose           = False,
        dry_run           = False,
        isDebug           = False,
        use_nonnominal    = False,
        hlt_filter        = False,
        use_home          = False,
        keep_logs         = False,
        submission_cmd    = None,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      localDir              = localDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_bbWW_TT2lctrl",
      samples               = samples,
      jet_cleaning_by_index = jet_cleaning_by_index,
      gen_matching_by_index = gen_matching_by_index,
      central_or_shifts     = central_or_shifts,
      max_files_per_job     = max_files_per_job,
      era                   = era,
      use_lumi              = use_lumi,
      lumi                  = lumi,
      check_output_files    = check_output_files,
      running_method        = running_method,
      num_parallel_jobs     = num_parallel_jobs,
      histograms_to_fit     = histograms_to_fit,
      triggers              = [ '1e', '1mu', '2e', '2mu', '1e1mu' ],
      lep_mva_wp            = lep_mva_wp,
      verbose               = verbose,
      dry_run               = dry_run,
      isDebug               = isDebug,
      use_home              = use_home,
      keep_logs             = keep_logs,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates'),
      submission_cmd        = submission_cmd,
    )

    self.lepton_selections = [ "Tight", "Fakeable" ]
    self.lepton_frWeights = [ "enabled", "disabled" ]
    self.applyFakeRateWeights = applyFakeRateWeights
    self.lepton_charge_selections = lepton_charge_selections

    self.apply_leptonGenMatching = True
    if self.run_mcClosure:
      self.lepton_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])
    self.central_or_shifts_fr = systematics.FRe_shape + systematics.FRm_shape
    self.pruneSystematics()
    self.internalizeSystematics()

    self.executable_addSysTT = executable_addSysTT
    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addFakes

    self.nonfake_backgrounds = self.get_nonfake_backgrounds()

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.prep_dcard_processesToCopy = [ "data_obs" ] + self.nonfake_backgrounds + [ "Convs", "data_fakes", "fakes_mc" ]
    self.prep_dcard_signals = []
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      sample_category = sample_info["sample_category"]
      if sample_category.startswith("signal"):
        self.prep_dcard_signals.append(sample_category)
    self.make_plots_backgrounds = self.get_makeplots_backgrounds()
    self.cfgFile_make_plots_inclusive = os.path.join(self.template_dir, "makePlots_hh_bbWW_TT2lctrl_inclusive_cfg.py")
    self.cfgFile_make_plots_in_categories = os.path.join(self.template_dir, "makePlots_hh_bbWW_TT2lctrl_in_categories_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_hh_bbWW_TT2lctrl_cfg.py")

    self.jobOptions_hadd_stage2_harvest = {}

    self.select_rle_output = select_rle_output
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    self.evtCategories = []
    for type_lepton in [ "2e", "1e1mu", "2mu" ]:
      # AN: add inclusive categories
      category = "hh_bbWW_%s_TT2lctrl" % type_lepton
      self.evtCategories.append(category)
      # CV: add categories for "resolved" AK4 jets without VBF jet selection
      self.evtCategories.append("hh_bbWW_%s_TT2lctrl_resolvedHbb" % type_lepton)                                                        
      # CV: add categories for "resolved" AK4 jets with VBF jet selection
      self.evtCategories.append("hh_bbWW_%s_TT2lctrl_resolvedHbb_vbf" % type_lepton)
      # CV: add categories for "boosted" AK8 jets passing H->bb selection (no VBF jet selection)
      self.evtCategories.append("hh_bbWW_%s_TT2lctrl_boostedHbb" % type_lepton)
    logging.info("Processing %i categories: %s" % (len(self.evtCategories), self.evtCategories))
    self.evtcategory_inclusive = "hh_bbWW_2l_TT2lctrl"
    if not self.evtcategory_inclusive in self.evtCategories:
      self.evtCategories.append(self.evtcategory_inclusive)

  def accept_systematics(self, central_or_shift, is_mc, lepton_selection, lepton_charge_selection, sample_info):
    if central_or_shift != "central":
      isFR_shape_shift = (central_or_shift in self.central_or_shifts_fr)
      if not ((lepton_selection == "Fakeable" and isFR_shape_shift) or lepton_selection == "Tight"):
        return False
      if isFR_shape_shift and lepton_selection == "Tight":
        return False
      if not is_mc and not isFR_shape_shift:
        return False
      if not self.accept_central_or_shift(central_or_shift, sample_info):
        return False
    return True

  def createCfg_analyze(self, jobOptions, sample_info, lepton_selection):
    """Create python configuration file for the analyze_hh_bbWW_TT2lctrl executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, or `signal`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_hh_bbWW_TT2lctrl.cc
    """
    lepton_frWeight = "disabled" if jobOptions['applyFakeRateWeights'] == "disabled" else "enabled"

    jobOptions['histogramDir'] = getHistogramDir(self.evtcategory_inclusive, lepton_selection, lepton_frWeight, jobOptions['leptonChargeSelection'])
    if 'mcClosure' in lepton_selection:
      self.mcClosure_dir[lepton_selection] = jobOptions['histogramDir']

    self.set_leptonFakeRateWeightHistogramNames(jobOptions['central_or_shift'], lepton_selection)
    jobOptions['leptonFakeRateWeight.inputFileName'] = self.leptonFakeRateWeight_inputFile
    jobOptions['leptonFakeRateWeight.histogramName_e'] = self.leptonFakeRateWeight_histogramName_e
    jobOptions['leptonFakeRateWeight.histogramName_mu'] = self.leptonFakeRateWeight_histogramName_mu

    lines = super(analyzeConfig_hh_bbWW_TT2lctrl, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def createCfg_makePlots(self, jobOptions):
    """Fills the template of python configuration file for making control plots

       Args:
         histogram_file: name of the input ROOT file
    """
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % jobOptions['inputFile'])
    lines.append("process.makePlots.outputFileName = cms.string('%s')" % jobOptions['outputFile'])
    lines.append("process.makePlots.processesBackground = cms.vstring(%s)" % jobOptions['make_plots_backgrounds'])
    lines.append("process.makePlots.categories = cms.VPSet(")
    for category in jobOptions['categories']:
      lines.append("  cms.PSet(")
      lines.append("    name = cms.string('%s')," % getHistogramDir(category, "Tight", "disabled", jobOptions['lepton_charge_selection']))
      lines.append("    label = cms.string('TT2l CR')")
      lines.append("  ),")
    lines.append(")")
    lines.append("process.makePlots.intLumiData = cms.double(%.1f)" % (self.lumi / 1000))
    create_cfg(jobOptions['cfgFile_original'], jobOptions['cfgFile_modified'], lines)

  def addToMakefile_backgrounds_from_data(self, lines_makefile, make_target = "phony_addFakes", make_dependency = "phony_copyHistograms"):
    self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds", make_dependency, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
    self.addToMakefile_hadd_stage1_5(lines_makefile, "phony_hadd_stage1_5", "phony_addBackgrounds", max_input_files_per_job = 10)
    self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds_sum", "phony_hadd_stage1_5", self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
    self.addToMakefile_addFakes(lines_makefile, "phony_addFakes", "phony_hadd_stage1_5")
    if make_target != "phony_addFakes":
      lines_makefile.append("%s: %s" % (make_target, "phony_addFakes"))
      lines_makefile.append("")
    self.make_dependency_hadd_stage2 = " ".join([ "phony_addBackgrounds_sum", make_target ])

  def addToMakefile_harvest_hadd_stage2(self, lines_makefile, make_target = "phony_hadd_stage2_harvest", make_dependency = "phony_hadd_stage2"):
    inputFiles_hadd_stage2_harvest = { key : self.jobOptions_hadd_stage2_harvest[key]['inputFiles'] for key in self.jobOptions_hadd_stage2_harvest }
    outputFile_hadd_stage2_harvest = { key : self.jobOptions_hadd_stage2_harvest[key]['outputFile'] for key in self.jobOptions_hadd_stage2_harvest }
    max_inputFiles_hadd_stage2_harvest = max([ len(inputFiles_hadd_stage2_harvest[key]) for key in inputFiles_hadd_stage2_harvest ])
    self.addToMakefile_hadd(lines_makefile, make_target, make_dependency, inputFiles_hadd_stage2_harvest, outputFile_hadd_stage2_harvest, max_inputFiles_hadd_stage2_harvest)
    for key_hadd_stage2_harvest_job in self.jobOptions_hadd_stage2_harvest:
      outputFile = self.jobOptions_hadd_stage2_harvest[key_hadd_stage2_harvest_job]['outputFile']
      lines_makefile.append("")
      lines_makefile.append("%s: %s" % (outputFile, make_target))
      lines_makefile.append("")

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue

      sample_category = sample_info["sample_category"]
      is_mc = (sample_info["type"] == "mc")
      process_name = sample_info["process_name_specific"]

      logging.info("Building dictionaries for sample %s..." % process_name)
      for lepton_charge_selection in self.lepton_charge_selections:
        for lepton_selection in self.lepton_selections:
          for lepton_frWeight in self.lepton_frWeights:
            if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
              continue
            if lepton_frWeight == "disabled" and not lepton_selection in ["Tight"]:
              continue

            lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)
            central_or_shift_extensions = ["", "hadd", "copyHistograms", "addSysTT", "addBackgrounds"]
            central_or_shift_dedicated = self.central_or_shifts if self.runTHweights(sample_info) else self.central_or_shifts_external
            central_or_shifts_extended = central_or_shift_extensions + central_or_shift_dedicated
            for central_or_shift_or_dummy in central_or_shifts_extended:
              process_name_extended = [ process_name, "hadd" ]
              for process_name_or_dummy in process_name_extended:
                if process_name_or_dummy in [ "hadd" ] and central_or_shift_or_dummy != "":
                  continue
                if central_or_shift_or_dummy in [ "hadd", "copyHistograms", "addSysTT", "addBackgrounds" ] and process_name_or_dummy in [ "hadd" ]:
                  continue

                if central_or_shift_or_dummy not in central_or_shift_extensions and not self.accept_systematics(
                    central_or_shift_or_dummy, is_mc, lepton_selection, lepton_charge_selection, sample_info
                ):
                  continue

                key_dir = getKey(process_name_or_dummy, lepton_charge_selection, lepton_selection_and_frWeight, central_or_shift_or_dummy)
                for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
                  if dir_type == DKEY_SYNC and not self.do_sync:
                    continue
                  initDict(self.dirs, [ key_dir, dir_type ])
                  if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
                    self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel,
                                                                "_".join([ lepton_selection_and_frWeight, lepton_charge_selection ]), process_name_or_dummy, central_or_shift_or_dummy)
                  else:
                    self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                                                                "_".join([ lepton_selection_and_frWeight, lepton_charge_selection ]), process_name_or_dummy)
  
    for subdirectory in [ "addSysTT", "addBackgrounds", "addBackgroundLeptonFakes", "prepareDatacards", "addSystFakeRates", "makePlots" ]:
      key_dir = getKey(subdirectory)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel, subdirectory)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, subdirectory)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      if dir_type == DKEY_SYNC and not self.do_sync:
        continue
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)

    numDirectories = 0
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        numDirectories += len(self.dirs[key])
      else:
        numDirectories += 1
    logging.info("Creating directory structure (numDirectories = %i)" % numDirectories)
    numDirectories_created = 0;
    frac = 1
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
        numDirectories_created += len(self.dirs[key])
      else:
        create_if_not_exists(self.dirs[key])
        numDirectories_created = numDirectories_created + 1
      while 100*numDirectories_created >= frac*numDirectories:
        logging.info(" %i%% completed" % frac)
        frac = frac + 1
    logging.info("Done.")

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    for lepton_charge_selection in self.lepton_charge_selections:
      for lepton_selection in self.lepton_selections:
        electron_selection = lepton_selection
        muon_selection = lepton_selection

        if lepton_selection == "Fakeable_mcClosure_e":
          electron_selection = "Fakeable"
          muon_selection = "Tight"
        elif lepton_selection == "Fakeable_mcClosure_m":
          electron_selection = "Tight"
          muon_selection = "Fakeable"

        for lepton_frWeight in self.lepton_frWeights:
          if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
            continue
          if lepton_frWeight == "disabled" and not lepton_selection in [ "Tight" ]:
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)

          for sample_name, sample_info in self.samples.items():
            if not sample_info["use_it"]:
              continue
            process_name = sample_info["process_name_specific"]
            logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
            inputFileList = inputFileLists[sample_name]

            sample_category = sample_info["sample_category"]
            is_mc = (sample_info["type"] == "mc")
            use_th_weights = self.runTHweights(sample_info)

            central_or_shift_dedicated = self.central_or_shifts if use_th_weights else self.central_or_shifts_external
            for central_or_shift in central_or_shift_dedicated:
              if not self.accept_systematics(
                  central_or_shift, is_mc, lepton_selection, lepton_charge_selection, sample_info
              ):
                continue

              central_or_shifts_local = []
              if central_or_shift == "central" and not use_th_weights:
                for central_or_shift_local in self.central_or_shifts_internal:
                  if self.accept_systematics(
                      central_or_shift_local, is_mc, lepton_selection, lepton_charge_selection, sample_info
                  ):
                    central_or_shifts_local.append(central_or_shift_local)

              logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_selection_and_frWeight, central_or_shift))

              # build config files for executing analysis code
              key_analyze_dir = getKey(process_name, lepton_charge_selection, lepton_selection_and_frWeight, central_or_shift)

              for jobId in inputFileList.keys():
                
                analyze_job_tuple = (process_name, lepton_charge_selection, lepton_selection_and_frWeight, central_or_shift, jobId)
                key_analyze_job = getKey(*analyze_job_tuple)
                ntupleFiles = inputFileList[jobId]
                if len(ntupleFiles) == 0:
                  logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                  continue
                cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_%s_%s_%s_%i_cfg.py" % analyze_job_tuple)
                histogramFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_HIST], "analyze_%s_%s_%s_%s_%i.root" % analyze_job_tuple)
                logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_%s_%s_%s_%i.log" % analyze_job_tuple)
                rleOutputFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_RLES], "rle_%s_%s_%s_%s_%i.txt" % analyze_job_tuple) \
                                     if self.select_rle_output else ""
                applyFakeRateWeights = self.applyFakeRateWeights  \
                  if not lepton_selection == "Tight" \
                  else "disabled"

                self.jobOptions_analyze[key_analyze_job] = {
                  'ntupleFiles'              : ntupleFiles,
                  'cfgFile_modified'         : cfgFile_modified_path,
                  'histogramFile'            : histogramFile_path,
                  'logFile'                  : logFile_path,
                  'selEventsFileName_output' : rleOutputFile_path,
                  'leptonChargeSelection'    : lepton_charge_selection,
                  'electronSelection'        : electron_selection,
                  'muonSelection'            : muon_selection,
                  'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                  'applyFakeRateWeights'     : applyFakeRateWeights,
                  'central_or_shift'         : central_or_shift,
                  'central_or_shifts_local'  : central_or_shifts_local,
                  'apply_hlt_filter'         : self.hlt_filter,
                  'useNonNominal'            : self.use_nonnominal,
                  'fillGenEvtHistograms'     : True,
                }
                self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_selection)

                # initialize input and output file names for hadd_stage1
                key_hadd_stage1_dir = getKey(process_name, lepton_charge_selection, lepton_selection_and_frWeight, "hadd")
                hadd_stage1_job_tuple = (process_name, lepton_charge_selection, lepton_selection_and_frWeight)
                key_hadd_stage1_job = getKey(*hadd_stage1_job_tuple)
                if not key_hadd_stage1_job in self.inputFiles_hadd_stage1:
                  self.inputFiles_hadd_stage1[key_hadd_stage1_job] = []
                self.inputFiles_hadd_stage1[key_hadd_stage1_job].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
                self.outputFile_hadd_stage1[key_hadd_stage1_job] = os.path.join(self.dirs[key_hadd_stage1_dir][DKEY_HIST], "hadd_stage1_%s_%s_%s.root" % hadd_stage1_job_tuple)

            #----------------------------------------------------------------------------
            # split hadd_stage1 files into separate files, one for each event category
            for category in self.evtCategories:
              key_hadd_stage1_job = getKey(process_name, lepton_charge_selection, lepton_selection_and_frWeight)
              key_copyHistograms_dir = getKey(process_name, lepton_charge_selection, lepton_selection_and_frWeight, "copyHistograms")
              copyHistograms_job_tuple = (category, process_name, lepton_charge_selection, lepton_selection_and_frWeight)
              key_copyHistograms_job = getKey(*copyHistograms_job_tuple)
              cfgFile_modified = os.path.join(self.dirs[key_copyHistograms_dir][DKEY_CFGS], "copyHistograms_%s_%s_%s_%s_cfg.py" % copyHistograms_job_tuple)
              outputFile = os.path.join(self.dirs[key_copyHistograms_dir][DKEY_HIST], "copyHistograms_%s_%s_%s_%s.root" % copyHistograms_job_tuple)
              self.jobOptions_copyHistograms[key_copyHistograms_job] = {
                'inputFile' : self.outputFile_hadd_stage1[key_hadd_stage1_job],
                'cfgFile_modified' : cfgFile_modified,
                'outputFile' : outputFile,
                'logFile' : os.path.join(self.dirs[key_copyHistograms_dir][DKEY_LOGS], os.path.basename(cfgFile_modified).replace("_cfg.py", ".log")),
                'categories' : [ getKey(category, lepton_charge_selection, lepton_selection_and_frWeight) ],
              }
              self.createCfg_copyHistograms(self.jobOptions_copyHistograms[key_copyHistograms_job])
            #----------------------------------------------------------------------------

            # add output files of copyHistograms jobs to list of input files for hadd_stage1_5
            for category in self.evtCategories:
              key_copyHistograms_job = getKey(category, process_name, lepton_charge_selection, lepton_selection_and_frWeight)
              key_hadd_stage1_5_dir = getKey("hadd", lepton_charge_selection, lepton_selection_and_frWeight)
              hadd_stage1_5_job_tuple = (category, lepton_charge_selection, lepton_selection_and_frWeight)
              key_hadd_stage1_5_job = getKey(*hadd_stage1_5_job_tuple)
              if not key_hadd_stage1_5_job in self.inputFiles_hadd_stage1_5:
                self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job] = []
              self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job].append(self.jobOptions_copyHistograms[key_copyHistograms_job]['outputFile'])
              self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job] = os.path.join(self.dirs[key_hadd_stage1_5_dir][DKEY_HIST],
                                                                          "hadd_stage1_5_%s_%s_%s.root" % hadd_stage1_5_job_tuple)

          if self.ttbar_syst_enabled:
            for category in self.evtCategories:
                addSysTT_job_tuple = (category, lepton_charge_selection, lepton_selection_and_frWeight)
                key_addSysTT_job = getKey(*addSysTT_job_tuple)
                key_addSysTT_dir = getKey("addSysTT")
                self.jobOptions_addSysTT[key_addSysTT_job] = {
                  'inputFile' : self.outputFile_hadd_stage1_5[key_addSysTT_job],
                  'cfgFile_modified' : os.path.join(self.dirs[key_addSysTT_dir][DKEY_CFGS], "addSysTT_%s_%s_%s_cfg.py" % addSysTT_job_tuple),
                  'outputFile' : os.path.join(self.dirs[key_addSysTT_dir][DKEY_HIST], "addSysTT_%s_%s_%s.root" % addSysTT_job_tuple),
                  'logFile' : os.path.join(self.dirs[key_addSysTT_dir][DKEY_LOGS], "addSysTT_%s_%s_%s.log" % addSysTT_job_tuple),
                  'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight, lepton_charge_selection) ],
                  'process_output' : "addSysTT"
                   }
                self.createCfg_addSysTT(self.jobOptions_addSysTT[key_addSysTT_job])

          for category in self.evtCategories:
            # sum fake background contributions for the total of all MC sample
            # input processes: TT_fake, TTW_fake, TTWW_fake, ...
            # output process: fakes_mc
            key_hadd_stage1_5_job = getKey(category, lepton_charge_selection, lepton_selection_and_frWeight)
            key_addBackgrounds_dir = getKey("addBackgrounds")
            addBackgrounds_job_fakes_tuple = ("fakes_mc", category, lepton_charge_selection, lepton_selection_and_frWeight)
            key_addBackgrounds_job_fakes = getKey(*addBackgrounds_job_fakes_tuple)
            sample_categories = []
            sample_categories.extend(self.nonfake_backgrounds)
            processes_input = []
            for sample_category in sample_categories:
              processes_input.append("%s_fake" % sample_category)
            self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
              'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_fakes_tuple),
              'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s.root" % addBackgrounds_job_fakes_tuple),
              'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s.log" % addBackgrounds_job_fakes_tuple),
              'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight, lepton_charge_selection) ],
              'processes_input' : processes_input,
              'process_output' : "fakes_mc"
              }
            self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

            # sum conversion background contributions for the total of all MC sample
            # input processes: TT_Convs, TTW_Convs, TTWW_Convs, ...
            # output process: Convs
            addBackgrounds_job_Convs_tuple = ("Convs", category, lepton_charge_selection, lepton_selection)
            key_addBackgrounds_job_Convs = getKey(*addBackgrounds_job_Convs_tuple)
            sample_categories = []
            sample_categories.extend(self.nonfake_backgrounds)
            processes_input = []
            for sample_category in self.convs_backgrounds:
              processes_input.append("%s_Convs" % sample_category)
            self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs] = {
              'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_Convs_tuple),
              'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s.root" % addBackgrounds_job_Convs_tuple),
              'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s.root" % addBackgrounds_job_Convs_tuple),
              'categories' : [ getHistogramDir(category, lepton_selection, lepton_frWeight, lepton_charge_selection) ],
              'processes_input' : processes_input,
              'process_output' : "Convs"
              }
            self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs])

            # initialize input and output file names for hadd_stage2
            key_hadd_stage1_5_job = getKey(category, lepton_charge_selection, lepton_selection_and_frWeight)
            key_hadd_stage2_dir = getKey("hadd", lepton_charge_selection, lepton_selection_and_frWeight)
            hadd_stage2_job_tuple = (category, lepton_charge_selection, lepton_selection_and_frWeight)
            key_hadd_stage2_job = getKey(*hadd_stage2_job_tuple)
            if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
              self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
            if lepton_selection == "Tight":
              self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
              self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs]['outputFile'])
            self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job])
            if self.ttbar_syst_enabled:
              self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addSysTT[key_hadd_stage1_5_job]['outputFile'])
            self.outputFile_hadd_stage2[key_hadd_stage2_job] = os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST],
                                                                            "hadd_stage2_%s_%s_%s.root" % hadd_stage2_job_tuple)


    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for lepton_charge_selection in self.lepton_charge_selections:
      for category in self.evtCategories:
        key_hadd_stage1_5_job = getKey(category, lepton_charge_selection, get_lepton_selection_and_frWeight("Fakeable", "enabled"))
        key_addFakes_dir = getKey("addBackgroundLeptonFakes")
        addFakes_job_tuple = (category, lepton_charge_selection, category)
        key_addFakes_job = getKey("data_fakes", *addFakes_job_tuple)
        self.jobOptions_addFakes[key_addFakes_job] = {
          'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
          'cfgFile_modified' : os.path.join(self.dirs[key_addFakes_dir][DKEY_CFGS], "addBackgroundLeptonFakes_%s_%s_%s_cfg.py" % addFakes_job_tuple),
          'outputFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_HIST], "addBackgroundLeptonFakes_%s_%s_%s.root" % addFakes_job_tuple),
          'logFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_LOGS], "addBackgroundLeptonFakes_%s_%s_%s.log" % addFakes_job_tuple),
          'category_signal' : getHistogramDir(category, "Tight", "disabled", lepton_charge_selection),
          'category_sideband' : getHistogramDir(category, "Fakeable", "enabled", lepton_charge_selection)
        }
        self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
        key_hadd_stage2_job = getKey(category, lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
        self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    logging.info("Creating configuration files to run 'prepareDatacards'")
    for lepton_charge_selection in self.lepton_charge_selections:
      for category in self.evtCategories:
        for histogramToFit in self.histograms_to_fit:
          key_hadd_stage2_job = getKey(category, lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
          key_prep_dcard_dir = getKey("prepareDatacards")
          prep_dcard_job_tuple = (self.channel, category, lepton_charge_selection, histogramToFit)
          key_prep_dcard_job = getKey(category, lepton_charge_selection, histogramToFit)
          self.jobOptions_prep_dcard[key_prep_dcard_job] = {
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_%s_%s_%s_cfg.py" % prep_dcard_job_tuple),
            'datacardFile' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_%s_%s_%s.root" % prep_dcard_job_tuple),
            'histogramDir' : getHistogramDir(category, "Tight", "disabled", lepton_charge_selection),
            'histogramToFit' : histogramToFit
          }
          self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

          # add shape templates for the following systematic uncertainties:
          #  - 'CMS_ttHl_Clos_norm_e'
          #  - 'CMS_ttHl_Clos_shape_e'
          #  - 'CMS_ttHl_Clos_norm_m'
          #  - 'CMS_ttHl_Clos_shape_m'
          key_add_syst_fakerate_dir = getKey("addSystFakeRates")
          add_syst_fakerate_job_tuple = (self.channel, category, lepton_charge_selection, histogramToFit)
          key_add_syst_fakerate_job = getKey(category, lepton_charge_selection, histogramToFit)
          self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
            'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
            'cfgFile_modified' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_CFGS], "addSystFakeRates_%s_%s_%s_%s_cfg.py" % add_syst_fakerate_job_tuple),
            'outputFile' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_DCRD], "addSystFakeRates_%s_%s_%s_%s.root" % add_syst_fakerate_job_tuple),
            'category' : category,
            'histogramToFit' : histogramToFit,
            'plots_outputFileName' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_PLOT], "addSystFakeRates.png")
          }
          histogramDir_nominal = getHistogramDir(category, "Tight", "disabled", lepton_charge_selection)
          for lepton_type in [ 'e', 'm' ]:
            lepton_mcClosure = "Fakeable_mcClosure_%s" % lepton_type
            if lepton_mcClosure not in self.lepton_selections:
              continue
            lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_mcClosure, "enabled")
            key_addBackgrounds_job_fakes = getKey("fakes_mc", category, lepton_charge_selection, lepton_selection_and_frWeight)
            histogramDir_mcClosure = self.mcClosure_dir[lepton_mcClosure]
            histogramDir_mcClosure = histogramDir_mcClosure.replace(self.evtcategory_inclusive, category)
            self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
              'add_Clos_%s' % lepton_type : ("Fakeable_mcClosure_%s" % lepton_type) in self.lepton_selections,
              'inputFile_nominal_%s' % lepton_type : self.outputFile_hadd_stage2[key_hadd_stage2_job],
              'histogramName_nominal_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_nominal, histogramToFit),
              'inputFile_mcClosure_%s' % lepton_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
              'histogramName_mcClosure_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_mcClosure, histogramToFit)
            })
          self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")
    for lepton_charge_selection in self.lepton_charge_selections:
      key_hadd_stage2_job = getKey(self.evtcategory_inclusive, lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
      key_makePlots_dir = getKey("makePlots")
      key_makePlots_job_inclusive = getKey(lepton_charge_selection)
      self.jobOptions_make_plots[key_makePlots_job_inclusive] = {    
        'executable' : self.executable_make_plots,
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
        'cfgFile_original' : self.cfgFile_make_plots_inclusive,
        'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_%s_cfg.py" % (self.channel, lepton_charge_selection, self.evtcategory_inclusive)),
        'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s_%s.png" % (self.channel, lepton_charge_selection, self.evtcategory_inclusive)),
        'categories' : [ self.evtcategory_inclusive ],
        'lepton_charge_selection' : lepton_charge_selection,
        'make_plots_backgrounds' : self.make_plots_backgrounds
      }
      self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job_inclusive])
      
      for category in self.evtCategories :
        key_makePlots_job_in_categories = getKey(category, lepton_charge_selection)
        key_hadd_stage2_job = getKey(category, lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
        self.jobOptions_make_plots[key_makePlots_job_in_categories] = {
          'executable' : self.executable_make_plots,
          'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
          'cfgFile_original' : self.cfgFile_make_plots_in_categories,
          'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_%s_cfg.py" % (self.channel, lepton_charge_selection, category)),
          'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s_%s.png" % (self.channel, lepton_charge_selection, category)),
          'categories' : [ category ],
          'lepton_charge_selection' : lepton_charge_selection,
          'make_plots_backgrounds' : self.make_plots_backgrounds
        }
        self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job_in_categories])
        if "Fakeable_mcClosure" in self.lepton_selections: #TODO
          key_makePlots_job_mcClosure = getKey(lepton_charge_selection)
          key_hadd_stage2 = getKey(lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
          self.jobOptions_make_plots[key_makePlots_job_mcClosure] = {
            'executable' : self.executable_make_plots_mcClosure,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_mcClosure_%s_%s_cfg.py" % (self.channel, lepton_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_mcClosure_%s_%s.png" % (self.channel, lepton_charge_selection))
          }
          self.createCfg_makePlots_mcClosure(self.jobOptions_make_plots[key_makePlots_job_mcClosure])

    logging.info("Creating configuration files to run hadd stage2 harvesting")
    for lepton_charge_selection in self.lepton_charge_selections:
      key_hadd_stage2_harvest_job = getKey(lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
      key_hadd_stage2_dir = getKey("hadd", lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
      inputFiles_hadd_stage2_harvest = []
      for category in self.evtCategories:
        key_hadd_stage2_job = getKey(category, lepton_charge_selection, get_lepton_selection_and_frWeight("Tight", "disabled"))
        inputFiles_hadd_stage2_harvest.append(self.outputFile_hadd_stage2[key_hadd_stage2_job])
      key_prep_dcard_dir = getKey("prepareDatacards")
      self.jobOptions_hadd_stage2_harvest[key_hadd_stage2_harvest_job] = {
        'inputFiles' : inputFiles_hadd_stage2_harvest,
        'outputFile' : os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST], "hadd_harvested_stage2_%s.root" % key_hadd_stage2_harvest_job),
      }

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_copyHistograms)
      self.sbatchFile_copyHistograms = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_copyHistograms_%s.py" % self.channel)
      self.createScript_sbatch_copyHistograms(self.executable_copyHistograms, self.sbatchFile_copyHistograms, self.jobOptions_copyHistograms)
      if self.ttbar_syst_enabled:
        logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addSysTT)
        self.sbatchFile_addSysTT = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addSysTT_%s.py" % self.channel)
        self.createScript_sbatch_addSysTT(self.executable_addSysTT, self.sbatchFile_addSysTT, self.jobOptions_addSysTT)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addBackgrounds)
      self.sbatchFile_addBackgrounds = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
      self.sbatchFile_addBackgrounds_sum = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_sum_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFakes)
      self.sbatchFile_addFakes = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFakes_%s.py" % self.channel)
      self.createScript_sbatch_addFakes(self.executable_addFakes, self.sbatchFile_addFakes, self.jobOptions_addFakes)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_copyHistograms(lines_makefile, make_target = "phony_copyHistograms", make_dependency = "phony_hadd_stage1")
    self.addToMakefile_backgrounds_from_data(lines_makefile, make_dependency = "phony_copyHistograms")
    if self.ttbar_syst_enabled:
      self.addToMakefile_addSysTT(lines_makefile, make_target = "phony_addSysTT", make_dependency = "phony_hadd_stage1_5")
      assert(self.make_dependency_hadd_stage2)
      self.make_dependency_hadd_stage2 += " phony_addSysTT" # note the space!
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_add_syst_fakerate(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.addToMakefile_harvest_hadd_stage2(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
