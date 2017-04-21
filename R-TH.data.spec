#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-TH.data
Version  : 1.0.8
Release  : 6
URL      : https://cran.r-project.org/src/contrib/TH.data_1.0-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TH.data_1.0-8.tar.gz
Summary  : TH's Data Archive
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
**********************************************************************
*  Reproducibility Information for
*  Spatio-Phylogenetic Multi-Species Distribution Models
*  by A. Kaldhusdal, R. Brandl, J. Mueller, L. Moest and T. Hothorn
**********************************************************************

%prep
%setup -q -c -n TH.data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492808672

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492808672
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TH.data
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library TH.data


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/TH.data/DESCRIPTION
/usr/lib64/R/library/TH.data/INDEX
/usr/lib64/R/library/TH.data/Meta/Rd.rds
/usr/lib64/R/library/TH.data/Meta/data.rds
/usr/lib64/R/library/TH.data/Meta/demo.rds
/usr/lib64/R/library/TH.data/Meta/features.rds
/usr/lib64/R/library/TH.data/Meta/hsearch.rds
/usr/lib64/R/library/TH.data/Meta/links.rds
/usr/lib64/R/library/TH.data/Meta/nsInfo.rds
/usr/lib64/R/library/TH.data/Meta/package.rds
/usr/lib64/R/library/TH.data/NAMESPACE
/usr/lib64/R/library/TH.data/PSGLMM_MEE/R/makeData.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/R/makeEnvir.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/R/psglmm.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/R/psglmmSim.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/README.txt
/usr/lib64/R/library/TH.data/PSGLMM_MEE/analysis_birdData/mBirdsESM1_2.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/analysis_birdData/mBirdsESM3_2.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel11.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel11bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel11pois.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel12.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel12bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel12pois.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel13.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel13bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel13pois.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel21.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel21bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel21pois.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel22.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel22bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel22pois.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel23.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel23bin.R
/usr/lib64/R/library/TH.data/PSGLMM_MEE/simulationStudy/simModel23pois.R
/usr/lib64/R/library/TH.data/data/Rdata.rdb
/usr/lib64/R/library/TH.data/data/Rdata.rds
/usr/lib64/R/library/TH.data/data/Rdata.rdx
/usr/lib64/R/library/TH.data/demo/PROACT.R
/usr/lib64/R/library/TH.data/help/AnIndex
/usr/lib64/R/library/TH.data/help/TH.data.rdb
/usr/lib64/R/library/TH.data/help/TH.data.rdx
/usr/lib64/R/library/TH.data/help/aliases.rds
/usr/lib64/R/library/TH.data/help/paths.rds
/usr/lib64/R/library/TH.data/html/00Index.html
/usr/lib64/R/library/TH.data/html/R.css
/usr/lib64/R/library/TH.data/rda/AML_Bullinger.rda
/usr/lib64/R/library/TH.data/rda/BavarianDVCs.rda
/usr/lib64/R/library/TH.data/rda/CHFLS.rda
/usr/lib64/R/library/TH.data/rda/birdsData.rda
