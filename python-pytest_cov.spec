Name:		python-pytest-cov
Version:	6.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-cov/pytest_cov-%{version}.tar.gz
Summary:	Pytest plugin for measuring coverage.
URL:		https://pypi.org/project/pytest-cov/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
Obsoletes:	python2-pytest-cov

%description
Pytest plugin for measuring coverage.

%prep
%autosetup -p1 -n pytest_cov-%{version}

%files
%{py_sitedir}/pytest_cov
%{py_sitedir}/pytest-cov.pth
%{py_sitedir}/pytest_cov-*.*-info
