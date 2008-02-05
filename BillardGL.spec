Summary:	3D billard simulation using OpenGL
Summary(pl.UTF-8):	Symulacja bilarda używająca OpenGL
Name:		BillardGL
Version:	1.75
Release:	3
Group:		X11/Applications/Games
License:	GPL
Source0:	http://billardgl.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	46f2cf99e1a2b2aa4707d3500e43be47
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-starting-resolution.patch
Patch1:		%{name}-depracted.patch
Patch2:		%{name}-config_buffer_overflows.patch
URL:		http://www.tobias-nopper.de/BillardGL/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D billard simulation using OpenGL.

%description -l pl.UTF-8
Trójwymiarowa symulacja bilarda używająca OpenGL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e "s:-L/usr/X11R6/lib::" src/Makefile
sed -i -e "s:/usr/share/:%{_datadir}/:" src/Namen.h

%build
%{__make} -C src \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -Wall -W %{!?debug:-DNO_DEBUG}" \
	LINK="%{__cxx}" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}/lang,%{_datadir}/%{name}/Texturen/{1,2,4,8}}

cd src
install BillardGL $RPM_BUILD_ROOT%{_bindir}
install lang/*.lang $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
