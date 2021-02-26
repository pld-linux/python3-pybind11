#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		pybind11
%define		egg_name	pybind11
%define		pypi_name	pybind11
Summary:	Seamless operability between C++11 and Python
Summary(pl.UTF-8):	Gładka współpraca między C++11 a Pythonem
Name:		python-%{pypi_name}
Version:	2.5.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pybind11/
Source0:	https://files.pythonhosted.org/packages/source/p/pybind11/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	5355e1fd05c8eedef19cc9bfd3d82a77
URL:		https://pypi.org/project/pybind11/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	libstdc++-devel >= 6:4.7
Requires:	python-devel >= 1:2.7
Conflicts:	eigen3 < 3.2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pybind11 is a lightweight header-only library that exposes C++ types
in Python and vice versa, mainly to create Python bindings of existing
C++ code. Its goals and syntax are similar to the excellent
Boost.Python library by David Abrahams: to minimize boilerplate code
in traditional extension modules by inferring type information using
compile-time introspection.

%description -l pl.UTF-8
pybind11 to lekka, składająca się z samych nagłówków biblioteka
udostępniająca typy C++ w Pythonie i na odwrót, służąca głównie do
tworzenia wiązań Pythona do istniejącego kodu w C++. Cele i składnia
są podobne do biblioteki Boost.Python autorstwa Davida Abrahamsa - aby
zminimalizować kod wiążący w tradycyjnych modułach rozszerzeń poprzez
wnioskowanie informacji o typach przy użyciu introspekcji w trakcie
kompilacji.

%package -n python3-%{pypi_name}
Summary:	Seamless operability between C++11 and Python
Summary(pl.UTF-8):	Gładka współpraca między C++11 a Pythonem
Group:		Libraries/Python
Requires:	libstdc++-devel >= 6:4.7
Requires:	python3-devel >= 1:3.2
Conflicts:	eigen3 < 3.2.7

%description -n python3-%{pypi_name}
pybind11 is a lightweight header-only library that exposes C++ types
in Python and vice versa, mainly to create Python bindings of existing
C++ code. Its goals and syntax are similar to the excellent
Boost.Python library by David Abrahams: to minimize boilerplate code
in traditional extension modules by inferring type information using
compile-time introspection.

%description -n python3-%{pypi_name} -l pl.UTF-8
pybind11 to lekka, składająca się z samych nagłówków biblioteka
udostępniająca typy C++ w Pythonie i na odwrót, służąca głównie do
tworzenia wiązań Pythona do istniejącego kodu w C++. Cele i składnia
są podobne do biblioteki Boost.Python autorstwa Davida Abrahamsa - aby
zminimalizować kod wiążący w tradycyjnych modułach rozszerzeń poprzez
wnioskowanie informacji o typach przy użyciu introspekcji w trakcie
kompilacji.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py_incdir}/pybind11
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py3_incdir}/pybind11
%endif
