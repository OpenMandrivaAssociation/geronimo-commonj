%{?_javapackages_macros:%_javapackages_macros}
Name: geronimo-commonj
Version: 1.1.0
Release: 10.2
Summary: CommonJ Specification
Group:	Development/Java
License: ASL 2.0
URL: http://geronimo.apache.org/

# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/specs-1.4/geronimo-commonj_1.1_spec geronimo-commonj-1.1.0
# tar cvfJ geronimo-commonj-1.1.0.tar.xz geronimo-commonj-1.1.0
Source: %{name}-%{version}.tar.xz

# Remove the SNAPSHOT tag from the version in the POM file:
Patch0: %{name}-version-fix.patch

BuildArch: noarch

BuildRequires: geronimo-parent-poms
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-local


Requires: java
Requires: jpackage-utils


%description
Geronimo CommonJ Specification.


%package javadoc
Summary: Javadocs for %{name}

Requires: jpackage-utils


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p0


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}_1.1_spec-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files -f .mfiles
%doc LICENSE.txt
%doc NOTICE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Juan Hernandez <juan.hernandez@redhat.com> - 1.1.0-6
- Add build dependency on geronimo-parent-poms (rhbz 914026)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.0-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 2 2012 Juan Hernandez <juan.hernandez@redhat.com> 1.1.0-2
- Cleanup of the spec file

* Tue Aug 30 2011 Andy Grimm <agrimm@gmail.com> 1.1.0-1
- Initial build
