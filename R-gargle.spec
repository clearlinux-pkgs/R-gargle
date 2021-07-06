#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gargle
Version  : 1.2.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/gargle_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gargle_1.2.0.tar.gz
Summary  : Utilities for Working with Google APIs
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-fs
Requires: R-glue
Requires: R-httr
Requires: R-jsonlite
Requires: R-mockr
Requires: R-rappdirs
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-fs
BuildRequires : R-glue
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-mockr
BuildRequires : R-rappdirs
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# gargle
<!-- badges: start -->
[![CRAN
status](https://www.r-pkg.org/badges/version/gargle)](https://cran.r-project.org/package=gargle)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/gargle/branch/master/graph/badge.svg)](https://codecov.io/gh/r-lib/gargle?branch=master)
[![R-CMD-check](https://github.com/r-lib/gargle/workflows/R-CMD-check/badge.svg)](https://github.com/r-lib/gargle/actions)
<!-- badges: end -->

%prep
%setup -q -c -n gargle
cd %{_builddir}/gargle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625589304

%install
export SOURCE_DATE_EPOCH=1625589304
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gargle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gargle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gargle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gargle || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gargle/DESCRIPTION
/usr/lib64/R/library/gargle/INDEX
/usr/lib64/R/library/gargle/LICENSE
/usr/lib64/R/library/gargle/Meta/Rd.rds
/usr/lib64/R/library/gargle/Meta/features.rds
/usr/lib64/R/library/gargle/Meta/hsearch.rds
/usr/lib64/R/library/gargle/Meta/links.rds
/usr/lib64/R/library/gargle/Meta/nsInfo.rds
/usr/lib64/R/library/gargle/Meta/package.rds
/usr/lib64/R/library/gargle/Meta/vignette.rds
/usr/lib64/R/library/gargle/NAMESPACE
/usr/lib64/R/library/gargle/NEWS.md
/usr/lib64/R/library/gargle/R/gargle
/usr/lib64/R/library/gargle/R/gargle.rdb
/usr/lib64/R/library/gargle/R/gargle.rdx
/usr/lib64/R/library/gargle/R/sysdata.rdb
/usr/lib64/R/library/gargle/R/sysdata.rdx
/usr/lib64/R/library/gargle/WORDLIST
/usr/lib64/R/library/gargle/discovery-doc-ingest/api-wide-parameter-names.txt
/usr/lib64/R/library/gargle/discovery-doc-ingest/api-wide-parameters-humane.txt
/usr/lib64/R/library/gargle/discovery-doc-ingest/api-wide-parameters.csv
/usr/lib64/R/library/gargle/discovery-doc-ingest/discover-discovery.R
/usr/lib64/R/library/gargle/discovery-doc-ingest/drive-example.R
/usr/lib64/R/library/gargle/discovery-doc-ingest/ingest-functions.R
/usr/lib64/R/library/gargle/discovery-doc-ingest/method-properties-humane.txt
/usr/lib64/R/library/gargle/discovery-doc-ingest/method-properties.csv
/usr/lib64/R/library/gargle/discovery-doc-ingest/method-property-names.txt
/usr/lib64/R/library/gargle/discovery-doc-ingest/parameter-properties-humane.txt
/usr/lib64/R/library/gargle/discovery-doc-ingest/parameter-properties.csv
/usr/lib64/R/library/gargle/discovery-doc-ingest/parameter-property-names.txt
/usr/lib64/R/library/gargle/doc/auth-from-web.R
/usr/lib64/R/library/gargle/doc/auth-from-web.Rmd
/usr/lib64/R/library/gargle/doc/auth-from-web.html
/usr/lib64/R/library/gargle/doc/gargle-auth-in-client-package.R
/usr/lib64/R/library/gargle/doc/gargle-auth-in-client-package.Rmd
/usr/lib64/R/library/gargle/doc/gargle-auth-in-client-package.html
/usr/lib64/R/library/gargle/doc/get-api-credentials.R
/usr/lib64/R/library/gargle/doc/get-api-credentials.Rmd
/usr/lib64/R/library/gargle/doc/get-api-credentials.html
/usr/lib64/R/library/gargle/doc/how-gargle-gets-tokens.R
/usr/lib64/R/library/gargle/doc/how-gargle-gets-tokens.Rmd
/usr/lib64/R/library/gargle/doc/how-gargle-gets-tokens.html
/usr/lib64/R/library/gargle/doc/index.html
/usr/lib64/R/library/gargle/doc/non-interactive-auth.R
/usr/lib64/R/library/gargle/doc/non-interactive-auth.Rmd
/usr/lib64/R/library/gargle/doc/non-interactive-auth.html
/usr/lib64/R/library/gargle/doc/request-helper-functions.R
/usr/lib64/R/library/gargle/doc/request-helper-functions.Rmd
/usr/lib64/R/library/gargle/doc/request-helper-functions.html
/usr/lib64/R/library/gargle/doc/troubleshooting.R
/usr/lib64/R/library/gargle/doc/troubleshooting.Rmd
/usr/lib64/R/library/gargle/doc/troubleshooting.html
/usr/lib64/R/library/gargle/help/AnIndex
/usr/lib64/R/library/gargle/help/aliases.rds
/usr/lib64/R/library/gargle/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/gargle/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/gargle/help/gargle.rdb
/usr/lib64/R/library/gargle/help/gargle.rdx
/usr/lib64/R/library/gargle/help/paths.rds
/usr/lib64/R/library/gargle/html/00Index.html
/usr/lib64/R/library/gargle/html/R.css
/usr/lib64/R/library/gargle/secret/gargle-testing.json
/usr/lib64/R/library/gargle/tests/spelling.R
/usr/lib64/R/library/gargle/tests/testthat.R
/usr/lib64/R/library/gargle/tests/testthat/_snaps/AuthState-class.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/Gargle-class.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/inside-the-house.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/oauth-cache.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/oauth-refresh.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/request-develop.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/request_retry.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/response_process.md
/usr/lib64/R/library/gargle/tests/testthat/_snaps/utils-ui.md
/usr/lib64/R/library/gargle/tests/testthat/fixtures/client_secret_123.googleusercontent.com.json
/usr/lib64/R/library/gargle/tests/testthat/fixtures/client_secret_456.googleusercontent.com.json
/usr/lib64/R/library/gargle/tests/testthat/fixtures/drive-files-get-nonexistent-file-id_404.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/drive-files-get-nonexistent-file-id_404.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/fitness-get-wrong-scope_403.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/fitness-get-wrong-scope_403.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/service-account-token.json
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-api-key-not-enabled_403.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-api-key-not-enabled_403.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-bad-field-mask_400.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-bad-field-mask_400.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-nonexistent-range_400.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-nonexistent-range_400.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-nonexistent-sheet-id_404.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-nonexistent-sheet-id_404.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-quota-exceeded-readgroup_429.R
/usr/lib64/R/library/gargle/tests/testthat/fixtures/sheets-spreadsheets-get-quota-exceeded-readgroup_429.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/tokeninfo-bad-path_404.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/tokeninfo-stale_400.rds
/usr/lib64/R/library/gargle/tests/testthat/fixtures/tokeninfo_40X.R
/usr/lib64/R/library/gargle/tests/testthat/helper.R
/usr/lib64/R/library/gargle/tests/testthat/test-AuthState-class.R
/usr/lib64/R/library/gargle/tests/testthat/test-Gargle-class.R
/usr/lib64/R/library/gargle/tests/testthat/test-aaa.R
/usr/lib64/R/library/gargle/tests/testthat/test-assets.R
/usr/lib64/R/library/gargle/tests/testthat/test-credentials-byo-oauth2.R
/usr/lib64/R/library/gargle/tests/testthat/test-credentials_app_default.R
/usr/lib64/R/library/gargle/tests/testthat/test-fetch.R
/usr/lib64/R/library/gargle/tests/testthat/test-field-mask.R
/usr/lib64/R/library/gargle/tests/testthat/test-gce-token.R
/usr/lib64/R/library/gargle/tests/testthat/test-inside-the-house.R
/usr/lib64/R/library/gargle/tests/testthat/test-oauth-app.R
/usr/lib64/R/library/gargle/tests/testthat/test-oauth-cache.R
/usr/lib64/R/library/gargle/tests/testthat/test-oauth-refresh.R
/usr/lib64/R/library/gargle/tests/testthat/test-registry.R
/usr/lib64/R/library/gargle/tests/testthat/test-request-develop.R
/usr/lib64/R/library/gargle/tests/testthat/test-request-make.R
/usr/lib64/R/library/gargle/tests/testthat/test-request_retry.R
/usr/lib64/R/library/gargle/tests/testthat/test-response_process.R
/usr/lib64/R/library/gargle/tests/testthat/test-token-info.R
/usr/lib64/R/library/gargle/tests/testthat/test-utils-ui.R
/usr/lib64/R/library/gargle/tests/testthat/test-utils.R
