%define		module		pybind11
%define		egg_name	pybind11
%define		pypi_name	pybind11
Summary:	Seamless operability between C++11 and Python
Summary(pl.UTF-8):	Gładka współpraca między C++11 a Pythonem
Name:		python3-%{pypi_name}
# keep 2.9.x here for python2 support
Version:	2.13.6
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pybind11/
Source0:	https://github.com/pybind/pybind11/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	a04dead9c83edae6d84e2e343da7feeb
URL:		https://pypi.org/project/pybind11/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	libstdc++-devel >= 6:4.7
Requires:	python3-devel >= 1:2.7
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

%prep
%setup -q -n %{pypi_name}-%{version}

%build
pys=""
pys="$pys python3"
for py in $pys; do
	mkdir $py
	%cmake -B $py -DCMAKE_BUILD_TYPE=Debug -DPYTHON_EXECUTABLE=%{_bindir}/$py -DPYBIND11_INSTALL=TRUE -DUSE_PYTHON_INCLUDE_DIR=FALSE -DPYBIND11_TEST=OFF
	%{__make} -C $py
done

%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C python3 DESTDIR=$RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/pybind11-config
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{_includedir}/%{module}
%{_datadir}/cmake/pybind11
%{_npkgconfigdir}/pybind11.pc
