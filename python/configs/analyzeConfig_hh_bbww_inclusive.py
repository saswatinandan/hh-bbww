import logging
import os.path

from hhAnalysis.multilepton.configs.analyzeConfig_hh import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

class analyzeConfig_hh_bbww_inclusive(analyzeConfig_hh):
  def __init__(self,
        configDir,
        localDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        lep_mva_wp,
        samples,
        era,
        output_tree,
        check_output_files,
        running_method,
        dry_run,
        isDebug,
        rle_select,
        central_or_shifts,
        jet_cleaning_by_index,
        gen_matching_by_index,
        use_nonnominal = False,
        use_home       = False,
        keep_logs      = False,
        submission_cmd = None,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      localDir              = localDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_bbww_inclusive",
      samples               = samples,
      jet_cleaning_by_index = jet_cleaning_by_index,
      gen_matching_by_index = gen_matching_by_index,
      central_or_shifts     = central_or_shifts,
      max_files_per_job     = 1,
      era                   = era,
      use_lumi              = False,
      lumi                  = -1.,
      check_output_files    = False,
      running_method        = running_method,
      num_parallel_jobs     = 1,
      histograms_to_fit     = [],
      triggers              = [
        '1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu',
        '1e2mu', '2e1mu', '1e1tau', '1mu1tau', '2tau',
      ],
      lep_mva_wp            = lep_mva_wp,
      verbose               = False,
      dry_run               = dry_run,
      isDebug               = isDebug,
      do_sync               = True,
      use_home              = use_home,
      keep_logs             = keep_logs,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'bbww', 'test', 'templates'),
      submission_cmd        = submission_cmd,
      apply_nc_correction   = None,
    )

    self.cfgFile_analyze = cfgFile_analyze
    self.output_tree = output_tree
    self.check_output_files = check_output_files
    self.rle_select = rle_select
    self.use_nonnominal = use_nonnominal

    if self.rle_select and not os.path.isfile(self.rle_select):
      raise ValueError('Input RLE file for the sync is missing: %s' % self.rle_select)

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)

  def createCfg_analyze(self, jobOptions, sample_info):
    lines = super(analyzeConfig_hh_bbww_inclusive, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def create(self):
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      process_name = sample_info["process_name_specific"]
      central_or_shifts_extended = [ "" ]
      central_or_shifts_extended.extend(self.central_or_shifts)
      central_or_shifts_extended.extend([ "hadd", "copyHistograms", "addBackgrounds" ])
      for central_or_shift_or_dummy in central_or_shifts_extended:
        process_name_extended = [ process_name, "hadd" ]
        for process_name_or_dummy in process_name_extended:
          if process_name_or_dummy in [ "hadd" ] and central_or_shift_or_dummy != "":
            continue
          if central_or_shift_or_dummy in [ "hadd", "copyHistograms", "addBackgrounds" ] and process_name_or_dummy in [ "hadd" ]:
            continue
          key_dir = getKey(process_name_or_dummy, central_or_shift_or_dummy)
          for dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
            if dir_type == DKEY_SYNC and not self.do_sync:
              continue
            initDict(self.dirs, [ key_dir, dir_type ])
            if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
              self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel, process_name_or_dummy, central_or_shift_or_dummy)
            else:
              self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, process_name_or_dummy)

    for subdirectory in [ "addBackgrounds", "addBackgroundLeptonFakes", "prepareDatacards", "addSystFakeRates", "makePlots" ]:
      key_dir = getKey(subdirectory)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel, subdirectory)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, subdirectory)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_SYNC, DKEY_HADD_RT ]:
      if dir_type == DKEY_SYNC and not self.do_sync:
        continue
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_HADD_RT ]:
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

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      process_name = sample_info["process_name_specific"]
      logging.info(
        "Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name)
      )
      inputFileList = inputFileLists[sample_name]

      for jobId in inputFileList.keys():
        for central_or_shift in self.central_or_shifts:
          logging.info(" ... for systematic uncertainty %s" % central_or_shift)

          key_analyze_dir = getKey(process_name, central_or_shift)
          analyze_job_tuple = (process_name, central_or_shift, jobId)
          key_analyze_job = getKey(*analyze_job_tuple)
          ntupleFiles = inputFileList[jobId]
          if len(ntupleFiles) == 0:
            print("Warning: no ntupleFiles --> skipping job !!")
            continue

          syncOutput = os.path.join(self.dirs[key_analyze_dir][DKEY_SYNC], '%s_%s.root' % (self.channel, central_or_shift))
          syncOutputTree = self.output_tree if central_or_shift == "central" else os.path.join(central_or_shift, self.output_tree)
          self.inputFiles_sync['sync'].append(syncOutput)

          cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_%s_%i_cfg.py" % analyze_job_tuple)
          logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_%s_%i.log" % analyze_job_tuple)

          self.jobOptions_analyze[key_analyze_job] = {
            'ntupleFiles'             : ntupleFiles,
            'cfgFile_modified'        : cfgFile_modified_path,
            'histogramFile'           : '',
            'logFile'                 : logFile_path,
            'syncTree'                : syncOutputTree,
            'syncOutput'              : syncOutput,
            'syncRLE'                 : self.rle_select if self.rle_select and '%s' not in self.rle_select else '',
            'useNonNominal'           : self.use_nonnominal,
            'useAssocJetBtag'         : self.do_sync,
          }
          self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info)

    logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
    self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
    self.createScript_sbatch_syncNtuple(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_syncNtuple(lines_makefile)
    outputFile_sync_path = os.path.join(self.outputDir, DKEY_SYNC, '%s.root' % self.channel)
    self.outputFile_sync['sync'] = outputFile_sync_path
    self.addToMakefile_hadd_sync(lines_makefile)
    self.targets.extend(self.phoniesToAdd)
    self.createMakefile(lines_makefile)
    logging.info("Done")
    return self.num_jobs
