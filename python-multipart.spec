Name:		python-multipart
Version:	1.2.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/m/multipart/multipart-%{version}.tar.gz
Summary:	Parser for multipart/form-data
URL:		https://pypi.org/project/multipart/
License:	None
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Parser for multipart/form-data

%prep
%autosetup -p1 -n multipart-%{version}

%build
%py_build

%install
%py_install
rm -rf %{buildroot}%{py_sitedir}/__pycache__

%files
%{py_sitedir}/multipart.py
%{py_sitedir}/multipart-*.*-info
