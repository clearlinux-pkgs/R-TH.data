#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-TH.data
Version  : 1.0.10
Release  : 39
URL      : https://cran.r-project.org/src/contrib/TH.data_1.0-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TH.data_1.0-10.tar.gz
Summary  : TH's Data Archive
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
maintains.

%prep
%setup -q -c -n TH.data
cd %{_builddir}/TH.data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589515952

%install
export SOURCE_DATE_EPOCH=1589515952
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TH.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TH.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TH.data
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc TH.data || :


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
/usr/lib64/R/library/TH.data/rda/ALSFRSdata.rda
/usr/lib64/R/library/TH.data/rda/ALSsurvdata.rda
/usr/lib64/R/library/TH.data/rda/AML_Bullinger.rda
/usr/lib64/R/library/TH.data/rda/BavarianDVCs.rda
/usr/lib64/R/library/TH.data/rda/CHFLS.rda
/usr/lib64/R/library/TH.data/rda/Primary_endpoint_data.rda
/usr/lib64/R/library/TH.data/rda/beetles.rda
/usr/lib64/R/library/TH.data/rda/birdsData.rda
/usr/lib64/R/library/TH.data/rda/fetus.rda
/usr/lib64/R/library/TH.data/rda/india.rda
