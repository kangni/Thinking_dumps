FROM fopnp/base

ADD service.pem /root/service.pem
ADD sample-mbox /var/mail/brandon

RUN	export DEBIAN_FRONTEND=noninteractive && \
	touch /etc/init.d/dovecot && \
	apt-get update && \
	apt-get	install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dovecot-imapd dovecot-pop3d postfix mailutils && \
	sed -i /myhostname/d /etc/postfix/main.cf && \
	sed -i /mydestination/d /etc/postfix/main.cf && \
	echo 'myhostname = mail.example.com' >> /etc/postfix/main.cf && \
	echo 'mydestination = mail.example.com, example.com, localhost.localdomain, localhost' >> /etc/postfix/main.cf && \
	chown brandon.brandon /var/mail/brandon && \
	cp /var/mail/brandon /root/var.mail.brandon.backup && \
	echo 'echo example.com > /etc/mailname' >> /startup.sh && \
	echo '/etc/init.d/postfix start' >> /startup.sh && \
	echo 'dovecot -F' >> /startup.sh && \
	rm -rf /var/lib/apt/lists/*
