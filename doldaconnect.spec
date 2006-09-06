Summary:	Direct Connect client
Name:		doldaconnect
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.dolda2000.com/~fredrik/doldaconnect/%{name}-%{version}.tar.gz
# Source0-md5:	8920593ede9d7866937cd2feb95923a8
#Source1:	%{name}.desktop
#Source2:	%{name}.png
URL:		http://www.dolda2000.com/~fredrik/doldaconnect/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dolda Connect is a client program for the Direct Connect peer-to-peer filesharing network, written for GNU/Linux systems. It is possible that it may run on other Unix systems as well, as long as it is compiled with GCC, but this is untested so far. It is licensed under the GPL, version 2 or later.

It consists of two parts - the client daemon and the user interface. The daemon is what does all the job of sharing files, searching, connecting to hubs, etc., while the user interface is a simple program that connects to the daemon in order to control it and give the user the current status of the daemon (such as the file transfers currently in progress, etc.). These two program run independently of each other, and the user interface can therefore be made to connect to a daemon running on another computer, over the internet or otherwise. For the average user, this yields two primary advantages:

 * The daemon can be made to run on another computer, which can be on all the time (a server, if you will), while the user interface can run on the user's workstation. That way, the user can turn off his workstation at night, while the server will continue all transfers in progress during that time.
 * A user can control his daemon from another location, such as from work, school, a friend, etc.

This architecture also has many other advantages in store for the more advanced users; since the user interface communicates with the daemon using a well-defined protocol, other user interfaces can be written, such as an automatic downloader, a chatbot, etc. It is also designed for secure multiuser operation.

%prep
%setup -q

%build
%configure \
	--disable-rpath \
	--enable-gtk2ui \
	--enable-gtk2pbar \
	--enable-gnomeapplet \
	--enable-gaimplugin

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS
#%attr(755,root,root) %{_bindir}/*
#%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/icons
#%{_desktopdir}/%{name}.desktop
#%{_pixmapsdir}/%{name}.png
