Summary:	Enables Netscape Communicator roaming profiles with Apache
Summary(cs):	Modul podpory roamingov�ch profil� Netscape Communicatora pro Apache
Summary(da):	Et apachemodul som lader webtjeneren h�ndtere profiler for Netscape Communicator
Summary(de):	Aktiviert den Netscape Communicator f�r das Profilroaming mit Apache
Summary(fr):	Permet l'itin�rance de profils Netscape Communicator avec Apache
Summary(it):	Abilita i profili di roaming di Netscape Communicator con Apache
Summary(no):	En apachemodul som lar webtjeneren h�ndtere profiler for Netscape Communicator
Summary(pl):	Modu� Apache obs�uguj�cy przechodnie profile Netscape Communicatora
Summary(sk):	WWW prehliada� Netscape Navigator
Summary(sv):	M�jligg�r Netscape Communicator reseprofiler med Apache
Name:		mod_roaming
Version:	1.0.2
Release:	5
License:	BSD type
Group:		Networking/Daemons
Group(cs):	S��ov�/D�moni
Group(da):	Netv�rks/D�moner
Group(de):	Netzwerkwesen/Server
Group(es):	Red/Servidores
Group(fr):	R�seau/Serveurs
Group(is):	Net/P�kar
Group(it):	Rete/Demoni
Group(no):	Nettverks/Daemoner
Group(pl):	Sieciowe/Serwery
Group(pt):	Rede/Servidores
Group(ru):	����/������
Group(sl):	Omre�ni/Stre�niki
Group(sv):	N�tverk/Demoner
Group(uk):	������/������
Source0:	http://www.klomp.org/mod_roaming/%{name}-%{version}.tar.gz
Source1:	roaming.conf
URL:		http://www.klomp.org/mod_roaming/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	apache-devel
Requires:	webserver

%description
With mod_roaming you can use your Apache web server as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies etc.
on the server so that you can use (and update) the same settings from
any Netscape Communicator 4.5 that can access the server.

%description -l cs
Bal��ek mod_roaming obsahuje modul pro podporu roamingov�ch profil�
Netscape Communicatora pro Apache. Profily umo��uj� ulo�it nastaven�
Netscape 4.5 (bookmarky, adres��, cookies, nastaven� Netacspe apod.)
na server, tak�e p�i spu�t�n� Netscape z libovoln�ho m�sta na
Internetu budete m�t stejn� nastaven�.

%description -l de
Mit mo_roaming k�nnen Sie Ihren Apache Web-Server als
Netscape-Roaming- Zugriffsserver verwenden. Auf diese Weise k�nnen Sie
Ihre Pr�ferenzen f�r Netscape Communicator 4.5, Lesezeichen,
Adressb�cher, Cookies etc. auf dem Server speichern, so dass Sie die
gleichen Einstellungen von jedem Netscape Communicator 4.5 verwenden
(und aktualisieren) k�nnen, die Zugriff auf den Server haben.

%description -l es
Con mod_roaming puede utilizar su servidor web apache como un servidor
Netscape Roaming Access. Esto le permite almacenar las preferencias de
su Netscape Communicator 4.5, los bookmarks, libros de direcciones,
cookies, etc. en el servidor de tal forma que puede utilizar (y
actualizar) las mismas opciones desde cualquier Netscape Communicator
4.5 que acceda al servidor.

%description -l fr
Mod_roaming vous permet d'utiliser le serveur Web Apache en tant que
Netscape pour acc�der � un serveur Access. Cela vous permet de stocker
vos pr�f�rences Netscape Communicator 4.5, signets, carnets
d'adresses, cookies, etc. sur le serveur afin d'utiliser (et de mettre
� jour) les m�mes r�glages depuis n'importe quel Netscapte
Communicator 4.5 ayant acc�s au serveur.

%description -l it
Grazie a mod_roaming � possibile utilizzare il server Web Apache come
un server Netscape Roaming Access. Questo consente di memorizzare le
preferenze, i segnalibri, le rubriche i cookie (e cos� via) di
Netscape Communicator 4.5 sul server, in modo da poter usare (e
aggiornare) le stesse impostazioni da qualsiasi Netscape Communicator
4.5 che possa accedere al server.

%description -l ja
mod_roaming ����Ѥ���ȡ�Apache Web �����С��� Netscape Roaming
Access �����С��Ȥ��ƻ��ѤǤ��ޤ�������ˤ�ä� Netscape Communicator
4.5 �Τ��������ꡢ�֥å��ޡ��������ɥ쥹
�֥å������å����ʤɤ򥵡��С���˳�Ǽ�Ǥ��������С��˥��������Ǥ���ɤ�
�� Netscape Communicator 4.5 ����Ǥ�Ʊ���������� (����ӹ���)
�Ǥ��� �褦�ˤʤ�ޤ���

%description -l pl
Dzi�ki mod_roaming mo�esz u�ywa� serwera Apache jako serwera Netscape
Roaming Access. Pozwala to na zapisywanie ustawie�, bookmark�w,
ksi��ek adresowych, cookie z Netscape Communicatora >= 4.5 na
serwerze, dzi�ki czemu mo�esz u�ywa� (i uaktualnia�) tych samych
ustawie� z dowolnego Netscape Communicatora >= 4.5, kt�ry ma dost�p do
serwera.

%description -l sv
Med mod_roaming kan du anv�nda din webbserver Apache som en server f�r
Netscape reseprofiler. Detta l�ter dig lagra dina Netscape
Communicator 4.5 preferenser, bokm�rken, adressbok, kakor, etc. p�
servern s� att du kan anv�nda (och �ndra) inst�llningarna fr�n valfri
Netscape Communicator 4.5 som kan komma �t servern.

%prep
%setup -q

%build
%{_sbindir}/apxs -c -o mod_roaming.so -lc mod_roaming.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/apache,%{_sysconfdir}/httpd,%{_var}/lib/mod_roaming}

install mod_roaming.so $RPM_BUILD_ROOT%{_libdir}/apache
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd

gzip -9nf CHANGES INSTALL LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* INSTALL* LICENSE* README*
%attr(755,root,root) %{_libdir}/apache/mod_roaming.so
%attr(660,root,http) %dir %{_var}/lib/mod_roaming
%config %{_sysconfdir}/httpd/roaming.conf
