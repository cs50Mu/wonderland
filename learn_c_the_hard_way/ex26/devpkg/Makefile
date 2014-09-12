PREFIX?=/usr
CFLAGS=-g -Wall -I${PREFIX}/include/apr-1 -I${PREFIX}/include/apr-util-1 -D_LARGEFILE64_SOURCE=1
LDFLAGS=-L${PREFIX}/lib -lapr-1 -pthread -laprutil-1

all: devpkg

devpkg: bstrlib.o db.o shell.o commands.o

install: all
	install -d $(DESTDIR)/$(PREFIX)/bin
	install devpkg $(DESTDIR)/$(PREFIX)/bin

clean:
	rm -f *.o
	rm -f devpkg
	rm -rf *.dSYM
