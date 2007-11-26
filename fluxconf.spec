%define         _Xprefix /usr/X11R6
%define         _Xbindir %_Xprefix/bin

Name:		fluxconf
Version: 0.9.9
Release: 1mdk
Summary:	Configuration utility for fluxbox
Url:		http://devaux.fabien.free.fr/flux
Source:		http://devaux.fabien.free.fr/flux/%name-%version.tar.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	gtk2-devel

%description

With this gtk-app you can easily change all fluxbox settings.


%prep
%setup -q


%build
%configure2_5x
%make


%install
%__rm -rf %buildroot %name.lang
%makeinstall bindir=%buildroot%_Xbindir
%find_lang %name
cd %buildroot%_Xbindir
ln -sf fluxconf fluxbare
ln -sf fluxconf fluxkeys
ln -sf fluxconf fluxmenu

%clean
%__rm -rf %buildroot


%files -f %name.lang
%defattr(0755,root,root,0755)
%_Xbindir/fluxconf
%_Xbindir/fluxkeys
%_Xbindir/fluxbare
%_Xbindir/fluxmenu
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL README


