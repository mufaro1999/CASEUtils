# capture the current directory in tarball
WD=$(pwd)
cd $CMSSW_BASE/../
tar --exclude-caches-all --exclude-vcs --exclude-caches-all --exclude-vcs -cvzf H5_env.tgz CMSSW_11_1_4 --exclude=tmp --exclude=".scram" --exclude=".SCRAM" --exclude=CMSSW_11_1_4/src/CASEUtils/H5_maker/logs --exclude=CMSSW_11_1_4/src/CASEUtils/H5_maker/*.h5
xrdcp -f H5_env.tgz root://cmseos.fnal.gov//store/user/$USER/H5_env.tgz
cd ${WD}
