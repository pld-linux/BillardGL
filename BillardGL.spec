Name:		BillardGL
Summary:	3d billard simulation using OpenGL
Summary(pl):	Symulacja bilarda u¿ywaj±ca OpenGL
Version:	1.70
Release:	0.1
Group:		X11/Applications/Games
License:	GPL
URL:		http://www.billardgl.de
Vendor:		University of Freiburg / Germany
Source0:	http://wesley.informatik.uni-freiburg.de/~nopper/BillardGL/download/%{name}-%{version}.tar.gz
BuildRoot: 	%{tmpdir}/%{name}-%{version}-build-root-%(id -u -n)

%define 	_x11bindir	%{_prefix}/X11R6/bin
%define		_x11share	%{_prefix}/X11R6/share

%description
3d billard simulation using OpenGL

Stefan Disch, Tobias Nopper, Martina Welte

University of Freiburg / Germany Department of computer-sience

%description -l pl
Trójwymiarowa symulacja bilarda u¿ywaj±ca OpenGL.

%prep
%setup -q 

%build
cd src
sed -e "s:/usr/share/:/usr/X11R6/share/:" Namen.h > Namen
mv -f Namen Namen.h
%{__make}

gzip -9nf README

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_x11bindir},%{_x11share},%{_x11share}/BillardGL,%{_prefix}/share/doc/%{name}-%{version}}
install -d $RPM_BUILD_ROOT%{_x11share}/%{name}/Texturen/{1,2,4,8}
cd src
install BillardGL $RPM_BUILD_ROOT%{_x11bindir}
install *.gz $RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}-%{version}
install *.lang $RPM_BUILD_ROOT%{_x11share}/%{name}

for i in Texturen/1/*; do
    install $i $RPM_BUILD_ROOT%{_x11share}/%{name}/Texturen/1
done

for i in Texturen/2/*; do
    install $i $RPM_BUILD_ROOT%{_x11share}/%{name}/Texturen/2
done

for i in Texturen/4/*; do
    install $i $RPM_BUILD_ROOT%{_x11share}/%{name}/Texturen/4
done

for i in Texturen/8/*; do
    install $i $RPM_BUILD_ROOT%{_x11share}/%{name}/Texturen/8
done


%files
%defattr(644,root,root,755)
#%doc src/*.gz
%attr(755,root,root) %{_x11bindir}/BillardGL
%dir %{_x11share}/%{name}/*
%{_x11share}/%{name}/Texturen/1/*
%{_x11share}/%{name}/Texturen/2/*
%{_x11share}/%{name}/Texturen/4/*
%{_x11share}/%{name}/Texturen/8/*
%{_prefix}/share/doc/*


%clean
rm -rf $RPM_BUILD_ROOT
