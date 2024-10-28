#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pecan
Version  : 1.5.1
Release  : 91
URL      : https://files.pythonhosted.org/packages/11/cb/a0e1972713b25029dd43554da94fdd4a280faa6395218f8f400941e2779b/pecan-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/cb/a0e1972713b25029dd43554da94fdd4a280faa6395218f8f400941e2779b/pecan-1.5.1.tar.gz
Summary  : A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pecan-bin = %{version}-%{release}
Requires: pypi-pecan-license = %{version}-%{release}
Requires: pypi-pecan-python = %{version}-%{release}
Requires: pypi-pecan-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(logutils)
BuildRequires : pypi(mako)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(webob)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Pecan
=====
A WSGI object-dispatching web framework, designed to be lean and fast with few
dependencies.

%package bin
Summary: bin components for the pypi-pecan package.
Group: Binaries
Requires: pypi-pecan-license = %{version}-%{release}

%description bin
bin components for the pypi-pecan package.


%package license
Summary: license components for the pypi-pecan package.
Group: Default

%description license
license components for the pypi-pecan package.


%package python
Summary: python components for the pypi-pecan package.
Group: Default
Requires: pypi-pecan-python3 = %{version}-%{release}

%description python
python components for the pypi-pecan package.


%package python3
Summary: python3 components for the pypi-pecan package.
Group: Default
Requires: python3-core
Provides: pypi(pecan)
Requires: pypi(logutils)
Requires: pypi(mako)
Requires: pypi(setuptools)
Requires: pypi(webob)

%description python3
python3 components for the pypi-pecan package.


%prep
%setup -q -n pecan-1.5.1
cd %{_builddir}/pecan-1.5.1
pushd ..
cp -a pecan-1.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689613004
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pecan
cp %{_builddir}/pecan-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pecan/468e4ca7bcd01061db356986e1746fb35002930d || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.4/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+
rm -f %{buildroot}*/usr/lib/python3.4/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
rm -f %{buildroot}*/usr/lib/python3.4/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/app.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/root.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/controllers/root.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/model
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/model/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/model/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/error.html
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/index.html
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/templates/layout.html
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/__init__.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/config.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_functional.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_units.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/base/+package+/tests/test_units.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/app.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/root.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/controllers/root.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/errors.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/errors.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/model
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/model/__init__.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/model/__init__.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/__init__.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/config.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_functional.py_tmpl
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_units.py
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_units.pyc
rm -f %{buildroot}*/usr/lib/python2.7/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/app.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers/__pycache__/root.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/controllers/root.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/model
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/model/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/model/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/model/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/templates
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/templates/error.html
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/templates/index.html
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/templates/layout.html
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/__init__.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/__pycache__/test_units.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/config.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/test_functional.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/base/+package+/tests/test_units.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/__pycache__/errors.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/app.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers/__pycache__/root.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/controllers/root.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/errors.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/model
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/model/__init__.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/model/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/model/__pycache__/__init__.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/__init__.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/__pycache__
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/__pycache__/test_units.cpython-35.pyc
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/config.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_functional.py_tmpl
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/scaffolds/rest-api/+package+/tests/test_units.py
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/tests/scaffold_fixtures/file_sub/bar_+package+/spam.txt
rm -f %{buildroot}*/usr/lib/python3.5/site-packages/pecan/tests/scaffold_fixtures/file_sub/foo_+package+
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gunicorn_pecan
/usr/bin/pecan

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pecan/468e4ca7bcd01061db356986e1746fb35002930d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
