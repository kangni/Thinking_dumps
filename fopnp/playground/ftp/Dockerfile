FROM fopnp/base

ADD ftp.crt /root/ftp.crt
ADD ftp.key /root/ftp.key

RUN apt-get update && \
	sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d && \
	mkdir -p /var/run/vsftpd/empty && \
	touch /etc/init.d/vsftpd && \
	echo 'write_enable=YES' >> /etc/vsftpd.conf && \
	echo 'user=root' >> /etc/vsftpd.conf && \
	echo '/etc/init.d/openbsd-inetd start' >> /startup.sh && \
	echo '/usr/sbin/vsftpd' >> /startup.sh && \
	sed -i /^rsa_cert/s:=.*:=/root/ftp.crt: /etc/vsftpd.conf && \
	sed -i /^rsa_priv/s:=.*:=/root/ftp.key: /etc/vsftpd.conf && \
	export DEBIAN_FRONTEND=noninteractive && \
	apt-get install -y telnetd && \
	apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" vsftpd && \
	rm -rf /var/lib/apt/lists/*
