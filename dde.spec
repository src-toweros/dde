%global debug_package   %{nil}

Name:           dde
Version:        2020.11.03
Release:        2
Summary:        Deepin New Desktop Environment - Next
License:        GPLv3
URL:            https://uos-packages.deepin.com/uos/pool/main/d/dde/
Source0:        dde.conf
Source1:        dde

BuildRequires:	shadow
Requires:  	lightdm
Requires:	plymouth
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
Requires:   	deepin-editor
Requires:   	deepin-font-manager
Requires:   	deepin-reader

Recommends:     gnu-free-fonts-common
Recommends:     sil-padauk-fonts
Recommends:     urw-base35-c059-fonts
Recommends:     urw-base35-z003-fonts
Recommends:     google-noto-cjk-fonts
Recommends:     paratype-pt-sans-fonts
Recommends:     urw-base35-nimbus-sans-fonts
Recommends:     fonts-filesystem
Recommends:     google-noto-emoji-fonts
Recommends:     google-noto-serif-cjk-ttc-fonts
Recommends:     gnu-free-serif-fonts
Recommends:     sil-abyssinica-fonts
Recommends:     jomolhari-fonts
Recommends:     urw-base35-gothic-fonts
Recommends:     urw-base35-p052-fonts
Recommends:     google-noto-sans-cjk-ttc-fonts
Recommends:     gnu-free-sans-fonts
Recommends:     sil-nuosu-fonts
Recommends:     julietaula-montserrat-fonts
Recommends:     urw-base35-fonts-common
Recommends:     urw-base35-bookman-fonts
Recommends:     urw-base35-nimbus-mono-ps-fonts
Recommends:     urw-base35-standard-symbols-ps-fonts
Recommends:     google-droid-sans-fonts
Recommends:     gnu-free-mono-fonts
Recommends:     paktype-naskh-basic-fonts
Recommends:     urw-base35-nimbus-roman-fonts
Recommends:     abattis-cantarell-fonts
Recommends:     stix-fonts
Recommends:     urw-base35-d050000l-fonts
Recommends:     navilu-fonts
Recommends:     dejavu-fonts
Recommends:     khmeros-fonts
Recommends:     lohit-telugu-fonts
Recommends:     deepin-image-viewer
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
Recommends:     onboard
Recommends:     glibc-all-langpacks
Recommends:     langpacks-zh_CN
Recommends:     fcitx fcitx-qt5 fcitx-pinyin fcitx-sunpinyin fcitx-configtool fcitx-table-chinese

%description
Deepin New Desktop Environment - Next.

%prep

%build

%install
mkdir -p %{buildroot}/etc/{rsyslog.d,logrotate.d}
install -Dm644 %{SOURCE0} %{buildroot}/etc/rsyslog.d/dde.conf
install -Dm644 %{SOURCE1} %{buildroot}/etc/logrotate.d/dde

%pre
getent group openeuler >/dev/null || groupadd -r openeuler
getent passwd openeuler >/dev/null || useradd -g openeuler -G wheel -m openeuler > /dev/null 
echo "openeuler
openeuler" | passwd openeuler > /dev/null 2>&1

%files
%{_sysconfdir}/rsyslog.d/dde.conf
%{_sysconfdir}/logrotate.d/dde

%changelog
* Tue Aug 03 2021 weidong <weidong@uniontech.com> - 2020.11.03-2
- Delete requires lightdm-greeter

* Wed Jul 07 2021 weidong <weidong@uniontech.com> - 2020.11.03-1
- Update to 2020.11.03

* Tue Mar 30 2021 weidong <weidong@uniontech.com> - 2020.03.30-13
- Set the default input method to fcitx

* Fri Dec 18 2020 weidong <weidong@uniontech.com> - 2020.03.30-12
- Fix version

* Mon Nov 09 2020 chenbo pan <panchenbo@uniontech.com> - 2020.06.11-11
- modify fonts rpm requires to recommends

* Mon Nov 09 2020 weidong <weidong@uniontech.com> - 2020.06.11-10
- modify some requires 

* Wed Nov 04 2020 weidong <weidong@uniontech.com> - 2020.06.11-9
- Change the default user to openeuler

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
