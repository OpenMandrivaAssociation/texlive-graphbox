Name:		texlive-graphbox
Version:	46360
Release:	1
Summary:	Extend graphicx to improve placement of graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphbox
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Graphbox is an extension of the standard graphicx LaTeX2e
package to allow the placement of graphics relative to the
"current position" using additional optional arguments of
\includegraphics. For example, changing the vertical alignment
is convenient for using graphics as elements of (mathematical)
formulae. Options for shifting, smashing and hiding the
graphics may be useful in support, for example, of the beamer
framework.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/graphbox
%{_texmfdistdir}/tex/latex/graphbox
%doc %{_texmfdistdir}/doc/latex/graphbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
