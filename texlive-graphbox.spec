%global tl_name graphbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.1
Release:	%{tl_revision}.1
Summary:	Extend graphicx to improve placement of graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Graphbox is an extension of the standard graphicx LaTeX2e package to
allow the placement of graphics relative to the "current position" using
additional optional arguments of \includegraphics. For example, changing
the vertical alignment is convenient for using graphics as elements of
(mathematical) formulae. Options for shifting, smashing and hiding the
graphics may be useful in support, for example, of the beamer framework.

