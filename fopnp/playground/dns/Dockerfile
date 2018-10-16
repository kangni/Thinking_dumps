FROM fopnp/base

ADD hosts /root/hosts
ADD mx-entries /etc/dnsmasq.d/mx-entries
RUN echo 'user=root' >> /etc/dnsmasq.conf && \
	echo 'mx-host=example.com,mail.example.com,50' >> /etc/dnsmasq.conf && \
	echo 'exec dnsmasq --no-daemon --log-queries --no-resolv --no-hosts --addn-hosts=/root/hosts' >> /startup.sh && \
	apt-get update && \
	sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d && \
	DEBIAN_FRONTEND=noninteractive \
	apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dnsmasq && \
	rm -rf /var/lib/apt/lists/*
