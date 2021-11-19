#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib_github_alt
Version  : 1.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/b8/d5/2880f4f441f3b46f264cb031d9e7135714b5060c895c8a6458051002c41a/sphinxcontrib_github_alt-1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/d5/2880f4f441f3b46f264cb031d9e7135714b5060c895c8a6458051002c41a/sphinxcontrib_github_alt-1.2.tar.gz
Summary  : Link to GitHub issues, pull requests, commits and users from Sphinx docs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sphinxcontrib_github_alt-license = %{version}-%{release}
Requires: sphinxcontrib_github_alt-python = %{version}-%{release}
Requires: sphinxcontrib_github_alt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
Link to GitHub issues, pull requests, commits and users for a particular project.

%package license
Summary: license components for the sphinxcontrib_github_alt package.
Group: Default

%description license
license components for the sphinxcontrib_github_alt package.


%package python
Summary: python components for the sphinxcontrib_github_alt package.
Group: Default
Requires: sphinxcontrib_github_alt-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib_github_alt package.


%package python3
Summary: python3 components for the sphinxcontrib_github_alt package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_github_alt)
Requires: pypi(docutils)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib_github_alt package.


%prep
%setup -q -n sphinxcontrib_github_alt-1.2
cd %{_builddir}/sphinxcontrib_github_alt-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637357731
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib_github_alt
cp %{_builddir}/sphinxcontrib_github_alt-1.2/COPYING.md %{buildroot}/usr/share/package-licenses/sphinxcontrib_github_alt/29a917ce14c7844d1d9bf491b2fd34ee44dc94b0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib_github_alt/29a917ce14c7844d1d9bf491b2fd34ee44dc94b0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*