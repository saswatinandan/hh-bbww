from collections import OrderedDict as OD

# file generated at 2020-10-24 22:13:41 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh_sync_ttbar.py -p /local/karl/ttHNtupleProduction/2017/2020Oct24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_sync_ttbar.py -M

samples_2017 = OD()
samples_2017["/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "background"),
  ("process_name_specific",           "TTTo2L2Nu_PSweights"),
  ("nof_files",                       1),
  ("nof_db_files",                    1056),
  ("nof_events",                      {
    'Count'                                                                          : [ 47260, ],
    'CountWeighted'                                                                  : [ 4.68950742e+04, 4.69030430e+04, 4.68932070e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.28974219e+04, 5.19187930e+04, 5.12783203e+04, 4.80958945e+04, 4.68946445e+04, 4.59748320e+04, 4.35111367e+04, 4.22300469e+04, 4.11789414e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.71396523e+04, 3.84007734e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.69400781e+04, 4.69233828e+04, 6.63701875e+04, 4.68366289e+04, 4.68362266e+04, 2.93100527e+04, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.72579656e+05, 4.72575188e+05, 4.72579656e+05, 4.72579656e+05, 4.72328312e+05, 4.72323844e+05, ],
    'CountWeightedFull'                                                              : [ 3.40786950e+06, 3.40834225e+06, 3.40791625e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.84409775e+06, 3.77299200e+06, 3.72646125e+06, 3.49517650e+06, 3.40780925e+06, 3.34106025e+06, 3.16202500e+06, 3.06891275e+06, 2.99252175e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.15238400e+06, 2.79062300e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.41118775e+06, 3.40998525e+06, 4.82322100e+06, 3.40367400e+06, 3.40365900e+06, 2.13000000e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.43436640e+07, 3.43433400e+07, 3.43436640e+07, 3.43436640e+07, 3.43254040e+07, 3.43250800e+07, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.55159727e+04, 4.55201758e+04, 4.55147344e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.55159727e+04, 4.51778867e+04, 4.58456055e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.13078984e+04, 5.03719102e+04, 4.97623477e+04, 4.66682578e+04, 4.55152422e+04, 4.46325156e+04, 4.22305000e+04, 4.09981445e+04, 3.99871289e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.54348789e+04, 3.72820117e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.55688125e+04, 4.55337383e+04, 6.44073633e+04, 4.54455859e+04, 4.54784805e+04, 2.84610215e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 4.58543469e+05, 4.58539125e+05, 4.58543469e+05, 4.58543469e+05, 4.58304500e+05, 4.58300188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.30765300e+06, 3.30790300e+06, 3.30770500e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.30765300e+06, 3.28308700e+06, 3.33160500e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.72859675e+06, 3.66057800e+06, 3.61628650e+06, 3.39143675e+06, 3.30758325e+06, 3.24347775e+06, 3.06896175e+06, 2.97939325e+06, 2.90589750e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.02850825e+06, 2.70932175e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.31154025e+06, 3.30900550e+06, 4.68057900e+06, 3.30256525e+06, 3.30498450e+06, 2.06830625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.33231780e+07, 3.33228600e+07, 3.33231780e+07, 3.33231780e+07, 3.33058240e+07, 3.33055020e+07, ],
    'CountWeightedTOP16011TopPtRwgtSF'                                               : [ 4.69298672e+04, 4.69352969e+04, 4.69225508e+04, ],
    'CountWeightedTOP16011TopPtRwgtSFSquared'                                        : [ 4.70240312e+04, 4.70311211e+04, 4.70143320e+04, ],
    'CountWeightedLinearTopPtRwgtSF'                                                 : [ 4.69625430e+04, 4.69680938e+04, 4.69556289e+04, ],
    'CountWeightedLinearTopPtRwgtSFSquared'                                          : [ 4.70795352e+04, 4.70869219e+04, 4.70704727e+04, ],
    'CountWeightedQuadraticTopPtRwgtSF'                                              : [ 4.69725781e+04, 4.69784766e+04, 4.69650742e+04, ],
    'CountWeightedQuadraticTopPtRwgtSFSquared'                                       : [ 4.71233867e+04, 4.71314766e+04, 4.71137773e+04, ],
    'CountWeightedHighPtTopPtRwgtSF'                                                 : [ 4.69673047e+04, 4.69730547e+04, 4.69605977e+04, ],
    'CountWeightedHighPtTopPtRwgtSFSquared'                                          : [ 4.70893086e+04, 4.70965391e+04, 4.70800234e+04, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSF'                                 : [ 5.29414023e+04, 5.19672500e+04, 5.13309766e+04, 4.81212266e+04, 4.69284141e+04, 4.60139883e+04, 4.35230664e+04, 4.22506602e+04, 4.12069922e+04, ],
    'CountWeightedLHEWeightScaleTOP16011TopPtRwgtSFSquared'                          : [ 5.30543906e+04, 5.20827383e+04, 5.14504062e+04, 4.82097148e+04, 4.70225312e+04, 4.61122578e+04, 4.35923672e+04, 4.23271602e+04, 4.12884219e+04, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSF'                                   : [ 5.29778047e+04, 5.20024297e+04, 5.13663008e+04, 4.81551680e+04, 4.69610820e+04, 4.60450703e+04, 4.35545039e+04, 4.22807461e+04, 4.12353477e+04, ],
    'CountWeightedLHEWeightScaleLinearTopPtRwgtSFSquared'                            : [ 5.31164414e+04, 5.21432891e+04, 5.15099258e+04, 4.82681602e+04, 4.70780586e+04, 4.61662227e+04, 4.36467305e+04, 4.23782891e+04, 4.13378477e+04, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSF'                                : [ 5.29930938e+04, 5.20176797e+04, 5.13807656e+04, 4.81646445e+04, 4.69710820e+04, 4.60557031e+04, 4.35599141e+04, 4.22869805e+04, 4.12425547e+04, ],
    'CountWeightedLHEWeightScaleQuadraticTopPtRwgtSFSquared'                         : [ 5.31738555e+04, 5.21997617e+04, 5.15656055e+04, 4.83112070e+04, 4.71218789e+04, 4.62102812e+04, 4.36795547e+04, 4.24127812e+04, 4.13732734e+04, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSF'                                   : [ 5.29859375e+04, 5.20095234e+04, 5.13710273e+04, 4.81609492e+04, 4.69659180e+04, 4.60490195e+04, 4.35590703e+04, 4.22841914e+04, 4.12382227e+04, ],
    'CountWeightedLHEWeightScaleHighPtTopPtRwgtSFSquared'                            : [ 5.31330273e+04, 5.21570234e+04, 5.15208672e+04, 4.82796758e+04, 4.70877070e+04, 4.61736758e+04, 4.36555977e+04, 4.23853633e+04, 4.13427891e+04, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSF'                                    : [ 5.71638828e+04, 3.84503164e+04, ],
    'CountWeightedLHEEnvelopeTOP16011TopPtRwgtSFSquared'                             : [ 5.72639102e+04, 3.85484961e+04, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSF'                                      : [ 5.72051875e+04, 3.84747422e+04, ],
    'CountWeightedLHEEnvelopeLinearTopPtRwgtSFSquared'                               : [ 5.73345859e+04, 3.85908906e+04, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSF'                                   : [ 5.72171797e+04, 3.84852500e+04, ],
    'CountWeightedLHEEnvelopeQuadraticTopPtRwgtSFSquared'                            : [ 5.73871758e+04, 3.86314688e+04, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSF'                                      : [ 5.72142188e+04, 3.84763477e+04, ],
    'CountWeightedLHEEnvelopeHighPtTopPtRwgtSFSquared'                               : [ 5.73521484e+04, 3.85938477e+04, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSF'                                       : [ 4.69733516e+04, 4.69589492e+04, 6.64041016e+04, 4.68682734e+04, 4.68722148e+04, 2.93451367e+04, ],
    'CountWeightedPSWeightTOP16011TopPtRwgtSFSquared'                                : [ 4.70684219e+04, 4.70555781e+04, 6.65246562e+04, 4.69608516e+04, 4.69696016e+04, 2.94185410e+04, ],
    'CountWeightedPSWeightLinearTopPtRwgtSF'                                         : [ 4.70061797e+04, 4.69911445e+04, 6.64511953e+04, 4.69009688e+04, 4.69046289e+04, 2.93647148e+04, ],
    'CountWeightedPSWeightLinearTopPtRwgtSFSquared'                                  : [ 4.71239922e+04, 4.71108984e+04, 6.66046406e+04, 4.70171562e+04, 4.70249141e+04, 2.94517344e+04, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSF'                                      : [ 4.70160273e+04, 4.70014766e+04, 6.64621484e+04, 4.69109102e+04, 4.69150078e+04, 2.93734473e+04, ],
    'CountWeightedPSWeightQuadraticTopPtRwgtSFSquared'                               : [ 4.71682773e+04, 4.71552188e+04, 6.66595938e+04, 4.70608516e+04, 4.70683125e+04, 2.94843848e+04, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSF'                                         : [ 4.70109180e+04, 4.69960742e+04, 6.64580703e+04, 4.69059844e+04, 4.69092930e+04, 2.93667949e+04, ],
    'CountWeightedPSWeightHighPtTopPtRwgtSFSquared'                                  : [ 4.71336406e+04, 4.71201172e+04, 6.66186250e+04, 4.70270078e+04, 4.70338164e+04, 2.94558770e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                         : [ 4.72810938e+05, 4.72806469e+05, 4.72810938e+05, 4.72810938e+05, 4.72560562e+05, 4.72556156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'                  : [ 4.73677312e+05, 4.73672969e+05, 4.73677312e+05, 4.73677312e+05, 4.73427375e+05, 4.73423031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                           : [ 4.73146750e+05, 4.73142344e+05, 4.73146750e+05, 4.73146750e+05, 4.72896156e+05, 4.72891750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                    : [ 4.74257562e+05, 4.74253219e+05, 4.74257562e+05, 4.74257562e+05, 4.74007531e+05, 4.74003156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                        : [ 4.73238594e+05, 4.73234125e+05, 4.73238594e+05, 4.73238594e+05, 4.72988219e+05, 4.72983812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'                 : [ 4.74676375e+05, 4.74672062e+05, 4.74676375e+05, 4.74676375e+05, 4.74426344e+05, 4.74422031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSF'                           : [ 4.73204625e+05, 4.73200188e+05, 4.73204625e+05, 4.73204625e+05, 4.72953844e+05, 4.72949406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPHighPtTopPtRwgtSFSquared'                    : [ 4.74363719e+05, 4.74359375e+05, 4.74363719e+05, 4.74363719e+05, 4.74113125e+05, 4.74108750e+05, ],
    'CountWeightedFullTOP16011TopPtRwgtSF'                                           : [ 3.41045050e+06, 3.41088900e+06, 3.40992075e+06, ],
    'CountWeightedFullTOP16011TopPtRwgtSFSquared'                                    : [ 3.41726100e+06, 3.41778950e+06, 3.41659650e+06, ],
    'CountWeightedFullLinearTopPtRwgtSF'                                             : [ 3.41282850e+06, 3.41324825e+06, 3.41231975e+06, ],
    'CountWeightedFullLinearTopPtRwgtSFSquared'                                      : [ 3.42136375e+06, 3.42188875e+06, 3.42069250e+06, ],
    'CountWeightedFullQuadraticTopPtRwgtSF'                                          : [ 3.41355700e+06, 3.41398025e+06, 3.41300100e+06, ],
    'CountWeightedFullQuadraticTopPtRwgtSFSquared'                                   : [ 3.42450000e+06, 3.42511275e+06, 3.42380300e+06, ],
    'CountWeightedFullHighPtTopPtRwgtSF'                                             : [ 3.41317475e+06, 3.41360550e+06, 3.41269050e+06, ],
    'CountWeightedFullHighPtTopPtRwgtSFSquared'                                      : [ 3.42202575e+06, 3.42252250e+06, 3.42137150e+06, ],
    'CountWeightedFullLHEWeightScaleTOP16011TopPtRwgtSF'                             : [ 3.84730750e+06, 3.77649650e+06, 3.73031875e+06, 3.49701075e+06, 3.41035100e+06, 3.34387750e+06, 3.16288450e+06, 3.07041625e+06, 2.99456450e+06, ],
    'CountWeightedFullLHEWeightScaleTOP16011TopPtRwgtSFSquared'                      : [ 3.85551200e+06, 3.78494500e+06, 3.73900325e+06, 3.50342275e+06, 3.41715300e+06, 3.35103050e+06, 3.16791500e+06, 3.07595925e+06, 3.00049600e+06, ],
    'CountWeightedFullLHEWeightScaleLinearTopPtRwgtSF'                               : [ 3.84996725e+06, 3.77910550e+06, 3.73285850e+06, 3.49950100e+06, 3.41273000e+06, 3.34618275e+06, 3.16515600e+06, 3.07258700e+06, 2.99664150e+06, ],
    'CountWeightedFullLHEWeightScaleLinearTopPtRwgtSFSquared'                        : [ 3.86005100e+06, 3.78937300e+06, 3.74329450e+06, 3.50770025e+06, 3.42125825e+06, 3.35497575e+06, 3.17184825e+06, 3.07968800e+06, 3.00408075e+06, ],
    'CountWeightedFullLHEWeightScaleQuadraticTopPtRwgtSF'                            : [ 3.85107475e+06, 3.78020425e+06, 3.73394300e+06, 3.50019500e+06, 3.41345650e+06, 3.34692225e+06, 3.16557525e+06, 3.07304250e+06, 2.99717000e+06, ],
    'CountWeightedFullLHEWeightScaleQuadraticTopPtRwgtSFSquared'                     : [ 3.86419525e+06, 3.79344400e+06, 3.74733300e+06, 3.51082950e+06, 3.42439200e+06, 3.35819050e+06, 3.17425650e+06, 3.08219375e+06, 3.00665125e+06, ],
    'CountWeightedFullLHEWeightScaleHighPtTopPtRwgtSF'                               : [ 3.85053500e+06, 3.77957725e+06, 3.73321450e+06, 3.49994575e+06, 3.41306375e+06, 3.34642925e+06, 3.16552550e+06, 3.07286100e+06, 2.99682800e+06, ],
    'CountWeightedFullLHEWeightScaleHighPtTopPtRwgtSFSquared'                        : [ 3.86121625e+06, 3.79030850e+06, 3.74411325e+06, 3.50854650e+06, 3.42191975e+06, 3.35549250e+06, 3.17247825e+06, 3.08017550e+06, 3.00443525e+06, ],
    'CountWeightedFullLHEEnvelopeTOP16011TopPtRwgtSF'                                : [ 4.15415875e+06, 2.79421150e+06, ],
    'CountWeightedFullLHEEnvelopeTOP16011TopPtRwgtSFSquared'                         : [ 4.16143200e+06, 2.80136900e+06, ],
    'CountWeightedFullLHEEnvelopeLinearTopPtRwgtSF'                                  : [ 4.15720525e+06, 2.79602975e+06, ],
    'CountWeightedFullLHEEnvelopeLinearTopPtRwgtSFSquared'                           : [ 4.16661550e+06, 2.80443275e+06, ],
    'CountWeightedFullLHEEnvelopeQuadraticTopPtRwgtSF'                               : [ 4.15804225e+06, 2.79678000e+06, ],
    'CountWeightedFullLHEEnvelopeQuadraticTopPtRwgtSFSquared'                        : [ 4.17042225e+06, 2.80738750e+06, ],
    'CountWeightedFullLHEEnvelopeHighPtTopPtRwgtSF'                                  : [ 4.15782600e+06, 2.79610175e+06, ],
    'CountWeightedFullLHEEnvelopeHighPtTopPtRwgtSFSquared'                           : [ 4.16783875e+06, 2.80466300e+06, ],
    'CountWeightedFullPSWeightTOP16011TopPtRwgtSF'                                   : [ 3.41366725e+06, 3.41256300e+06, 4.82571950e+06, 3.40597100e+06, 3.40630150e+06, 2.13256525e+06, ],
    'CountWeightedFullPSWeightTOP16011TopPtRwgtSFSquared'                            : [ 3.42053450e+06, 3.41960800e+06, 4.83441650e+06, 3.41270425e+06, 3.41335775e+06, 2.13788850e+06, ],
    'CountWeightedFullPSWeightLinearTopPtRwgtSF'                                     : [ 3.41600900e+06, 3.41493850e+06, 4.82908550e+06, 3.40837200e+06, 3.40864675e+06, 2.13397925e+06, ],
    'CountWeightedFullPSWeightLinearTopPtRwgtSFSquared'                              : [ 3.42458750e+06, 3.42360225e+06, 4.84029100e+06, 3.41681250e+06, 3.41735800e+06, 2.14029800e+06, ],
    'CountWeightedFullPSWeightQuadraticTopPtRwgtSF'                                  : [ 3.41670800e+06, 3.41566900e+06, 4.82986200e+06, 3.40908175e+06, 3.40936700e+06, 2.13461275e+06, ],
    'CountWeightedFullPSWeightQuadraticTopPtRwgtSFSquared'                           : [ 3.42777925e+06, 3.42682650e+06, 4.84426200e+06, 3.41998275e+06, 3.42052550e+06, 2.14266975e+06, ],
    'CountWeightedFullPSWeightHighPtTopPtRwgtSF'                                     : [ 3.41634300e+06, 3.41525900e+06, 4.82962600e+06, 3.40872300e+06, 3.40899125e+06, 2.13412350e+06, ],
    'CountWeightedFullPSWeightHighPtTopPtRwgtSFSquared'                              : [ 3.42526100e+06, 3.42427800e+06, 4.84130850e+06, 3.41750525e+06, 3.41804525e+06, 2.14060550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPTOP16011TopPtRwgtSF'                     : [ 3.43598120e+07, 3.43594960e+07, 3.43598120e+07, 3.43598120e+07, 3.43416280e+07, 3.43413120e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPTOP16011TopPtRwgtSFSquared'              : [ 3.44231080e+07, 3.44227880e+07, 3.44231080e+07, 3.44231080e+07, 3.44049480e+07, 3.44046280e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPLinearTopPtRwgtSF'                       : [ 3.43840960e+07, 3.43837720e+07, 3.43840960e+07, 3.43840960e+07, 3.43659000e+07, 3.43655800e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPLinearTopPtRwgtSFSquared'                : [ 3.44650240e+07, 3.44647080e+07, 3.44650240e+07, 3.44650240e+07, 3.44468240e+07, 3.44465080e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPQuadraticTopPtRwgtSF'                    : [ 3.43908840e+07, 3.43905640e+07, 3.43908840e+07, 3.43908840e+07, 3.43726880e+07, 3.43723680e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPQuadraticTopPtRwgtSFSquared'             : [ 3.44955880e+07, 3.44952760e+07, 3.44955880e+07, 3.44955880e+07, 3.44774240e+07, 3.44771080e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPHighPtTopPtRwgtSF'                       : [ 3.43882280e+07, 3.43879080e+07, 3.43882280e+07, 3.43882280e+07, 3.43700080e+07, 3.43696840e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPHighPtTopPtRwgtSFSquared'                : [ 3.44725760e+07, 3.44722600e+07, 3.44725760e+07, 3.44725760e+07, 3.44543960e+07, 3.44540800e+07, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSF'                                   : [ 4.55596875e+04, 4.55630547e+04, 4.55548750e+04, ],
    'CountWeightedL1PrefireNomTOP16011TopPtRwgtSFSquared'                            : [ 4.56616406e+04, 4.56665781e+04, 4.56549648e+04, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSF'                                     : [ 4.55907891e+04, 4.55940234e+04, 4.55862539e+04, ],
    'CountWeightedL1PrefireNomLinearTopPtRwgtSFSquared'                              : [ 4.57143672e+04, 4.57193125e+04, 4.57079727e+04, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSF'                                  : [ 4.56026758e+04, 4.56061641e+04, 4.55976836e+04, ],
    'CountWeightedL1PrefireNomQuadraticTopPtRwgtSFSquared'                           : [ 4.57614219e+04, 4.57671562e+04, 4.57543672e+04, ],
    'CountWeightedL1PrefireNomHighPtTopPtRwgtSF'                                     : [ 4.55950234e+04, 4.55986289e+04, 4.55905664e+04, ],
    'CountWeightedL1PrefireNomHighPtTopPtRwgtSFSquared'                              : [ 4.57235547e+04, 4.57284570e+04, 4.57169414e+04, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSF'                                      : [ 4.55596875e+04, 4.52231680e+04, 4.58873984e+04, ],
    'CountWeightedL1PrefireTOP16011TopPtRwgtSFSquared'                               : [ 4.56616406e+04, 4.53265469e+04, 4.59880156e+04, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSF'                                        : [ 4.55907891e+04, 4.52537070e+04, 4.59188477e+04, ],
    'CountWeightedL1PrefireLinearTopPtRwgtSFSquared'                                 : [ 4.57143672e+04, 4.53782266e+04, 4.60412109e+04, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSF'                                     : [ 4.56026758e+04, 4.52661719e+04, 4.59303828e+04, ],
    'CountWeightedL1PrefireQuadraticTopPtRwgtSFSquared'                              : [ 4.57614219e+04, 4.54261758e+04, 4.60880508e+04, ],
    'CountWeightedL1PrefireHighPtTopPtRwgtSF'                                        : [ 4.55950234e+04, 4.52580820e+04, 4.59231758e+04, ],
    'CountWeightedL1PrefireHighPtTopPtRwgtSFSquared'                                 : [ 4.57235547e+04, 4.53875430e+04, 4.60507578e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                     : [ 5.13640156e+04, 5.04312188e+04, 4.98253711e+04, 4.67045195e+04, 4.55583125e+04, 4.46808516e+04, 4.22522070e+04, 4.10278789e+04, 4.00233359e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'              : [ 5.14868320e+04, 5.05559023e+04, 4.99531680e+04, 4.68017070e+04, 4.56601992e+04, 4.47861836e+04, 4.23295898e+04, 4.11113320e+04, 4.01114336e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                       : [ 5.13982930e+04, 5.04648672e+04, 4.98586250e+04, 4.67366016e+04, 4.55893945e+04, 4.47102109e+04, 4.22822383e+04, 4.10561797e+04, 4.00501602e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'                : [ 5.15452773e+04, 5.06131562e+04, 5.00091211e+04, 4.68567617e+04, 4.57129219e+04, 4.48373750e+04, 4.23808945e+04, 4.11598750e+04, 4.01580273e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                    : [ 5.14159766e+04, 5.04819609e+04, 4.98748984e+04, 4.67478086e+04, 4.56012305e+04, 4.47225312e+04, 4.22893984e+04, 4.10643555e+04, 4.00591641e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'             : [ 5.16062891e+04, 5.06727695e+04, 5.00678438e+04, 4.69032188e+04, 4.57600195e+04, 4.48845156e+04, 4.24169062e+04, 4.11973633e+04, 4.01963398e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSF'                       : [ 5.14060664e+04, 5.04712227e+04, 4.98633242e+04, 4.67418867e+04, 4.55936758e+04, 4.47139492e+04, 4.22864844e+04, 4.10592031e+04, 4.00528516e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSFSquared'                : [ 5.15605898e+04, 5.06258516e+04, 5.00195703e+04, 4.68675469e+04, 4.57220977e+04, 4.48443164e+04, 4.23890664e+04, 4.11663398e+04, 4.01627148e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                        : [ 5.54719805e+04, 3.73390859e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'                 : [ 5.55828320e+04, 3.74435508e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                          : [ 5.55114766e+04, 3.73623047e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'                   : [ 5.56494180e+04, 3.74831953e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                       : [ 5.55255312e+04, 3.73743125e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'                : [ 5.57062266e+04, 3.75262539e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSF'                          : [ 5.55198125e+04, 3.73634453e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSFSquared'                   : [ 5.56660625e+04, 3.74860508e+04, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                           : [ 4.56120977e+04, 4.55795039e+04, 6.44559336e+04, 4.54872070e+04, 4.55238516e+04, 2.85018379e+04, ],
    'CountWeightedPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                    : [ 4.57148281e+04, 4.56844414e+04, 6.45879297e+04, 4.55883828e+04, 4.56284414e+04, 2.85795664e+04, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSF'                             : [ 4.56430469e+04, 4.56100469e+04, 6.45001953e+04, 4.55183438e+04, 4.55544102e+04, 2.85201426e+04, ],
    'CountWeightedPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                      : [ 4.57674297e+04, 4.57362148e+04, 6.46634961e+04, 4.56413008e+04, 4.56808789e+04, 2.86109180e+04, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                          : [ 4.56548086e+04, 4.56224258e+04, 6.45141445e+04, 4.55302383e+04, 4.55665195e+04, 2.85301367e+04, ],
    'CountWeightedPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'                   : [ 4.58146250e+04, 4.57840312e+04, 6.47236758e+04, 4.56882070e+04, 4.57273516e+04, 2.86454707e+04, ],
    'CountWeightedPSWeightL1PrefireNomHighPtTopPtRwgtSF'                             : [ 4.56475117e+04, 4.56143438e+04, 6.45070117e+04, 4.55230000e+04, 4.55590898e+04, 2.85222930e+04, ],
    'CountWeightedPSWeightL1PrefireNomHighPtTopPtRwgtSFSquared'                      : [ 4.57763438e+04, 4.57449414e+04, 6.46767617e+04, 4.56504219e+04, 4.56893203e+04, 2.86149004e+04, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'             : [ 4.58888031e+05, 4.58883750e+05, 4.58888031e+05, 4.58888031e+05, 4.58649906e+05, 4.58645625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'      : [ 4.59840250e+05, 4.59836031e+05, 4.59840250e+05, 4.59840250e+05, 4.59602594e+05, 4.59598375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'               : [ 4.59206406e+05, 4.59202062e+05, 4.59206406e+05, 4.59206406e+05, 4.58967906e+05, 4.58963562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'        : [ 4.60388312e+05, 4.60384062e+05, 4.60388312e+05, 4.60388312e+05, 4.60150156e+05, 4.60145906e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'            : [ 4.59316500e+05, 4.59312188e+05, 4.59316500e+05, 4.59316500e+05, 4.59078094e+05, 4.59073781e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared'     : [ 4.60842062e+05, 4.60837875e+05, 4.60842062e+05, 4.60842062e+05, 4.60603844e+05, 4.60599656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSF'               : [ 4.59256625e+05, 4.59252312e+05, 4.59256625e+05, 4.59256625e+05, 4.59018219e+05, 4.59013969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSFSquared'        : [ 4.60489031e+05, 4.60484844e+05, 4.60489031e+05, 4.60489031e+05, 4.60250625e+05, 4.60246438e+05, ],
    'CountWeightedFullL1PrefireNomTOP16011TopPtRwgtSF'                               : [ 3.31090225e+06, 3.31114200e+06, 3.31053000e+06, ],
    'CountWeightedFullL1PrefireNomTOP16011TopPtRwgtSFSquared'                        : [ 3.31828900e+06, 3.31862400e+06, 3.31781250e+06, ],
    'CountWeightedFullL1PrefireNomLinearTopPtRwgtSF'                                 : [ 3.31313325e+06, 3.31337525e+06, 3.31280100e+06, ],
    'CountWeightedFullL1PrefireNomLinearTopPtRwgtSFSquared'                          : [ 3.32215050e+06, 3.32248750e+06, 3.32167625e+06, ],
    'CountWeightedFullL1PrefireNomQuadraticTopPtRwgtSF'                              : [ 3.31400325e+06, 3.31427000e+06, 3.31363350e+06, ],
    'CountWeightedFullL1PrefireNomQuadraticTopPtRwgtSFSquared'                       : [ 3.32553450e+06, 3.32595200e+06, 3.32501475e+06, ],
    'CountWeightedFullL1PrefireNomHighPtTopPtRwgtSF'                                 : [ 3.31347775e+06, 3.31372100e+06, 3.31313250e+06, ],
    'CountWeightedFullL1PrefireNomHighPtTopPtRwgtSFSquared'                          : [ 3.32278250e+06, 3.32310700e+06, 3.32230075e+06, ],
    'CountWeightedFullL1PrefireTOP16011TopPtRwgtSF'                                  : [ 3.31090225e+06, 3.28643400e+06, 3.33470500e+06, ],
    'CountWeightedFullL1PrefireTOP16011TopPtRwgtSFSquared'                           : [ 3.31828900e+06, 3.29392425e+06, 3.34200625e+06, ],
    'CountWeightedFullL1PrefireLinearTopPtRwgtSF'                                    : [ 3.31313325e+06, 3.28864600e+06, 3.33697400e+06, ],
    'CountWeightedFullL1PrefireLinearTopPtRwgtSFSquared'                             : [ 3.32215050e+06, 3.29773550e+06, 3.34590700e+06, ],
    'CountWeightedFullL1PrefireQuadraticTopPtRwgtSF'                                 : [ 3.31400325e+06, 3.28954675e+06, 3.33782175e+06, ],
    'CountWeightedFullL1PrefireQuadraticTopPtRwgtSFSquared'                          : [ 3.32553450e+06, 3.30115825e+06, 3.34926175e+06, ],
    'CountWeightedFullL1PrefireHighPtTopPtRwgtSF'                                    : [ 3.31347775e+06, 3.28897250e+06, 3.33731400e+06, ],
    'CountWeightedFullL1PrefireHighPtTopPtRwgtSFSquared'                             : [ 3.32278250e+06, 3.29837650e+06, 3.34655275e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSF'                 : [ 3.73268650e+06, 3.66488700e+06, 3.62089900e+06, 3.39406425e+06, 3.31080300e+06, 3.24697875e+06, 3.07052200e+06, 2.98152950e+06, 2.90854725e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomTOP16011TopPtRwgtSFSquared'          : [ 3.74161800e+06, 3.67398775e+06, 3.63018750e+06, 3.40112325e+06, 3.31818625e+06, 3.25467250e+06, 3.07614825e+06, 2.98760625e+06, 2.91496000e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomLinearTopPtRwgtSF'                   : [ 3.73520050e+06, 3.66735725e+06, 3.62329375e+06, 3.39640900e+06, 3.31303625e+06, 3.24916475e+06, 3.07269650e+06, 2.98360150e+06, 2.91052425e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomLinearTopPtRwgtSFSquared'            : [ 3.74586875e+06, 3.67813100e+06, 3.63422800e+06, 3.40514600e+06, 3.32205050e+06, 3.25839475e+06, 3.07987075e+06, 2.99113325e+06, 2.91834025e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSF'                : [ 3.73644600e+06, 3.66860125e+06, 3.62450950e+06, 3.39725225e+06, 3.31390525e+06, 3.25004450e+06, 3.07323450e+06, 2.98420450e+06, 2.91116850e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomQuadraticTopPtRwgtSFSquared'         : [ 3.75028525e+06, 3.68247250e+06, 3.63851725e+06, 3.40853100e+06, 3.32543225e+06, 3.26184475e+06, 3.08249150e+06, 2.99385500e+06, 2.92112375e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSF'                   : [ 3.73572400e+06, 3.66780100e+06, 3.62365675e+06, 3.39682100e+06, 3.31337275e+06, 3.24939700e+06, 3.07302200e+06, 2.98385825e+06, 2.91069975e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNomHighPtTopPtRwgtSFSquared'            : [ 3.74695800e+06, 3.67904650e+06, 3.63500925e+06, 3.40593150e+06, 3.32267550e+06, 3.25889800e+06, 3.08046450e+06, 2.99160600e+06, 2.91869575e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSF'                    : [ 4.03123925e+06, 2.71346850e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomTOP16011TopPtRwgtSFSquared'             : [ 4.03927250e+06, 2.72105650e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomLinearTopPtRwgtSF'                      : [ 4.03409925e+06, 2.71517600e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomLinearTopPtRwgtSFSquared'               : [ 4.04413800e+06, 2.72394125e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSF'                   : [ 4.03511250e+06, 2.71605750e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomQuadraticTopPtRwgtSFSquared'            : [ 4.04825175e+06, 2.72708300e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSF'                      : [ 4.03468475e+06, 2.71526700e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNomHighPtTopPtRwgtSFSquared'               : [ 4.04532050e+06, 2.72415675e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomTOP16011TopPtRwgtSF'                       : [ 3.31472350e+06, 3.31231725e+06, 4.68412600e+06, 3.30561200e+06, 3.30830150e+06, 2.07127825e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomTOP16011TopPtRwgtSFSquared'                : [ 3.32215875e+06, 3.31994275e+06, 4.69367700e+06, 3.31295525e+06, 3.31589525e+06, 2.07692388e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomLinearTopPtRwgtSF'                         : [ 3.31695350e+06, 3.31455800e+06, 4.68732350e+06, 3.30787175e+06, 3.31053025e+06, 2.07262638e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomLinearTopPtRwgtSFSquared'                  : [ 3.32600850e+06, 3.32373125e+06, 4.69922950e+06, 3.31681325e+06, 3.31967325e+06, 2.07919512e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomQuadraticTopPtRwgtSF'                      : [ 3.31778750e+06, 3.31542550e+06, 4.68830850e+06, 3.30874275e+06, 3.31137225e+06, 2.07333412e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomQuadraticTopPtRwgtSFSquared'               : [ 3.32941700e+06, 3.32717475e+06, 4.70354350e+06, 3.32022425e+06, 3.32307475e+06, 2.08170450e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomHighPtTopPtRwgtSF'                         : [ 3.31726575e+06, 3.31485950e+06, 4.68782750e+06, 3.30820300e+06, 3.31083550e+06, 2.07275350e+06, ],
    'CountWeightedFullPSWeightL1PrefireNomHighPtTopPtRwgtSFSquared'                  : [ 3.32664125e+06, 3.32434200e+06, 4.70019800e+06, 3.31746000e+06, 3.32032000e+06, 2.07949438e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSF'         : [ 3.33479960e+07, 3.33476840e+07, 3.33479960e+07, 3.33479960e+07, 3.33306960e+07, 3.33303880e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomTOP16011TopPtRwgtSFSquared'  : [ 3.34175100e+07, 3.34172000e+07, 3.34175100e+07, 3.34175100e+07, 3.34002400e+07, 3.33999320e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSF'           : [ 3.33710340e+07, 3.33707220e+07, 3.33710340e+07, 3.33710340e+07, 3.33537000e+07, 3.33533880e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomLinearTopPtRwgtSFSquared'    : [ 3.34568280e+07, 3.34565200e+07, 3.34568280e+07, 3.34568280e+07, 3.34395140e+07, 3.34392060e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSF'        : [ 3.33793300e+07, 3.33790160e+07, 3.33793300e+07, 3.33793300e+07, 3.33620100e+07, 3.33617000e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomQuadraticTopPtRwgtSFSquared' : [ 3.34901740e+07, 3.34898680e+07, 3.34901740e+07, 3.34901740e+07, 3.34728720e+07, 3.34725660e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSF'           : [ 3.33747860e+07, 3.33744720e+07, 3.33747860e+07, 3.33747860e+07, 3.33574540e+07, 3.33571400e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNomHighPtTopPtRwgtSFSquared'    : [ 3.34642180e+07, 3.34639120e+07, 3.34642180e+07, 3.34642180e+07, 3.34469060e+07, 3.34466000e+07, ],
  }),
  ("nof_tree_events",                 47260),
  ("nof_db_events",                   69155808),
  ("fsize_local",                     218496767), # 218.50MB, avg file size 218.50MB
  ("fsize_db",                        3693271643807), # 3.69TB, avg file size 3.50GB
  ("use_it",                          True),
  ("xsection",                        88.4),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 91400 - 91432 -> PDF4LHC15_nnlo_30_pdfas PDF set, expecting 33 weights (counted 33 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/local/karl/ttHNtupleProduction/2017/2020Oct24_woPresel_nonNom_hh_bbww_sync_ttbar/ntuples/TTTo2L2Nu_PSweights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["sum_events"] = [
]

