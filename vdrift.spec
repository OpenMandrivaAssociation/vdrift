%define name vdrift
%define version 0.4
%define fulldate 2012-07-22
%define date %(echo %{fulldate} | sed -e 's/-//g')
%define release %mkrel 0.%{date}.1
%define distname %{name}-%{fulldate}
%define oname VDrift
%define dataname %{name}-data

Summary: Open Source Car Racing Simulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
#upstream  SDL2 compatibility patch
Patch0:	vdrift-2012-07-22c_patch.diff
License: GPLv3
Group: Games/Arcade
Url: https://vdrift.net/
BuildRequires: doxygen
BuildRequires: scons
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(sdl) 
BuildRequires: pkgconfig(SDL_image) 
BuildRequires: pkgconfig(SDL_net)
BuildRequires: pkgconfig(SDL_gfx)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(freealut) 
BuildRequires: pkgconfig(openal) 
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(bullet) 
BuildRequires: pkgconfig(glew)
BuildRequires: libboost-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: asio
BuildRequires: mongodb-devel
Obsoletes: %{name} < 0.4
Requires:  %{dataname}

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind.

#-------------
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
%setup -q -n %{oname}
%patch0 -p0

chmod 644 LICENSE README.md

%build
LDFLAGS="%{ldflags} -lGL"
scons NLS=0 use_binreloc=0 prefix=%{_prefix} 

%install
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


%files
%doc LICENSE README.md
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n %{dataname}
%doc LICENSE README.md
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*

