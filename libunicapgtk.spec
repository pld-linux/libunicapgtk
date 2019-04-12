Summary:	GTK+2 widget for the unicap video capture library
Summary(pl.UTF-8):	Widget GTK+2 dla biblioteki przechwytywania obrazu unicap
Name:		libunicapgtk
Version:	0.9.8
Release:	9
License:	GPL v2+
Group:		Libraries
#Source0Download: http://unicap-imaging.org/download.htm
Source0:	http://unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e68aac64ebf1c8149f9b8009ab855dd0
URL:		http://unicap-imaging.org/
BuildRequires:	glib2-devel >= 1:2.11.0
BuildRequires:	gtk+2-devel >= 2:2.9.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libucil-devel
BuildRequires:	libunicap-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXv-devel
Requires:	glib2 >= 1:2.11.0
Requires:	gtk+2 >= 2:2.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+2 widget for the unicap video capture library.

%description -l pl.UTF-8
Widget GTK+2 dla biblioteki przechwytywania obrazu unicap.

%package devel
Summary:	Header files for unicapgtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki unicapgtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.11.0
Requires:	gtk+2-devel >= 2:2.9.0
Requires:	libucil-devel
Requires:	libunicap-devel
Requires:	pango-devel
Requires:	xorg-lib-libXv-devel

%description devel
Header files for unicapgtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki unicapgtk.

%package static
Summary:	Static unicapgtk library
Summary(pl.UTF-8):	Statyczna biblioteka unicapgtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static unicapgtk library.

%description static -l pl.UTF-8
Statyczna biblioteka unicapgtk.

%package apidocs
Summary:	unicapgtk API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki unicapgtk
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for unicapgtk library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki unicapgtk.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunicapgtk.la

%find_lang unicapgtk

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f unicapgtk.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libunicapgtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunicapgtk.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunicapgtk.so
%{_includedir}/unicap/unicapgtk*.h
%{_pkgconfigdir}/libunicapgtk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libunicapgtk.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libunicapgtk
