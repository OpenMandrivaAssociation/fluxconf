Name:		fluxconf
Version:	0.9.9
Release:	%mkrel 4
Summary:	Configuration utility for fluxbox
URL:		http://devaux.fabien.free.fr/flux
Source:		http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	automake1.7

%description
This application allows you to configure most Fluxbox settings
graphically.

%prep
%setup -q
# Don't build with -Werror, I am not fixing warnings in years-old code
sed -i -e 's,-Werror,,g' src/Makefile.am

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot} %{name}.lang
%makeinstall

%find_lang %{name}

pushd %{buildroot}%{_bindir}
ln -sf fluxconf fluxbare
ln -sf fluxconf fluxkeys
ln -sf fluxconf fluxmenu
popd

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(0755,root,root,0755)
%{_bindir}/fluxconf
%{_bindir}/fluxkeys
%{_bindir}/fluxbare
%{_bindir}/fluxmenu
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL README

