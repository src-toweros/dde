%global debug_package   %{nil}

Name:           dde
Version:        2020.06.11
Release:        8
Summary:        Deepin New Desktop Environment - Next
License:        GPLv3
URL:            https://uos-packages.deepin.com/uos/pool/main/d/dde/
Source0:        https://uos-packages.deepin.com/uos/pool/main/d/dde/%{name}_%{version}.orig.tar.xz
Source1:        dde.conf
Source2:        dde

BuildRequires:	shadow
Requires:  	lightdm
Requires:	plymouth
Requires:  	lightdm-gtk-greeter
Requires:  	mesa-dri-drivers
Requires:  	xorg-x11-server
Requires:  	dde-api
Requires:  	dde-kwin
Requires:  	dde-dock
Requires:  	deepin-default-settings
Requires:  	dde-daemon
Requires:  	dde-desktop
Requires:  	dde-launcher
Requires:  	dde-clipboard
Requires:  	startdde
Requires:  	dde-polkit-agent
Requires:  	dde-file-manager
Requires:  	dde-polkit-agent
Requires:  	dde-account-faces
Requires:  	dde-network-utils
Requires:  	dde-control-center
Requires:  	libdde-file-manager
Requires:  	dde-session-shell
Requires:  	dde-session-ui
Requires:  	dde-qt5integration
Requires:  	dde-qt-dbus-factory
Requires:  	dde-disk-mount-plugin
Requires:  	dde-dock-onboard-plugin
Requires:  	deepin-anything-libs
Requires:  	deepin-qml-widgets
Requires:  	deepin-menu
Requires:  	deepin-desktop-base
Requires:  	deepin-icon-theme
Requires:  	deepin-default-settings
Requires:  	deepin-desktop-schemas
Requires:  	deepin-system-monitor
Requires:  	qt5dxcb-plugin
Requires:  	dde-network-utils
Requires:  	deepin-wallpapers
Requires:  	deepin-gtk-theme
Requires:  	deepin-anything-server
Requires:  	deepin-anything-dkms
Requires:	dde-device-formatter
Requires:	dde-device-formatter
Requires:	deepin-icon-theme
Requires:	deepin-turbo
Requires:	deepin-clone
Requires:	deepin-dbus-generator
Requires:	deepin-desktop-base
Requires:	deepin-gettext-tools
Requires:	gnu-free-fonts-common
Requires:	sil-padauk-fonts
Requires:	urw-base35-c059-fonts
Requires:	urw-base35-z003-fonts
Requires:	google-noto-cjk-fonts
Requires:	paratype-pt-sans-fonts
Requires:	urw-base35-nimbus-sans-fonts
Requires:	fonts-filesystem
Requires:	google-noto-emoji-fonts
Requires:	google-noto-serif-cjk-ttc-fonts
Requires:	gnu-free-serif-fonts
Requires:	sil-abyssinica-fonts
Requires:	jomolhari-fonts
Requires:	urw-base35-gothic-fonts
Requires:	urw-base35-p052-fonts
Requires:	google-noto-sans-cjk-ttc-fonts
Requires:	gnu-free-sans-fonts
Requires:	sil-nuosu-fonts
Requires:	julietaula-montserrat-fonts
Requires:	urw-base35-fonts-common
Requires:	urw-base35-bookman-fonts
Requires:	urw-base35-nimbus-mono-ps-fonts
Requires:	urw-base35-standard-symbols-ps-fonts
Requires:	google-droid-sans-fonts
Requires:	gnu-free-mono-fonts
Requires:	paktype-naskh-basic-fonts
Requires:	urw-base35-nimbus-roman-fonts
Requires:	abattis-cantarell-fonts
Requires:	stix-fonts
Requires:	urw-base35-d050000l-fonts
Requires:	navilu-fonts
Requires:	dejavu-fonts
Requires:	khmeros-fonts
Requires:	lohit-telugu-fonts
Requires:   	deepin-editor
Requires:   	deepin-image-viewer
Requires:   	deepin-font-manager
Requires:   	deepin-reader

Recommends:  	deepin-shortcut-viewer
Recommends:  	deepin-calendar
Recommends:  	deepin-sound-theme
Recommends:  	deepin-terminal
Recommends:  	deepin-keyring
Recommends:  	blur-effect
Recommends:  	deepin-ab-recovery
Recommends:  	deepin-compressor
Recommends:  	deepin-devicemanager
Recommends:  	deepin-elf-verify
Recommends:  	deepin-graphics-driver-manager
Recommends:  	deepin-log-viewer
Recommends:  	libpam-deepin-security
Recommends:  	deepin-manual 
Recommends:	dde-introduction
Recommends:	deepin-calculator
Recommends:	deepin-screenshot
Recommends:	deepin-picker
Recommends:	firefox
Recommends:	gparted
Recommends:	im-chooser
Recommends:	ibus-libpinyin
Recommends:     onboard
Recommends:     glibc-all-langpacks
Recommends:     langpacks-zh_CN

%description
Deepin New Desktop Environment - Next.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/etc/{rsyslog.d,logrotate.d}
install -Dm644 %{SOURCE1} %{buildroot}/etc/rsyslog.d/dde.conf
install -Dm644 %{SOURCE2} %{buildroot}/etc/logrotate.d/dde

%pre
getent group ddeuser >/dev/null || groupadd -r ddeuser
getent passwd ddeuser >/dev/null || useradd -g ddeuser -G wheel -m ddeuser > /dev/null 
echo "ddeuser
ddeuser" | passwd ddeuser > /dev/null 2>&1

%files
%doc debian/copyright
%doc debian/changelog
%{_sysconfdir}/rsyslog.d/dde.conf
%{_sysconfdir}/logrotate.d/dde

%changelog
* Wed Oct 21 2020 weidong <weidong@uniontech.com> - 2020.06.11-8
- modify some requires 

* Fri Oct 16 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-7
- modify some requires 

* Fri Sep 11 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-6
- fix ddeuser error

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-5
- fix add ddeuser

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-4
- add ddeuser

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-3
- remove requires deepin-gir-generator 

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-2
- fix src tar

* Tue Sep 8 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-1
- project init.
