Name: motley-cue
Version: 0.0.12
Release: 1
Summary: Mapper Oidc To Local idEntitY with loCal User managEment
Group: Misc
License: MIT-License
URL: https://git.scc.kit.edu/dianagudu/motley_cue.git
Source0: motley-cue.tar

BuildRequires: python3-setuptools >= 39, python36 >= 3.6, python3-pip >= 9.0, python3-virtualenv >= 15.1, python36-devel >= 3.6

BuildRoot:	%{_tmppath}/%{name}
Requires: python36 >= 3.6, nginx

%define debug_package %{nil}

%description
This tool provides an OIDC-protected REST interface that allows requesting
the creation, deletion, and information of a user-account.

%prep
%setup -q

%build
#make virtualenv DESTDIR=${RPM_BUILD_ROOT}

#%clean
#rm -rf %{buildroot}

%install
echo "Buildroot: ${RPM_BUILD_ROOT}"
echo "ENV: "
env | grep -i rpm
echo "PWD"
pwd
#make install INSTALL_PATH=${RPM_BUILD_ROOT}/usr MAN_PATH=${RPM_BUILD_ROOT}/usr/share/man CONFIG_PATH=${RPM_BUILD_ROOT}/etc
#make virtualenv DESTDIR=/tmp/build/motley_cue/rpm/rpmbuild/BUILD/motley-cue-0.0.9-1.x86_64
#make install DESTDIR=/tmp/build/motley_cue/rpm/rpmbuild/BUILD/motley-cue-0.0.9-1.x86_64
make virtualenv DESTDIR=${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_DIR{/etc/motley_cue,/var/log/motley_cue,/run/motley_cue}
install -m644 $RPM_BUILD_ROOT/etc/motley_cue/* $RPM_BUILD_DIR/etc/motley_cue
mv $RPM_BUILD_ROOT/etc/nginx/nginx.motley_cue $RPM_BUILD_ROOT/etc/nginx/nginx.motley_cue.conf
install -m644 $RPM_BUILD_ROOT/etc/nginx/nginx.motley_cue.conf $RPM_BUILD_DIR/etc/nginx/conf.d/

%files
%defattr(-,root,root,-)
/usr/*
/lib/*
/bin/*
/etc/*

%changelog

