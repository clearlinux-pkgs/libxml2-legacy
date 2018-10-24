#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxml2-legacy
Version  : 2.9.7
Release  : 8
URL      : https://git.gnome.org/browse/libxml2/snapshot/libxml2-2.9.7.tar.xz
Source0  : https://git.gnome.org/browse/libxml2/snapshot/libxml2-2.9.7.tar.xz
Summary  : libXML library version2.
Group    : Development/Tools
License  : MIT
Requires: libxml2-legacy-bin
Requires: libxml2-legacy-legacypython
Requires: libxml2-legacy-lib
Requires: libxml2-legacy-data
Requires: libxml2-legacy-doc
Requires: libxml2-legacy-python
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)


%description
XML toolkit from the GNOME project
Full documentation is available on-line at
http://xmlsoft.org/

%package bin
Summary: bin components for the libxml2-legacy package.
Group: Binaries
Requires: libxml2-legacy-data

%description bin
bin components for the libxml2-legacy package.


%package data
Summary: data components for the libxml2-legacy package.
Group: Data

%description data
data components for the libxml2-legacy package.


%package dev
Summary: dev components for the libxml2-legacy package.
Group: Development
Requires: libxml2-legacy-lib
Requires: libxml2-legacy-bin
Requires: libxml2-legacy-data
Provides: libxml2-legacy-devel

%description dev
dev components for the libxml2-legacy package.


%package doc
Summary: doc components for the libxml2-legacy package.
Group: Documentation

%description doc
doc components for the libxml2-legacy package.


%package legacypython
Summary: legacypython components for the libxml2-legacy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the libxml2-legacy package.


%package lib
Summary: lib components for the libxml2-legacy package.
Group: Libraries
Requires: libxml2-legacy-data

%description lib
lib components for the libxml2-legacy package.


%package python
Summary: python components for the libxml2-legacy package.
Group: Default

%description python
python components for the libxml2-legacy package.


%prep
%setup -q -n libxml2-2.9.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517707556
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong "
%autogen --disable-static PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1517707556
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%exclude /usr/lib64/cmake/libxml2/libxml2-config.cmake
%exclude /usr/lib64/xml2Conf.sh

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/xml2-config
%exclude /usr/bin/xmlcatalog
%exclude /usr/bin/xmllint

