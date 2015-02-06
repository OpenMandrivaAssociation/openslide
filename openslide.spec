%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	C library and command line tools for reading virtual slides
Name:		openslide
Version:	3.4.0
Release:	2
License:	LGPLv2+
Group:		Graphics
Url:		http://openslide.org/
Source0:	https://github.com/downloads/openslide/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
Provides:	openslide-tools = %{EVRD}

%description
Command line tools for working with virtual slides.

%files
%doc README.txt lgpl-2.1.txt LICENSE.txt CHANGELOG.txt
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}-*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	C library for reading virtual slides
Group:		System/Libraries

%description -n %{libname}
The OpenSlide library allows programs to access virtual slide files regardless
of the underlying image format.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%files -n %{develname}
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --disable-static
%make


%install
%makeinstall_std

