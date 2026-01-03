%define module pytest-cov
%define oname pytest_cov

Name:		python-pytest-cov
Version:	7.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Pytest plugin for measuring coverage
URL:		https://pypi.org/project/pytest-cov/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(pytest)
Requires:	python%{pyver}dist(pluggy)
Requires:	python%{pyver}dist(coverage)

%rename	python2-pytest-cov

%description
Pytest plugin for measuring coverage.

%prep
%autosetup -p1 -n %{oname}-%{version}

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
