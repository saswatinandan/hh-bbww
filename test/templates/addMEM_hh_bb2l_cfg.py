import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(''),
    skipEvents = cms.uint32(0),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(1000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.addMEM_hh_bb2l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),

    era = cms.string(''),
    isMC = cms.bool(True),
    addMEM_forGenParticles = cms.bool(True),

    leptonSelection = cms.string(''),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8 = cms.string('FatJet'),
    branchName_subjets_ak8 = cms.string('SubJet'),
    branchName_met = cms.string('MET'),
    branchName_vertex = cms.string('PV'),

    branchNames_genParticles = cms.PSet(
        # branches specific to HH->bbWW signal events
        branchName_genLeptons = cms.string('GenLep'),
        branchName_genNeutrinos = cms.string('GenNu'),
        branchName_genParticlesFromHiggs = cms.string('GenHiggsDaughters'),
        
        # branches specific to tt+jets background events   
        branchName_genLeptonsFromTop = cms.string('GenLepFromTop'),
        branchName_genNeutrinosFromTop = cms.string('GenNuFromTop'),
        branchName_genBJetsFromTop = cms.string('GenBQuarkFromTop'),
    ),

    copy_all_branches = cms.bool(True),
    copy_histograms = cms.vstring('Count.*'),

    selEventsFileName_input = cms.string(''),
    isDEBUG = cms.bool(False),
    readGenObjects = cms.bool(True),
    isForBDTtraining = cms.bool(False),

    central_or_shift = cms.vstring(),
    jetCleaningByIndex = cms.bool(True),
    useNonNominal = cms.bool(False),
    dryRun = cms.bool(False),
)
