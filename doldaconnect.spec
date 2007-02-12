# TODO:
# - use the same macros as in other gaim plugins packages
# - package guile app to some subpackage
# - package gnome applet to separate package
Summary:	Direct Connect client
Summary(pl.UTF-8):	Klient Direct Connect
Name:		doldaconnect
Version:	0.1
Release:	0.7
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.dolda2000.com/~fredrik/doldaconnect/%{name}-%{version}.tar.gz
# Source0-md5:	8920593ede9d7866937cd2feb95923a8
Source1:	%{name}.desktop
Source2:	%{name}.init
Source3:	%{name}.pam
URL:		http://www.dolda2000.com/~fredrik/doldaconnect/
BuildRequires:	bzip2-devel
BuildRequires:	gaim-devel
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	guile-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appconfdir	/etc/%{name}

%description
Dolda Connect is a client program for the Direct Connect peer-to-peer
filesharing network, written for GNU/Linux systems. It is possible
that it may run on other Unix systems as well, as long as it is
compiled with GCC, but this is untested so far.

It consists of two parts - the client daemon and the user interface.
The daemon is what does all the job of sharing files, searching,
connecting to hubs, etc., while the user interface is a simple program
that connects to the daemon in order to control it and give the user
the current status of the daemon (such as the file transfers currently
in progress, etc.). These two program run independently of each other,
and the user interface can therefore be made to connect to a daemon
running on another computer, over the internet or otherwise. For the
average user, this yields two primary advantages:

- The daemon can be made to run on another computer, which can be on
  all the time (a server, if you will), while the user interface can run
  on the user's workstation. That way, the user can turn off his
  workstation at night, while the server will continue all transfers in
  progress during that time.
- A user can control his daemon from another location, such as from
  work, school, a friend, etc.

This architecture also has many other advantages in store for the more
advanced users; since the user interface communicates with the daemon
using a well-defined protocol, other user interfaces can be written,
such as an automatic downloader, a chatbot, etc. It is also designed
for secure multiuser operation.

%description -l pl.UTF-8
Dolda Connect to program kliencki dla sieci współdzielenia plików
peer-to-peer Direct Connect. Został napisany dla systemów GNU/Linux.
Być może działa także na innych systemach uniksowych, jeśli zostanie
skompilowany GCC, ale nie było to testowane.

Program składa się z dwóch części: demona klienckiego oraz interfejsu
użytkownika. Demon wykonuje właściwą pracę współdzielenia plików,
wyszukiwania, łączenia z hubami itp., natomiast interfejs użytkownika
to prosty program łączący się z demonem w celu sterowania nim i
podawania użytkownikowi aktualnego stanu demona (tzn. aktualnie
przesyłanych plików itp.). Te dwa programy działają niezależnie od
siebie, dzięki czemu interfejs użytkownika może łączyć się z demonem
działającym na innym komputerze poprzez Internet lub w inny sposób.
Dla przeciętnego użytkownika ma to dwie główne zalety:

- Demon może działać na innym komputerze, który jest włączony przez
  cały czas (np. na serwerze), podczas gdy interfejs użytkownika może
  działać na stacji roboczej użytkownika; w ten sposób użytkownik może
  wyłączyć swoją stację na noc, podczas gdy serwer nadal będzie
  przesyłał pliki.
- Użytkownik może kontrolować swojego demona z innego miejsca, np. z
  pracy, ze szkoły, od kolegi itp.

Architektura ta ma także wiele innych zalet dla bardziej
zaawansowanych użytkowników; ponieważ interfejs użytkownika komunikuje
się z demonem za pomocą dobrze zdefiniowanego protokołu, można napisać
inne interfejsy użytkownika, takie jak automatyczny ściągać, chatbot
itp. Jest zaprojektowana także z myślą o bezpiecznej pracy
wieloużytkownikowej.

%package libs
Summary:	%{name} libraries
Summary(pl.UTF-8):	Biblioteki doldaconnecta
Group:		Libraries

%description libs
%{name} libraries.

%description libs -l pl.UTF-8
Biblioteki doldaconnecta.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki doldaconnecta
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki doldaconnecta.

%package static
Summary:	Static %{name} libraries
Summary(pl.UTF-8):	Statyczne biblioteki doldaconnecta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} libraries.

%description static -l pl.UTF-8
Statyczne biblioteki doldaconnecta.

%package -n doldacond
Summary:	Daemon for %{name}
Summary(pl.UTF-8):	Demon doldaconnecta
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts

%description -n doldacond
Daemon for doldaconnect that handles all of the network connections.

%description -n doldacond -l pl.UTF-8
Demon doldaconnecta obsługujący wszystkie połączenia sieciowe.

%package -n gaim-plugin-%{name}
Summary:	Gaim plugin for %{name}
Summary(pl.UTF-8):	Wtyczka Gaima dla doldaconnecta
Group:		Applications/Communications
Requires:	%{name}-libs = %{version}-%{release}

%description -n gaim-plugin-%{name}
Gaim plugin for %{name}.

%description -n gaim-plugin-%{name} -l pl.UTF-8
Wtyczka Gaima dla doldaconnecta.

%prep
%setup -q

%build
%configure \
	--sysconfdir=%{_appconfdir} \
	--disable-rpath \
	--with-guile \
	--enable-gtk2ui \
	--enable-gtk2pbar \
	--enable-gnomeapplet \
	--enable-gaimplugin

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},/etc/{rc.d/init.d,pam.d,sysconfig}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/doldacond
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/doldacond

rm -f $RPM_BUILD_ROOT%{_libdir}/gaim/*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post -n doldacond
/sbin/chkconfig --add doldacond
%service doldacond restart

%preun -n doldacond
if [ "$1" = 0 ]; then
	%service doldacond stop
	/sbin/chkconfig --del doldacond
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dolcon
%attr(755,root,root) %{_libdir}/bonobo/servers/*.server
%attr(755,root,root) %{_libdir}/dolcon-trans-applet
%attr(755,root,root) %{_libdir}/speedrec
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.jpg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n doldacond
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README
%dir %{_appconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_appconfdir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/doldacond
%attr(754,root,root) /etc/rc.d/init.d/doldacond
%attr(755,root,root) %{_bindir}/doldacond
%attr(755,root,root) %{_bindir}/locktouch
%attr(755,root,root) %{_bindir}/tthsum

%files -n gaim-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gaim/libdolcon-gaim.so
