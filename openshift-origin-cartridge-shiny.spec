%global cartridgedir %{_libexecdir}/openshift/cartridges/php
%global frameworkdir %{_libexecdir}/openshift/cartridges/php

Name:          openshift-origin-cartridge-shiny
Version:       0.1
Release:       1%{?dist}
Summary:       Shiny server cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      facter
Requires:      rubygem(openshift-origin-node)
%if 0%{?fedora}%{?rhel} <= 6
Requires:      httpd < 2.4
%endif
%if 0%{?fedora} >= 19
Requires:      httpd > 2.3
Requires:      httpd < 2.5
%endif
Requires:      R >= 3.0.0
Requires:      shiny-server >= 1.1.0
BuildArch:     noarch


%description
Shiny-server cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{cartridgedir}/versions/shared/configuration/etc/conf/

%if 0%{?fedora}%{?rhel} <= 6
mv %{buildroot}%{cartridgedir}/metadata/manifest.yml.rhel %{buildroot}%{cartridgedir}/metadata/manifest.yml
%endif
%if 0%{?fedora} == 18
mv %{buildroot}%{cartridgedir}/metadata/manifest.yml.fedora18 %{buildroot}%{cartridgedir}/metadata/manifest.yml
%endif
%if 0%{?fedora} == 19
mv %{buildroot}%{cartridgedir}/metadata/manifest.yml.fedora19 %{buildroot}%{cartridgedir}/metadata/manifest.yml
%endif
rm %{buildroot}%{cartridgedir}/metadata/manifest.yml.*

%files
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md


%changelog
* Sat Mar 8 2014 Oleg Fayans <ofayans@redhat.com> 1.18.0.3-1
- Initial revision
