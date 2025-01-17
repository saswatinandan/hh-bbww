import FWCore.ParameterSet.Config as cms

from hhAnalysis.bbww.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_ll"),
        xAxisTitle = cms.string("m_{ll} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{ll} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_ll"),
        xAxisTitle = cms.string("#Delta R_{ll}"),
        yAxisTitle = cms.string("dN/d#Delta R_{ll}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dPhi_ll"),
        xAxisTitle = cms.string("#Delta#phi_{ll}"),
        yAxisTitle = cms.string("dN/d#Delta#phi_{ll}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_Hbb"),
        xAxisTitle = cms.string("m_{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/pT_Hbb"),
        xAxisTitle = cms.string("p_{T}^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T}^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/dR_Hbb"),
        xAxisTitle = cms.string("#Delta R^{bb} [GeV]"),
        yAxisTitle = cms.string("dN/d#Delta R^{bb} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HHvis"),
        xAxisTitle = cms.string("m_{HH}^{vis} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH}^{vis} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/m_HH_hme"),
        xAxisTitle = cms.string("m_{HH} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{HH} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_pt"),
        xAxisTitle = cms.string("leading VBF jet p_{T} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet1_eta"),
        xAxisTitle = cms.string("leading VBF jet #eta"),
        yAxisTitle = cms.string("dN/d#eta [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_pt"),
        xAxisTitle = cms.string("subleading VBF jet p_{T} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_jet2_eta"),
        xAxisTitle = cms.string("subleading VBF jet #eta"),
        yAxisTitle = cms.string("dN/d#eta")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_m_jj"),
        xAxisTitle = cms.string("VBF jet m_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/vbf_dEta_jj"),
        xAxisTitle = cms.string("VBF jet #Delta#eta_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/d#Delta#eta_{jj}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/pt"),
        xAxisTitle = cms.string("AK8 jet p_{T} [GeV]"),
        yAxisTitle = cms.string("dN/dp_{T} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/eta"),
        xAxisTitle = cms.string("AK8 jet #eta"),
        yAxisTitle = cms.string("dN/d#eta")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/phi"),
        xAxisTitle = cms.string("AK8 jet #phi"),
        yAxisTitle = cms.string("dN/d#phi")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/msoftdrop"),
        xAxisTitle = cms.string("AK8 jet m_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/msubjet"),
        xAxisTitle = cms.string("AK8 jet m_{jj} [GeV]"),
        yAxisTitle = cms.string("dN/dm_{jj} [1/GeV]")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/tau21"),
        xAxisTitle = cms.string("AK8 jet #tau_{21}"),
        yAxisTitle = cms.string("dN/d#tau_{21}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/jetsAK8_Hbb/$PROCESS/dR_subjets"),
        xAxisTitle = cms.string("AK8 jet #Delta R_{jj}"),
        yAxisTitle = cms.string("dN/#Delta R_{jj}")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
        xAxisTitle = cms.string("Run Period"),
        yAxisTitle = cms.string("Events / 1 fb^{-1}"),
        divideByBinWidth = cms.bool(False)
    )
])
