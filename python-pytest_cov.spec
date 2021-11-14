# Created by pyp2rpm-2.0.0
%global pypi_name pytest_cov
%global	alt_name pytest-cov
%global with_python2 0
%define version 2.6.1

Name:           python-%{alt_name}
Version:	3.0.0
Release:	1
Group:          Development/Python
Summary:        This plugin produces coverage reports.

License:        MIT
URL:            https://github.com/pytest-dev/pytest-cov

Source0:	https://files.pythonhosted.org/packages/61/41/e046526849972555928a6d31c2068410e47a31fb5ab0a77f868596811329/pytest-cov-3.0.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif 
# if with_python2


%description
This plugin produces coverage reports. Compared to just using coverage run this plugin does some extras:

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        This plugin produces coverage reports.

%description -n python2-%{pypi_name}
This plugin produces coverage reports. Compared to just using coverage run this plugin does some extras:
%endif 
# with_python2


%prep
%setup -q -n %{alt_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif 
# with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif 
# with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif 
# with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.rst LICENSE CHANGELOG.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/pytest-cov.pth


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst LICENSE CHANGELOG.rst
%{python2_sitelib}/{pypi_name}/
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/pytest-cov.pth
%endif 
# with_python2

