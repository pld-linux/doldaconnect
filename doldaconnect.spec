# TODO:
# - use the same macros as in other gaim plugins packages
# - package guile app to some subpackage
# - package gnome applet to separate package
Summary:	Direct Connect client
Summary(pl):	Klient Direct Connect
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

%description -l pl
Dolda Connect to program kliencki dla sieci wspó³dzielenia plików
peer-to-peer Direct Connect. Zosta³ napisany dla systemów GNU/Linux.
Byæ mo¿e dzia³a tak¿e na innych systemach uniksowych, je¶li zostanie
skompilowany GCC, ale nie by³o to testowane.

Program sk³ada siê z dwóch czê¶ci: demona klienckiego oraz interfejsu
u¿ytkownika. Demon wykonuje w³a¶ciw± pracê wspó³dzielenia plików,
wyszukiwania, ³±czenia z hubami itp., natomiast interfejs u¿ytkownika
to prosty program ³±cz±cy siê z demonem w celu sterowania nim i
podawania u¿ytkownikowi aktualnego stanu demona (tzn. aktualnie
przesy³anych plików itp.). Te dwa programy dzia³aj± niezale¿nie od
siebie, dziêki czemu interfejs u¿ytkownika mo¿e ³±czyæ siê z demonem
dzia³aj±cym na innym komputerze poprzez Internet lub w inny sposób.
Dla przeciêtnego u¿ytkownika ma to dwie g³ówne zalety:

- Demon mo¿e dzia³aæ na innym komputerze, który jest w³±czony przez
  ca³y czas (np. na serwerze), podczas gdy interfejs u¿ytkownika mo¿e
  dzia³aæ na stacji roboczej u¿ytkownika; w ten sposób u¿ytkownik mo¿e
  wy³±czyæ swoj± stacjê na noc, podczas gdy serwer nadal bêdzie
  przesy³a³ pliki.
- U¿ytkownik mo¿e kontrolowaæ swojego demona z innego miejsca, np. z
  pracy, ze szko³y, od kolegi itp.

Architektura ta ma tak¿e wiele innych zalet dla bardziej
zaawansowanych u¿ytkowników; poniewa¿ interfejs u¿ytkownika komunikuje
siê z demonem za pomoc± dobrze zdefiniowanego protoko³u, mo¿na napisaæ
inne interfejsy u¿ytkownika, takie jak automatyczny ¶ci±gaæ, chatbot
itp. Jest zaprojektowana tak¿e z my¶l± o bezpiecznej pracy
wielou¿ytkownikowej.

%package libs
Summary:	%{name} libraries
Summary(pl):	Biblioteki doldaconnecta
Group:		Libraries

%description libs
%{name} libraries.

%description libs -l pl
Biblioteki doldaconnecta.

%package devel
Summary:	Header files for %{name} library
Summary(pl):	Pliki nag³ówkowe biblioteki doldaconnecta
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl
Pliki nag³ówkowe biblioteki doldaconnecta.

%package static
Summary:	Static %{name} libraries
Summary(pl):	Statyczne biblioteki doldaconnecta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} libraries.

%description static -l pl
Statyczne biblioteki doldaconnecta.

%package -n doldacond
Summary:	Daemon for %{name}
Summary(pl):	Demon doldaconnecta
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts

%description -n doldacond
Daemon for doldaconnect that handles all of the network connections.

%description -n doldacond -l pl
Demon doldaconnecta obs³uguj±cy wszystkie po³±czenia sieciowe.

%package -n gaim-plugin-%{name}
Summary:	Gaim plugin for %{name}
Summary(pl):	Wtyczka Gaima dla doldaconnecta
Group:		Applications/Communications
Requires:	%{name}-libs = %{version}-%{release}

%description -n gaim-plugin-%{name}
Gaim plugin for %{name}.

%description -n gaim-plugin-%{name} -l pl
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
