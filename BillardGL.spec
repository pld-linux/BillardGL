Name:		BillardGL
Summary:	3D billard simulation using OpenGL
Summary(pl):	Symulacja bilarda u¿ywaj±ca OpenGL
Version:	1.70
Release:	1
Group:		X11/Applications/Games
License:	GPL
Vendor:		University of Freiburg / Germany
Source0:	http://wesley.informatik.uni-freiburg.de/~nopper/BillardGL/download/%{name}-%{version}.tar.gz
# Source0-md5:	925e8a3f42690b9c6b009bc77781cc52
URL:		http://www.billardgl.de
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
3D billard simulation using OpenGL.

%description -l pl
Trójwymiarowa symulacja bilarda u¿ywaj±ca OpenGL.

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
install *.lang $RPM_BUILD_ROOT%{_datadir}/%{name}

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
