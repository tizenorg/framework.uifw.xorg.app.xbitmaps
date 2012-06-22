Name:           xorg-xbitmaps
Version:        1.1.1
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          User Interface/X
Source0:        ftp://ftp.x.org/pub/individual/data/xbitmaps-%{version}.tar.gz
Source1001:     packaging/xorg-xbitmaps.manifest
BuildRequires:  pkgconfig(xorg-macros)
Provides:       xbitmaps
Provides:       xbitmaps-devel
BuildArch:      noarch

%description
X.Org X11 application bitmaps

%prep
%setup -q -n xbitmaps-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --libdir=%{_datadir}
make %{?_smp_mflags}

%install
%make_install




%files
%manifest xorg-xbitmaps.manifest
%{_includedir}/X11/bitmaps
%{_datadir}/pkgconfig/xbitmaps.pc