%files data
%defattr(-,root,root,-)
%exclude /usr/share/doc/libxml2-2.9.7/Copyright
%exclude /usr/share/doc/libxml2-2.9.7/examples/testHTML.c
%exclude /usr/share/doc/libxml2-2.9.7/examples/testSAX.c
%exclude /usr/share/doc/libxml2-2.9.7/examples/testXPath.c
%exclude /usr/share/doc/libxml2-2.9.7/examples/xmllint.c
%exclude /usr/share/doc/libxml2-2.9.7/html/DOM.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/FAQ.html
%exclude /usr/share/doc/libxml2-2.9.7/html/Libxml2-Logo-180x168.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/Libxml2-Logo-90x34.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/encoding.html
%exclude /usr/share/doc/libxml2-2.9.7/html/examples.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/examples.xsl
%exclude /usr/share/doc/libxml2-2.9.7/html/html/book1.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/home.png
%exclude /usr/share/doc/libxml2-2.9.7/html/html/index.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/left.png
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-DOCBparser.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-HTMLparser.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-HTMLtree.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-SAX.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-SAX2.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-c14n.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-catalog.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-chvalid.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-debugXML.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-dict.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-encoding.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-entities.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-globals.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-hash.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-lib.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-list.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-nanoftp.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-nanohttp.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-parser.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-parserInternals.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-pattern.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-relaxng.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-schemasInternals.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-schematron.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-threads.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-tree.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-uri.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-valid.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xinclude.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xlink.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlIO.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlautomata.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlerror.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlexports.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlmemory.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlmodule.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlreader.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlregexp.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlsave.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlschemas.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlschemastypes.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlstring.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlunicode.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlversion.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xmlwriter.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xpath.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xpathInternals.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xpointer.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/libxml-xzlib.html
%exclude /usr/share/doc/libxml2-2.9.7/html/html/right.png
%exclude /usr/share/doc/libxml2-2.9.7/html/html/up.png
%exclude /usr/share/doc/libxml2-2.9.7/html/index.html
%exclude /usr/share/doc/libxml2-2.9.7/html/io1.c
%exclude /usr/share/doc/libxml2-2.9.7/html/io1.res
%exclude /usr/share/doc/libxml2-2.9.7/html/io2.c
%exclude /usr/share/doc/libxml2-2.9.7/html/io2.res
%exclude /usr/share/doc/libxml2-2.9.7/html/libxml.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/parse1.c
%exclude /usr/share/doc/libxml2-2.9.7/html/parse2.c
%exclude /usr/share/doc/libxml2-2.9.7/html/parse3.c
%exclude /usr/share/doc/libxml2-2.9.7/html/parse4.c
%exclude /usr/share/doc/libxml2-2.9.7/html/reader1.c
%exclude /usr/share/doc/libxml2-2.9.7/html/reader1.res
%exclude /usr/share/doc/libxml2-2.9.7/html/reader2.c
%exclude /usr/share/doc/libxml2-2.9.7/html/reader3.c
%exclude /usr/share/doc/libxml2-2.9.7/html/reader3.res
%exclude /usr/share/doc/libxml2-2.9.7/html/reader4.c
%exclude /usr/share/doc/libxml2-2.9.7/html/reader4.res
%exclude /usr/share/doc/libxml2-2.9.7/html/redhat.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/smallfootonly.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/structure.gif
%exclude /usr/share/doc/libxml2-2.9.7/html/test1.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/test2.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/test3.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/testWriter.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tree1.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tree1.res
%exclude /usr/share/doc/libxml2-2.9.7/html/tree2.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tree2.res
%exclude /usr/share/doc/libxml2-2.9.7/html/tst.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apa.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apb.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apc.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apd.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ape.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apf.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/apg.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/aph.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/api.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s02.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s03.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s04.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s05.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s06.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s07.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s08.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ar01s09.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/customfo.xsl
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/customhtml.xsl
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/blank.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/1.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/10.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/2.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/3.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/4.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/5.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/6.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/7.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/8.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/callouts/9.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/caution.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/draft.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/home.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/important.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/next.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/note.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/prev.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/tip.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/toc-blank.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/toc-minus.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/toc-plus.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/up.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/images/warning.png
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includeaddattribute.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includeaddkeyword.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includeconvert.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includegetattribute.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includekeyword.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includestory.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/includexpath.c
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/index.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/ix01.html
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/xmltutorial.pdf
%exclude /usr/share/doc/libxml2-2.9.7/html/tutorial/xmltutorial.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/w3c.png
%exclude /usr/share/doc/libxml2-2.9.7/html/writer.xml
%exclude /usr/share/doc/libxml2-2.9.7/html/xml.html
%exclude /usr/share/doc/libxml2-2.9.7/html/xpath1.c
%exclude /usr/share/doc/libxml2-2.9.7/html/xpath1.res
%exclude /usr/share/doc/libxml2-2.9.7/html/xpath2.c
%exclude /usr/share/doc/libxml2-2.9.7/html/xpath2.res
%exclude /usr/share/doc/libxml2-python-2.9.7/TODO
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/attribs.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/attribs.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/build.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/build.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/compareNodes.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/compareNodes.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/ctxterror.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/ctxterror.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/cutnpaste.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/cutnpaste.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/dtdvalid.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/dtdvalid.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/error.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/error.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/inbuf.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/inbuf.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/indexes.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/indexes.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/input_callback.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/input_callback.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/invalid.xml
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/nsdel.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/nsdel.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/outbuf.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/outbuf.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/push.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/push.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/pushSAX.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/pushSAX.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/pushSAXhtml.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/pushSAXhtml.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader2.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader2.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader3.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader3.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader4.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader4.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader5.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader5.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader6.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader6.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader7.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader7.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader8.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/reader8.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/readererr.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/readererr.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/readernext.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/readernext.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/regexp.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/regexp.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/relaxng.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/relaxng.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/resolver.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/resolver.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/schema.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/schema.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/serialize.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/serialize.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/sync.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/sync.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/test.dtd
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/thread2.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/thread2.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tst.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tst.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tst.xml
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstLastError.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstLastError.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstURI.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstURI.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstmem.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstmem.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstxpath.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/tstxpath.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/valid.xml
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validDTD.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validDTD.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validRNG.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validRNG.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validSchemas.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validSchemas.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validate.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/validate.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/walker.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/walker.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpath.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpath.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathext.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathext.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathleak.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathleak.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathns.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathns.pyc
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathret.py
%exclude /usr/share/doc/libxml2-python-2.9.7/examples/xpathret.pyc

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/libxml2/libxml/DOCBparser.h
%exclude /usr/include/libxml2/libxml/HTMLparser.h
%exclude /usr/include/libxml2/libxml/HTMLtree.h
%exclude /usr/include/libxml2/libxml/SAX.h
%exclude /usr/include/libxml2/libxml/SAX2.h
%exclude /usr/include/libxml2/libxml/c14n.h
%exclude /usr/include/libxml2/libxml/catalog.h
%exclude /usr/include/libxml2/libxml/chvalid.h
%exclude /usr/include/libxml2/libxml/debugXML.h
%exclude /usr/include/libxml2/libxml/dict.h
%exclude /usr/include/libxml2/libxml/encoding.h
%exclude /usr/include/libxml2/libxml/entities.h
%exclude /usr/include/libxml2/libxml/globals.h
%exclude /usr/include/libxml2/libxml/hash.h
%exclude /usr/include/libxml2/libxml/list.h
%exclude /usr/include/libxml2/libxml/nanoftp.h
%exclude /usr/include/libxml2/libxml/nanohttp.h
%exclude /usr/include/libxml2/libxml/parser.h
%exclude /usr/include/libxml2/libxml/parserInternals.h
%exclude /usr/include/libxml2/libxml/pattern.h
%exclude /usr/include/libxml2/libxml/relaxng.h
%exclude /usr/include/libxml2/libxml/schemasInternals.h
%exclude /usr/include/libxml2/libxml/schematron.h
%exclude /usr/include/libxml2/libxml/threads.h
%exclude /usr/include/libxml2/libxml/tree.h
%exclude /usr/include/libxml2/libxml/uri.h
%exclude /usr/include/libxml2/libxml/valid.h
%exclude /usr/include/libxml2/libxml/xinclude.h
%exclude /usr/include/libxml2/libxml/xlink.h
%exclude /usr/include/libxml2/libxml/xmlIO.h
%exclude /usr/include/libxml2/libxml/xmlautomata.h
%exclude /usr/include/libxml2/libxml/xmlerror.h
%exclude /usr/include/libxml2/libxml/xmlexports.h
%exclude /usr/include/libxml2/libxml/xmlmemory.h
%exclude /usr/include/libxml2/libxml/xmlmodule.h
%exclude /usr/include/libxml2/libxml/xmlreader.h
%exclude /usr/include/libxml2/libxml/xmlregexp.h
%exclude /usr/include/libxml2/libxml/xmlsave.h
%exclude /usr/include/libxml2/libxml/xmlschemas.h
%exclude /usr/include/libxml2/libxml/xmlschemastypes.h
%exclude /usr/include/libxml2/libxml/xmlstring.h
%exclude /usr/include/libxml2/libxml/xmlunicode.h
%exclude /usr/include/libxml2/libxml/xmlversion.h
%exclude /usr/include/libxml2/libxml/xmlwriter.h
%exclude /usr/include/libxml2/libxml/xpath.h
%exclude /usr/include/libxml2/libxml/xpathInternals.h
%exclude /usr/include/libxml2/libxml/xpointer.h
%exclude /usr/lib64/libxml2.so
%exclude /usr/lib64/pkgconfig/libxml-2.0.pc
%exclude /usr/share/aclocal/libxml.m4

