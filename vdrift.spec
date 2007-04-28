%define name vdrift
%define version 0.1
%define fulldate 2007-03-23
%define date %(echo %{fulldate} | sed -e 's/-//g')
%define release %mkrel 0.%{date}.1
%define distname %{name}-%{fulldate}-src

Summary: Driving simulation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: Games/Arcade
Url: http://vdrift.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons
BuildRequires: SDL-devel SDL_image-devel SDL_net-devel libSDL_gfx0-devel
BuildRequires: mesaglu-devel
BuildRequires: freealut-devel, openal-devel
Requires: %{name}-data

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind.

%prep
%setup -q -n %{distname}
echo > data/SConscript

%build
scons NLS=0 use_binreloc=0

%install
rm -rf %{buildroot}
install -D -m755 build/%{name} %{buildroot}%{_gamesbindir}/%{name}
install -d %{buildroot}%{_gamesdatadir}/%{name}/data

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=VDrift
Comment=Driving simulation
Exec=soundwrapper %_gamesbindir/%{name}
Icon=%{_gamesdatadir}/%{name}/data/textures/large/icons/%{name}-64x64.png
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/AUTHORS docs/ChangeLog docs/NEWS docs/README docs/TODO docs/VAMOS.txt
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/data
%{_datadir}/applications/mandriva-%{name}.desktop