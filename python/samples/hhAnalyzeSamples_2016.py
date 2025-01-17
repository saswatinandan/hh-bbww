from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2016_base import samples_2016 as samples_2016_bkg
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016_hh import samples_2016 as samples_2016_hh
from hhAnalysis.bbww.samples.hhAnalyzeSamples_2016_ttbar import samples_2016 as samples_2016_ttbar

from hhAnalysis.bbww.samples.reclassifySamples import reclassifySamples
samples_2016 = reclassifySamples(samples_2016_hh, samples_2016_bkg, samples_2016_ttbar, separate_ST = True)
