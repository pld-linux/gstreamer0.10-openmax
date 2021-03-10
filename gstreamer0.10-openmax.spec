Summary:	GStreamer 0.10 plug-in that allows communication with OpenMAX IL components
Summary(pl.UTF-8):	Wtyczka GStreamera 0.10 pozwalająca na komunikację z komponentami OpenMAX IL
Name:		gstreamer0.10-openmax
Version:	0.10.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-openmax/gst-openmax-%{version}.tar.bz2
# Source0-md5:	4d0370bfe99dea20918c84347abadb4e
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gstreamer0.10-devel >= 0.10.22
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
Requires:	gstreamer0.10 >= 0.10.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GstOpenMAX is a GStreamer 0.10 plug-in that allows communication with
OpenMAX IL components.

OpenMAX IL is an industry standard that provides an abstraction layer
for computer graphics, video, and sound routines.

%description -l pl.UTF-8
GstOpenMAX to wtyczka GStreamera 0.10 pozwalająca na komunikację z
komponentami OpenMAX IL.

OpenMAX IL to standard przemysłowy zapewniający warstwę abstrakcji dla
funkcji grafiki komputerowej, obrazu i dźwięku komp.

%prep
%setup -q -n gst-openmax-%{version}

# disable -Werror (unused-but-sed variable, deprecated glib APIs)
%{__sed} -i -e 's/AG_GST_SET_ERROR_CFLAGS.*/AG_GST_SET_ERROR_CFLAGS([no])/' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstomx.so
