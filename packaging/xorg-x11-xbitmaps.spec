Summary: X.Org X11 application bitmaps
Name: xorg-x11-xbitmaps
Version: 1.1.1
Release: 3
License: MIT
Group: User Interface/X
URL: http://www.x.org
BuildArch: noarch

Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: xorg-x11-xutils-dev
Provides: xbitmaps

%description
X.Org X11 application bitmaps

%prep
%setup -q

%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs} %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%remove_docs

%files
%defattr(-,root,root,-)
#%doc COPYING
%{_includedir}/X11
%{_datadir}/pkgconfig/xbitmaps.pc