Name:		BillardGL
Summary:	3D billard simulation using OpenGL
Summary(pl):	Symulacja bilarda używająca OpenGL
Version:	1.75
Release:	1
Group:		X11/Applications/Games
License:	GPL
Vendor:		University of Freiburg / Germany
Source0:	http://wesley.informatik.uni-freiburg.de/~nopper/BillardGL/download/%{name}-%{version}.tar.gz
# Source0-md5:	46f2cf99e1a2b2aa4707d3500e43be47
URL:		http://www.billardgl.de
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
3D billard simulation using OpenGL.

%description -l pl
Trójwymiarowa symulacja bilarda używająca OpenGL.

%prep
%setup -q

%build
cd src
sed -e "s:/usr/share/:%{_datadir}/:" Namen.h > Namen
mv -f Namen Namen.h
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
