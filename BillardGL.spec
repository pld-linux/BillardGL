Name:		BillardGL
Summary:	3D billard simulation using OpenGL
Summary(pl.UTF-8):   Symulacja bilarda używająca OpenGL
Version:	1.75
Release:	2
Group:		X11/Applications/Games
License:	GPL
Vendor:		University of Freiburg / Germany
Source0:	http://billardgl.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	46f2cf99e1a2b2aa4707d3500e43be47
URL:		http://www.tobias-nopper.de/BillardGL/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D billard simulation using OpenGL.

%description -l pl.UTF-8
Trójwymiarowa symulacja bilarda używająca OpenGL.

%prep
%setup -q

%build
cd src
sed -i -e "s:/usr/X11R6/lib:/usr/X11R6/%{_lib}:g" Makefile
sed -i -e "s:/usr/share/:%{_datadir}/:" Namen.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/Texturen/{1,2,4,8}}

cd src
install BillardGL $RPM_BUILD_ROOT%{_bindir}
install lang/*.lang $RPM_BUILD_ROOT%{_datadir}/%{name}

for j in 1 2 4 8 ; do
	for i in Texturen/$j/*; do
		install $i $RPM_BUILD_ROOT%{_datadir}/%{name}/Texturen/$j
	done
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/README
%attr(755,root,root) %{_bindir}/BillardGL
%{_datadir}/%{name}
