# Created by pyp2rpm-2.0.0
%global pypi_name pytest-cov
%global with_python2 0
%define version 2.6.1

Name:           python-%{pypi_name}
Version:	2.10.0
Release:	1
Group:          Development/Python
Summary:        This plugin produces coverage reports.

License:        MIT
URL:            https://github.com/pytest-dev/pytest-cov

Source0:	https://files.pythonhosted.org/packages/8c/0d/a2b62bbd80285ce9f1f308292eb2d5af852e7b57b6c096e91b8476ac0d5e/pytest-cov-2.10.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
This plugin produces coverage reports. Compared to just using coverage run this plugin does some extras:

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        This plugin produces coverage reports.

%description -n python2-%{pypi_name}
This plugin produces coverage reports. Compared to just using coverage run this plugin does some extras:
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.rst LICENSE CHANGELOG.rst
%{python_sitelib}/*/*
%{python_sitelib}/pytest-cov.pth


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst LICENSE CHANGELOG.rst
%{python2_sitelib}/*/*
%{python2_sitelib}/pytest-cov.pth
%endif # with_python2

