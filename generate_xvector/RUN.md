# Enviroment prepare

1. Init `Kaldi`
`cd $KALDI_ROOT/egs/sre16/v2`
`source ./path.sh`
`source ./cmd.sh`

2. Add path to usefull scrips
`ln -s $KALDI_ROOT/egs/wsj/s5/steps steps`
`ln -s $KALDI_ROOT/egs/wsj/s5/utils utils`
`ln -s $KALDI_ROOT/egs/sre16/v2/sid/nnet3/xvector`

3. Using `generate_xvecotr_embeddings.ipynb` prepare client voice sample and generate `wav.scp`, `sp2utt` and `utt2spk`. 


# Extract MFCC features
`steps/make_mfcc.sh --nj 24 --mfcc-config conf/mfcc.conf --cmd "run.pl" data/metadata exp/make_mfcc/voice_samples data/samples_mfcc` _Extract MFCC features_
`steps/compute_vad_decision.sh --nj 24 --cmd "run.pl" --vad-config conf/vad.conf data/metadata/ exp/make_vad data/samples_mfcc_vad` _Perform VAD (Voice Activity Detection)_
`xvector/extract_xvectors.sh --cmd "run.pl" --nj 1 --use-gpu true $KALDI_ROOT/egs/0003_sre16_v2_1a/exp/xvector_nnet_1a data/metadata exp/xvectors_clients` _Extract x-vectors_