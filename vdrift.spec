%define name vdrift
%define version 0.4
%define fulldate 2010-06-30
%define date %(echo %{fulldate} | sed -e 's/-//g')
%define release %mkrel 0.%{date}.1
%define distname %{name}-%{fulldate}

%define dataname %{name}-data

Summary: Open Source Car Racing Simulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPLv3
Group: Games/Arcade
Url: http://vdrift.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons
BuildRequires: SDL-devel SDL_image-devel SDL_net-devel libSDL_gfx-devel
BuildRequires: mesaglu-devel
BuildRequires: freealut-devel, openal-devel, libvorbis-devel, bullet-devel, glew-devel
BuildRequires: libboost-devel
BuildRequires: asio
BuildRequires: mongodb-devel
Obsoletes: %{name} < 0.4
Requires:  %{dataname}

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind.

%package -n %{dataname}
Summary:    Data files for the VDrift driving simulation
Requires:   %{name}  
Group: Games/Arcade
Obsoletes: %{dataname} < 0.4
BuildArch:  noarch
%description -n %{dataname}
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind.
This package contains data files for VDrift.


%prep
%setup -q -n %{distname}


%build
scons NLS=0 use_binreloc=0 prefix=%{_prefix}

%install
rm -rf %{buildroot}
install -D -m755 build/%{name} %{buildroot}%{_gamesbindir}/%{name}
install -d %{buildroot}%{_gamesdatadir}/%{name}/data
cp -a data %{buildroot}%{_gamesdatadir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=VDrift
Comment=Driving simulation
Exec=soundwrapper %_gamesbindir/%{name}
Icon=%{_gamesdatadir}/%{name}/data/textures/icons/%{name}-64x64.png
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
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n %{dataname}
%defattr(-,root,root)
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*
