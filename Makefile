PROG=lurch

fake:
	# NOOP

install:
	mkdir -p /usr/local/lib/$(PROG)
	cp -a * /usr/local/lib/$(PROG)
	ln -f -s /usr/local/lib/$(PROG)/$(PROG) /usr/local/bin/$(PROG)

uninstall:
	rm -rf /usr/local/lib/$(PROG)
	rm -rf /usr/local/bin/$(PROG)
