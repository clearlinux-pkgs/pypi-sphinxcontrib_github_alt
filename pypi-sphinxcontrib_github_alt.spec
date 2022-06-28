#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxcontrib_github_alt
Version  : 1.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/b8/d5/2880f4f441f3b46f264cb031d9e7135714b5060c895c8a6458051002c41a/sphinxcontrib_github_alt-1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/d5/2880f4f441f3b46f264cb031d9e7135714b5060c895c8a6458051002c41a/sphinxcontrib_github_alt-1.2.tar.gz
Summary  : Link to GitHub issues, pull requests, commits and users from Sphinx docs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sphinxcontrib_github_alt-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_github_alt-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_github_alt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
Link to GitHub issues, pull requests, commits and users for a particular project.

%package license
Summary: license components for the pypi-sphinxcontrib_github_alt package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_github_alt package.


%package python
Summary: python components for the pypi-sphinxcontrib_github_alt package.
Group: Default
Requires: pypi-sphinxcontrib_github_alt-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_github_alt package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_github_alt package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_github_alt)
Requires: pypi(docutils)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_github_alt package.


%prep
%setup -q -n sphinxcontrib_github_alt-1.2
cd %{_builddir}/sphinxcontrib_github_alt-1.2
pushd ..
cp -a sphinxcontrib_github_alt-1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656409194
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_github_alt
cp %{_builddir}/sphinxcontrib_github_alt-1.2/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_github_alt/29a917ce14c7844d1d9bf491b2fd34ee44dc94b0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_github_alt/29a917ce14c7844d1d9bf491b2fd34ee44dc94b0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
