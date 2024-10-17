Name:		texlive-chemsec
Version:	46972
Release:	2
Summary:	Automated creation of numeric entity labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemsec
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemsec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemsec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemsec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Packages provides creation of sequential numeric labels for
entities in a document. The motivating example is chemical
structures in a scientific document. The package can
automatically output a full object name and label on the first
occurence in the document and just labels only on subsequent
references.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/chemsec
%{_texmfdistdir}/tex/latex/chemsec
%doc %{_texmfdistdir}/doc/latex/chemsec

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
