from hhAnalysis.bbww.samples.tthAnalyzeSamples_2018_preselected_sl import samples_2018 as samples_2018_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_hh_preselected_sl import samples_2018 as samples_2018_hh
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2018_ttbar_preselected_sl import samples_2018 as samples_2018_ttbar

from hhAnalysis.bbww.samples.reclassifySamples import reclassifySamples
samples_2018 = reclassifySamples(samples_2018_hh, samples_2018_bkg, samples_2018_ttbar)
