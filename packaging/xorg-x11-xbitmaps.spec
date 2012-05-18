Name:       xorg-x11-xbitmaps
Summary:    X.Org X11 application bitmaps
Version:    1.1.1
Release:    1
Group:      User Interface/X
License:    MIT
BuildArch:  noarch
URL:        http://www.x.org
Source0:    ftp://ftp.x.org/pub/individual/data/xbitmaps-%{version}.tar.gz
BuildRequires: pkgconfig(xorg-macros)
Provides:   xbitmaps
Provides:   xbitmaps-devel

%description
X.Org X11 application bitmaps


%prep
%setup -q -n %{name}-%{version}


%build
# hack to move the pc file
#sed -i 's/^libdir.*//' *.pc.in

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%make_install




%files
%defattr(-,root,root,-)
#%doc
%{_includedir}/X11/bitmaps
%{_datadir}/pkgconfig/xbitmaps.pc