%files doc
%defattr(-,root,root,-)
%exclude /usr/share/gtk-doc/html/libxml2/general.html
%exclude /usr/share/gtk-doc/html/libxml2/home.png
%exclude /usr/share/gtk-doc/html/libxml2/index.html
%exclude /usr/share/gtk-doc/html/libxml2/left.png
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-DOCBparser.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-HTMLparser.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-HTMLtree.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-SAX.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-SAX2.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-c14n.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-catalog.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-chvalid.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-debugXML.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-dict.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-encoding.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-entities.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-globals.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-hash.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-list.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-nanoftp.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-nanohttp.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-parser.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-parserInternals.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-pattern.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-relaxng.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-schemasInternals.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-schematron.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-threads.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-tree.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-uri.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-valid.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xinclude.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xlink.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlIO.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlautomata.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlerror.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlexports.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlmemory.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlmodule.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlreader.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlregexp.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlsave.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlschemas.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlschemastypes.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlstring.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlunicode.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlversion.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xmlwriter.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xpath.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xpathInternals.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2-xpointer.html
%exclude /usr/share/gtk-doc/html/libxml2/libxml2.devhelp
%exclude /usr/share/gtk-doc/html/libxml2/right.png
%exclude /usr/share/gtk-doc/html/libxml2/style.css
%exclude /usr/share/gtk-doc/html/libxml2/up.png
%exclude /usr/share/man/man1/xml2-config.1
%exclude /usr/share/man/man1/xmlcatalog.1
%exclude /usr/share/man/man1/xmllint.1
%exclude /usr/share/man/man3/libxml.3

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libxml2.so.2
%exclude /usr/lib64/libxml2.so.2.9.7

%files python
%defattr(-,root,root,-)
