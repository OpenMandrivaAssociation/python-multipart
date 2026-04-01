%define module multipart

Name:		python-multipart
Version:	1.3.1
Release:	1
Summary:	Parser for multipart/form-data
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/multipart/
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Parser for multipart/form-data

%install -a
rm -rf %{buildroot}%{py_sitedir}/__pycache__

%files
%{py_sitedir}/%{module}.py
%{py_sitedir}/%{module}-%{version}.dist-info
